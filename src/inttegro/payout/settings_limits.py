"""SettingsLimits in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SettingsLimits(ApiModel):
    """Platform limits applied to payouts."""

    amount: PayoutAmountLimits = field(init=False)
    """Inclusive payout amount range. Required. Python type: ``PayoutAmountLimits``; wire name: ``amount``; JSON type: object"""


from inttegro.payout.amount_limits import AmountLimits as PayoutAmountLimits
