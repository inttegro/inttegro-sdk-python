import json
import sys
import unittest
from dataclasses import FrozenInstanceError, is_dataclass
from datetime import datetime, timezone
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inttegro import InttegroClient
from inttegro.balance_transaction import BalanceTransaction
from inttegro.chime import EmailMailboxInput, EmailMessageInput
from inttegro.purchase_intent import UpdateRequest
from inttegro.refund import Refund


class StaticTransport:
    def __init__(self, body):
        self.body = body

    def __call__(self, request, timeout):
        del request, timeout
        return 200, {"content-type": "application/json"}, json.dumps(self.body)


class TypedModelTest(unittest.TestCase):
    def test_request_objects_are_frozen_and_preserve_wire_field_names(self):
        request = EmailMessageInput(
            subject="Payment receipt",
            text="Your payment succeeded.",
            from_=EmailMailboxInput(address="billing@example.com"),
        )

        self.assertTrue(is_dataclass(request))
        self.assertEqual(
            {
                "subject": "Payment receipt",
                "text": "Your payment succeeded.",
                "from": {"address": "billing@example.com"},
            },
            request.to_dict(),
        )
        with self.assertRaises(FrozenInstanceError):
            request.subject = "Changed"

    def test_endpoint_returns_nested_dataclass_models(self):
        client = InttegroClient(
            api_key="test",
            transport=StaticTransport(
                {
                    "refund": {
                        "id": "rf_1",
                        "order_id": "or_1",
                        "reason": "requested_by_customer",
                        "status": "pending",
                        "total": {"currency": "ghs", "value": 2500},
                        "line_items": [],
                        "created_at": "2026-09-02T12:00:00Z",
                    }
                }
            ),
        )

        response = client.refunds.lookup("rf_1")

        self.assertIsInstance(response, Refund)
        self.assertTrue(is_dataclass(response))
        self.assertEqual("rf_1", response.id)
        self.assertEqual(2500, response.total.value)
        self.assertIsInstance(response.created_at, datetime)
        self.assertEqual(timezone.utc, response.created_at.tzinfo)
        self.assertEqual("rf_1", response["id"])
        with self.assertRaises(FrozenInstanceError):
            response.id = "rf_2"

    def test_models_preserve_unknown_fields_and_round_trip(self):
        response = Refund.from_dict(
            {
                "id": "rf_1",
                "order_id": "or_1",
                "reason": "custom",
                "status": "failed",
                "total": {"currency": "ghs", "value": 100},
                "line_items": [],
                "created_at": "2026-09-02T12:00:00Z",
                "failure": {
                    "reason": "unknown",
                    "detail": "The refund could not be completed.",
                    "retryable": False,
                },
                "future_field": {"enabled": True},
            }
        )

        self.assertEqual({"enabled": True}, response["future_field"])
        self.assertEqual({"enabled": True}, response.to_dict()["future_field"])
        self.assertEqual("2026-09-02T12:00:00Z", response.to_dict()["created_at"])
        self.assertEqual("unknown", response.failure.reason)
        self.assertEqual(False, response.failure.retryable)

    def test_timestamp_fields_reject_values_without_an_offset(self):
        with self.assertRaisesRegex(ValueError, "UTC offset"):
            Refund.from_dict(
                {
                    "id": "rf_1",
                    "order_id": "or_1",
                    "reason": "custom",
                    "status": "pending",
                    "total": {"currency": "ghs", "value": 100},
                    "line_items": [],
                    "created_at": "2026-09-02T12:00:00",
                }
            )

    def test_request_timestamps_serialize_to_iso_8601(self):
        request = UpdateRequest(
            expires_at=datetime(2026, 10, 1, 12, 0, tzinfo=timezone.utc)
        )
        self.assertEqual("2026-10-01T12:00:00Z", request.to_dict()["expires_at"])

        with self.assertRaisesRegex(ValueError, "UTC offset"):
            UpdateRequest(expires_at=datetime(2026, 10, 1, 12, 0)).to_dict()

    def test_absent_optional_fields_retain_presence_semantics(self):
        response = BalanceTransaction.from_dict(
            {
                "id": "bt_1",
                "type": "payment",
                "amount": {"currency": "ghs", "value": 100},
                "created_at": "2026-09-02T12:00:00Z",
            }
        )

        self.assertFalse(hasattr(response, "refund_id"))
        self.assertNotIn("refund_id", response)
