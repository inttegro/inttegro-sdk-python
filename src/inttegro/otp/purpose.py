"""Purpose in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Purpose(WireEnum):
    """Customer action protected by an OTP."""

    ACCOUNT_CREATION = "account_creation"
    ACCOUNT_RECOVERY = "account_recovery"
    EMAIL_VERIFICATION = "email_verification"
    FINANCIAL_ACCOUNT_VERIFICATION = "financial_account_verification"
    PASSWORD_RESET = "password_reset"
    PAYMENT_CONFIRMATION = "payment_confirmation"
    PAYMENT_METHOD_VERIFICATION = "payment_method_verification"
    PAYOUT_CONFIRMATION = "payout_confirmation"
    PHONE_VERIFICATION = "phone_verification"
    SENSITIVE_ACTION = "sensitive_action"
    SIGN_IN = "sign_in"
    TRANSACTION_CONFIRMATION = "transaction_confirmation"
    UNSPECIFIED = "unspecified"
