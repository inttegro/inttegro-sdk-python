"""Suggested customer-selected amount request data."""

from __future__ import annotations

from dataclasses import dataclass, field

from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class SuggestedAmountParams(ApiRequest):
    """A convenient amount choice; suggestions do not restrict valid amounts."""

    id: str
    value: int
    recommended: bool | UnsetType = field(default=UNSET)
