"""Hosted Buy page presentation input for a purchase intent."""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest
from inttegro.purchase_intent.create_request_presentation_buy_page_text import (
    CreateRequestPresentationBuyPageText,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequestPresentationBuyPage(ApiRequest):
    """Presentation settings for the hosted Buy page."""

    text: CreateRequestPresentationBuyPageText
