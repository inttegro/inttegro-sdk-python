"""Typed financial-account verification state."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class VerificationRequest(ApiModel):
    """Identifies a verification request and its mechanism."""

    id: str | None = field(init=False)
    mechanism: str | None = field(init=False)
    type: str | None = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Verification(ApiModel):
    """Financial-account verification state and request evidence."""

    initiated_at: datetime = field(init=False)
    completed_at: datetime | None = field(init=False)
    request: VerificationRequest = field(init=False)
