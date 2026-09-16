"""CreateRequest in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequest(ApiRequest):
    """Parameters accepted by the create request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreateRefundRequest``.
    """
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    reason_details: str | UnsetType = field(default=UNSET)
    """Overall explanation. Required when `reason` is `custom`. Optional. Python type: ``str``; wire name: ``reason_details``; JSON type: string. Constraints: maximum length 2048"""
    reference: str | UnsetType = field(default=UNSET)
    """Your reconciliation reference. Optional. Python type: ``str``; wire name: ``reference``; JSON type: string. Constraints: maximum length 256"""
    request_meta: RefundRequestMetaInput | UnsetType = field(default=UNSET)
    """The request meta associated with this create request. Optional. Python type: ``RefundRequestMetaInput``; wire name: ``request_meta``; JSON type: object (RefundRequestMeta)"""
    line_items: list[CreateRefundLineItemInput]
    """The line items associated with this create request. Required. Python type: ``list[CreateRefundLineItemInput]``; wire name: ``line_items``; JSON type: array of object (CreateRefundLineItem) values. Constraints: minimum items 1; maximum items 64"""
    order_id: str
    """Paid order to refund. Required. Python type: ``str``; wire name: ``order_id``; JSON type: string"""
    reason: RefundReasonInput
    """The reason associated with this create request. Required. Python type: ``RefundReasonInput``; wire name: ``reason``; JSON type: object (RefundReason)"""

from inttegro.refund.create_line_item_input import CreateLineItemInput as CreateRefundLineItemInput
from inttegro.refund.reason_input import ReasonInput as RefundReasonInput
from inttegro.refund.request_meta_input import RequestMetaInput as RefundRequestMetaInput
from inttegro.custom_data import CustomData
