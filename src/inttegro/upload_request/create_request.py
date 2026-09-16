"""CreateRequest in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequest(ApiRequest):
    """Parameters accepted by the create request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreateUploadRequestRequest``.
    """
    constraints: UploadRequestConstraintsInput | UnsetType = field(default=UNSET)
    """The constraints associated with this create request. Optional. Python type: ``UploadRequestConstraintsInput``; wire name: ``constraints``; JSON type: object (UploadRequestConstraints)"""
    display: UploadRequestDisplayInput | UnsetType = field(default=UNSET)
    """The display associated with this create request. Optional. Python type: ``UploadRequestDisplayInput``; wire name: ``display``; JSON type: object (UploadRequestDisplay)"""
    subject: FilePartyInput | UnsetType = field(default=UNSET)
    """The subject associated with this create request. Optional. Python type: ``FilePartyInput``; wire name: ``subject``; JSON type: object (FileParty)"""
    recipient: FilePartyInput | UnsetType = field(default=UNSET)
    """The recipient associated with this create request. Optional. Python type: ``FilePartyInput``; wire name: ``recipient``; JSON type: object (FileParty)"""
    resource: FileResourceInput | UnsetType = field(default=UNSET)
    """The resource associated with this create request. Optional. Python type: ``FileResourceInput``; wire name: ``resource``; JSON type: object (FileResource)"""
    requester: FileActorInput | UnsetType = field(default=UNSET)
    """The requester associated with this create request. Optional. Python type: ``FileActorInput``; wire name: ``requester``; JSON type: object (FileActorInput)"""
    attempts: UploadRequestAttemptsRequest | UnsetType = field(default=UNSET)
    """The attempts associated with this create request. Optional. Python type: ``UploadRequestAttemptsRequest``; wire name: ``attempts``; JSON type: object (UploadRequestAttemptsRequest)"""
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    expires_at: datetime | UnsetType = field(default=UNSET)
    """Timestamp for expires at. Optional. Python type: ``datetime``; wire name: ``expires_at``; JSON type: string (date-time)"""
    purpose: str
    """The purpose associated with this create request. Required. Python type: ``str``; wire name: ``purpose``; JSON type: string"""

from inttegro.file.actor_input import ActorInput as FileActorInput
from inttegro.file.party_input import PartyInput as FilePartyInput
from inttegro.file.resource_input import ResourceInput as FileResourceInput
from inttegro.upload_request.attempts_request import AttemptsRequest as UploadRequestAttemptsRequest
from inttegro.upload_request.constraints_input import ConstraintsInput as UploadRequestConstraintsInput
from inttegro.upload_request.display_input import DisplayInput as UploadRequestDisplayInput
from inttegro.custom_data import CustomData
