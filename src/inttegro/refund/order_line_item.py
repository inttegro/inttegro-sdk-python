"""Supported order-line snapshots attached to refunds."""

from __future__ import annotations
from typing import TypeAlias

from inttegro.refund.order_fee_line_item import OrderFeeLineItem
from inttegro.refund.order_product_line_item import OrderProductLineItem
from inttegro.refund.order_shipping_line_item import OrderShippingLineItem


OrderLineItem: TypeAlias = OrderProductLineItem | OrderFeeLineItem | OrderShippingLineItem
"""Immutable order-line snapshot selected by its required ``type`` discriminator."""

__all__ = ["OrderLineItem"]
