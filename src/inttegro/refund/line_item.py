"""LineItem in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LineItem(ApiModel):
    """Typed line item data in the refund resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``RefundLineItem``.
    """
    id: str = field(init=False)
    """Server-generated refund line-item identifier. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    order_line_item_id: str = field(init=False)
    """Deprecated compatibility identifier. Use ``order_line_item.id`` when available. Required. Python type: ``str``; wire name: ``order_line_item_id``; JSON type: string"""
    order_line_item: RefundOrderLineItem | None = field(init=False)
    """Immutable display snapshot of the refunded order line. Optional; nullable. Python type: ``RefundOrderLineItem | None``; wire name: ``order_line_item``; JSON type: object (RefundOrderLineItem)"""
    original_amount_paid: Amount = field(init=False)
    """Monetary original amount paid, represented by a currency and an integer minor-unit value. Required. Python type: ``Amount``; wire name: ``original_amount_paid``; JSON type: object (Amount)"""
    reason: RefundReasonValue | None = field(init=False)
    """The reason associated with this line item. Optional; nullable. Python type: ``RefundReasonValue | None``; wire name: ``reason``; JSON type: object (RefundReason)"""
    reason_details: str | None = field(init=False)
    """The reason details associated with this line item. Optional; nullable. Python type: ``str | None``; wire name: ``reason_details``; JSON type: string. Constraints: maximum length 2048"""
    refund_amount: Amount = field(init=False)
    """Monetary refund amount, represented by a currency and an integer minor-unit value. Required. Python type: ``Amount``; wire name: ``refund_amount``; JSON type: object (Amount)"""

from inttegro.refund.reason_value import ReasonValue as RefundReasonValue
from inttegro.refund.order_line_item import OrderLineItem as RefundOrderLineItem
