import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inttegro import (
    bank_account,
    broadcast,
    chime,
    order,
    payment,
    payment_method,
    price,
    product,
    schedule,
    wallet,
)
from inttegro.money import Amount, Currency


class DomainModuleTest(unittest.TestCase):
    def test_amount_and_price_types_preserve_request_and_response_shapes(self) -> None:
        inline_price_params = price.InlineParams(currency=Currency.GHS, value=3005)
        catalog_params = price.Params(
            type=price.Type.FIXED_AMOUNT,
            fixed_amount=inline_price_params,
            label="Retail",
        )
        catalog_price = price.Price.from_dict(
            {
                "id": "pr_123",
                "active": True,
                "type": "fixed_amount",
                "nominal": {"currency": "ghs", "value": 3005},
                "fixed_amount": {"currency": "ghs", "value": 3005},
                "product_id": "prod_123",
                "created_at": "2026-09-02T12:00:00Z",
            }
        )
        inline_price = price.Inline.from_dict({"currency": "eur", "value": 900})

        self.assertEqual({"currency": "ghs", "value": 3005}, inline_price_params.to_dict())
        self.assertEqual(
            {
                "type": "fixed_amount",
                "fixed_amount": {"currency": "ghs", "value": 3005},
                "label": "Retail",
            },
            catalog_params.to_dict(),
        )
        self.assertIsInstance(catalog_price.nominal, Amount)
        self.assertIsInstance(catalog_price.fixed_amount, Amount)
        self.assertEqual(Currency.GHS, catalog_price.nominal.currency)
        self.assertEqual("prod_123", catalog_price.product_id)
        self.assertEqual(Currency.EUR, inline_price.currency)
        self.assertEqual(Currency.GHS, Currency("GHS"))
        self.assertIsInstance(inline_price, price.Inline)

        with self.assertRaises(ValueError):
            price.Params(fixed_amount=inline_price_params)

        product_price = product.AddPriceRequest(
            product_id="prod_123",
            type=price.Type.FIXED_AMOUNT,
            fixed_amount=inline_price_params,
        )
        self.assertEqual(
            {
                "product_id": "prod_123",
                "type": "fixed_amount",
                "fixed_amount": {"currency": "ghs", "value": 3005},
            },
            product_price.to_dict(),
        )

        selected_params = price.Params(
            product_id="prod_123",
            type=price.Type.CUSTOMER_SELECTED_AMOUNT,
            customer_selected_amount=price.CustomerSelectedAmountParams(
                currency=Currency.GHS,
                minimum=500,
                suggested_amounts=[
                    price.SuggestedAmountParams(
                        id="supporter", value=1000, recommended=True
                    )
                ],
            ),
        )
        self.assertEqual(
            {
                "product_id": "prod_123",
                "type": "customer_selected_amount",
                "customer_selected_amount": {
                    "currency": "ghs",
                    "minimum": 500,
                    "suggested_amounts": [
                        {"id": "supporter", "value": 1000, "recommended": True}
                    ],
                },
            },
            selected_params.to_dict(),
        )

        selected_price = price.Price.from_dict(
            {
                "id": "pr_selected",
                "active": True,
                "type": "customer_selected_amount",
                "customer_selected_amount": {
                    "currency": "ghs",
                    "minimum": 500,
                    "suggested_amounts": [
                        {"id": "supporter", "value": 1000, "recommended": True}
                    ],
                },
                "product_id": "prod_123",
                "created_at": "2026-09-02T12:00:00Z",
            }
        )
        self.assertEqual(1000, selected_price.customer_selected_amount.suggested_amounts[0].value)

        catalog_product = product.CatalogWithCustomerSelectedPriceInput(
            product_id="prod_123",
            quantity=1,
            customer_selected_price=product.CustomerSelectedPriceInput(
                price_id="pr_selected",
                selected_amount=price.InlineParams(currency=Currency.GHS, value=750),
            ),
        )
        self.assertEqual(
            {
                "product_id": "prod_123",
                "quantity": 1,
                "customer_selected_price": {
                    "price_id": "pr_selected",
                    "selected_amount": {"currency": "ghs", "value": 750},
                },
            },
            catalog_product.to_dict(),
        )

    def test_payments_module_exposes_payment_lifecycle_types(self) -> None:
        payment_resource = payment.Payment.from_dict(
            {"id": "py_1", "status": "initiated", "amount": {"currency": "ghs", "value": 5000}}
        )

        self.assertEqual("py_1", payment_resource.id)
        self.assertEqual(5000, payment_resource.amount.value)
        self.assertEqual("initiated", payment.Status.INITIATED.value)
        self.assertEqual("mobile_money", payment_method.Type.MOBILE_MONEY.value)
        self.assertEqual("product", order.LineItemType.PRODUCT.value)
        self.assertEqual("digital", product.Type.DIGITAL.value)

    def test_chimes_module_exposes_chimes_broadcasts_and_schedules(self) -> None:
        chime_resource = chime.Chime.from_dict({"id": "ch_1"})
        broadcast_resource = broadcast.Broadcast.from_dict(
            {
                "id": "br_1",
                "recipients": ["+233544998605"],
                "content": "Hello",
                "sender_id": "Inttegro",
                "send_after": "2026-09-03T12:00:00Z",
                "created_at": "2026-09-03T11:00:00Z",
            }
        )
        schedule_resource = schedule.Schedule.from_dict(
            {
                "id": "sch_1",
                "recipients": ["+233544998605"],
                "content": "Hello later",
                "sender_id": "Inttegro",
                "send_after": "2026-09-04T12:00:00Z",
                "created_at": "2026-09-03T11:00:00Z",
            }
        )

        self.assertEqual("ch_1", chime_resource.id)
        self.assertEqual("br_1", broadcast_resource.id)
        self.assertEqual("sch_1", schedule_resource.id)
        self.assertEqual("sms", chime.Transport.SMS.value)

    def test_financial_account_variants_have_focused_modules(self) -> None:
        wallet_resource = wallet.Wallet.from_dict(
            {
                "id": "wallet_1",
                "type": "mobile_money",
                "mobile_money": {"account_number": "233200000000", "network": "mtn"},
            }
        )
        bank_account_resource = bank_account.BankAccount.from_dict(
            {
                "type": "ghana_bank_account",
                "ghana_bank_account": {
                    "number": "0123456789",
                    "holder": {
                        "name": "Yaw Boakye",
                        "address": {
                            "country": "GH",
                            "city": "Accra",
                            "line_1": "1 Independence Avenue",
                            "region": "Greater Accra",
                        },
                    },
                },
            }
        )

        self.assertEqual("mtn", wallet_resource.mobile_money.network)
        self.assertEqual("0123456789", bank_account_resource.ghana_bank_account.number)

        bank_params = bank_account.Params(
            type=bank_account.Type.GHANA_BANK_ACCOUNT,
            ghana_bank_account=bank_account.GhanaBankAccountParams(
                number="0123456789",
                sort_code="010100",
                holder=bank_account.OwnerParams(
                    name="Yaw Boakye",
                    address=bank_account.OwnerAddressParams(country="GH"),
                ),
            ),
        )
        self.assertEqual(
            "0123456789",
            bank_params.to_dict()["ghana_bank_account"]["number"],
        )


if __name__ == "__main__":
    unittest.main()
