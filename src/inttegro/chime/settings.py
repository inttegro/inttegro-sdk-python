"""Effective, non-secret delivery settings for Chimes."""

from __future__ import annotations

from dataclasses import dataclass, field

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SMSSettings(ApiModel):
    """SMS sender defaults and public length limits."""

    default_sender: str = field(init=False)
    min_sender_char_len: int = field(init=False)
    max_sender_char_len: int = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EmailSettings(ApiModel):
    """Email sender defaults and authorized From addresses."""

    default_from: str = field(init=False)
    allowed_from: list[str] = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Settings(ApiModel):
    """Typed SMS and email delivery settings used by Chimes."""

    sms: SMSSettings = field(init=False)
    email: EmailSettings = field(init=False)
