"""InvoiceSettingsInput in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.custom_data import CustomData


@dataclass(frozen=True, slots=True, kw_only=True)
class InvoiceSettingsInput(ApiRequest):
    """Order-level invoice rendering data. Pages uses this data when rendering invoice web and download views.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.
    """
    number: str | UnsetType = field(default=UNSET)
    """Optional invoice number. When omitted, invoice delivery falls back to the order number and then the order ID for labels. Optional. Python type: ``str``; wire name: ``number``; JSON type: string"""
    memo: str | UnsetType = field(default=UNSET)
    """Optional invoice memo. Optional. Python type: ``str``; wire name: ``memo``; JSON type: string"""
    footer: str | UnsetType = field(default=UNSET)
    """Optional invoice footer. Optional. Python type: ``str``; wire name: ``footer``; JSON type: string"""
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
