"""Receipt issued for a paid order payment."""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.order.receipt_format import ReceiptFormat


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Receipt(ApiModel):
    """Receipt metadata and hosted document formats."""

    format: ReceiptFormat = field(init=False)
    number: str | None = field(init=False)
    delivery_summary: dict[str, object] | None = field(init=False)
