"""Product identity captured in a refund order-line snapshot."""

from __future__ import annotations
from dataclasses import dataclass, field

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderProductLineItemProduct(ApiModel):
    """Catalog or inline product identity captured by the order."""

    id: str | None = field(init=False)
    name: str = field(init=False)
