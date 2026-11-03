"""SettingsLookupScheduleAgingSpec in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SettingsLookupScheduleAgingSpec(ApiModel):
    """Typed settings lookup schedule aging spec data in the payout resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PayoutSettingsLookupScheduleAgingSpec``.
    """
    abide: str = field(init=False)
    """The abide associated with this settings lookup schedule aging spec. Required. Python type: ``str``; wire name: ``abide``; JSON type: string"""
    public_id: str = field(init=False)
    """The public identifier associated with this settings lookup schedule aging spec. Required. Python type: ``str``; wire name: ``public_id``; JSON type: string"""
    label: str = field(init=False)
    """The label associated with this settings lookup schedule aging spec. Required. Python type: ``str``; wire name: ``label``; JSON type: string"""
    t_plus: str = field(init=False)
    """The t plus associated with this settings lookup schedule aging spec. Required. Python type: ``str``; wire name: ``t_plus``; JSON type: string"""
