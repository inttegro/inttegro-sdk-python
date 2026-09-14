"""Supported original payment-method snapshots for refunds."""

from __future__ import annotations
from typing import TypeAlias

from inttegro.refund.settlement_bank_account_payment_method import SettlementBankAccountPaymentMethod
from inttegro.refund.settlement_mobile_money_payment_method import SettlementMobileMoneyPaymentMethod


SettlementPaymentMethod: TypeAlias = (
    SettlementMobileMoneyPaymentMethod | SettlementBankAccountPaymentMethod
)
"""Caller-safe original method selected by its required ``type`` discriminator."""
