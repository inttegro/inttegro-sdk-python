"""SettingsLookup in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SettingsLookup(ApiModel):
    """Complete payout settings read model.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PayoutSettingsLookup``.
    """
    destinations: PayoutDestinations = field(init=False)
    """Supported currency-to-financial-account assignments. Required. Python type: ``PayoutDestinations``; wire name: ``destinations``; JSON type: object (PayoutDestinations)."""
    fx_enabled: bool | None = field(init=False)
    """Present only when foreign exchange is enabled in stored settings. Optional; nullable. Python type: ``bool | None``; wire name: ``fx_enabled``; JSON type: boolean"""
    schedule: PayoutSettingsLookupSchedule | None = field(init=False)
    """Active payout schedule. Optional; nullable. Python type: ``PayoutSettingsLookupSchedule | None``; wire name: ``schedule``; JSON type: object"""

from inttegro.payout.settings_lookup_schedule import SettingsLookupSchedule as PayoutSettingsLookupSchedule
from inttegro.payout.destinations import Destinations as PayoutDestinations
