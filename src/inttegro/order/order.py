"""Order in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Order(ApiModel):
    """Complete order record with line items, customer details, payment state, and fulfillment information.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    canceled_at: datetime | None = field(init=False)
    """When the order was canceled. Omitted otherwise. Optional; nullable. Python type: ``datetime | None``; wire name: ``canceled_at``; JSON type: string (date-time)"""
    checkout_settings: OrderCheckoutSettings | None = field(init=False)
    """Checkout and payment flow configuration for this order. Optional; nullable. Python type: ``OrderCheckoutSettings | None``; wire name: ``checkout_settings``; JSON type: object"""
    completed_at: datetime | None = field(init=False)
    """When the order was completed. Omitted otherwise. Optional; nullable. Python type: ``datetime | None``; wire name: ``completed_at``; JSON type: string (date-time)"""
    created_from: OrderCreatedFrom | None = field(init=False)
    """Attribution for the public resource that created this order, when available. Optional; nullable. Python type: ``OrderCreatedFrom | None``; wire name: ``created_from``; JSON type: object"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    customer: OrderCustomer = field(init=False)
    """The customer associated with this order. Required. Python type: ``OrderCustomer``; wire name: ``customer``; JSON type: object"""
    expires_at: datetime | None = field(init=False)
    """When the order expires. Omitted when no expiry is set. Optional; nullable. Python type: ``datetime | None``; wire name: ``expires_at``; JSON type: string (date-time)"""
    id: str = field(init=False)
    """Unique identifier for this order. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    initiated_at: datetime = field(init=False)
    """When order processing began. Required. Python type: ``datetime``; wire name: ``initiated_at``; JSON type: string (date-time)"""
    invoice: OrderInvoice | None = field(init=False)
    """The invoice associated with this order. Optional; nullable. Python type: ``OrderInvoice | None``; wire name: ``invoice``; JSON type: object"""
    number: str | None = field(init=False)
    """Human-readable order number. Optional; nullable. Python type: ``str | None``; wire name: ``number``; JSON type: string"""
    receipt_number: str | None = field(init=False)
    """Merchant-provided receipt number, when set. Optional; nullable. Python type: ``str | None``; wire name: ``receipt_number``; JSON type: string"""
    refunds: list[Refund] | None = field(init=False)
    """All refunds issued for this order, newest first. Omitted when no refunds exist. Optional; nullable. Python type: ``list[Refund] | None``; wire name: ``refunds``; JSON type: array of object (Refund) values"""
    invoice_settings: InvoiceSettings | None = field(init=False)
    """Order-level invoice rendering data. Pages uses this data when rendering invoice web and download views. Optional; nullable. Python type: ``InvoiceSettings | None``; wire name: ``invoice_settings``; JSON type: object (InvoiceSettings)"""
    status: Literal['preparing', 'requires_payment', 'paid', 'completed', 'canceled', 'expired', 'unknown'] = field(init=False)
    """Current lifecycle state of the order. Required. Python type: ``Literal['preparing', 'requires_payment', 'paid', 'completed', 'canceled', 'expired', 'unknown']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``preparing``, ``requires_payment``, ``paid``, ``completed``, ``canceled``, ``expired``, ``unknown``"""
    sealed_at: datetime | None = field(init=False)
    """When the order was finalized and became immutable—ready for payment or fulfillment. Optional; nullable. Python type: ``datetime | None``; wire name: ``sealed_at``; JSON type: string (date-time)"""
    line_item_group: OrderLineItemGroup | None = field(init=False)
    """Cart contents and totals. Optional; nullable. Python type: ``OrderLineItemGroup | None``; wire name: ``line_item_group``; JSON type: object"""
    payment: Payment | None = field(init=False)
    """Payment intent tied to this order. Optional; nullable. Python type: ``Payment | None``; wire name: ``payment``; JSON type: object"""
    paid_at: datetime | None = field(init=False)
    """When the order became paid. Optional; nullable. Python type: ``datetime | None``; wire name: ``paid_at``; JSON type: string (date-time)"""
    payment_due_at: datetime | None = field(init=False)
    """When the order payment becomes overdue. Optional; nullable. Python type: ``datetime | None``; wire name: ``payment_due_at``; JSON type: string (date-time)"""
    reference: str | None = field(init=False)
    """External order reference when present. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""

    def is_paid(self) -> bool:
        """Whether the order has recorded payment, including after completion."""
        return self.status == "paid" or getattr(self, "paid_at", None) is not None

    def requires_payment(self) -> bool:
        """Whether the order is waiting for payment."""
        return self.status == "requires_payment"

    def is_terminal(self) -> bool:
        """Whether the order has reached a final state."""
        return self.status in {"paid", "completed", "canceled", "expired"}

    def required_payment_action(self) -> PaymentNextAction | None:
        """Return nested action details when the order payment requires action."""
        payment = getattr(self, "payment", None)
        return payment.required_action() if payment is not None else None

from inttegro.order.invoice_settings import InvoiceSettings
from inttegro.order.checkout_settings import CheckoutSettings as OrderCheckoutSettings
from inttegro.order.created_from import CreatedFrom as OrderCreatedFrom
from inttegro.order.customer import Customer as OrderCustomer
from inttegro.order.invoice import Invoice as OrderInvoice
from inttegro.order.line_item_group import LineItemGroup as OrderLineItemGroup
from inttegro.payment.payment import Payment
from inttegro.payment.next_action import NextAction as PaymentNextAction
from inttegro.refund.refund import Refund
from inttegro.custom_data import CustomData
