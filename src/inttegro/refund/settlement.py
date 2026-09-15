"""Discriminated refund settlement destination."""

from __future__ import annotations
from typing import TypeAlias

from inttegro.refund.offline_settlement import OfflineSettlement
from inttegro.refund.payment_method_settlement import PaymentMethodSettlement


Settlement: TypeAlias = OfflineSettlement | PaymentMethodSettlement
"""Immutable refund destination selected by the required ``type`` discriminator."""

__all__ = ["Settlement"]
