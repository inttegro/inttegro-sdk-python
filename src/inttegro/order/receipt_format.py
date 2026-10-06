"""Hosted document formats for a paid order receipt."""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.order.document_format import DocumentFormat as OrderDocumentFormat


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ReceiptFormat(ApiModel):
    """Web and PDF representations of a payment receipt."""

    web: OrderDocumentFormat = field(init=False)
    pdf: OrderDocumentFormat = field(init=False)
