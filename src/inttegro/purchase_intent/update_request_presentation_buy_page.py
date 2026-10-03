"""Hosted Buy page presentation update for a purchase intent."""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest
from inttegro.purchase_intent.update_request_presentation_buy_page_text import (
    UpdateRequestPresentationBuyPageText,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequestPresentationBuyPage(ApiRequest):
    """Changes to the hosted Buy page presentation."""

    text: UpdateRequestPresentationBuyPageText
