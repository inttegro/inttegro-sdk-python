"""Suggested customer-selected amount response data."""

from __future__ import annotations

from dataclasses import dataclass, field

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SuggestedAmount(ApiModel):
    """A convenient amount choice returned with a catalog price."""

    id: str = field(init=False)
    value: int = field(init=False)
    recommended: bool | None = field(init=False)
