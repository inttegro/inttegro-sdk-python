"""AmountLimits in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class AmountLimits(ApiModel):
    """Inclusive payout amount range."""

    min: Amount = field(init=False)
    """Smallest permitted payout amount. Required. Python type: ``Amount``; wire name: ``min``; JSON type: object"""
    max: Amount = field(init=False)
    """Largest permitted payout amount. Required. Python type: ``Amount``; wire name: ``max``; JSON type: object"""
