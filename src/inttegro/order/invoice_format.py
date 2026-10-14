"""InvoiceFormat in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class InvoiceFormat(ApiModel):
    """Typed invoice format data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderInvoiceFormat``.
    """
    web: OrderDocumentFormat = field(init=False)
    """The web associated with this invoice format. Required. Python type: ``OrderDocumentFormat``; wire name: ``web``; JSON type: object (OrderDocumentFormat)"""
    pdf: OrderDocumentFormat = field(init=False)
    """The pdf associated with this invoice format. Required. Python type: ``OrderDocumentFormat``; wire name: ``pdf``; JSON type: object (OrderDocumentFormat)"""

from inttegro.order.document_format import DocumentFormat as OrderDocumentFormat
