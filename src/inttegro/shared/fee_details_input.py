"""FeeDetailsInput in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.money import AmountParams
from inttegro.custom_data import CustomData


@dataclass(frozen=True, slots=True, kw_only=True)
class FeeDetailsInput(ApiRequest):
    """Parameters accepted by the fee details input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.
    """
    id: str | UnsetType = field(default=UNSET)
    """Fee identifier. Optional. Python type: ``str``; wire name: ``id``; JSON type: string"""
    label: str | UnsetType = field(default=UNSET)
    """Customer-facing label for this fee. Optional. Python type: ``str``; wire name: ``label``; JSON type: string"""
    tax_code: str | UnsetType = field(default=UNSET)
    """The tax classification code for the shipping fee. Optional. Python type: ``str``; wire name: ``tax_code``; JSON type: string"""
    description: str | UnsetType = field(default=UNSET)
    """Customer-facing description for this fee. Optional. Python type: ``str``; wire name: ``description``; JSON type: string"""
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    amount: AmountParams
    """Monetary amount, represented by a currency and an integer minor-unit value. Required. Python type: ``AmountParams``; wire name: ``amount``; JSON type: object (AmountParams)"""
