"""Offline refund settlement destination."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OfflineSettlement(ApiModel):
    """A refund for an order paid outside Inttegro."""

    type: Literal["offline"] = field(init=False)
    """Settlement discriminator. Required; always ``offline``."""

    _strict_wire_shape = True
