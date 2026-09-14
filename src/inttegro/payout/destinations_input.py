"""Typed payout destination assignments accepted by the Inttegro API."""

from __future__ import annotations

from dataclasses import dataclass, field

from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class DestinationsInput(ApiRequest):
    """Supported destination assignments for a payout settings update."""

    ghs: str | UnsetType = field(default=UNSET)
    """Financial account that receives Ghana cedi payouts.

    Supply an empty string to remove the current GHS assignment.
    """
