"""Customer-facing presentation update for a purchase intent."""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest
from inttegro.purchase_intent.update_request_presentation_buy_page import (
    UpdateRequestPresentationBuyPage,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequestPresentation(ApiRequest):
    """Customer-facing presentation changes for a purchase intent."""

    buy_page: UpdateRequestPresentationBuyPage
