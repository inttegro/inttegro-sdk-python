"""Text overrides for a hosted Buy page created by a purchase intent."""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequestPresentationBuyPageText(ApiRequest):
    """Optional text overrides for a new hosted Buy page."""

    checkout_section_title: str | UnsetType = field(default=UNSET)
    amount_field_label: str | UnsetType = field(default=UNSET)
    primary_action_label: str | UnsetType = field(default=UNSET)
