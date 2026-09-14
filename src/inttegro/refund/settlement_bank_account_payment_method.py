"""Bank-account snapshot used as a refund destination."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SettlementBankAccountPaymentMethod(ApiModel):
    """Safe snapshot of the original bank-account method."""

    id: str = field(init=False)
    """Public payment-method identifier."""
    type: Literal["bank_account"] = field(init=False)
    """Payment-method discriminator. Required; always ``bank_account``."""
    bank_account: SettlementBankAccount = field(init=False)
    """Masked bank-account recognition details."""

    _strict_wire_shape = True


from inttegro.refund.settlement_bank_account import SettlementBankAccount
