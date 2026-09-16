"""Updated in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Updated(ApiModel):
    """Typed updated data in the product resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UpdatedProduct``.
    """
    id: str = field(init=False)
    """Product identifier returned by the update operation. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    name: str = field(init=False)
    """Human-readable name of the updated. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    description: str | None = field(init=False)
    """Human-readable description of the updated. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    about: str | None = field(init=False)
    """The about associated with this updated. Optional; nullable. Python type: ``str | None``; wire name: ``about``; JSON type: string"""
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause'] = field(init=False)
    """Discriminator identifying the updated type. Required. Python type: ``Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``physical``, ``digital``, ``service``, ``voucher``, ``custom``, ``cause``"""
    reference: str | None = field(init=False)
    """Merchant-defined external reference for the updated. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""
    tax_code: str | None = field(init=False)
    """The tax code associated with this updated. Optional; nullable. Python type: ``str | None``; wire name: ``tax_code``; JSON type: string"""
    category: str | None = field(init=False)
    """The category associated with this updated. Optional; nullable. Python type: ``str | None``; wire name: ``category``; JSON type: string"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    dimensions: ProductDimensions | None = field(init=False)
    """At most one of `physical`, `digital`, or `custom`. Optional; nullable. Python type: ``ProductDimensions | None``; wire name: ``dimensions``; JSON type: object (ProductDimensions)"""
    prices: list[ProductPriceSummary] | None = field(init=False)
    """The prices associated with this updated. Optional; nullable. Python type: ``list[ProductPriceSummary] | None``; wire name: ``prices``; JSON type: array of object (ProductPriceSummary) values"""
    unit_dim: str | None = field(init=False)
    """The unit dim associated with this updated. Optional; nullable. Python type: ``str | None``; wire name: ``unit_dim``; JSON type: string"""
    created_at: datetime = field(init=False)
    """When the updated was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    updated_at: datetime | None = field(init=False)
    """When the updated was last updated. Optional; nullable. Python type: ``datetime | None``; wire name: ``updated_at``; JSON type: string (date-time)"""

from inttegro.product.dimensions import Dimensions as ProductDimensions
from inttegro.product.price_summary import PriceSummary as ProductPriceSummary
from inttegro.custom_data import CustomData
