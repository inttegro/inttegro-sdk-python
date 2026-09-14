"""Supported bank-account snapshot for a refund destination."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SettlementBankAccount(ApiModel):
    """Supported bank-account subtype and its masked details."""

    type: Literal["ghana_bank_account"] = field(init=False)
    ghana_bank_account: SettlementGhanaBankAccount = field(init=False)

    _strict_wire_shape = True


from inttegro.refund.settlement_ghana_bank_account import SettlementGhanaBankAccount
