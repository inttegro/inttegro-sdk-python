"""Shipping details captured in a refund order-line snapshot."""

from __future__ import annotations
from dataclasses import dataclass, field

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderShippingLineItemShipping(ApiModel):
    """Descriptive shipping fields captured by the order."""

    label: str | None = field(init=False)
    description: str | None = field(init=False)
