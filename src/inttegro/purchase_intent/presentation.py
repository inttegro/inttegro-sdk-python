"""Customer-facing presentation returned for a purchase intent."""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.purchase_intent.presentation_buy_page import PresentationBuyPage


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Presentation(ApiModel):
    """Customer-facing presentation settings for a purchase intent."""

    buy_page: PresentationBuyPage | None = field(init=False)
