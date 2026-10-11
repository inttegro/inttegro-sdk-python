"""UpdateResponseApp in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdateResponseApp(ApiModel):
    """Typed update response app data in the app resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UpdateApplicationResponseApp``.
    """
    id: str = field(init=False)
    """Product identifier returned by the update operation. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    name: str = field(init=False)
    """Human-readable name of the update response app. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    alias: str | None = field(init=False)
    """The alias associated with this update response app. Optional; nullable. Python type: ``str | None``; wire name: ``alias``; JSON type: string"""
    description: str | None = field(init=False)
    """Human-readable description of the update response app. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    created_at: datetime = field(init=False)
    """When the update response app was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    updated_at: datetime | None = field(init=False)
    """When the update response app was last updated. Optional; nullable. Python type: ``datetime | None``; wire name: ``updated_at``; JSON type: string (date-time)"""
    capabilities: dict[str, object] = field(init=False)
    """Public capabilities currently available to this app. Required. Python type: ``dict[str, object]``; wire name: ``capabilities``; JSON type: object"""
