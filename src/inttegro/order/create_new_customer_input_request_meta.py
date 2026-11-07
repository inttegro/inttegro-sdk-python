"""CreateNewCustomerInputRequestMeta in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.request import Response


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateNewCustomerInputRequestMeta(ApiRequest):
    """Optional metadata controlling request processing.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreateOrderNewCustomerInputRequestMeta``.
    """
    idempotency_key: str | UnsetType = field(default=UNSET)
    """Unique key to prevent duplicate order creation. Optional. Python type: ``str``; wire name: ``idempotency_key``; JSON type: string"""
    response: Response | UnsetType = field(default=UNSET)
    """Optional typed selection of public response properties. Python type: ``Response``; wire name: ``response``; JSON type: object (RequestResponse)"""
