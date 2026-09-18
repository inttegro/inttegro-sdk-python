"""Shipping order-line snapshot attached to a refund."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

from inttegro._model_base import ApiModel
from inttegro.refund.order_shipping_line_item_shipping import OrderShippingLineItemShipping


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderShippingLineItem(ApiModel):
    """Immutable shipping line captured from the originating order."""

    id: str = field(init=False)
    type: Literal["shipping"] = field(init=False)
    shipping: OrderShippingLineItemShipping = field(init=False)
