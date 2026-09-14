"""Masked Ghana bank-account recognition details for a refund."""

from __future__ import annotations
from dataclasses import dataclass, field

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SettlementGhanaBankAccount(ApiModel):
    """Masked bank details; no raw account value is exposed."""

    account_number: str = field(init=False)
    """Masked account in ``****1234`` form."""
    last4: str = field(init=False)
    """Final four numeric digits."""

    _strict_wire_shape = True
