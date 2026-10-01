"""Catalog price definition discriminator."""

from __future__ import annotations

from inttegro._enum_base import WireEnum


class Type(WireEnum):
    """Definition carried by a catalog price."""

    FIXED_AMOUNT = "fixed_amount"
    CUSTOMER_SELECTED_AMOUNT = "customer_selected_amount"
