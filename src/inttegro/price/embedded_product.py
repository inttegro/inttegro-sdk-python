"""EmbeddedProduct in the ``inttegro.price`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EmbeddedProduct(ApiModel):
    """Typed embedded product data in the price resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PriceEmbeddedProduct``.
    """
    id: str = field(init=False)
    """Unique product identifier with prod_ prefix. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    about: str | None = field(init=False)
    """Full product description. Optional; nullable. Python type: ``str | None``; wire name: ``about``; JSON type: string"""
    active: bool = field(init=False)
    """Whether product is published and available. Required. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    archived_at: datetime | None = field(init=False)
    """Archive timestamp (if archived). Optional; nullable. Python type: ``datetime | None``; wire name: ``archived_at``; JSON type: string (date-time)"""
    attributes: list[PriceEmbeddedProductAttributesItem] | None = field(init=False)
    """Product attributes. Optional; nullable. Python type: ``list[PriceEmbeddedProductAttributesItem] | None``; wire name: ``attributes``; JSON type: array of object values"""
    category: str | None = field(init=False)
    """Product category. Optional; nullable. Python type: ``str | None``; wire name: ``category``; JSON type: string"""
    created_at: datetime = field(init=False)
    """Product creation timestamp. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    description: str | None = field(init=False)
    """Short description. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    dimensions: ProductDimensions | None = field(init=False)
    """Product dimensions and size metadata. Optional; nullable. Python type: ``ProductDimensions | None``; wire name: ``dimensions``; JSON type: object (ProductDimensions)"""
    media: ProductMedia | None = field(init=False)
    """Product media assets. Optional; nullable. Python type: ``ProductMedia | None``; wire name: ``media``; JSON type: object (ProductMedia)"""
    name: str = field(init=False)
    """Product name. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    published_at: datetime | None = field(init=False)
    """When the product was published. Optional; nullable. Python type: ``datetime | None``; wire name: ``published_at``; JSON type: string (date-time)"""
    reference: str | None = field(init=False)
    """External reference or SKU. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""
    shipment: ProductShipment | None = field(init=False)
    """Shipment and fulfillment details. Optional; nullable. Python type: ``ProductShipment | None``; wire name: ``shipment``; JSON type: object (ProductShipment)"""
    tax_code: str | None = field(init=False)
    """Tax classification code. Optional; nullable. Python type: ``str | None``; wire name: ``tax_code``; JSON type: string"""
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause'] = field(init=False)
    """Product type. Required. Python type: ``Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``physical``, ``digital``, ``service``, ``voucher``, ``custom``, ``cause``"""
    unit_dim: str | None = field(init=False)
    """Unit dimension label. Optional; nullable. Python type: ``str | None``; wire name: ``unit_dim``; JSON type: string"""
    updated_at: datetime | None = field(init=False)
    """Last update timestamp. Optional; nullable. Python type: ``datetime | None``; wire name: ``updated_at``; JSON type: string (date-time)"""

from inttegro.price.embedded_product_attributes_item import EmbeddedProductAttributesItem as PriceEmbeddedProductAttributesItem
from inttegro.product.dimensions import Dimensions as ProductDimensions
from inttegro.product.media import Media as ProductMedia
from inttegro.product.shipment import Shipment as ProductShipment
from inttegro.custom_data import CustomData
