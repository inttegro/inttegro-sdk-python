"""Allocation target in the ``inttegro.balance_transaction`` namespace."""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class AllocationUse(ApiModel):
    """Refund or payout reference and the amount consumed from one transaction."""

    id: str = field(init=False)
    amount: BalanceTransactionAmount = field(init=False)


from inttegro.balance_transaction.amount import Amount as BalanceTransactionAmount
