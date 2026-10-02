"""CompactResponse in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CompactResponse(ApiModel):
    """Typed response returned by the compact operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FinancialAccountCompactResponse``.
    """
    created_at: datetime = field(init=False)
    """When the compact response was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    currency: str = field(init=False)
    """The currency associated with this compact response. Required. Python type: ``str``; wire name: ``currency``; JSON type: string"""
    description: str | None = field(init=False)
    """Human-readable description of the compact response. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    disconnected_at: datetime | None = field(init=False)
    """Timestamp for disconnected at. Optional; nullable. Python type: ``datetime | None``; wire name: ``disconnected_at``; JSON type: string (date-time)"""
    fingerprint: str | None = field(init=False)
    """Application-scoped value for recognizing duplicate financial-account connections. Optional; nullable. Python type: ``str | None``; wire name: ``fingerprint``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this compact response. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    label: str | None = field(init=False)
    """The label associated with this compact response. Optional; nullable. Python type: ``str | None``; wire name: ``label``; JSON type: string"""
    type: Literal['wallet', 'bank_account', 'dosh_account'] = field(init=False)
    """Discriminator identifying the compact response type. Required. Python type: ``Literal['wallet', 'bank_account', 'dosh_account']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``wallet``, ``bank_account``, ``dosh_account``"""
