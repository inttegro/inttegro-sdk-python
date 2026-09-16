"""DataInput in the ``inttegro.customer`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.custom_data import CustomDataInput


@dataclass(frozen=True, slots=True, kw_only=True)
class DataInput(ApiRequest):
    """Parameters accepted by the data input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CustomerDataInput``.
    """
    reference: str | UnsetType = field(default=UNSET)
    """External reference ID for the customer. Optional. Python type: ``str``; wire name: ``reference``; JSON type: string"""
    custom_data: CustomDataInput | UnsetType = field(default=UNSET)
    """Merchant-defined values accepted on resource creation. Values are serialized to strings before storage. Optional. Python type: ``CustomDataInput``; wire name: ``custom_data``; JSON type: object (CustomDataInput)"""
    name: str
    """Customer's full name. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    email_address: str
    """Customer's email address. Required. Python type: ``str``; wire name: ``email_address``; JSON type: string (email)"""
    phone_number: str
    """Customer's phone number. Required. Python type: ``str``; wire name: ``phone_number``; JSON type: string"""
