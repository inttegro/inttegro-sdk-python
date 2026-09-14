"""FailureReason in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class FailureReason(WireEnum):
    """Stable, caller-safe reason that terminal refund processing failed."""

    INSUFFICIENT_BALANCE = "insufficient_balance"
    """Wire value ``insufficient_balance``"""
    ORIGINAL_PAYMENT_METHOD_UNAVAILABLE = "original_payment_method_unavailable"
    """Wire value ``original_payment_method_unavailable``"""
    ORIGINAL_PAYMENT_NOT_REFUNDABLE = "original_payment_not_refundable"
    """Wire value ``original_payment_not_refundable``"""
    REFUND_NOT_SUPPORTED = "refund_not_supported"
    """Wire value ``refund_not_supported``"""
    AMOUNT_NOT_SUPPORTED = "amount_not_supported"
    """Wire value ``amount_not_supported``"""
    REFUND_DECLINED = "refund_declined"
    """Wire value ``refund_declined``"""
    REFUND_NOT_PERMITTED = "refund_not_permitted"
    """Wire value ``refund_not_permitted``"""
    TEMPORARILY_UNAVAILABLE = "temporarily_unavailable"
    """Wire value ``temporarily_unavailable``"""
    UNKNOWN = "unknown"
    """Wire value ``unknown``"""
