"""SetDestinationsRequest in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class SetDestinationsRequest(ApiRequest):
    """Payout settings fields returned after a mutation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``SetPayoutDestinationsRequest``.
    """
    destinations: PayoutDestinationsInput
    """Supported currency-to-financial-account assignments. Required. Python type: ``PayoutDestinationsInput``; wire name: ``destinations``; JSON type: object (PayoutDestinations)."""

from inttegro.payout.destinations_input import DestinationsInput as PayoutDestinationsInput
