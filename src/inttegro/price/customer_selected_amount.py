"""Customer-selected catalog price response data."""

from __future__ import annotations

from dataclasses import dataclass, field

from inttegro._model_base import ApiModel
from inttegro.money import Currency
from inttegro.price.suggested_amount import SuggestedAmount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CustomerSelectedAmount(ApiModel):
    """Persisted currency, range, and suggestions for a selected amount."""

    currency: Currency = field(init=False)
    minimum: int = field(init=False)
    maximum: int | None = field(init=False)
    suggested_amounts: list[SuggestedAmount] | None = field(init=False)
