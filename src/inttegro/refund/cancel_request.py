"""CancelRequest in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CancelRequest(ApiRequest):
    """Parameters accepted by the cancel request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CancelRefundRequest``.
    """
    reason: str | UnsetType = field(default=UNSET)
    """Optional explanation for canceling the refund. Leading and trailing whitespace is removed. Optional. Python type: ``str``; wire name: ``reason``; JSON type: string. Constraints: minimum length 1; maximum length 2048"""
    request_meta: RefundRequestMetaInput | UnsetType = field(default=UNSET)
    """The request meta associated with this cancel request. Optional. Python type: ``RefundRequestMetaInput``; wire name: ``request_meta``; JSON type: object (RefundRequestMeta)"""
    refund_id: str
    """Refund to cancel before processing begins. Required. Python type: ``str``; wire name: ``refund_id``; JSON type: string"""

from inttegro.refund.request_meta_input import RequestMetaInput as RefundRequestMetaInput
