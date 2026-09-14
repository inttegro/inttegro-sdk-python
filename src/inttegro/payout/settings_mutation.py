"""SettingsMutation in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SettingsMutation(ApiModel):
    """Payout settings fields returned after a mutation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PayoutSettingsMutation``.
    """
    destinations: PayoutDestinations | None = field(init=False)
    """Supported currency-to-financial-account assignments. Optional; nullable. Python type: ``PayoutDestinations | None``; wire name: ``destinations``; JSON type: object (PayoutDestinations)."""
    fx_enabled: bool | None = field(init=False)
    """Updated foreign-exchange setting. Optional; nullable. Python type: ``bool | None``; wire name: ``fx_enabled``; JSON type: boolean."""
    id: str | None = field(init=False)
    """Payout settings identifier. Optional; nullable. Python type: ``str | None``; wire name: ``id``; JSON type: string"""
    schedule: PayoutSettingsMutationSchedule | None = field(init=False)
    """Updated payout schedule. Optional; nullable. Python type: ``PayoutSettingsMutationSchedule | None``; wire name: ``schedule``; JSON type: object"""

from inttegro.payout.settings_mutation_schedule import SettingsMutationSchedule as PayoutSettingsMutationSchedule
from inttegro.payout.destinations import Destinations as PayoutDestinations
