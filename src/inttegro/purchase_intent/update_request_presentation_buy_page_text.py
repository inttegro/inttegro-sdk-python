"""Sparse text update for a hosted Buy page."""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequestPresentationBuyPageText(ApiRequest):
    """Sparse text changes for the hosted Buy page."""

    checkout_section_title: str | None | UnsetType = field(default=UNSET)
    amount_field_label: str | None | UnsetType = field(default=UNSET)
    primary_action_label: str | None | UnsetType = field(default=UNSET)
