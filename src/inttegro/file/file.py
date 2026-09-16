"""File in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class File(ApiModel):
    """Public file metadata. Storage provider details, object keys, and idempotency internals are not exposed.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    id: str = field(init=False)
    """Unique identifier for this file. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    purpose: str = field(init=False)
    """The purpose associated with this file. Required. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    status: Literal['uploading', 'processing', 'available', 'failed', 'deleted'] = field(init=False)
    """Current lifecycle status of the file. Required. Python type: ``Literal['uploading', 'processing', 'available', 'failed', 'deleted']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``uploading``, ``processing``, ``available``, ``failed``, ``deleted``"""
    scan_status: Literal['pending', 'passed', 'failed', 'skipped'] = field(init=False)
    """The scan status associated with this file. Required. Python type: ``Literal['pending', 'passed', 'failed', 'skipped']``; wire name: ``scan_status``; JSON type: string. Constraints: allowed values ``pending``, ``passed``, ``failed``, ``skipped``"""
    name: str | None = field(init=False)
    """Human-readable name of the file. Optional; nullable. Python type: ``str | None``; wire name: ``name``; JSON type: string"""
    filename: str | None = field(init=False)
    """The filename associated with this file. Optional; nullable. Python type: ``str | None``; wire name: ``filename``; JSON type: string"""
    content_type: str = field(init=False)
    """The content type associated with this file. Required. Python type: ``str``; wire name: ``content_type``; JSON type: string"""
    size: int = field(init=False)
    """Original byte size. Required. Python type: ``int``; wire name: ``size``; JSON type: integer (int64)"""
    checksum_sha256: str = field(init=False)
    """The checksum sha256 associated with this file. Required. Python type: ``str``; wire name: ``checksum_sha256``; JSON type: string"""
    created_by: FileActor = field(init=False)
    """The created by associated with this file. Required. Python type: ``FileActor``; wire name: ``created_by``; JSON type: object (FileActor)"""
    source: FileSource = field(init=False)
    """The source associated with this file. Required. Python type: ``FileSource``; wire name: ``source``; JSON type: object (FileSource)"""
    media: FileMedia | None = field(init=False)
    """The media associated with this file. Optional; nullable. Python type: ``FileMedia | None``; wire name: ``media``; JSON type: object (FileMedia)"""
    storage: PublicFileStorage = field(init=False)
    """The storage associated with this file. Required. Python type: ``PublicFileStorage``; wire name: ``storage``; JSON type: object (PublicFileStorage)"""
    delivery: FileDeliveryDetails | None = field(init=False)
    """Purpose-authorized public delivery metadata for browser-rendered assets. Callers should store file IDs as canonical references and treat these URLs as render URLs. Optional; nullable. Python type: ``FileDeliveryDetails | None``; wire name: ``delivery``; JSON type: object (FileDelivery)"""
    latest_error: FileLatestError | None = field(init=False)
    """The latest error associated with this file. Optional; nullable. Python type: ``FileLatestError | None``; wire name: ``latest_error``; JSON type: object (FileLatestError)"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    metadata: dict[str, str] | None = field(init=False)
    """System-managed string metadata attached to a file resource. Optional; nullable. Python type: ``dict[str, str] | None``; wire name: ``metadata``; JSON type: object (FileMetadata)"""
    created_at: datetime = field(init=False)
    """When the file was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    updated_at: datetime = field(init=False)
    """When the file was last updated. Required. Python type: ``datetime``; wire name: ``updated_at``; JSON type: string (date-time)"""
    available_at: datetime | None = field(init=False)
    """Timestamp for available at. Optional; nullable. Python type: ``datetime | None``; wire name: ``available_at``; JSON type: string (date-time)"""
    expires_at: datetime | None = field(init=False)
    """Timestamp for expires at. Optional; nullable. Python type: ``datetime | None``; wire name: ``expires_at``; JSON type: string (date-time)"""

from inttegro.file.actor import Actor as FileActor
from inttegro.file.delivery_details import DeliveryDetails as FileDeliveryDetails
from inttegro.file.latest_error import LatestError as FileLatestError
from inttegro.file.media import Media as FileMedia
from inttegro.file.source import Source as FileSource
from inttegro.file.public_storage import PublicStorage as PublicFileStorage
from inttegro.custom_data import CustomData
