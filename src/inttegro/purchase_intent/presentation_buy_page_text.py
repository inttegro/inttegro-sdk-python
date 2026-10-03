"""Merchant-authored copy returned for a hosted Buy page."""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PresentationBuyPageText(ApiModel):
    """Current merchant-authored text for the hosted Buy page."""

    checkout_section_title: str | None = field(init=False)
    amount_field_label: str | None = field(init=False)
    primary_action_label: str | None = field(init=False)
