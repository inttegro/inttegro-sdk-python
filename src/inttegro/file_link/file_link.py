"""FileLink in the ``inttegro.file_link`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileLink(ApiModel):
    """Public file link metadata. Token hashes and provider URLs are not exposed.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    id: str = field(init=False)
    """Unique identifier for this file link. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    kind: Literal['public'] = field(init=False)
    """The kind associated with this file link. Required. Python type: ``Literal['public']``; wire name: ``kind``; JSON type: string. Constraints: allowed values ``public``"""
    file_id: str = field(init=False)
    """Identifier of the related file. Required. Python type: ``str``; wire name: ``file_id``; JSON type: string"""
    purpose: str = field(init=False)
    """The purpose associated with this file link. Required. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    status: Literal['active', 'revoked', 'expired', 'disabled'] = field(init=False)
    """Current lifecycle status of the file link. Required. Python type: ``Literal['active', 'revoked', 'expired', 'disabled']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``active``, ``revoked``, ``expired``, ``disabled``"""
    active: bool = field(init=False)
    """Whether the file link is active. Required. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    delivery: FileLinkDelivery = field(init=False)
    """The delivery associated with this file link. Required. Python type: ``FileLinkDelivery``; wire name: ``delivery``; JSON type: object (FileLinkDelivery)"""
    access: FileLinkAccess = field(init=False)
    """The access associated with this file link. Required. Python type: ``FileLinkAccess``; wire name: ``access``; JSON type: object (FileLinkAccess)"""
    created_by: FileLinkActor = field(init=False)
    """The created by associated with this file link. Required. Python type: ``FileLinkActor``; wire name: ``created_by``; JSON type: object (FileLinkActor)"""
    revoked_by: FileLinkActor | None = field(init=False)
    """The revoked by associated with this file link. Optional; nullable. Python type: ``FileLinkActor | None``; wire name: ``revoked_by``; JSON type: object (FileLinkActor)"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    metadata: dict[str, str] | None = field(init=False)
    """System-managed string metadata attached to a file resource. Optional; nullable. Python type: ``dict[str, str] | None``; wire name: ``metadata``; JSON type: object (FileMetadata)"""
    created_at: datetime = field(init=False)
    """When the file link was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    updated_at: datetime = field(init=False)
    """When the file link was last updated. Required. Python type: ``datetime``; wire name: ``updated_at``; JSON type: string (date-time)"""
    expires_at: datetime = field(init=False)
    """Timestamp for expires at. Required. Python type: ``datetime``; wire name: ``expires_at``; JSON type: string (date-time)"""
    revoked_at: datetime | None = field(init=False)
    """Timestamp for revoked at. Optional; nullable. Python type: ``datetime | None``; wire name: ``revoked_at``; JSON type: string (date-time)"""

from inttegro.file_link.access import Access as FileLinkAccess
from inttegro.file_link.actor import Actor as FileLinkActor
from inttegro.file_link.delivery import Delivery as FileLinkDelivery
from inttegro.custom_data import CustomData
