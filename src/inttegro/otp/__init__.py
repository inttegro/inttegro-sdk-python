"""Models, requests, and enums for Inttegro otp operations.

Import public types from the singular ``inttegro.otp`` namespace. Related request types, response shapes, and string-backed enums are grouped here for discovery."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .alphabet_type import AlphabetType as AlphabetType
    from .initiate_request import InitiateRequest as InitiateRequest
    from .initiate_response import InitiateResponse as InitiateResponse
    from .lookup_request import LookupRequest as LookupRequest
    from .lookup_response import LookupResponse as LookupResponse
    from .purpose import Purpose as Purpose
    from .status import Status as Status
    from .transaction import Transaction as Transaction
    from .transmission import Transmission as Transmission
    from .transmission_status import TransmissionStatus as TransmissionStatus
    from .verification import Verification as Verification
    from .verification_attempt import VerificationAttempt as VerificationAttempt
    from .verification_attempt_result import VerificationAttemptResult as VerificationAttemptResult
    from .verification_verdict import VerificationVerdict as VerificationVerdict
    from .verify_request import VerifyRequest as VerifyRequest


_EXPORTS: dict[str, tuple[str, str]] = {
    "AlphabetType": ("inttegro.otp.alphabet_type", "AlphabetType"),
    "InitiateRequest": ("inttegro.otp.initiate_request", "InitiateRequest"),
    "InitiateResponse": ("inttegro.otp.initiate_response", "InitiateResponse"),
    "LookupRequest": ("inttegro.otp.lookup_request", "LookupRequest"),
    "LookupResponse": ("inttegro.otp.lookup_response", "LookupResponse"),
    "Purpose": ("inttegro.otp.purpose", "Purpose"),
    "Status": ("inttegro.otp.status", "Status"),
    "Transaction": ("inttegro.otp.transaction", "Transaction"),
    "Transmission": ("inttegro.otp.transmission", "Transmission"),
    "TransmissionStatus": ("inttegro.otp.transmission_status", "TransmissionStatus"),
    "Verification": ("inttegro.otp.verification", "Verification"),
    "VerificationAttempt": ("inttegro.otp.verification_attempt", "VerificationAttempt"),
    "VerificationAttemptResult": ("inttegro.otp.verification_attempt_result", "VerificationAttemptResult"),
    "VerificationVerdict": ("inttegro.otp.verification_verdict", "VerificationVerdict"),
    "VerifyRequest": ("inttegro.otp.verify_request", "VerifyRequest"),
}

__all__ = [
    "AlphabetType",
    "InitiateRequest",
    "InitiateResponse",
    "LookupRequest",
    "LookupResponse",
    "Purpose",
    "Status",
    "Transaction",
    "Transmission",
    "TransmissionStatus",
    "Verification",
    "VerificationAttempt",
    "VerificationAttemptResult",
    "VerificationVerdict",
    "VerifyRequest",
]


def __getattr__(name: str) -> Any:
    """Load a public resource type on first access."""
    try:
        module_name, attribute_name = _EXPORTS[name]
    except KeyError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from None
    value = getattr(import_module(module_name), attribute_name)
    globals()[name] = value
    return value
