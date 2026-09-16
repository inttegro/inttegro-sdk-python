"""UploadRequest in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequest(ApiModel):
    """Typed upload request data in the upload request resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    id: str = field(init=False)
    """Unique identifier for this upload request. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    purpose: str = field(init=False)
    """The purpose associated with this upload request. Required. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    status: Literal['pending', 'uploading', 'fulfilled', 'expired', 'canceled', 'failed'] = field(init=False)
    """Current lifecycle status of the upload request. Required. Python type: ``Literal['pending', 'uploading', 'fulfilled', 'expired', 'canceled', 'failed']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``pending``, ``uploading``, ``fulfilled``, ``expired``, ``canceled``, ``failed``"""
    active: bool = field(init=False)
    """Whether the upload request is active. Required. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    file_id: str | None = field(init=False)
    """Identifier of the related file. Optional; nullable. Python type: ``str | None``; wire name: ``file_id``; JSON type: string"""
    upload_url: str | None = field(init=False)
    """Public capability URL returned when available. Treat as bearer-secret material. Optional; nullable. Python type: ``str | None``; wire name: ``upload_url``; JSON type: string (uri)"""
    constraints: UploadRequestConstraints = field(init=False)
    """The constraints associated with this upload request. Required. Python type: ``UploadRequestConstraints``; wire name: ``constraints``; JSON type: object (UploadRequestConstraints)"""
    display: UploadRequestDisplay = field(init=False)
    """The display associated with this upload request. Required. Python type: ``UploadRequestDisplay``; wire name: ``display``; JSON type: object (UploadRequestDisplay)"""
    subject: FileParty = field(init=False)
    """The subject associated with this upload request. Required. Python type: ``FileParty``; wire name: ``subject``; JSON type: object (FileParty)"""
    recipient: FileParty = field(init=False)
    """The recipient associated with this upload request. Required. Python type: ``FileParty``; wire name: ``recipient``; JSON type: object (FileParty)"""
    resource: FileResource = field(init=False)
    """The resource associated with this upload request. Required. Python type: ``FileResource``; wire name: ``resource``; JSON type: object (FileResource)"""
    requester: UploadRequestActor = field(init=False)
    """The requester associated with this upload request. Required. Python type: ``UploadRequestActor``; wire name: ``requester``; JSON type: object (UploadRequestActor)"""
    attempts: UploadRequestAttempts = field(init=False)
    """The attempts associated with this upload request. Required. Python type: ``UploadRequestAttempts``; wire name: ``attempts``; JSON type: object (UploadRequestAttempts)"""
    latest_error: UploadRequestLatestError | None = field(init=False)
    """The latest error associated with this upload request. Optional; nullable. Python type: ``UploadRequestLatestError | None``; wire name: ``latest_error``; JSON type: object (UploadRequestLatestError)"""
    canceled_by: UploadRequestActor | None = field(init=False)
    """The canceled by associated with this upload request. Optional; nullable. Python type: ``UploadRequestActor | None``; wire name: ``canceled_by``; JSON type: object (UploadRequestActor)"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    metadata: dict[str, str] | None = field(init=False)
    """System-managed string metadata attached to a file resource. Optional; nullable. Python type: ``dict[str, str] | None``; wire name: ``metadata``; JSON type: object (FileMetadata)"""
    created_at: datetime = field(init=False)
    """When the upload request was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    updated_at: datetime = field(init=False)
    """When the upload request was last updated. Required. Python type: ``datetime``; wire name: ``updated_at``; JSON type: string (date-time)"""
    expires_at: datetime = field(init=False)
    """Timestamp for expires at. Required. Python type: ``datetime``; wire name: ``expires_at``; JSON type: string (date-time)"""
    uploading_at: datetime | None = field(init=False)
    """Timestamp for uploading at. Optional; nullable. Python type: ``datetime | None``; wire name: ``uploading_at``; JSON type: string (date-time)"""
    fulfilled_at: datetime | None = field(init=False)
    """Timestamp for fulfilled at. Optional; nullable. Python type: ``datetime | None``; wire name: ``fulfilled_at``; JSON type: string (date-time)"""
    expired_at: datetime | None = field(init=False)
    """When the upload request expired. Optional; nullable. Python type: ``datetime | None``; wire name: ``expired_at``; JSON type: string (date-time)"""
    canceled_at: datetime | None = field(init=False)
    """When the upload request was canceled. Optional; nullable. Python type: ``datetime | None``; wire name: ``canceled_at``; JSON type: string (date-time)"""
    attempt: UploadRequestAttempt | None = field(init=False)
    """The attempt associated with this upload request. Optional; nullable. Python type: ``UploadRequestAttempt | None``; wire name: ``attempt``; JSON type: object (UploadRequestAttempt)"""

from inttegro.file.party import Party as FileParty
from inttegro.file.resource import Resource as FileResource
from inttegro.upload_request.actor import Actor as UploadRequestActor
from inttegro.upload_request.attempt import Attempt as UploadRequestAttempt
from inttegro.upload_request.attempts import Attempts as UploadRequestAttempts
from inttegro.upload_request.constraints import Constraints as UploadRequestConstraints
from inttegro.upload_request.display import Display as UploadRequestDisplay
from inttegro.upload_request.latest_error import LatestError as UploadRequestLatestError
from inttegro.custom_data import CustomData
