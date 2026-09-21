from __future__ import annotations

import json
import time
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Generator
from urllib.parse import urljoin, urlparse
from urllib.request import Request

from .errors import APIError, NetworkError, TimeoutError
from .error_reporting import (
    ErrorReporter,
    ErrorReportingPolicy,
    create_error_report,
    should_report,
)
from .errors import InttegroError

if TYPE_CHECKING:
    from opentelemetry.trace import Span, TracerProvider


INSTRUMENTATION_NAME = "inttegro"
SAFE_RESOURCES = frozenset(
    {
        "apps", "balance_transactions", "balances", "broadcasts", "checkout", "chimes", "customers",
        "file_links", "file_references", "files", "financial_accounts", "keys", "message_templates",
        "orders", "otp", "payment_methods", "payouts", "ping", "prices", "products", "purchase_intents",
        "refunds", "schedules", "sessions", "spec", "upload_requests",
    }
)
SAFE_ACTIONS = frozenset(
    {
        "activate", "add_price", "archive", "broadcast", "cancel", "complete", "confirm_payment",
        "confirm_verification", "connect", "contents", "countries", "create", "deactivate", "delete",
        "destroy", "disable", "disable_fx", "disable_pull", "disable_push", "disactivate", "disconnect",
        "enable", "enable_fx", "enable_pull", "enable_push", "finalize", "generate", "initiate", "lookup",
        "new", "open", "page", "pay", "publish", "reconcile", "reconnect", "refund", "render_preview",
        "request_confirmation", "review", "revoke", "schedule", "search", "send", "send_invoice", "send_receipt",
        "set_default_unit_price", "set_destinations", "settings", "tokenize", "unarchive", "unpublish",
        "update", "upload", "usage", "verify",
    }
)


class Telemetry:
    """Vendor-neutral SDK tracing using the application's OpenTelemetry provider."""

    def __init__(
        self,
        version: str,
        *,
        enabled: bool = True,
        tracer_provider: TracerProvider | None = None,
        error_reporter: ErrorReporter | None = None,
        error_reporting_policy: ErrorReportingPolicy = "unexpected",
    ) -> None:
        self.enabled = enabled
        self.error_reporter = error_reporter
        self.error_reporting_policy = error_reporting_policy
        # Import OpenTelemetry lazily. Cloudflare snapshots Python Worker modules
        # outside request context, where opentelemetry.context's UUID setup is
        # not permitted to request entropy. Client construction happens within
        # a request and keeps the ordinary server behavior unchanged.
        from opentelemetry import propagate, trace
        from opentelemetry.trace import SpanKind, Status, StatusCode

        self.tracer: Any = trace.get_tracer(INSTRUMENTATION_NAME, version, tracer_provider)
        self._propagate = propagate
        self._span_kind_client = SpanKind.CLIENT
        self._status = Status
        self._status_error = StatusCode.ERROR

    @contextmanager
    def operation(
        self,
        path_or_url: str,
        method: str,
        base_url: str,
        version: str,
        operation_override: str | None = None,
    ) -> Generator[Span | None, None, None]:
        if not self.enabled and self.error_reporter is None:
            yield None
            return

        operation, route, server_address = _request_details(path_or_url, base_url, operation_override)
        started_at = time.monotonic() if self.error_reporter is not None else None

        if not self.enabled:
            try:
                yield None
            except Exception as error:
                self._report(
                    error,
                    operation=operation,
                    route=route,
                    server_address=server_address,
                    method=method,
                    version=version,
                    started_at=started_at,
                    span=None,
                )
                raise
            return
        attributes: dict[str, str] = {
            "inttegro.operation.name": operation,
            "inttegro.sdk.language": "python",
            "inttegro.sdk.version": version,
            "http.request.method": method.upper(),
            "server.address": server_address,
        }
        if route is not None:
            attributes["url.template"] = route

        with self.tracer.start_as_current_span(
            f"inttegro.{operation}",
            kind=self._span_kind_client,
            attributes=attributes,
            record_exception=False,
            set_status_on_exception=False,
        ) as span:
            try:
                yield span
            except Exception as error:
                error_type = _classify_error(error)
                span.set_attribute("error.type", error_type)
                span.set_status(self._status(self._status_error))
                span.add_event("inttegro.request.failed", {"error.type": error_type})
                self._report(
                    error,
                    operation=operation,
                    route=route,
                    server_address=server_address,
                    method=method,
                    version=version,
                    started_at=started_at,
                    span=span,
                )
                raise

    def _report(
        self,
        error: Exception,
        *,
        operation: str,
        route: str | None,
        server_address: str,
        method: str,
        version: str,
        started_at: float | None,
        span: Span | None,
    ) -> None:
        reporter = self.error_reporter
        if reporter is None:
            return
        try:
            category = _classify_error(error)
            if not should_report(error, category, self.error_reporting_policy):
                return
            report = create_error_report(
                error=error,
                category=category,
                operation=operation,
                method=method,
                route=route,
                server_address=server_address,
                version=version,
                started_at=started_at if started_at is not None else time.monotonic(),
                span=span,
            )
            if isinstance(error, InttegroError):
                error.report = report
            reporter(report)
        except Exception:
            # A collector failure must never replace the original SDK error.
            pass

    def prepare(self, span: Span | None, request: Request) -> None:
        if self.enabled:
            carrier: dict[str, str] = {}
            self._propagate.inject(carrier)
            for key, value in carrier.items():
                if not any(existing.lower() == key.lower() for existing, _ in request.header_items()):
                    request.add_header(key, value)
        if span is not None:
            span.add_event("inttegro.request.prepared")
            span.add_event("inttegro.http.attempt.started", {"http.request.resend_count": 0})

    @staticmethod
    def response(span: Span | None, status: int, headers: dict[str, str], *, decoded: bool) -> None:
        if span is None:
            return
        span.set_attribute("http.response.status_code", status)
        request_id = next((value for key, value in headers.items() if key.lower() == "x-request-id"), None)
        if request_id:
            span.set_attribute("inttegro.request.id", request_id)
        span.add_event(
            "inttegro.response.received",
            {"http.response.status_code": status, "http.request.resend_count": 0},
        )
        if decoded:
            span.add_event("inttegro.response.decoded")

    @staticmethod
    def decoded(span: Span | None) -> None:
        if span is not None:
            span.add_event("inttegro.response.decoded")


def _request_details(
    path_or_url: str,
    base_url: str,
    operation_override: str | None,
) -> tuple[str, str | None, str]:
    parsed = urlparse(urljoin(f"{base_url.rstrip('/')}/", path_or_url.lstrip('/')))
    is_static_api_route = not path_or_url.startswith(("http://", "https://"))
    segments = [segment for segment in parsed.path.split("/") if segment] if is_static_api_route else []
    resource = segments[0] if segments else None
    action = segments[1] if len(segments) > 1 else None
    known_route = (
        0 < len(segments) <= 2
        and resource in SAFE_RESOURCES
        and (action is None or action in SAFE_ACTIONS)
    )
    route = parsed.path if known_route else None
    derived_operation = (
        f"{resource}.{action or ('lookup' if resource == 'balances' else 'request')}"
        if known_route
        else "http.request"
    )
    return operation_override or derived_operation, route, parsed.hostname or "unknown"


def _classify_error(error: Exception) -> str:
    if isinstance(error, TimeoutError):
        return "timeout"
    if isinstance(error, NetworkError):
        return "network_error"
    if isinstance(error, APIError):
        return f"http_{error.status}"
    if isinstance(error, (json.JSONDecodeError, UnicodeDecodeError)):
        return "decode_error"
    return "unknown_error"
