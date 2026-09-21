"""InitiateRequest in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class InitiateRequest(ApiRequest):
    """Parameters accepted by the initiate request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``InitiateOTPRequest``.
    """
    async_delivery: bool | UnsetType = field(default=UNSET)
    """Return after accepting the transaction while SMS delivery continues asynchronously. Optional. Python type: ``bool``; wire name: ``async_delivery``; JSON type: boolean"""
    message_template: str | UnsetType = field(default=UNSET)
    """SMS text containing the required `{token}` placeholder and optional `{service}` placeholder. Optional. Python type: ``str``; wire name: ``message_template``; JSON type: string"""
    purpose: Literal['account_creation', 'account_recovery', 'email_verification', 'financial_account_verification', 'password_reset', 'payment_confirmation', 'payment_method_verification', 'payout_confirmation', 'phone_verification', 'sensitive_action', 'sign_in', 'transaction_confirmation', 'unspecified', OTPPurpose.ACCOUNT_CREATION, OTPPurpose.ACCOUNT_RECOVERY, OTPPurpose.EMAIL_VERIFICATION, OTPPurpose.FINANCIAL_ACCOUNT_VERIFICATION, OTPPurpose.PASSWORD_RESET, OTPPurpose.PAYMENT_CONFIRMATION, OTPPurpose.PAYMENT_METHOD_VERIFICATION, OTPPurpose.PAYOUT_CONFIRMATION, OTPPurpose.PHONE_VERIFICATION, OTPPurpose.SENSITIVE_ACTION, OTPPurpose.SIGN_IN, OTPPurpose.TRANSACTION_CONFIRMATION, OTPPurpose.UNSPECIFIED]
    """Customer action protected by the OTP. Required. Python type: ``Literal[Purpose values]``; wire name: ``purpose``; JSON type: string"""
    sender: str | UnsetType = field(default=UNSET)
    """Optional sender identifier shown to the recipient (3-12 characters). Optional. Python type: ``str``; wire name: ``sender``; JSON type: string. Constraints: minimum length 3; maximum length 12"""
    token_alphabet: str | UnsetType = field(default=UNSET)
    """Custom alphabet for token generation (mutually exclusive with token_alphabet_type). Optional. Python type: ``str``; wire name: ``token_alphabet``; JSON type: string"""
    token_alphabet_type: Literal['numeric', 'alpha', 'alphanumeric', OTPAlphabetType.NUMERIC, OTPAlphabetType.ALPHA, OTPAlphabetType.ALPHANUMERIC] | UnsetType = field(default=UNSET)
    """Predefined alphabet type (mutually exclusive with token_alphabet). Optional. Python type: ``Literal['numeric', 'alpha', 'alphanumeric', OTPAlphabetType.NUMERIC, OTPAlphabetType.ALPHA, OTPAlphabetType.ALPHANUMERIC]``; wire name: ``token_alphabet_type``; JSON type: string. Constraints: allowed values ``numeric``, ``alpha``, ``alphanumeric``"""
    validity_duration_in_minutes: int | UnsetType = field(default=UNSET)
    """How long the token remains valid (3-10080 minutes). Optional. Python type: ``int``; wire name: ``validity_duration_in_minutes``; JSON type: integer. Constraints: minimum 3; maximum 10080"""
    recipient: str
    """Phone number in international format (E.164). Required. Python type: ``str``; wire name: ``recipient``; JSON type: string"""
    service_name: str
    """Service name substituted for `{service}` (2-20 characters). Required. Python type: ``str``; wire name: ``service_name``; JSON type: string. Constraints: minimum length 2; maximum length 20"""
    token_size: int
    """Length of generated token (5-10 characters). Required. Python type: ``int``; wire name: ``token_size``; JSON type: integer. Constraints: minimum 5; maximum 10"""

from inttegro.otp.alphabet_type import AlphabetType as OTPAlphabetType
from inttegro.otp.purpose import Purpose as OTPPurpose
