"""Fee order-line snapshot attached to a refund."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

from inttegro._model_base import ApiModel
from inttegro.refund.order_fee_line_item_fee import OrderFeeLineItemFee


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderFeeLineItem(ApiModel):
    """Immutable fee line captured from the originating order."""

    id: str = field(init=False)
    type: Literal["fee"] = field(init=False)
    fee: OrderFeeLineItemFee = field(init=False)
