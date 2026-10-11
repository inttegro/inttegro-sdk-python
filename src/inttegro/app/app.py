"""App in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class App(ApiModel):
    """Typed app data in the app resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``Application``.
    """
    id: str = field(init=False)
    """Unique product identifier with prod_ prefix. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    name: str = field(init=False)
    """Product name. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    alias: str | None = field(init=False)
    """The alias associated with this app. Optional; nullable. Python type: ``str | None``; wire name: ``alias``; JSON type: string"""
    description: str | None = field(init=False)
    """Short description. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    created_at: datetime = field(init=False)
    """Product creation timestamp. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    updated_at: datetime | None = field(init=False)
    """Last update timestamp. Optional; nullable. Python type: ``datetime | None``; wire name: ``updated_at``; JSON type: string (date-time)"""
    archived_at: datetime | None = field(init=False)
    """Archive timestamp (if archived). Optional; nullable. Python type: ``datetime | None``; wire name: ``archived_at``; JSON type: string (date-time)"""
    capabilities: dict[str, object] = field(init=False)
    """Public capabilities currently available to this app. Required. Python type: ``dict[str, object]``; wire name: ``capabilities``; JSON type: object"""
    secret_key: ApplicationSecretKey | None = field(init=False)
    """The secret key associated with this app. Optional; nullable. Python type: ``ApplicationSecretKey | None``; wire name: ``secret_key``; JSON type: object"""
    relationship: ApplicationRelationship | None = field(init=False)
    """The relationship associated with this app. Optional; nullable. Python type: ``ApplicationRelationship | None``; wire name: ``relationship``; JSON type: object"""

from inttegro.app.relationship import Relationship as ApplicationRelationship
from inttegro.app.secret_key import SecretKey as ApplicationSecretKey
