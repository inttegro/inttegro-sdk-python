"""FailureReason in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class FailureReason(WireEnum):
    """Stable, caller-safe reason that a payout failed."""

    PROVIDER_DECLINED = "provider_declined"
    """Wire value ``provider_declined``"""
    DELIVERY_FAILED = "delivery_failed"
    """Wire value ``delivery_failed``"""
    TEMPORARILY_UNAVAILABLE = "temporarily_unavailable"
    """Wire value ``temporarily_unavailable``"""
    UNKNOWN = "unknown"
    """Wire value ``unknown``"""
