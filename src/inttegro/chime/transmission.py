"""Transmission in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Transmission(ApiModel):
    """Public delivery lifecycle for a Chime.

    Instances are immutable API responses; ``from_dict()`` parses timezone-aware
    ISO-8601 timestamps and ignores undeclared wire fields.

    API contract schema: ``ChimeTransmission``.
    """
    address: str = field(init=False)
    """The address associated with this transmission. Required. Python type: ``str``; wire name: ``address``; JSON type: string"""
    created_at: datetime = field(init=False)
    """When the transmission was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    delivered_at: datetime | None = field(init=False)
    """Timestamp for delivered at. Optional; nullable. Python type: ``datetime | None``; wire name: ``delivered_at``; JSON type: string (date-time)"""
    failed_at: datetime | None = field(init=False)
    """When the transmission failed. Optional; nullable. Python type: ``datetime | None``; wire name: ``failed_at``; JSON type: string (date-time)"""
    initialized_at: datetime = field(init=False)
    """Timestamp for initialized at. Required. Python type: ``datetime``; wire name: ``initialized_at``; JSON type: string (date-time)"""
    mechanism: Literal['sms', 'email'] = field(init=False)
    """The mechanism associated with this transmission. Required. Python type: ``Literal['sms', 'email']``; wire name: ``mechanism``; JSON type: string. Constraints: allowed values ``sms``, ``email``"""
    sent_at: datetime | None = field(init=False)
    """Timestamp for sent at. Optional; nullable. Python type: ``datetime | None``; wire name: ``sent_at``; JSON type: string (date-time)"""
    sent_via: Literal['sms', 'email'] | None = field(init=False)
    """The sent via associated with this transmission. Optional; nullable. Python type: ``Literal['sms', 'email'] | None``; wire name: ``sent_via``; JSON type: string. Constraints: allowed values ``sms``, ``email``"""
    status: str = field(init=False)
    """Current lifecycle status of the transmission. Required. Python type: ``str``; wire name: ``status``; JSON type: string"""
    suppressed_at: datetime | None = field(init=False)
    """Timestamp for suppressed at. Optional; nullable. Python type: ``datetime | None``; wire name: ``suppressed_at``; JSON type: string (date-time)"""
