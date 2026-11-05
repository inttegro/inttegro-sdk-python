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
    PaymentsCapabilitiesInput,
    UpdateRequest,
)
from inttegro.app import CreateRequest as CreateAppRequest


class PolicyTransport:
    def __init__(self) -> None:
        self.requests: list[tuple[str, dict]] = []

    def __call__(self, request, timeout):
        del timeout
        path = urllib.parse.urlparse(request.full_url).path
        payload = json.loads(request.data.decode("utf-8")) if request.data else {}
        self.requests.append((path, payload))
        if path == "/children_policies/lookup":
            body = {
                "children_policy": {
                    "id": "cp_123",
                    "version": 1,
                    "active_version": 1,
                    "name": "Default",
                    "capabilities": {},
                    "created_at": "2026-11-05T10:00:00Z",
                    "updated_at": "2026-11-05T10:00:00Z",
                    "version_created_at": "2026-11-05T10:00:00Z",
                }
            }
        else:
            body = {
                "operating_policy": {
                    "id": "op_123",
                    "version": 1,
                    "active_version": 1,
                    "name": "Retail",
                    "capabilities": {},
                    "children_policy_id": "cp_123",
                    "children_policy_version": 1,
                    "created_at": "2026-11-05T10:00:00Z",
                    "updated_at": "2026-11-05T10:00:00Z",
                    "version_created_at": "2026-11-05T10:00:00Z",
                }
            }
        return 200, {"content-type": "application/json"}, json.dumps(body)


class PolicyResourcesTest(unittest.TestCase):
    def test_policy_resources_and_app_selection(self) -> None:
        transport = PolicyTransport()
        client = InttegroClient(api_key="sk_test_123", transport=transport)
        capabilities = CapabilitiesInput(
            payments=PaymentsCapabilitiesInput(currencies=["ghs"]),
        )

        self.assertEqual("cp_123", client.children_policies.lookup().id)
        self.assertEqual(
            "op_123",
            client.operating_policies.create(
                CreateRequest(name="Retail", capabilities=capabilities)
            ).id,
        )
        self.assertEqual("op_123", client.operating_policies.lookup("op_123").id)
        self.assertEqual(
            1,
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


if __name__ == "__main__":
    unittest.main()
