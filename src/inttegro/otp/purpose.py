"""Purpose in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Purpose(WireEnum):
    """Customer action protected by an OTP."""

    ACCOUNT_CREATION = "account_creation"
    """Wire value ``account_creation`` for a new-account verification flow."""
    ACCOUNT_RECOVERY = "account_recovery"
    """Wire value ``account_recovery`` for an account-recovery flow."""
    EMAIL_VERIFICATION = "email_verification"
    """Wire value ``email_verification`` for email ownership verification."""
    FINANCIAL_ACCOUNT_VERIFICATION = "financial_account_verification"
    """Wire value ``financial_account_verification`` for financial-account verification."""
    PASSWORD_RESET = "password_reset"
    """Wire value ``password_reset`` for a password-reset flow."""
    PAYMENT_CONFIRMATION = "payment_confirmation"
    """Wire value ``payment_confirmation`` for payment confirmation."""
    PAYMENT_METHOD_VERIFICATION = "payment_method_verification"
    """Wire value ``payment_method_verification`` for payment-method verification."""
    PAYOUT_CONFIRMATION = "payout_confirmation"
    """Wire value ``payout_confirmation`` for payout confirmation."""
    PHONE_VERIFICATION = "phone_verification"
    """Wire value ``phone_verification`` for phone ownership verification."""
    SENSITIVE_ACTION = "sensitive_action"
    """Wire value ``sensitive_action`` for a sensitive account action."""
    SIGN_IN = "sign_in"
    """Wire value ``sign_in`` for sign-in verification."""
    TRANSACTION_CONFIRMATION = "transaction_confirmation"
    """Wire value ``transaction_confirmation`` for transaction confirmation."""
    UNSPECIFIED = "unspecified"
    """Wire value ``unspecified`` when no narrower verification purpose applies."""
