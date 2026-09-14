"""Masked mobile-money recognition details for a refund."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SettlementMobileMoney(ApiModel):
    """Masked mobile-money details; no raw account value is exposed."""

    network: Literal["airtel", "mtn", "telecel", "vodafone"] = field(init=False)
    account_number: str = field(init=False)
    """Masked account in ``****1234`` form."""
    last4: str = field(init=False)
    """Final four numeric digits."""

    _strict_wire_shape = True
