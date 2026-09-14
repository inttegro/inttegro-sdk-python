"""Refund in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Refund(ApiModel):
    """Typed refund data in the refund resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    cancel_reason: str | None = field(init=False)
    """Omitted unless a reason was supplied when the refund was canceled. Optional; nullable. Python type: ``str | None``; wire name: ``cancel_reason``; JSON type: string"""
    canceled_at: datetime | None = field(init=False)
    """Omitted unless the refund was canceled before processing began. Optional; nullable. Python type: ``datetime | None``; wire name: ``canceled_at``; JSON type: string (date-time)"""
    created_at: datetime = field(init=False)
    """When the refund was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    custom_data: dict[str, str] | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``dict[str, str] | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    failed_at: datetime | None = field(init=False)
    """Omitted unless processing failed. Optional; nullable. Python type: ``datetime | None``; wire name: ``failed_at``; JSON type: string (date-time)"""
    failure: RefundFailure | None = field(init=False)
    """Sanitized terminal failure information. Optional; nullable. Python type: ``RefundFailure | None``; wire name: ``failure``; JSON type: object (RefundFailure)"""
    id: str = field(init=False)
    """Unique identifier for this refund. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    line_items: list[RefundLineItem] = field(init=False)
    """One or more immutable line-level refund allocations. Required. Python type: ``list[RefundLineItem]``; wire name: ``line_items``; JSON type: array of object (RefundLineItem) values"""
    order_id: str = field(init=False)
    """Identifier of the related order. Required. Python type: ``str``; wire name: ``order_id``; JSON type: string"""
    order_amount: Amount | None = field(init=False)
    """Total amount of the originating order captured when the refund was created. Optional; nullable. Python type: ``Amount | None``; wire name: ``order_amount``; JSON type: object (Amount)"""
    processing_at: datetime | None = field(init=False)
    """Omitted until processing starts. Optional; nullable. Python type: ``datetime | None``; wire name: ``processing_at``; JSON type: string (date-time)"""
    reason: RefundReasonValue = field(init=False)
    """The reason associated with this refund. Required. Python type: ``RefundReasonValue``; wire name: ``reason``; JSON type: object (RefundReason)"""
    reason_details: str | None = field(init=False)
    """The reason details associated with this refund. Optional; nullable. Python type: ``str | None``; wire name: ``reason_details``; JSON type: string. Constraints: maximum length 2048"""
    reference: str | None = field(init=False)
    """Merchant-defined external reference for the refund. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""
    settlement: RefundSettlement = field(init=False)
    """Immutable refund destination. Required. Python type: ``RefundSettlement``; wire name: ``settlement``; JSON type: object (RefundSettlement) selected by the required ``type`` discriminator"""
    status: Literal['canceled', 'failed', 'pending', 'processing', 'succeeded'] = field(init=False)
    """Current lifecycle status of the refund. Required. Python type: ``Literal['canceled', 'failed', 'pending', 'processing', 'succeeded']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``canceled``, ``failed``, ``pending``, ``processing``, ``succeeded``"""
    succeeded_at: datetime | None = field(init=False)
    """Omitted unless processing succeeded. Optional; nullable. Python type: ``datetime | None``; wire name: ``succeeded_at``; JSON type: string (date-time)"""
    total: Amount = field(init=False)
    """Monetary total, represented by a currency and an integer minor-unit value. Required. Python type: ``Amount``; wire name: ``total``; JSON type: object (Amount)"""

from inttegro.refund.line_item import LineItem as RefundLineItem
from inttegro.refund.failure import Failure as RefundFailure
from inttegro.refund.reason_value import ReasonValue as RefundReasonValue
from inttegro.refund.settlement import Settlement as RefundSettlement
