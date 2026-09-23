import json
import sys
import unittest
from dataclasses import FrozenInstanceError, is_dataclass
from datetime import datetime, timezone
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inttegro import CustomData, CustomDataInput, CustomDataPatch, InttegroClient
from inttegro.balance_transaction import BalanceTransaction
from inttegro.chime import EmailMailboxInput, EmailMessageInput
from inttegro.customer import CreateRequest as CreateCustomerRequest
from inttegro.customer import Customer
from inttegro.purchase_intent import UpdateRequest
from inttegro.payout import Payout
from inttegro.refund import (
    PaymentMethodSettlement,
    Refund,
    SettlementBankAccountPaymentMethod,
)


class StaticTransport:
    def __init__(self, body):
        self.body = body

    def __call__(self, request, timeout):
        del request, timeout
        return 200, {"content-type": "application/json"}, json.dumps(self.body)


class TypedModelTest(unittest.TestCase):
    def test_payout_decodes_balance_transaction_contributions(self):
        payout = Payout.from_dict(
            {
                "id": "po_1",
                "destination_id": "fa_1",
                "execute_after": "2026-09-02T12:00:00Z",
                "initiated_at": "2026-09-02T11:00:00Z",
                "max_amount": {"currency": "ghs", "value": 5000},
                "status": "processing",
                "balance_transactions": [
                    {
                        "id": "bt_1",
                        "amount": {"currency": "ghs", "value": 5000},
                        "allocated_amount": {"currency": "ghs", "value": 2000},
                    }
                ],
            }
        )

        self.assertEqual("bt_1", payout.balance_transactions[0].id)
        self.assertEqual(5000, payout.balance_transactions[0].amount.value)
        self.assertEqual(2000, payout.balance_transactions[0].allocated_amount.value)

    def test_customer_addresses_and_custom_data_keep_semantic_types(self):
        request = CreateCustomerRequest(
            name="Ama Mensah",
            custom_data=CustomDataInput({"segment": "vip", "visits": 3}),
        )
        self.assertEqual(
            {"segment": "vip", "visits": 3},
            request.to_dict()["custom_data"],
        )

        customer = Customer.from_dict(
            {
                "balance": {},
                "billing_address": {"country": "gh", "city": "Accra"},
                "created_at": "2026-09-02T12:00:00Z",
                "custom_data": {"segment": "vip"},
                "guest": False,
                "id": "cu_1",
                "name": "Ama Mensah",
                "shipping_address": {"country": "gh", "city": "Kumasi"},
            }
        )
        self.assertIsInstance(customer.custom_data, CustomData)
        self.assertEqual("Accra", customer.billing_address.city)
        self.assertEqual("Kumasi", customer.shipping_address.city)

    def test_custom_data_patch_distinguishes_unset_from_omission(self):
        patch = CustomDataPatch().set("segment", "returning").unset("legacy")
        self.assertEqual(
            {"segment": "returning", "legacy": None},
            patch.to_dict(),
        )

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
                        "settlement": {"type": "offline"},
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
                "settlement": {"type": "offline"},
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

    def test_refund_settlement_is_discriminated_and_strict(self):
        refund = Refund.from_dict(
            {
                "id": "rf_1",
                "order_id": "or_1",
                "reason": "requested_by_customer",
                "settlement": {
                    "type": "payment_method",
                    "payment_method": {
                        "id": "pm_123",
                        "type": "bank_account",
                        "bank_account": {
                            "type": "ghana_bank_account",
                            "ghana_bank_account": {
                                "account_number": "****1234",
                                "last4": "1234",
                            },
                        },
                    },
                },
                "status": "pending",
                "total": {"currency": "ghs", "value": 100},
                "line_items": [],
                "created_at": "2026-09-02T12:00:00Z",
            }
        )

        self.assertIsInstance(refund.settlement, PaymentMethodSettlement)
        self.assertIsInstance(
            refund.settlement.payment_method,
            SettlementBankAccountPaymentMethod,
        )
        self.assertEqual(
            "****1234",
            refund.settlement.payment_method.bank_account.ghana_bank_account.account_number,
        )

        with self.assertRaisesRegex(ValueError, "invalid OfflineSettlement shape"):
            Refund.from_dict(
                {
                    "id": "rf_1",
                    "order_id": "or_1",
                    "reason": "requested_by_customer",
                    "settlement": {
                        "type": "offline",
                        "payment_method": {"id": "pm_123"},
                    },
                    "status": "pending",
                    "total": {"currency": "ghs", "value": 100},
                    "line_items": [],
                    "created_at": "2026-09-02T12:00:00Z",
                }
            )

        with self.assertRaisesRegex(ValueError, "PaymentMethodSettlement"):
            Refund.from_dict(
                {
                    "id": "rf_1",
                    "order_id": "or_1",
                    "reason": "requested_by_customer",
                    "settlement": {"type": "payment_method"},
                    "status": "pending",
                    "total": {"currency": "ghs", "value": 100},
                    "line_items": [],
                    "created_at": "2026-09-02T12:00:00Z",
                }
            )

    def test_timestamp_fields_reject_values_without_an_offset(self):
        with self.assertRaisesRegex(ValueError, "UTC offset"):
            Refund.from_dict(
                {
                    "id": "rf_1",
                    "order_id": "or_1",
                    "reason": "custom",
                    "settlement": {"type": "offline"},
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

    def test_balance_transaction_decodes_public_allocations(self):
        response = BalanceTransaction.from_dict(
            {
                "id": "bt_1",
                "type": "payment",
                "payment_id": "py_1",
                "order_id": "or_1",
                "amount": {"currency": "ghs", "value": 2500},
                "available_amount": {"currency": "ghs", "value": 1500},
                "pending_amount": {"currency": "ghs", "value": 1000},
                "spent_amount": {"currency": "ghs", "value": 0},
                "allocations": [
                    {
                        "id": "bta_1",
                        "type": "payout",
                        "status": "pending",
                        "payout": {
                            "id": "po_1",
                            "amount": {"currency": "ghs", "value": 1000},
                        },
                        "created_at": "2026-09-02T12:01:00Z",
                        "updated_at": "2026-09-02T12:01:00Z",
                    }
                ],
                "created_at": "2026-09-02T12:00:00Z",
            }
        )

        self.assertEqual(1500, response.available_amount.value)
        self.assertEqual("payout", response.allocations[0].type)
        self.assertEqual("po_1", response.allocations[0].payout.id)
