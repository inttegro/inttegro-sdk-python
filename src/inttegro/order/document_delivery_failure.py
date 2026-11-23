"""DocumentDeliveryFailure in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DocumentDeliveryFailure(ApiModel):
    """Chime delivery failure for one channel.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderDocumentDeliveryFailure``.
    """
    channel: Literal['email', 'sms'] | None = field(init=False)
    """Delivery channel. Optional; nullable. Python type: ``Literal['email', 'sms'] | None``; wire name: ``channel``; JSON type: string. Constraints: allowed values ``email``, ``sms``"""
