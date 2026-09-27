"""Type in the ``inttegro.balance_transaction`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Type(WireEnum):
    """Semantic source or cause of the transaction, not its direction.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``BalanceTransactionType``.
    """
    PAYMENT = "payment"
    """Wire value ``payment`` (payment) for semantic source or cause of the transaction, not its direction"""
    REFUND = "refund"
    """Wire value ``refund`` (refund) for semantic source or cause of the transaction, not its direction"""
    PAYOUT = "payout"
    """Wire value ``payout`` for an immutable successful-payout debit"""
