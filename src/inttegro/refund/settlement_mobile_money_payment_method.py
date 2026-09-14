"""Mobile-money snapshot used as a refund destination."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SettlementMobileMoneyPaymentMethod(ApiModel):
    """Safe snapshot of the original mobile-money method."""

    id: str = field(init=False)
    """Public payment-method identifier."""
    type: Literal["mobile_money"] = field(init=False)
    """Payment-method discriminator. Required; always ``mobile_money``."""
    mobile_money: SettlementMobileMoney = field(init=False)
    """Masked mobile-money recognition details."""

    _strict_wire_shape = True


from inttegro.refund.settlement_mobile_money import SettlementMobileMoney
