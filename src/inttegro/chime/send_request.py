"""SendRequest in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class SendRequest(ApiRequest):
    """Request to send a chime to a recipient. SMS recipients accept either `full_message` or `message_template`. Email recipients accept either `email` or `message_template`.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``SendChimeRequest``.
    """
    full_message: str | UnsetType = field(default=UNSET)
    """Complete SMS message content. Use only with SMS recipients. Optional. Python type: ``str``; wire name: ``full_message``; JSON type: string"""
    email: ChimeEmailMessageInput | UnsetType = field(default=UNSET)
    """Email content accepted for email chimes, broadcasts, and schedules. Optional. Python type: ``ChimeEmailMessageInput``; wire name: ``email``; JSON type: object (ChimeEmailMessageInput)"""
    message_template: MessageTemplateReferenceInput | UnsetType = field(default=UNSET)
    """The message template associated with this send request. Optional. Python type: ``MessageTemplateReferenceInput``; wire name: ``message_template``; JSON type: object (MessageTemplateReference)"""
    sender_id: str | UnsetType = field(default=UNSET)
    """Sender identifier shown to recipient. Uses default sender if not provided. Optional. Python type: ``str``; wire name: ``sender_id``; JSON type: string"""
    purpose: str | UnsetType = field(default=UNSET)
    """Purpose of this chime for categorization and analytics. Optional. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    request_meta: SendChimeRequestRequestMeta | UnsetType = field(default=UNSET)
    """Optional metadata controlling request processing. Optional. Python type: ``SendChimeRequestRequestMeta``; wire name: ``request_meta``; JSON type: object"""
    recipient: ChimeRecipientInput
    """The recipient associated with this send request. Required. Python type: ``ChimeRecipientInput``; wire name: ``recipient``; JSON type: object (ChimeRecipient)"""

from inttegro.chime.email_message_input import EmailMessageInput as ChimeEmailMessageInput
from inttegro.chime.recipient_input import RecipientInput as ChimeRecipientInput
from inttegro.message_template.reference_input import ReferenceInput as MessageTemplateReferenceInput
from inttegro.chime.send_request_request_meta import SendRequestRequestMeta as SendChimeRequestRequestMeta
from inttegro.custom_data import CustomData
