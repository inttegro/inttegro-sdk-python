from __future__ import annotations

import json
import mimetypes
import secrets
import socket
import time
import uuid
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Mapping
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Dict, NoReturn, Optional

from ._model_base import ApiModel, ModelDecodeError, decode_value
from ._request_base import ApiRequest, encode_request_value
from ._response_types import response_type_for_path
from .errors import APIError, AuthenticationError, NetworkError, RateLimitError, TimeoutError
from ._dynamic_value import DynamicValue
from ._telemetry import Telemetry
from .error_reporting import ErrorReporter, ErrorReportingPolicy
from .response import InttegroResponse
from .version import VERSION
if TYPE_CHECKING:
    from opentelemetry.trace import TracerProvider


Transport = Callable[[urllib.request.Request, float | None], tuple[int, Dict[str, str], str | bytes]]
RequestBody = ApiRequest | Mapping[str, Any]


class HttpClient:
    api_key: str
    base_url: str
    timeout: float
    transport: Transport | None
    user_agent: str
    telemetry: Telemetry

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.inttegro.com",
        timeout: float = 30.0,
        transport: Optional[Transport] = None,
        telemetry_enabled: bool = True,
        tracer_provider: TracerProvider | None = None,
        error_reporter: ErrorReporter | None = None,
        error_reporting_policy: ErrorReportingPolicy = "unexpected",
    ) -> None:
        if not api_key:
            raise ValueError("api_key is required")

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.transport = transport
        self.user_agent = f"inttegro-sdk-python/{VERSION}"
        self.telemetry = Telemetry(
            VERSION,
            enabled=telemetry_enabled,
            tracer_provider=tracer_provider,
            error_reporter=error_reporter,
            error_reporting_policy=error_reporting_policy,
        )

    def get(self, path: str, query: Optional[dict[str, Any]] = None) -> Any:
        return self.request("GET", path, query=query)

    def get_with_response(self, path: str, query: Optional[dict[str, Any]] = None) -> InttegroResponse[Any]:
        return self.request_with_response("GET", path, query=query)

    def post(
        self,
        path: str,
        body: Optional[RequestBody] = None,
        query: Optional[dict[str, Any]] = None,
    ) -> Any:
        return self.request("POST", path, body=body, query=query)

    def post_with_response(
        self,
        path: str,
        body: Optional[RequestBody] = None,
        query: Optional[dict[str, Any]] = None,
    ) -> InttegroResponse[Any]:
        return self.request_with_response("POST", path, body=body, query=query)

    def post_resource_with_response(
        self,
        path: str,
        field: str,
        model_type: type[ApiModel],
        body: Optional[RequestBody] = None,
        query: Optional[dict[str, Any]] = None,
    ) -> InttegroResponse[Any]:
        response = self.post_with_response(path, body=body, query=query)
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

    def post_with_headers(
        self,
        path: str,
        body: Optional[RequestBody] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> Any:
        with self.telemetry.operation(path, "POST", self.base_url, VERSION) as span:
            request_headers = dict(headers or {})
            request_body = self._without_top_level_idempotency(body or {})
            if self._is_idempotent_mutation_path(path) and not self._has_header(request_headers, "Idempotency-Key"):
                request_body = self._with_request_meta_idempotency(request_body)
            data = json.dumps(request_body).encode("utf-8")
            req = urllib.request.Request(url=self._build_url(path, None), data=data, method="POST")
            req.add_header("Accept", "application/json")
            req.add_header("Authorization", f"Bearer {self.api_key}")
            req.add_header("Content-Type", "application/json")
            req.add_header("User-Agent", self.user_agent)
            for key, value in request_headers.items():
                req.add_header(key, value)
            self.telemetry.prepare(span, req)
            status, response_headers, response_body = self._send(req)
            self.telemetry.response(span, status, response_headers, decoded=False)
            result = self._parse_response(status, response_body.decode("utf-8"), response_headers, path)
            self.telemetry.decoded(span)
            return result

    def post_multipart(
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
            status, response_headers, response_body = self._send(req)
            self.telemetry.response(span, status, response_headers, decoded=False)
            result = self._parse_response(status, response_body.decode("utf-8"), response_headers, path)
            self.telemetry.decoded(span)
            return result

    def post_binary_json(self, path: str, body: RequestBody) -> tuple[bytes, dict[str, str]]:
        with self.telemetry.operation(path, "POST", self.base_url, VERSION) as span:
            body = self._without_top_level_idempotency(body)
            data = json.dumps(body).encode("utf-8")
            req = urllib.request.Request(url=self._build_url(path, None), data=data, method="POST")
            req.add_header("Accept", "application/octet-stream")
            req.add_header("Authorization", f"Bearer {self.api_key}")
            req.add_header("Content-Type", "application/json")
            req.add_header("User-Agent", self.user_agent)
            self.telemetry.prepare(span, req)
            status, headers, response_body = self._send(req)
            self.telemetry.response(span, status, headers, decoded=False)
            if status >= 400:
                self._handle_error(status, headers, response_body.decode("utf-8"))
            self.telemetry.decoded(span)
            return response_body, headers

    def get_binary_public(
        self,
        url: str,
        operation: str = "file_links.download",
    ) -> tuple[bytes, dict[str, str]]:
        with self.telemetry.operation(url, "GET", self.base_url, VERSION, operation) as span:
            req = urllib.request.Request(url=url, method="GET")
            req.add_header("User-Agent", self.user_agent)
            self.telemetry.prepare(span, req)
            status, headers, response_body = self._send(req)
            self.telemetry.response(span, status, headers, decoded=False)
            if status >= 400:
                self._handle_error(status, headers, response_body.decode("utf-8"))
            self.telemetry.decoded(span)
            return response_body, headers

    def request(
        self,
        method: str,
        path: str,
        body: Optional[RequestBody] = None,
        query: Optional[dict[str, Any]] = None,
    ) -> Any:
        return self.request_with_response(method, path, body=body, query=query).data

    def request_with_response(
        self,
        method: str,
        path: str,
        body: Optional[RequestBody] = None,
        query: Optional[dict[str, Any]] = None,
    ) -> InttegroResponse[Any]:
        with self.telemetry.operation(path, method, self.base_url, VERSION) as span:
            url = self._build_url(path, query)
            if body is not None:
                body = self._without_top_level_idempotency(body)
            if method.upper() == "POST" and self._is_idempotent_mutation_path(path):
                body = self._with_request_meta_idempotency(body or {})
            data = json.dumps(body).encode("utf-8") if body is not None else None

            req = urllib.request.Request(url=url, data=data, method=method.upper())
            req.add_header("Accept", "application/json")
            req.add_header("Authorization", f"Bearer {self.api_key}")
            req.add_header("User-Agent", self.user_agent)
            if data is not None:
                req.add_header("Content-Type", "application/json")
            self.telemetry.prepare(span, req)

            try:
                if self.transport:
                    status, headers, resp_body = self.transport(req, self.timeout)
                else:
                    with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                        status = resp.status
                        headers = {k.lower(): v for k, v in resp.headers.items()}
                        resp_body = resp.read().decode("utf-8")
            except urllib.error.HTTPError as e:
                status = e.code
                headers = {k.lower(): v for k, v in e.headers.items()}
                resp_body = e.read().decode("utf-8")
                self.telemetry.response(span, status, headers, decoded=False)
                return self._handle_error(status, headers, resp_body)
            except urllib.error.URLError as e:
                if isinstance(e.reason, socket.timeout):
                    raise TimeoutError("Request timed out", e)
                raise NetworkError("Network request failed", e)
            except TimeoutError as e:
                raise TimeoutError("Request timed out", e)
            except Exception as e:
                raise NetworkError("Network request failed", e)

            text_body = resp_body.decode("utf-8") if isinstance(resp_body, bytes) else resp_body
            self.telemetry.response(span, status, headers, decoded=False)
            result = self._parse_response(status, text_body, headers, path)
            self.telemetry.decoded(span)
            return InttegroResponse(
                data=result,
                status=status,
                headers=headers,
                meta=self._response_meta(text_body),
            )

    def _build_url(self, path: str, query: Optional[dict[str, Any]]) -> str:
        if path.startswith("http://") or path.startswith("https://"):
            return path
        normalized = path if path.startswith("/") else f"/{path}"
        url = f"{self.base_url}{normalized}"
        if query:
            url += "?" + urllib.parse.urlencode(query)
        return url

    def _with_request_meta_idempotency(self, body: dict[str, Any]) -> dict[str, Any]:
        payload = self._without_top_level_idempotency(body)
        request_meta_value = payload.get("request_meta")
        request_meta = dict(request_meta_value) if isinstance(request_meta_value, dict) else {}
        existing_key = request_meta.get("idempotency_key")
        if isinstance(existing_key, str) and existing_key.strip():
            payload["request_meta"] = request_meta
            return payload
        request_meta["idempotency_key"] = generate_idempotency_key()
        payload["request_meta"] = request_meta
        return payload

    def _without_top_level_idempotency(self, body: RequestBody) -> dict[str, Any]:
        encoded = encode_request_value(body)
        if not isinstance(encoded, dict):
            raise TypeError("request body must encode to a JSON object")
        payload = dict(encoded)
        payload.pop("idempotency_key", None)
        return payload

    def _is_idempotent_mutation_path(self, path_or_url: str) -> bool:
        path = urllib.parse.urlparse(path_or_url).path if path_or_url.startswith(("http://", "https://")) else path_or_url
        action = next((part for part in reversed(path.split("/")) if part), "")
        return action not in {"", "lookup", "page", "search", "settings", "countries", "contents", "balances", "render_preview", "usage"}

    def _has_header(self, headers: dict[str, str], name: str) -> bool:
        return any(key.lower() == name.lower() and bool(str(value).strip()) for key, value in headers.items())

    def _send(self, req: urllib.request.Request) -> tuple[int, dict[str, str], bytes]:
        if self.transport:
            status, headers, response_body = self.transport(req, self.timeout)
            if isinstance(response_body, bytes):
                return status, headers, response_body
            return status, headers, str(response_body).encode("utf-8")
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return resp.status, {k.lower(): v for k, v in resp.headers.items()}, resp.read()
        except urllib.error.HTTPError as e:
            return e.code, {k.lower(): v for k, v in e.headers.items()}, e.read()
        except urllib.error.URLError as e:
            if isinstance(e.reason, socket.timeout):
                raise TimeoutError("Request timed out", e)
            raise NetworkError("Network request failed", e)

    def _encode_multipart(self, fields: dict[str, Any], files: dict[str, str], boundary: str) -> bytes:
        chunks: list[bytes] = []
        for name, value in fields.items():
            if value is None:
                continue
            if isinstance(value, (dict, list)):
                value = json.dumps(value)
            chunks.extend([
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                str(value).encode(),
                b"\r\n",
            ])
        for name, file_path in files.items():
            path = Path(file_path)
            content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            chunks.extend([
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"; filename="{path.name}"\r\n'.encode(),
                f"Content-Type: {content_type}\r\n\r\n".encode(),
                path.read_bytes(),
                b"\r\n",
            ])
        chunks.append(f"--{boundary}--\r\n".encode())
        return b"".join(chunks)

    def _parse_response(
        self,
        status: int,
        body: str,
        headers: dict[str, str],
        path: str | None = None,
    ) -> Any:
        parsed = self._parse_json(body)
        if status < 400:
            payload = parsed if isinstance(parsed, dict) else {}
            normalized_path = urllib.parse.urlparse(path).path if path else ""
            response_shape = response_type_for_path(normalized_path)
            if response_shape is not None:
                try:
                    value = payload if response_shape.field is None else payload[response_shape.field]
                    return decode_value(response_shape.model, value)
                except (ModelDecodeError, KeyError):
                    # Preserve unexpected wire data for forward compatibility. Valid
                    # documented payloads always decode to the endpoint's domain type.
                    pass
            return DynamicValue(payload)
        return self._handle_error(status, headers, body, parsed)

    def _parse_json(self, body: str) -> Any:
        if not body:
            return {}
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            return body

    def _response_meta(self, body: str) -> dict[str, Any] | None:
        parsed = self._parse_json(body)
        if not isinstance(parsed, dict):
            return None
        meta = parsed.get("response_meta")
        return meta if isinstance(meta, dict) else None

    def _handle_error(
        self,
        status: int,
        headers: dict[str, str],
        raw_body: str,
        parsed_body: Any | None = None,
    ) -> NoReturn:
        data = parsed_body if parsed_body is not None else self._parse_json(raw_body)
        message = "HTTP {}".format(status)
        payload = data
        if isinstance(data, dict) and isinstance(data.get("error"), dict):
            payload = data["error"]
        if isinstance(payload, dict):
            message = payload.get("message") or payload.get("detail") or data.get("message") or message
        code = payload.get("code") if isinstance(payload, dict) else None
        error_type = payload.get("type") if isinstance(payload, dict) else None
        url = payload.get("url") if isinstance(payload, dict) else None
        detail = payload.get("detail") if isinstance(payload, dict) else None
        fix_code = payload.get("fix_code") if isinstance(payload, dict) else None
        cause = payload.get("cause") if isinstance(payload, dict) else None
        request_id = next(
            (value for key, value in headers.items() if key.lower() == "x-request-id"),
            None,
        )
        if status == 401:
            raise AuthenticationError(
                message,
                status=status,
                code=code,
                error_type=error_type,
                url=url,
                detail=detail,
                fix_code=fix_code,
                cause=cause,
                body=raw_body,
                data=data,
                request_id=request_id,
            )
        if status == 429:
            retry_after = headers.get("retry-after")
            retry_after_int = int(retry_after) if retry_after and retry_after.isdigit() else None
            raise RateLimitError(
                message,
                status=status,
                code=code,
                error_type=error_type,
                url=url,
                detail=detail,
                fix_code=fix_code,
                cause=cause,
                body=raw_body,
                data=data,
                retry_after=retry_after_int,
                request_id=request_id,
            )
        raise APIError(
            message,
            status=status,
            code=code,
            error_type=error_type,
            url=url,
            detail=detail,
            fix_code=fix_code,
            cause=cause,
            body=raw_body,
            data=data,
            request_id=request_id,
        )


def generate_idempotency_key() -> str:
    timestamp_ms = int(time.time() * 1000) & ((1 << 48) - 1)
    random = secrets.token_bytes(10)
    rand_a = int.from_bytes(random[:2], "big") & 0x0FFF
    rand_b = int.from_bytes(random[2:], "big") & ((1 << 62) - 1)
    value = (timestamp_ms << 80) | (0x7 << 76) | (rand_a << 64) | (0x2 << 62) | rand_b
    hex_value = f"{value:032x}"
    return f"{hex_value[:8]}-{hex_value[8:12]}-{hex_value[12:16]}-{hex_value[16:20]}-{hex_value[20:]}"
