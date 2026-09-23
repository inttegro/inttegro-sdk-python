"""Payout balance-transaction contribution model."""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BalanceTransaction(ApiModel):
    """A sparse view of one balance transaction's contribution to a payout."""

    allocated_amount: Amount = field(init=False)
    """The exact portion allocated to this payout."""
    amount: Amount = field(init=False)
    """The balance transaction's original amount before allocations."""
    id: str = field(init=False)
    """Unique balance transaction identifier."""
