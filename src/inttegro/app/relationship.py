"""Relationship in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Relationship(ApiModel):
    """Typed relationship data in the app resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ApplicationRelationship``.
    """
    id: str = field(init=False)
    """Order that consumed the Buy link. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    kind: Literal['placement'] = field(init=False)
    """The kind associated with this relationship. Optional. Python type: ``Literal['placement']``; wire name: ``kind``; JSON type: string"""
    parent: RelationshipParent = field(init=False)
    """Application that directly contains the app. Required. Python type: ``RelationshipParent``; wire name: ``parent``; JSON type: object"""
    status: Literal['active', 'inactive', 'suspended', 'revoked'] = field(init=False)
    """Current lifecycle status of the relationship. Optional. Python type: ``Literal['active', 'inactive', 'suspended', 'revoked']``; wire name: ``status``; JSON type: string"""
    created_at: datetime = field(init=False)
    """When order creation consumed the single-use Buy link. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class RelationshipParent(ApiModel):
    """Public identity of the app that directly contains another app."""

    id: str = field(init=False)
    """Parent app identifier. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    name: str = field(init=False)
    """Current parent app name. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    alias: str | None = field(init=False)
    """Current parent app alias. Optional; nullable. Python type: ``str | None``; wire name: ``alias``; JSON type: string"""
