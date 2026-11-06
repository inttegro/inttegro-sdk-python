"""Status of one balance transaction's contribution to a payout."""

from __future__ import annotations

from inttegro._enum_base import WireEnum


class BalanceTransactionStatus(WireEnum):
    """Whether a payout contribution remains reserved, completed, or released."""

    RESERVED = "reserved"
    """The contribution remains reserved while the payout is open."""

    COMPLETED = "completed"
    """The contribution was consumed by a successful payout."""

    RELEASED = "released"
    """The contribution was returned after the payout did not complete."""
