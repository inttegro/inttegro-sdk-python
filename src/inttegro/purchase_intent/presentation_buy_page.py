"""Hosted Buy page presentation returned for a purchase intent."""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.purchase_intent.presentation_buy_page_text import PresentationBuyPageText


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PresentationBuyPage(ApiModel):
    """Presentation settings returned for the hosted Buy page."""

    text: PresentationBuyPageText | None = field(init=False)
