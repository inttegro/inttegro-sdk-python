"""ProductLineItemProduct in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.price.inline import Inline as Price
from inttegro.custom_data import CustomData


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductLineItemProduct(ApiModel):
    """Typed product line item product data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderProductLineItemProduct``.
    """
    id: str = field(init=False)
    """Immutable order-line identifier with the `oli_` prefix. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    product_id: str | None = field(init=False)
    """Source catalog product ID when this line snapshots a catalog product. Optional; nullable. Python type: ``str | None``; wire name: ``product_id``; JSON type: string"""
    price_id: str | None = field(init=False)
    """Source catalog price ID when this line snapshots a saved price. Optional; nullable. Python type: ``str | None``; wire name: ``price_id``; JSON type: string"""
    reference: str | None = field(init=False)
    """Merchant-defined external reference for the product line item product. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""
    about: str | None = field(init=False)
    """The about associated with this product line item product. Optional; nullable. Python type: ``str | None``; wire name: ``about``; JSON type: string"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    tax_code: str | None = field(init=False)
    """The tax code associated with this product line item product. Optional; nullable. Python type: ``str | None``; wire name: ``tax_code``; JSON type: string"""
    name: str = field(init=False)
    """Human-readable name of the product line item product. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    category: str | None = field(init=False)
    """The category associated with this product line item product. Optional; nullable. Python type: ``str | None``; wire name: ``category``; JSON type: string"""
    type: str | None = field(init=False)
    """Discriminator identifying the product line item product type. Optional; nullable. Python type: ``str | None``; wire name: ``type``; JSON type: string"""
    price: Price = field(init=False)
    """An inline price returned by the API. Required. Python type: ``Price``; wire name: ``price``; JSON type: object (Price)"""
    quantity: int = field(init=False)
    """Numeric quantity used by this operation. Required. Python type: ``int``; wire name: ``quantity``; JSON type: integer"""
