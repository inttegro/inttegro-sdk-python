"""Customer-facing presentation input for a new purchase intent."""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest
from inttegro.purchase_intent.create_request_presentation_buy_page import (
    CreateRequestPresentationBuyPage,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequestPresentation(ApiRequest):
    """Customer-facing presentation settings for a new purchase intent."""

    buy_page: CreateRequestPresentationBuyPage
