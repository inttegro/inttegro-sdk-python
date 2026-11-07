import asyncio
import inspect
import json
import subprocess
import sys
import unittest
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import httpx

from inttegro import AsyncInttegroClient, AuthenticationError, InttegroClient
from inttegro.order import Order


ORDER_BODY = {
    "id": "or_async_123",
    "status": "preparing",
    "initiated_at": "2026-09-07T12:00:00Z",
    "customer": {"id": "cu_123", "guest": True, "name": "Ama Mensah"},
}


class AsyncTransportRecorder:
    def __init__(self) -> None:
        self.requests = []

    async def __call__(self, req, timeout):
        self.requests.append(req)
        await asyncio.sleep(0)
        path = urllib.parse.urlparse(req.full_url).path
        body = json.loads(req.data.decode("utf-8")) if req.data else {}
        if path.startswith("/orders/"):
            response = {"order": ORDER_BODY}
        else:
            response = body or {"ok": True}
        return 200, {"content-type": "application/json"}, json.dumps(response)


class AsyncClientTest(unittest.IsolatedAsyncioTestCase):
    async def test_response_envelope_exposes_response_only_metadata(self) -> None:
        async def transport(req, timeout):
            del req, timeout
            await asyncio.sleep(0)
            return (
                200,
                {
                    "content-type": "application/json",
                    "x-request-id": "req_async_meta",
                    "retry-after": "12",
                },
                json.dumps(
                    {
                        "order": ORDER_BODY,
                        "response_meta": {
                            "request_id": "req_async_meta",
                            "debug": {"provider_attempts": 1},
                        },
                    }
                ),
            )

        async with AsyncInttegroClient(api_key="sk_test_async", transport=transport) as client:
            response = await client.orders.create_with_response({"line_items": []})

        self.assertIsInstance(response.data, Order)
        self.assertEqual("or_async_123", response.data.id)
        self.assertEqual(200, response.status)
        self.assertEqual("req_async_meta", response.request_id)
        self.assertEqual("12", response.retry_after)
        self.assertEqual("req_async_meta", response.meta["request_id"])

    async def test_resource_request_is_awaitable_and_decodes_typed_models(self) -> None:
        recorder = AsyncTransportRecorder()
        async with AsyncInttegroClient(api_key="sk_test_async", transport=recorder) as client:
            pending = client.orders.lookup("or_async_123")
            self.assertTrue(inspect.isawaitable(pending))
            order = await pending

        self.assertIsInstance(order, Order)
        self.assertEqual("or_async_123", order.id)
        self.assertEqual("Bearer sk_test_async", recorder.requests[0].get_header("Authorization"))

    async def test_mutations_receive_request_meta_idempotency(self) -> None:
        recorder = AsyncTransportRecorder()
        async with AsyncInttegroClient(api_key="sk_test_async", transport=recorder) as client:
            await client.products.create({"name": "Seed contribution"})

        payload = json.loads(recorder.requests[0].data.decode("utf-8"))
        key = payload["request_meta"]["idempotency_key"]
        self.assertRegex(key, r"^[0-9a-f-]{36}$")

    async def test_httpx_transport_maps_api_errors(self) -> None:
        async def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(
                401,
                headers={"x-request-id": "req_async"},
                json={"error": {"code": "invalid_api_key", "message": "invalid key"}},
            )

        http_client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
        client = AsyncInttegroClient(api_key="bad", http_client=http_client)
        with self.assertRaises(AuthenticationError) as raised:
            await client.orders.lookup("or_async_123")
        self.assertEqual("req_async", raised.exception.request_id)

        await client.aclose()
        self.assertFalse(http_client.is_closed, "injected HTTP clients remain application-owned")
        await http_client.aclose()

    async def test_closed_sdk_owned_client_rejects_requests(self) -> None:
        client = AsyncInttegroClient(api_key="sk_test_async", transport=AsyncTransportRecorder())
        await client.aclose()
        with self.assertRaisesRegex(RuntimeError, "closed"):
            await client.orders.lookup("or_async_123")


class AsyncSurfaceParityTest(unittest.TestCase):
    def test_package_import_does_not_request_entropy(self) -> None:
        """Worker snapshots import modules before request-scoped entropy exists."""

        script = """
import os

def reject_entropy(length):
    raise AssertionError(f\"os.urandom({length}) called during import\")

os.urandom = reject_entropy
import inttegro
assert inttegro.AsyncInttegroClient
"""
        result = subprocess.run(
            [sys.executable, "-c", script],
            cwd=Path(__file__).resolve().parents[1],
            env={"PYTHONPATH": str(Path(__file__).resolve().parents[1] / "src")},
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_every_sync_resource_method_has_an_async_counterpart(self) -> None:
        sync_client = InttegroClient(api_key="sk_test_sync", transport=lambda req, timeout: (200, {}, "{}"))
        async_client = AsyncInttegroClient(api_key="sk_test_async", transport=AsyncTransportRecorder())

        resource_names = sorted(name for name in sync_client.__dict__ if name != "http")
        self.assertEqual(resource_names, sorted(name for name in async_client.__dict__ if name != "http"))
        for resource_name in resource_names:
            sync_resource = getattr(sync_client, resource_name)
            async_resource = getattr(async_client, resource_name)
            sync_methods = {
                name
                for name in dir(sync_resource)
                if not name.startswith("_") and callable(getattr(sync_resource, name))
            }
            async_methods = {
                name
                for name in dir(async_resource)
                if not name.startswith("_") and callable(getattr(async_resource, name))
            }
            self.assertEqual(sync_methods, async_methods, resource_name)
            for method_name in sync_methods:
                self.assertTrue(
                    inspect.iscoroutinefunction(getattr(async_resource, method_name)),
                    f"{resource_name}.{method_name} must be async",
                )

        asyncio.run(async_client.aclose())

    def test_generated_async_resources_are_current(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/generate_async_resources.py", "--check"],
            cwd=Path(__file__).resolve().parents[1],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
