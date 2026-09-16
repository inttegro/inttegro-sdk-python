"""Payout in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Payout(ApiModel):
    """A payout scheduled from your Inttegro balance to a destination financial account.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    amount: Amount | None = field(init=False)
    """Monetary amount, represented by a currency and an integer minor-unit value. Optional; nullable. Python type: ``Amount | None``; wire name: ``amount``; JSON type: object (Amount)"""
    balance_transactions: list[str] | None = field(init=False)
    """Balance transaction IDs linked to this payout. Optional; nullable. Python type: ``list[str] | None``; wire name: ``balance_transactions``; JSON type: array of string values"""
    canceled_at: datetime | None = field(init=False)
    """When the payout was canceled. Optional; nullable. Python type: ``datetime | None``; wire name: ``canceled_at``; JSON type: string (date-time)"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    destination_id: str = field(init=False)
    """Financial account receiving the funds. Required. Python type: ``str``; wire name: ``destination_id``; JSON type: string"""
    error: PayoutError | None = field(init=False)
    """Public failure details when execution fails. Optional; nullable. Python type: ``PayoutError | None``; wire name: ``error``; JSON type: object"""
    execute_after: datetime = field(init=False)
    """Earliest moment payout execution may begin. Required. Python type: ``datetime``; wire name: ``execute_after``; JSON type: string (date-time)"""
    executed_by: str | None = field(init=False)
    """Actor that executed the payout. Optional; nullable. Python type: ``str | None``; wire name: ``executed_by``; JSON type: string"""
    expected_at: datetime | None = field(init=False)
    """Expected completion time. Optional; nullable. Python type: ``datetime | None``; wire name: ``expected_at``; JSON type: string (date-time)"""
    failed_at: datetime | None = field(init=False)
    """When the payout entered its unsuccessful terminal state. Optional; nullable. Python type: ``datetime | None``; wire name: ``failed_at``; JSON type: string (date-time)"""
    id: str = field(init=False)
    """Unique payout identifier. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    initiated_at: datetime = field(init=False)
    """When the payout was created. Required. Python type: ``datetime``; wire name: ``initiated_at``; JSON type: string (date-time)"""
    initiated_by: str | None = field(init=False)
    """Actor that initiated the payout. Optional; nullable. Python type: ``str | None``; wire name: ``initiated_by``; JSON type: string"""
    max_amount: Amount = field(init=False)
    """Monetary max amount, represented by a currency and an integer minor-unit value. Required. Python type: ``Amount``; wire name: ``max_amount``; JSON type: object (Amount)"""
    reference: str | None = field(init=False)
    """Merchant reference carried on the payout. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""
    schedule_id: str | None = field(init=False)
    """Schedule associated with the payout. Optional; nullable. Python type: ``str | None``; wire name: ``schedule_id``; JSON type: string"""
    scheduled_at: datetime | None = field(init=False)
    """When the payout was scheduled. Optional; nullable. Python type: ``datetime | None``; wire name: ``scheduled_at``; JSON type: string (date-time)"""
    scheduled_by: str | None = field(init=False)
    """Actor that scheduled the payout. Optional; nullable. Python type: ``str | None``; wire name: ``scheduled_by``; JSON type: string"""
    sent_at: datetime | None = field(init=False)
    """When the transfer was sent. Optional; nullable. Python type: ``datetime | None``; wire name: ``sent_at``; JSON type: string (date-time)"""
    source_id: str | None = field(init=False)
    """Source identifier associated with the payout. Optional; nullable. Python type: ``str | None``; wire name: ``source_id``; JSON type: string"""
    status: Literal['initialized', 'scheduled', 'processing', 'executing', 'succeeded', 'invalid', 'canceled'] = field(init=False)
    """Current payout lifecycle state. Required. Python type: ``Literal['initialized', 'scheduled', 'processing', 'executing', 'succeeded', 'invalid', 'canceled']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``initialized``, ``scheduled``, ``processing``, ``executing``, ``succeeded``, ``invalid``, ``canceled``"""
    succeeded_at: datetime | None = field(init=False)
    """When the payout succeeded. Optional; nullable. Python type: ``datetime | None``; wire name: ``succeeded_at``; JSON type: string (date-time)"""

from inttegro.payout.error import Error as PayoutError
from inttegro.custom_data import CustomData
