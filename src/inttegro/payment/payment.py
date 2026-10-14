"""Payment in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Payment(ApiModel):
    """Payment intent tied to this order.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    id: str = field(init=False)
    """Payment intent ID. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    status: Literal['initiated', 'requires_action', 'overdue', 'executed', 'paid', 'canceled', 'expired', 'failed', 'unknown'] = field(init=False)
    """Payment state. Required. Python type: ``Literal['initiated', 'requires_action', 'overdue', 'executed', 'paid', 'canceled', 'expired', 'failed', 'unknown']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``initiated``, ``requires_action``, ``overdue``, ``executed``, ``paid``, ``canceled``, ``expired``, ``failed``, ``unknown``"""
    statement_descriptor: str = field(init=False)
    """Optional statement descriptor shown on the customer's bank statement. Required. Python type: ``str``; wire name: ``statement_descriptor``; JSON type: string"""
    amount: Amount = field(init=False)
    """Monetary amount, represented by a currency and an integer minor-unit value. Required. Python type: ``Amount``; wire name: ``amount``; JSON type: object (Amount)"""
    balance_transaction: BalanceTransaction | None = field(init=False)
    """Merchant balance entry caused by a payment or refund. `type` describes the semantic source, not direction. A payment transaction contains `payment_id`; a refund transaction contains `refund_id`. Exactly one matching reference is present. Optional; nullable. Python type: ``BalanceTransaction | None``; wire name: ``balance_transaction``; JSON type: object (BalanceTransaction)"""
    payment_method: PaymentMethodSnapshot | None = field(init=False)
    """The payment method associated with this payment. Optional; nullable. Python type: ``PaymentMethodSnapshot | None``; wire name: ``payment_method``; JSON type: object (OrderPaymentMethod)"""
    billing_details: PaymentBillingDetails | None = field(init=False)
    """The billing details associated with this payment. Optional; nullable. Python type: ``PaymentBillingDetails | None``; wire name: ``billing_details``; JSON type: object"""
    customer: OrderCustomer | None = field(init=False)
    """The customer associated with this payment. Optional; nullable. Python type: ``OrderCustomer | None``; wire name: ``customer``; JSON type: object"""
    receipt: OrderReceipt | None = field(init=False)
    """Receipt issued for a paid order payment. Optional; nullable. Python type: ``OrderReceipt | None``; wire name: ``receipt``; JSON type: object"""
    latest_attempt: PaymentAttempt | None = field(init=False)
    """Most recent payment attempt details. Optional; nullable. Python type: ``PaymentAttempt | None``; wire name: ``latest_attempt``; JSON type: object"""
    next_action: PaymentNextAction | None = field(init=False)
    """Next action required to complete a payment. Optional; nullable. Python type: ``PaymentNextAction | None``; wire name: ``next_action``; JSON type: object (PaymentNextAction)"""
    latest_error: PaymentError | None = field(init=False)
    """The latest error associated with this payment. Optional; nullable. Python type: ``PaymentError | None``; wire name: ``latest_error``; JSON type: object"""
    initiated_at: datetime = field(init=False)
    """When we kicked off the payment intent. Required. Python type: ``datetime``; wire name: ``initiated_at``; JSON type: string (date-time)"""
    executed_at: datetime | None = field(init=False)
    """When payment execution started. Optional; nullable. Python type: ``datetime | None``; wire name: ``executed_at``; JSON type: string (date-time)"""
    paid_at: datetime | None = field(init=False)
    """When payment completed successfully. Optional; nullable. Python type: ``datetime | None``; wire name: ``paid_at``; JSON type: string (date-time)"""
    canceled_at: datetime | None = field(init=False)
    """When payment was canceled. Optional; nullable. Python type: ``datetime | None``; wire name: ``canceled_at``; JSON type: string (date-time)"""
    due_at: datetime | None = field(init=False)
    """When payment becomes overdue. Optional; nullable. Python type: ``datetime | None``; wire name: ``due_at``; JSON type: string (date-time)"""
    expired_at: datetime | None = field(init=False)
    """When payment expired. Optional; nullable. Python type: ``datetime | None``; wire name: ``expired_at``; JSON type: string (date-time)"""
    failed_at: datetime | None = field(init=False)
    """When payment failed. Optional; nullable. Python type: ``datetime | None``; wire name: ``failed_at``; JSON type: string (date-time)"""
    paid_offline: bool | None = field(init=False)
    """Whether payment was recorded as received outside Inttegro. Optional; nullable. Python type: ``bool | None``; wire name: ``paid_offline``; JSON type: boolean"""
    payment_method_types: list[str] | None = field(init=False)
    """The payment method types associated with this payment. Optional; nullable. Python type: ``list[str] | None``; wire name: ``payment_method_types``; JSON type: array of string values"""
    payout_configuration: PaymentPayoutConfiguration | None = field(init=False)
    """Payout configuration for this payment. Optional; nullable. Python type: ``PaymentPayoutConfiguration | None``; wire name: ``payout_configuration``; JSON type: object"""

    def is_paid(self) -> bool:
        """Whether the payment completed successfully."""
        return self.status == "paid"

    def requires_action(self) -> bool:
        """Whether the payment is waiting for customer or merchant action."""
        return self.status == "requires_action"

    def is_terminal(self) -> bool:
        """Whether the payment has reached a final state."""
        return self.status in {"paid", "canceled", "expired", "failed"}

    def required_action(self) -> PaymentNextAction | None:
        """Return action details when the payment currently requires action."""
        return getattr(self, "next_action", None) if self.requires_action() else None

from inttegro.balance_transaction.balance_transaction import BalanceTransaction
from inttegro.order.customer import Customer as OrderCustomer
from inttegro.order.receipt import Receipt as OrderReceipt
from inttegro.payment.attempt import Attempt as PaymentAttempt
from inttegro.payment.billing_details import BillingDetails as PaymentBillingDetails
from inttegro.payment.error import Error as PaymentError
from inttegro.payment.payment_method import PaymentMethod as PaymentMethodSnapshot
from inttegro.payment.next_action import NextAction as PaymentNextAction
from inttegro.payment.payout_configuration import PayoutConfiguration as PaymentPayoutConfiguration
