"""Customer-selected catalog price request data."""

from __future__ import annotations

from dataclasses import dataclass, field

from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.money import Currency
from inttegro.price.suggested_amount_params import SuggestedAmountParams


@dataclass(frozen=True, slots=True, kw_only=True)
class CustomerSelectedAmountParams(ApiRequest):
    """Currency, range, and optional conveniences for a selected amount."""

    currency: Currency
    minimum: int
    maximum: int | UnsetType = field(default=UNSET)
    suggested_amounts: list[SuggestedAmountParams] | UnsetType = field(default=UNSET)
