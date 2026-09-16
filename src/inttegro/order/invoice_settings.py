"""InvoiceSettings in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.custom_data import CustomData


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class InvoiceSettings(ApiModel):
    """Order-level invoice rendering data. Pages uses this data when rendering invoice web and download views.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    number: str | None = field(init=False)
    """Optional invoice number. When omitted, invoice delivery falls back to the order number and then the order ID for labels. Optional; nullable. Python type: ``str | None``; wire name: ``number``; JSON type: string"""
    memo: str | None = field(init=False)
    """Optional invoice memo. Optional; nullable. Python type: ``str | None``; wire name: ``memo``; JSON type: string"""
    footer: str | None = field(init=False)
    """Optional invoice footer. Optional; nullable. Python type: ``str | None``; wire name: ``footer``; JSON type: string"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
