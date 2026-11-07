from __future__ import annotations

import json
import urllib.request
import uuid
from collections.abc import Awaitable, Callable, Mapping
from typing import TYPE_CHECKING, Any, Dict, NoReturn, Optional, Protocol

import httpx
from .error_reporting import ErrorReporter, ErrorReportingPolicy
from .errors import NetworkError, TimeoutError
from ._model_base import ApiModel
from ._dynamic_value import DynamicValue
from .http_client import HttpClient, RequestBody, generate_idempotency_key
from .response import InttegroResponse
from ._telemetry import Telemetry
from .version import VERSION

if TYPE_CHECKING:
    from opentelemetry.trace import TracerProvider


AsyncTransport = Callable[
    [urllib.request.Request, float | None],
    Awaitable[tuple[int, Dict[str, str], str | bytes]],
]


class AsyncHTTPResponse(Protocol):
    """Response shape required from an application-owned async HTTP pool."""

    status_code: int
    headers: Mapping[str, str]
    content: bytes


class AsyncHTTPClient(Protocol):
    """Minimal transport protocol implemented by ``httpx.AsyncClient``."""

    async def request(
        self,
        method: str,
        url: str,
        *,
        headers: Mapping[str, str],
        content: bytes | None,
        timeout: float,
    ) -> AsyncHTTPResponse:
        raise NotImplementedError

    async def aclose(self) -> None:
        raise NotImplementedError


class AsyncHttpClient:
    """Non-blocking HTTP client used by :class:`AsyncInttegroClient`.

    Response decoding, error mapping, idempotency, and telemetry delegate to
    the synchronous codec so both clients obey the same wire contract. Only
    network I/O and lifecycle management differ.
    """

    async_transport: AsyncTransport | None
    api_key: str
    base_url: str
    timeout: float
    user_agent: str
    telemetry: Telemetry

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.inttegro.com",
        timeout: float = 30.0,
        transport: AsyncTransport | None = None,
        telemetry_enabled: bool = True,
        tracer_provider: TracerProvider | None = None,
        error_reporter: ErrorReporter | None = None,
        error_reporting_policy: ErrorReportingPolicy = "unexpected",
        http_client: AsyncHTTPClient | None = None,
    ) -> None:
        self._codec = HttpClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            transport=None,
            telemetry_enabled=telemetry_enabled,
            tracer_provider=tracer_provider,
            error_reporter=error_reporter,
            error_reporting_policy=error_reporting_policy,
        )
        self.api_key = self._codec.api_key
        self.base_url = self._codec.base_url
        self.timeout = self._codec.timeout
        self.user_agent = self._codec.user_agent
        self.telemetry = self._codec.telemetry
        self.async_transport = transport
        self._http_client = http_client or (None if transport is not None else httpx.AsyncClient())
        self._owns_http_client = http_client is None and transport is None
        self._closed = False

    async def __aenter__(self) -> AsyncHttpClient:
        return self

    async def __aexit__(self, exc_type: object, exc: object, traceback: object) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        """Close connections owned by this SDK client.

        An injected ``httpx.AsyncClient`` remains application-owned and is not
        closed here. This makes it safe to share a configured connection pool.
        """

        if not self._closed and self._owns_http_client and self._http_client is not None:
            await self._http_client.aclose()
        self._closed = True

    async def get(self, path: str, query: Optional[dict[str, Any]] = None) -> Any:
        return await self.request("GET", path, query=query)

    async def get_with_response(self, path: str, query: Optional[dict[str, Any]] = None) -> InttegroResponse[Any]:
        return await self.request_with_response("GET", path, query=query)

    async def post(
        self,
        path: str,
        body: Optional[RequestBody] = None,
        query: Optional[dict[str, Any]] = None,
    ) -> Any:
        return await self.request("POST", path, body=body, query=query)

    async def post_with_response(
        self,
        path: str,
        body: Optional[RequestBody] = None,
        query: Optional[dict[str, Any]] = None,
    ) -> InttegroResponse[Any]:
        return await self.request_with_response("POST", path, body=body, query=query)

    async def post_resource_with_response(
        self,
        path: str,
        field: str,
        model_type: type[ApiModel],
        body: Optional[RequestBody] = None,
        query: Optional[dict[str, Any]] = None,
    ) -> InttegroResponse[Any]:
        response = await self.post_with_response(path, body=body, query=query)
        data = response.data
        if isinstance(data, model_type):
            resource = data
        elif isinstance(data, DynamicValue):
            payload = data.to_dict()
            value = payload.get(field) if isinstance(payload, dict) else None
            if not isinstance(value, dict):
                raise TypeError(f"Inttegro returned an invalid {field} response")
            resource = model_type.from_dict(value)
        else:
            value = getattr(data, field, None)
            if not isinstance(value, model_type):
                raise TypeError(f"Inttegro returned an invalid {field} response")
            resource = value
        return InttegroResponse(
            data=resource,
            status=response.status,
            headers=response.headers,
            meta=response.meta,
        )

    async def post_with_headers(
        self,
        path: str,
        body: Optional[RequestBody] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> Any:
        with self.telemetry.operation(path, "POST", self.base_url, VERSION) as span:
            request_headers = dict(headers or {})
            request_body = self._validated_request_body(body or {})
            if self._is_idempotent_mutation_path(path) and not self._has_header(request_headers, "Idempotency-Key"):
                request_body = self._with_request_meta_idempotency(request_body)
            data = json.dumps(request_body).encode("utf-8")
            req = self._json_request("POST", path, data, request_headers)
            self.telemetry.prepare(span, req)
            status, response_headers, response_body = await self._send_async(req)
            self.telemetry.response(span, status, response_headers, decoded=False)
            result = self._parse_response(status, response_body.decode("utf-8"), response_headers, path)
            self.telemetry.decoded(span)
            return result

    async def post_multipart(
        self,
        path: str,
        fields: dict[str, Any],
        files: dict[str, str],
        headers: Optional[dict[str, str]] = None,
        authenticated: bool = True,
        operation: str | None = None,
    ) -> Any:
        with self.telemetry.operation(path, "POST", self.base_url, VERSION, operation) as span:
            boundary = "----InttegroBoundary{}".format(uuid.uuid4().hex)
            data = self._encode_multipart(fields, files, boundary)
            req = urllib.request.Request(url=self._build_url(path, None), data=data, method="POST")
            req.add_header("Accept", "application/json")
            req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
            req.add_header("User-Agent", self.user_agent)
            if authenticated:
                req.add_header("Authorization", f"Bearer {self.api_key}")
            request_headers = dict(headers or {})
            if authenticated and self._is_idempotent_mutation_path(path) and not self._has_header(request_headers, "Idempotency-Key"):
                request_headers["Idempotency-Key"] = generate_idempotency_key()
            for key, value in request_headers.items():
                req.add_header(key, value)
            self.telemetry.prepare(span, req)
            status, response_headers, response_body = await self._send_async(req)
            self.telemetry.response(span, status, response_headers, decoded=False)
            result = self._parse_response(status, response_body.decode("utf-8"), response_headers, path)
            self.telemetry.decoded(span)
            return result

    async def post_binary_json(self, path: str, body: RequestBody) -> tuple[bytes, dict[str, str]]:
        with self.telemetry.operation(path, "POST", self.base_url, VERSION) as span:
            encoded = self._validated_request_body(body)
            req = self._json_request("POST", path, json.dumps(encoded).encode("utf-8"), {})
            req.headers["Accept"] = "application/octet-stream"
            self.telemetry.prepare(span, req)
            status, headers, response_body = await self._send_async(req)
            self.telemetry.response(span, status, headers, decoded=False)
            if status >= 400:
                self._handle_error(status, headers, response_body.decode("utf-8"))
            self.telemetry.decoded(span)
            return response_body, headers

    async def get_binary_public(
        self,
        url: str,
        operation: str = "file_links.download",
    ) -> tuple[bytes, dict[str, str]]:
        with self.telemetry.operation(url, "GET", self.base_url, VERSION, operation) as span:
            req = urllib.request.Request(url=url, method="GET")
            req.add_header("User-Agent", self.user_agent)
            self.telemetry.prepare(span, req)
            status, headers, response_body = await self._send_async(req)
            self.telemetry.response(span, status, headers, decoded=False)
            if status >= 400:
                self._handle_error(status, headers, response_body.decode("utf-8"))
            self.telemetry.decoded(span)
            return response_body, headers

    async def request(
        self,
        method: str,
        path: str,
        body: Optional[RequestBody] = None,
        query: Optional[dict[str, Any]] = None,
    ) -> Any:
        return (await self.request_with_response(method, path, body=body, query=query)).data

    async def request_with_response(
        self,
        method: str,
        path: str,
        body: Optional[RequestBody] = None,
        query: Optional[dict[str, Any]] = None,
    ) -> InttegroResponse[Any]:
        with self.telemetry.operation(path, method, self.base_url, VERSION) as span:
            url = self._build_url(path, query)
            encoded: RequestBody | dict[str, Any] | None = body
            if encoded is not None:
                encoded = self._validated_request_body(encoded)
            if method.upper() == "POST" and self._is_idempotent_mutation_path(path):
                encoded = self._with_request_meta_idempotency(encoded or {})
            data = json.dumps(encoded).encode("utf-8") if encoded is not None else None
            req = urllib.request.Request(url=url, data=data, method=method.upper())
            req.add_header("Accept", "application/json")
            req.add_header("Authorization", f"Bearer {self.api_key}")
            req.add_header("User-Agent", self.user_agent)
            if data is not None:
                req.add_header("Content-Type", "application/json")
            self.telemetry.prepare(span, req)
            status, headers, response_body = await self._send_async(req)
            text_body = response_body.decode("utf-8")
            self.telemetry.response(span, status, headers, decoded=False)
            result = self._parse_response(status, text_body, headers, path)
            self.telemetry.decoded(span)
            return InttegroResponse(
                data=result,
                status=status,
                headers=headers,
                meta=self._codec._response_meta(text_body),
            )

    def _json_request(
        self,
        method: str,
        path: str,
        data: bytes,
        headers: dict[str, str],
    ) -> urllib.request.Request:
        req = urllib.request.Request(url=self._build_url(path, None), data=data, method=method)
        req.add_header("Accept", "application/json")
        req.add_header("Authorization", f"Bearer {self.api_key}")
        req.add_header("Content-Type", "application/json")
        req.add_header("User-Agent", self.user_agent)
        for key, value in headers.items():
            req.add_header(key, value)
        return req

    async def _send_async(self, req: urllib.request.Request) -> tuple[int, dict[str, str], bytes]:
        if self._closed:
            raise RuntimeError("AsyncInttegroClient is closed")
        if self.async_transport is not None:
            status, headers, response_body = await self.async_transport(req, self.timeout)
            body = response_body if isinstance(response_body, bytes) else str(response_body).encode("utf-8")
            return status, {key.lower(): value for key, value in headers.items()}, body
        try:
            content = req.data if isinstance(req.data, bytes) else None
            if self._http_client is None:
                raise RuntimeError("Async HTTP transport is unavailable")
            response = await self._http_client.request(
                req.get_method(),
                req.full_url,
                headers=dict(req.header_items()),
                content=content,
                timeout=self.timeout,
            )
            return response.status_code, dict(response.headers), response.content
        except httpx.TimeoutException as error:
            raise TimeoutError("Request timed out", error) from error
        except httpx.HTTPError as error:
            raise NetworkError("Network request failed", error) from error

    def _build_url(self, path: str, query: Optional[dict[str, Any]]) -> str:
        return self._codec._build_url(path, query)

    def _with_request_meta_idempotency(self, body: dict[str, Any]) -> dict[str, Any]:
        return self._codec._with_request_meta_idempotency(body)

    def _validated_request_body(self, body: RequestBody) -> dict[str, Any]:
        return self._codec._validated_request_body(body)

    def _is_idempotent_mutation_path(self, path_or_url: str) -> bool:
        return self._codec._is_idempotent_mutation_path(path_or_url)

    def _has_header(self, headers: dict[str, str], name: str) -> bool:
        return self._codec._has_header(headers, name)

    def _encode_multipart(self, fields: dict[str, Any], files: dict[str, str], boundary: str) -> bytes:
        return self._codec._encode_multipart(fields, files, boundary)

    def _parse_response(
        self,
        status: int,
        body: str,
        headers: dict[str, str],
        path: str | None = None,
    ) -> Any:
        return self._codec._parse_response(status, body, headers, path)

    def _handle_error(self, status: int, headers: dict[str, str], raw_body: str) -> NoReturn:
        self._codec._handle_error(status, headers, raw_body)
