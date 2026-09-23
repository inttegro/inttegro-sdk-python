"""Allocation in the ``inttegro.balance_transaction`` namespace."""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Allocation(ApiModel):
    """Caller-safe allocation of part of a payment balance transaction.

    Exactly one of ``refund`` and ``payout`` is present, matching ``type``.
    """

    id: str = field(init=False)
    type: Literal["payout", "refund"] = field(init=False)
    status: Literal["pending", "completed"] = field(init=False)
    refund: AllocationUse | None = field(init=False)
    payout: AllocationUse | None = field(init=False)
    created_at: datetime = field(init=False)
    updated_at: datetime = field(init=False)
    completed_at: datetime | None = field(init=False)


from inttegro.balance_transaction.allocation_use import AllocationUse
