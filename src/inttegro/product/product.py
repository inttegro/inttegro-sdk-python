"""Product in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Product(ApiModel):
    """Typed product data in the product resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    id: str = field(init=False)
    """Unique product identifier with prod_ prefix. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause'] = field(init=False)
    """Product type. Required. Python type: ``Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``physical``, ``digital``, ``service``, ``voucher``, ``custom``, ``cause``"""
    reference: str | None = field(init=False)
    """External reference or SKU. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""
    name: str = field(init=False)
    """Product name. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    description: str | None = field(init=False)
    """Short description. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    about: str | None = field(init=False)
    """Full product description. Optional; nullable. Python type: ``str | None``; wire name: ``about``; JSON type: string"""
    tax_code: str | None = field(init=False)
    """Tax classification code. Optional; nullable. Python type: ``str | None``; wire name: ``tax_code``; JSON type: string"""
    category: str | None = field(init=False)
    """Product category. Optional; nullable. Python type: ``str | None``; wire name: ``category``; JSON type: string"""
    prices: list[ProductPriceSummary] | None = field(init=False)
    """Non-archived prices that belong to this product. Optional; nullable. Python type: ``list[ProductPriceSummary] | None``; wire name: ``prices``; JSON type: array of object (ProductPriceSummary) values"""
    shipment: ProductShipment | None = field(init=False)
    """The shipment associated with this product. Optional; nullable. Python type: ``ProductShipment | None``; wire name: ``shipment``; JSON type: object (ProductShipment)"""
    media: ProductMedia | None = field(init=False)
    """The media associated with this product. Optional; nullable. Python type: ``ProductMedia | None``; wire name: ``media``; JSON type: object (ProductMedia)"""
    attributes: list[ProductAttribute] | None = field(init=False)
    """Product attributes. Optional; nullable. Python type: ``list[ProductAttribute] | None``; wire name: ``attributes``; JSON type: array of object (ProductAttribute) values"""
    dimensions: ProductDimensions | None = field(init=False)
    """At most one of `physical`, `digital`, or `custom`. Optional; nullable. Python type: ``ProductDimensions | None``; wire name: ``dimensions``; JSON type: object (ProductDimensions)"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    active: bool = field(init=False)
    """Whether product is published and available. Required. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    created_at: datetime = field(init=False)
    """Product creation timestamp. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    updated_at: datetime | None = field(init=False)
    """Last update timestamp. Optional; nullable. Python type: ``datetime | None``; wire name: ``updated_at``; JSON type: string (date-time)"""
    archived_at: datetime | None = field(init=False)
    """Archive timestamp (if archived). Optional; nullable. Python type: ``datetime | None``; wire name: ``archived_at``; JSON type: string (date-time)"""
    published_at: datetime | None = field(init=False)
    """When the product was published. Optional; nullable. Python type: ``datetime | None``; wire name: ``published_at``; JSON type: string (date-time)"""
    unit_dim: str | None = field(init=False)
    """Unit dimension label. Optional; nullable. Python type: ``str | None``; wire name: ``unit_dim``; JSON type: string"""

    def is_archived(self) -> bool:
        """Whether the product is archived."""
        return getattr(self, "archived_at", None) is not None

    def is_published(self) -> bool:
        """Whether the product is currently published and available."""
        return self.active and not self.is_archived()

    def was_ever_published(self) -> bool:
        """Whether the product has a recorded first publication."""
        return getattr(self, "published_at", None) is not None

from inttegro.product.attribute import Attribute as ProductAttribute
from inttegro.product.dimensions import Dimensions as ProductDimensions
from inttegro.product.media import Media as ProductMedia
from inttegro.product.price_summary import PriceSummary as ProductPriceSummary
from inttegro.product.shipment import Shipment as ProductShipment
from inttegro.custom_data import CustomData
