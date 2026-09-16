"""UpdateRequest in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequest(ApiRequest):
    """Parameters accepted by the update request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdateProductRequest``.
    """
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause', ProductType.PHYSICAL, ProductType.DIGITAL, ProductType.SERVICE, ProductType.VOUCHER, ProductType.CUSTOM, ProductType.CAUSE] | UnsetType = field(default=UNSET)
    """Product type. If provided, it must equal the existing type. Optional. Python type: ``Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause', ProductType.PHYSICAL, ProductType.DIGITAL, ProductType.SERVICE, ProductType.VOUCHER, ProductType.CUSTOM, ProductType.CAUSE]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``physical``, ``digital``, ``service``, ``voucher``, ``custom``, ``cause``"""
    name: str | UnsetType = field(default=UNSET)
    """Product name. Optional. Python type: ``str``; wire name: ``name``; JSON type: string. Constraints: minimum length 1; maximum length 100"""
    description: str | UnsetType = field(default=UNSET)
    """Short description. Optional. Python type: ``str``; wire name: ``description``; JSON type: string. Constraints: maximum length 200"""
    about: str | UnsetType = field(default=UNSET)
    """Full description. Optional. Python type: ``str``; wire name: ``about``; JSON type: string"""
    tax_code: str | UnsetType = field(default=UNSET)
    """Tax classification code. Optional. Python type: ``str``; wire name: ``tax_code``; JSON type: string"""
    category: str | UnsetType = field(default=UNSET)
    """Product category. Optional. Python type: ``str``; wire name: ``category``; JSON type: string"""
    shipment: ProductShipmentInput | UnsetType = field(default=UNSET)
    """The shipment associated with this update request. Optional. Python type: ``ProductShipmentInput``; wire name: ``shipment``; JSON type: object (ProductShipmentInput)"""
    dimensions: ProductDimensionsInput | UnsetType = field(default=UNSET)
    """At most one of `physical`, `digital`, or `custom`. Optional. Python type: ``ProductDimensionsInput``; wire name: ``dimensions``; JSON type: object (ProductDimensions)"""
    unit_dimension: str | UnsetType = field(default=UNSET)
    """The unit dimension associated with this update request. Optional. Python type: ``str``; wire name: ``unit_dimension``; JSON type: string. Constraints: maximum length 20"""
    media: ProductMediaInput | UnsetType = field(default=UNSET)
    """The media associated with this update request. Optional. Python type: ``ProductMediaInput``; wire name: ``media``; JSON type: object (ProductMedia)"""
    images: list[str] | UnsetType = field(default=UNSET)
    """Legacy image list. Mutually exclusive with `media`. Optional. Python type: ``list[str]``; wire name: ``images``; JSON type: array of string values"""
    attributes: list[ProductAttributeInput] | UnsetType = field(default=UNSET)
    """Product attributes. Optional. Python type: ``list[ProductAttributeInput]``; wire name: ``attributes``; JSON type: array of object (ProductAttribute) values"""
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    product_id: str
    """Product ID to update. Required. Python type: ``str``; wire name: ``product_id``; JSON type: string"""

from inttegro.product.attribute_input import AttributeInput as ProductAttributeInput
from inttegro.product.dimensions_input import DimensionsInput as ProductDimensionsInput
from inttegro.product.media_input import MediaInput as ProductMediaInput
from inttegro.product.shipment_input import ShipmentInput as ProductShipmentInput
from inttegro.product.type import Type as ProductType
from inttegro.custom_data import CustomData
