import json
import sys
import unittest
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inttegro import InttegroClient
from inttegro.operating_policy import (
    CapabilitiesInput,
    CreateRequest,
    IDSelection,
    PageRequest as OperatingPolicyPageRequest,
    PaymentsCapabilitiesInput,
    UpdateRequest,
)
from inttegro.children_policy import PageRequest as ChildrenPolicyPageRequest
from inttegro.app import CreateRequest as CreateAppRequest


class PolicyTransport:
    def __init__(self) -> None:
        self.requests: list[tuple[str, dict]] = []

    def __call__(self, request, timeout):
        del timeout
        path = urllib.parse.urlparse(request.full_url).path
        payload = json.loads(request.data.decode("utf-8")) if request.data else {}
        self.requests.append((path, payload))
        version = payload.get("version", 2)
        policy = {
            "id": "cp_123",
            "version": version,
            "active_version": 2,
            "name": "Default",
            "capabilities": {},
            "created_at": "2026-11-05T10:00:00Z",
            "updated_at": "2026-11-05T10:00:00Z",
            "version_created_at": "2026-11-05T10:00:00Z",
        }
        if path.startswith("/operating_policies/"):
            policy.update({
                "id": "op_123",
                "name": "Retail",
                "children_policy_id": "cp_123",
                "children_policy_version": 2,
            })
        if path.endswith("/page"):
            body = {
                "page": {
                    "number": 2,
                    "size": 1,
                    "count": 1,
                    "total": 2,
                    "has_more": True,
                    "versions": [policy],
                }
            }
        elif path == "/children_policies/lookup":
            body = {"children_policy": policy}
        else:
            body = {"operating_policy": policy}
        return 200, {"content-type": "application/json"}, json.dumps(body)


class PolicyResourcesTest(unittest.TestCase):
    def test_policy_resources_and_app_selection(self) -> None:
        transport = PolicyTransport()
        client = InttegroClient(api_key="sk_test_123", transport=transport)
        capabilities = CapabilitiesInput(
            payments=PaymentsCapabilitiesInput(currencies=["ghs"]),
        )

        self.assertEqual(2, client.children_policies.lookup().version)
        self.assertEqual(1, client.children_policies.lookup(1).version)
        children_page = client.children_policies.page(
            ChildrenPolicyPageRequest(number=2, size=1)
        )
        self.assertTrue(children_page.has_more)
        self.assertEqual("cp_123", children_page.versions[0].id)
        self.assertEqual(
            "op_123",
            client.operating_policies.create(
                CreateRequest(name="Retail", capabilities=capabilities)
            ).id,
        )
        self.assertEqual(2, client.operating_policies.lookup("op_123").version)
        self.assertEqual(1, client.operating_policies.lookup("op_123", version=1).version)
        operating_page = client.operating_policies.page(
            OperatingPolicyPageRequest(
                operating_policy_id="op_123",
                number=2,
                size=1,
            )
        )
        self.assertEqual(2, operating_page.total)
        self.assertEqual("op_123", operating_page.versions[0].id)
        self.assertEqual(
            2,
            client.operating_policies.update(
                UpdateRequest(
                    operating_policy_id="op_123",
                    expected_version=1,
                    name="Retail v2",
                )
            ).version,
        )

        app_request = CreateAppRequest(
            name="Child",
            operating_policy=IDSelection(id="op_123"),
        )
        self.assertEqual(
            {"id": "op_123"},
            app_request.to_dict()["operating_policy"],
        )
        self.assertEqual(("/children_policies/lookup", {}), transport.requests[0])
        self.assertEqual(("/children_policies/lookup", {"version": 1}), transport.requests[1])
        self.assertEqual(
            ("/children_policies/page", {"number": 2, "size": 1}),
            transport.requests[2],
        )
        self.assertIn(
            ("/operating_policies/lookup", {"operating_policy_id": "op_123"}),
            transport.requests,
        )
        self.assertIn(
            (
                "/operating_policies/lookup",
                {"operating_policy_id": "op_123", "version": 1},
            ),
            transport.requests,
        )
        self.assertIn(
            (
                "/operating_policies/page",
                {"operating_policy_id": "op_123", "number": 2, "size": 1},
            ),
            transport.requests,
        )

    def test_policy_versions_must_be_positive(self) -> None:
        client = InttegroClient(api_key="sk_test_123", transport=PolicyTransport())

        with self.assertRaisesRegex(ValueError, "version"):
            client.children_policies.lookup(0)
        with self.assertRaisesRegex(ValueError, "version"):
            client.operating_policies.lookup("op_123", version=0)


if __name__ == "__main__":
    unittest.main()
