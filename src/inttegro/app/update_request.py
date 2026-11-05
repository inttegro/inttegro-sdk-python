"""UpdateRequest in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.operating_policy import Selection as OperatingPolicySelection


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequest(ApiRequest):
    """Parameters accepted by the update request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdateApplicationRequest``.
    """
    name: str | UnsetType = field(default=UNSET)
    """Human-readable name of the update request. Optional. Python type: ``str``; wire name: ``name``; JSON type: string"""
    alias: str | UnsetType = field(default=UNSET)
    """The alias associated with this update request. Optional. Python type: ``str``; wire name: ``alias``; JSON type: string"""
    description: str | UnsetType = field(default=UNSET)
    """Human-readable description of the update request. Optional. Python type: ``str``; wire name: ``description``; JSON type: string"""
    legal_entity_type: str | UnsetType = field(default=UNSET)
    """The legal entity type associated with this update request. Optional. Python type: ``str``; wire name: ``legal_entity_type``; JSON type: string"""
    operating_policy: OperatingPolicySelection | UnsetType = field(default=UNSET)
    """Named or inline operating policy. Optional. Python type: ``OperatingPolicySelection``; wire name: ``operating_policy``; JSON type: object"""
