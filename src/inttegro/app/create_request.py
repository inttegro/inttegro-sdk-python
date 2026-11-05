"""CreateRequest in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.operating_policy import Selection as OperatingPolicySelection


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequest(ApiRequest):
    """Parameters accepted by the create request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreateApplicationRequest``.
    """
    alias: str | UnsetType = field(default=UNSET)
    """The alias associated with this create request. Optional. Python type: ``str``; wire name: ``alias``; JSON type: string"""
    description: str | UnsetType = field(default=UNSET)
    """Human-readable description of the create request. Optional. Python type: ``str``; wire name: ``description``; JSON type: string"""
    legal_entity_type: str | UnsetType = field(default=UNSET)
    """The legal entity type associated with this create request. Optional. Python type: ``str``; wire name: ``legal_entity_type``; JSON type: string"""
    placement_parent_application_id: str | UnsetType = field(default=UNSET)
    """Identifier of the related placement parent application. Optional. Python type: ``str``; wire name: ``placement_parent_application_id``; JSON type: string"""
    relationship_policy: CreateApplicationRequestRelationshipPolicy | UnsetType = field(default=UNSET)
    """The relationship policy associated with this create request. Optional. Python type: ``CreateApplicationRequestRelationshipPolicy``; wire name: ``relationship_policy``; JSON type: object"""
    name: str
    """Human-readable name of the create request. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    operating_policy: OperatingPolicySelection | UnsetType = field(default=UNSET)
    """Named or inline operating policy. Optional. Python type: ``OperatingPolicySelection``; wire name: ``operating_policy``; JSON type: object"""

from inttegro.app.create_request_relationship_policy import CreateRequestRelationshipPolicy as CreateApplicationRequestRelationshipPolicy
