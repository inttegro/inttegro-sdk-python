"""Failure in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Failure(ApiModel):
    """Sanitized terminal refund failure information."""

    detail: str = field(init=False)
    """Safe merchant-facing explanation. Required. Python type: ``str``; wire name: ``detail``; JSON type: string"""
    reason: RefundFailureReason = field(init=False)
    """Stable caller-safe failure reason. Required. Python type: ``RefundFailureReason``; wire name: ``reason``; JSON type: string enum"""
    retryable: bool = field(init=False)
    """Whether the underlying condition may be resolved. Required. Python type: ``bool``; wire name: ``retryable``; JSON type: boolean"""


from inttegro.refund.failure_reason import FailureReason as RefundFailureReason
