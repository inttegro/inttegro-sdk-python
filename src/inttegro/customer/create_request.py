"""CreateRequest in the ``inttegro.customer`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequest(ApiRequest):
    """Parameters accepted by the create request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreateCustomerRequest``.
    """
    billing_address: CustomerAddressInput | UnsetType = field(default=UNSET)
    """The billing address associated with this create request. Optional. Python type: ``CustomerAddressInput``; wire name: ``billing_address``; JSON type: object (CustomerAddressInput)"""
    custom_data: CustomDataInput | UnsetType = field(default=UNSET)
    """Merchant-defined values accepted on resource creation. Values are serialized to strings before storage. Optional. Python type: ``CustomDataInput``; wire name: ``custom_data``; JSON type: object (CustomDataInput)"""
    email_address: str | UnsetType = field(default=UNSET)
    """Customer or recipient email address. Optional. Python type: ``str``; wire name: ``email_address``; JSON type: string. Constraints: minimum length 3; maximum length 254"""
    phone_number: str | UnsetType = field(default=UNSET)
    """Customer or recipient phone number in international form. Optional. Python type: ``str``; wire name: ``phone_number``; JSON type: string. Constraints: minimum length 7; maximum length 20"""
    reference: str | UnsetType = field(default=UNSET)
    """Merchant-defined external reference for the create request. Optional. Python type: ``str``; wire name: ``reference``; JSON type: string. Constraints: minimum length 1; maximum length 100"""
    shipping_address: CustomerAddressInput | UnsetType = field(default=UNSET)
    """The shipping address associated with this create request. Optional. Python type: ``CustomerAddressInput``; wire name: ``shipping_address``; JSON type: object (CustomerAddressInput)"""
    title: str | UnsetType = field(default=UNSET)
    """The title associated with this create request. Optional. Python type: ``str``; wire name: ``title``; JSON type: string. Constraints: minimum length 1; maximum length 20"""
    name: str
    """Human-readable name of the create request. Required. Python type: ``str``; wire name: ``name``; JSON type: string. Constraints: maximum length 200"""

from inttegro.customer.address_input import AddressInput as CustomerAddressInput
from inttegro.custom_data import CustomDataInput
