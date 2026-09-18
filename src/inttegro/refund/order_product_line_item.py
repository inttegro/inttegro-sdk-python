"""Product order-line snapshot attached to a refund."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

from inttegro._model_base import ApiModel
from inttegro.refund.order_product_line_item_product import OrderProductLineItemProduct


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderProductLineItem(ApiModel):
    """Immutable product line captured from the originating order."""

    id: str = field(init=False)
    type: Literal["product"] = field(init=False)
    quantity: int = field(init=False)
    product: OrderProductLineItemProduct = field(init=False)
