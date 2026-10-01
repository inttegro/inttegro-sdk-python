"""Customer-selected catalog price order input."""

from __future__ import annotations

from dataclasses import dataclass

from inttegro._request_base import ApiRequest
from inttegro.money import AmountParams


@dataclass(frozen=True, slots=True, kw_only=True)
class CustomerSelectedPriceInput(ApiRequest):
    """Couples a saved price policy with the concrete selected amount."""

    price_id: str
    selected_amount: AmountParams
