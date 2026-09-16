"""InlineDetailsInput in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.price.inline_params import InlineParams as PriceParams


@dataclass(frozen=True, slots=True, kw_only=True)
class InlineDetailsInput(ApiRequest):
    """Parameters accepted by the inline details input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``InlineProductDetailsInput``.
    """
    about: str | UnsetType = field(default=UNSET)
    """Long-form description or marketing copy. Optional. Python type: ``str``; wire name: ``about``; JSON type: string"""
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    reference: str | UnsetType = field(default=UNSET)
    """Your SKU or internal product reference. Optional. Python type: ``str``; wire name: ``reference``; JSON type: string"""
    tax_code: str | UnsetType = field(default=UNSET)
    """Tax classification code. Optional. Python type: ``str``; wire name: ``tax_code``; JSON type: string"""
    name: str
    """Product name shown to the customer. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    price: PriceParams
    """An inline price supplied in a request. Required. Python type: ``PriceParams``; wire name: ``price``; JSON type: object (PriceParams)"""
    quantity: int
    """How many units the customer is purchasing. Required. Python type: ``int``; wire name: ``quantity``; JSON type: integer. Constraints: minimum 1"""
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause', ProductType.PHYSICAL, ProductType.DIGITAL, ProductType.SERVICE, ProductType.VOUCHER, ProductType.CUSTOM, ProductType.CAUSE]
    """Product type—affects shipping requirements. Required. Python type: ``Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause', ProductType.PHYSICAL, ProductType.DIGITAL, ProductType.SERVICE, ProductType.VOUCHER, ProductType.CUSTOM, ProductType.CAUSE]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``physical``, ``digital``, ``service``, ``voucher``, ``custom``, ``cause``"""

from inttegro.product.type import Type as ProductType
from inttegro.custom_data import CustomData
