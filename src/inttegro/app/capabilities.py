"""Typed application capability states returned by ``/apps/capabilities``."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CapabilityRequirement(ApiModel):
    """A setup item that must be completed before a capability can be enabled."""

    code: str = field(init=False)
    description: str = field(init=False)
    due_at: datetime | None = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CapabilityRequirements(ApiModel):
    """Requirements that currently prevent a capability from being enabled."""

    currently_due: list[CapabilityRequirement] = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Capability(ApiModel):
    """The current availability of one commerce capability."""

    status: Literal["enabled", "restricted", "pending_review"] = field(init=False)
    status_changed_at: datetime = field(init=False)
    status_reason: Literal[
        "setup_incomplete",
        "account_under_review",
        "account_restricted",
        "account_inactive",
    ] | None = field(init=False)
    requirements: CapabilityRequirements | None = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Capabilities(ApiModel):
    """Payment and payout capabilities available to the authenticated app."""

    payments: Capability = field(init=False)
    payouts: Capability = field(init=False)
