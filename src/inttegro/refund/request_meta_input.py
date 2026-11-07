"""RequestMetaInput in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.request import Response


@dataclass(frozen=True, slots=True, kw_only=True)
class RequestMetaInput(ApiRequest):
    """Parameters accepted by the request meta input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``RefundRequestMetaInput``.
    """
    idempotency_key: str | UnsetType = field(default=UNSET)
    """Stable retry key carried inside ``request_meta``. It must match the ``Idempotency-Key`` header when both are provided. Optional. Python type: ``str``; wire name: ``idempotency_key``; JSON type: string. Constraints: minimum length 1; maximum length 255"""
    response: Response | UnsetType = field(default=UNSET)
    """Optional typed selection of public response properties. Python type: ``Response``; wire name: ``response``; JSON type: object (RequestResponse)"""
