"""CreateRequest in the ``inttegro.file_link`` resource namespace.

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

    API contract schema: ``CreateFileLinkRequest``.
    """
    delivery: FileLinkDeliveryInput | UnsetType = field(default=UNSET)
    """The delivery associated with this create request. Optional. Python type: ``FileLinkDeliveryInput``; wire name: ``delivery``; JSON type: object (FileLinkDelivery)"""
    access: FileLinkAccessRequest | UnsetType = field(default=UNSET)
    """The access associated with this create request. Optional. Python type: ``FileLinkAccessRequest``; wire name: ``access``; JSON type: object (FileLinkAccessRequest)"""
    created_by: FileActorInput | UnsetType = field(default=UNSET)
    """The created by associated with this create request. Optional. Python type: ``FileActorInput``; wire name: ``created_by``; JSON type: object (FileActorInput)"""
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    expires_at: datetime | UnsetType = field(default=UNSET)
    """Timestamp for expires at. Optional. Python type: ``datetime``; wire name: ``expires_at``; JSON type: string (date-time)"""
    file_id: str
    """Identifier of the related file. Required. Python type: ``str``; wire name: ``file_id``; JSON type: string"""

from inttegro.file.actor_input import ActorInput as FileActorInput
from inttegro.file_link.access_request import AccessRequest as FileLinkAccessRequest
from inttegro.file_link.delivery_input import DeliveryInput as FileLinkDeliveryInput
from inttegro.custom_data import CustomData
