"""Price in the ``inttegro.price`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel
from inttegro.money import Amount
from inttegro.price.customer_selected_amount import CustomerSelectedAmount
from inttegro.price.type import Type


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Price(ApiModel):
    """Typed price data in the price resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``CatalogPrice``.
    """
    id: str = field(init=False)
    """Unique price identifier with pr_ prefix. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    label: str | None = field(init=False)
    """Short label for this price. Optional; nullable. Python type: ``str | None``; wire name: ``label``; JSON type: string"""
    about: str | None = field(init=False)
    """Longer description of this price. Optional; nullable. Python type: ``str | None``; wire name: ``about``; JSON type: string"""
    active: bool = field(init=False)
    """Whether this price is active and usable in new flows. Required. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    type: Type = field(init=False)
    """Price definition discriminator. Required. Python type: ``Type``; wire name: ``type``; JSON type: string (PriceType)"""
    nominal: Amount | None = field(init=False)
    """Deprecated fixed-price compatibility alias. Present only for fixed prices. Python type: ``Amount | None``; wire name: ``nominal``; JSON type: object (Amount)"""
    fixed_amount: Amount | None = field(init=False)
    """Fixed amount present only for fixed prices. Python type: ``Amount | None``; wire name: ``fixed_amount``; JSON type: object (Amount)"""
    customer_selected_amount: CustomerSelectedAmount | None = field(init=False)
    """Selection policy present only for customer-selected prices. Python type: ``CustomerSelectedAmount | None``; wire name: ``customer_selected_amount``; JSON type: object (CustomerSelectedAmount)"""
    product_id: str | None = field(init=False)
    """Product ID when the operation returns the relationship by reference. Optional; nullable. Python type: ``str | None``; wire name: ``product_id``; JSON type: string"""
    product: PriceEmbeddedProduct | None = field(init=False)
    """Embedded product details, if this price belongs to a product. Optional; nullable. Python type: ``PriceEmbeddedProduct | None``; wire name: ``product``; JSON type: object (PriceEmbeddedProduct)"""
    created_at: datetime = field(init=False)
    """Price creation timestamp. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    updated_at: datetime | None = field(init=False)
    """Last update timestamp. Optional; nullable. Python type: ``datetime | None``; wire name: ``updated_at``; JSON type: string (date-time)"""
    archived_at: datetime | None = field(init=False)
    """Archive timestamp (if archived). Optional; nullable. Python type: ``datetime | None``; wire name: ``archived_at``; JSON type: string (date-time)"""

from inttegro.price.embedded_product import EmbeddedProduct as PriceEmbeddedProduct
