"""Typed payout destination assignments returned by the Inttegro API."""

from __future__ import annotations

from dataclasses import dataclass, field

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Destinations(ApiModel):
    """Supported currency-to-financial-account payout assignments.

    ``ghs`` is the financial account that receives Ghana cedi payouts. The
    object is decoded from API responses and retains mapping-style access.
    """

    ghs: str | None = field(init=False)
    """Financial account that receives Ghana cedi payouts. Optional."""
