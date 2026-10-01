"""AddPriceRequest in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.money import AmountParams
from inttegro.price.customer_selected_amount_params import CustomerSelectedAmountParams
from inttegro.price.type import Type as PriceType


@dataclass(frozen=True, slots=True, kw_only=True)
class AddPriceRequest(ApiRequest):
    """Parameters accepted by the add price request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``AddProductPriceRequest``.
    """
    label: str | UnsetType = field(default=UNSET)
    """Optional short label for the new price. Optional. Python type: ``str``; wire name: ``label``; JSON type: string. Constraints: maximum length 100"""
    about: str | UnsetType = field(default=UNSET)
    """Optional internal description for the new price. Optional. Python type: ``str``; wire name: ``about``; JSON type: string. Constraints: maximum length 500"""
    product_id: str
    """Product ID to attach the new price to. Required. Python type: ``str``; wire name: ``product_id``; JSON type: string"""
    type: PriceType | UnsetType = field(default=UNSET)
    """Price definition discriminator. Required by the tagged definition. Python type: ``PriceType``; wire name: ``type``; JSON type: string (PriceType)"""
    fixed_amount: AmountParams | UnsetType = field(default=UNSET)
    """Fixed price amount. Required when ``type`` is ``fixed_amount``. Python type: ``AmountParams``; wire name: ``fixed_amount``; JSON type: object (AmountParams)"""
    customer_selected_amount: CustomerSelectedAmountParams | UnsetType = field(default=UNSET)
    """Customer-selected price policy. Required when ``type`` is ``customer_selected_amount``. Python type: ``CustomerSelectedAmountParams``; wire name: ``customer_selected_amount``; JSON type: object (CustomerSelectedAmountParams)"""

    def __post_init__(self) -> None:
        fixed = (
            self.type == PriceType.FIXED_AMOUNT
            and self.fixed_amount is not UNSET
            and self.customer_selected_amount is UNSET
        )
        selected = (
            self.type == PriceType.CUSTOMER_SELECTED_AMOUNT
            and self.customer_selected_amount is not UNSET
            and self.fixed_amount is UNSET
        )
        if sum((fixed, selected)) != 1:
            raise ValueError("provide exactly one valid product price definition")
