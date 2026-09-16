"""Chime in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Chime(ApiModel):
    """A notification sent to one recipient.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    created_at: datetime = field(init=False)
    """When the chime was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    customer_id: str | None = field(init=False)
    """Identifier of the related customer. Optional; nullable. Python type: ``str | None``; wire name: ``customer_id``; JSON type: string"""
    email: ChimeEmailMessage | None = field(init=False)
    """Email content, safety scan result, and system-generated schema markup for email chimes. Optional; nullable. Python type: ``ChimeEmailMessage | None``; wire name: ``email``; JSON type: object (ChimeEmailMessage)"""
    full_message: str = field(init=False)
    """Rendered SMS content. Empty for email Chimes. Required. Python type: ``str``; wire name: ``full_message``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this chime. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    idempotency_key: str | None = field(init=False)
    """Stable key used to make retries of the same logical write safe. Optional; nullable. Python type: ``str | None``; wire name: ``idempotency_key``; JSON type: string"""
    purpose: str | None = field(init=False)
    """The purpose associated with this chime. Optional; nullable. Python type: ``str | None``; wire name: ``purpose``; JSON type: string"""
    recipient: ChimeRecipient = field(init=False)
    """Recipient information in response. Required. Python type: ``ChimeRecipient``; wire name: ``recipient``; JSON type: object (ChimeRecipientResponse)"""
    sender_id: str = field(init=False)
    """Identifier of the related sender. Required. Python type: ``str``; wire name: ``sender_id``; JSON type: string"""
    transmission: ChimeTransmission | None = field(init=False)
    """The transmission associated with this chime. Optional; nullable. Python type: ``ChimeTransmission | None``; wire name: ``transmission``; JSON type: object (ChimeTransmission)"""

from inttegro.chime.email_message import EmailMessage as ChimeEmailMessage
from inttegro.chime.recipient import Recipient as ChimeRecipient
from inttegro.chime.transmission import Transmission as ChimeTransmission
from inttegro.custom_data import CustomData
