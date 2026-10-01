"""Params in the ``inttegro.price`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.money import AmountParams
from inttegro.price.customer_selected_amount_params import CustomerSelectedAmountParams
from inttegro.price.type import Type


@dataclass(frozen=True, slots=True, kw_only=True)
class Params(ApiRequest):
    """Parameters accepted by the params operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CatalogPriceParams``.
    """
    product_id: str | UnsetType = field(default=UNSET)
    """Product ID to associate with the price. Optional for fixed prices, required for customer-selected prices, and immutable once set. Python type: ``str``; wire name: ``product_id``; JSON type: string"""
    label: str | UnsetType = field(default=UNSET)
    """Short label for this price (max 100 characters). Optional. Python type: ``str``; wire name: ``label``; JSON type: string"""
    about: str | UnsetType = field(default=UNSET)
    """Longer description of this price (max 500 characters). Optional. Python type: ``str``; wire name: ``about``; JSON type: string"""
    type: Type | UnsetType = field(default=UNSET)
    """Price definition discriminator. Required by the tagged definition. Python type: ``Type``; wire name: ``type``; JSON type: string (PriceType)"""
    fixed_amount: AmountParams | UnsetType = field(default=UNSET)
    """Fixed price amount. Required when ``type`` is ``fixed_amount``. Python type: ``AmountParams``; wire name: ``fixed_amount``; JSON type: object (AmountParams)"""
    customer_selected_amount: CustomerSelectedAmountParams | UnsetType = field(default=UNSET)
    """Customer-selected price policy. Required when ``type`` is ``customer_selected_amount``. Python type: ``CustomerSelectedAmountParams``; wire name: ``customer_selected_amount``; JSON type: object (CustomerSelectedAmountParams)"""

    def __post_init__(self) -> None:
        fixed = (
            self.type == Type.FIXED_AMOUNT
            and self.fixed_amount is not UNSET
            and self.customer_selected_amount is UNSET
        )
        selected = (
            self.type == Type.CUSTOMER_SELECTED_AMOUNT
            and self.customer_selected_amount is not UNSET
            and self.fixed_amount is UNSET
            and self.product_id is not UNSET
            and bool(self.product_id)
        )
        if sum((fixed, selected)) != 1:
            raise ValueError("provide exactly one valid catalog price definition")
