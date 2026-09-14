"""Original-payment-method refund settlement destination."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodSettlement(ApiModel):
    """A refund returned to the original payment method."""

    type: Literal["payment_method"] = field(init=False)
    """Settlement discriminator. Required; always ``payment_method``."""
    payment_method: SettlementPaymentMethod = field(init=False)
    """Caller-safe immutable snapshot of the original payment method."""

    _strict_wire_shape = True


from inttegro.refund.settlement_payment_method import SettlementPaymentMethod
