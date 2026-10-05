"""Failure in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Failure(ApiModel):
    """Caller-safe information about a terminal payout failure."""

    detail: str = field(init=False)
    """Human-readable failure explanation. Required. Python type: ``str``; wire name: ``detail``; JSON type: string"""
    reason: PayoutFailureReason = field(init=False)
    """Stable caller-safe failure reason. Required. Python type: ``PayoutFailureReason``; wire name: ``reason``; JSON type: string enum"""
    retryable: bool = field(init=False)
    """Whether a new attempt may succeed. Required. Python type: ``bool``; wire name: ``retryable``; JSON type: boolean"""


from inttegro.payout.failure_reason import FailureReason as PayoutFailureReason
