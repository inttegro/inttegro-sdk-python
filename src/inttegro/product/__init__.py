"""Models, requests, and enums for the Inttegro product resource.

The primary returned object is ``inttegro.product.Product``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .action_request import ActionRequest as ActionRequest
    from .add_price_request import AddPriceRequest as AddPriceRequest
    from .add_price_response import AddPriceResponse as AddPriceResponse
    from .attribute import Attribute as Attribute
    from .attribute_input import AttributeInput as AttributeInput
    from .catalog_with_price_data_input import CatalogWithPriceDataInput as CatalogWithPriceDataInput
    from .catalog_with_price_reference_input import CatalogWithPriceReferenceInput as CatalogWithPriceReferenceInput
    from .catalog_with_customer_selected_price_input import CatalogWithCustomerSelectedPriceInput as CatalogWithCustomerSelectedPriceInput
    from .customer_selected_price_input import CustomerSelectedPriceInput as CustomerSelectedPriceInput
    from .create_request import CreateRequest as CreateRequest
    from .delivery import Delivery as Delivery
    from .details_input import DetailsInput as DetailsInput
    from .dimensions import Dimensions as Dimensions
    from .dimensions_custom import DimensionsCustom as DimensionsCustom
    from .dimensions_digital import DimensionsDigital as DimensionsDigital
    from .dimensions_input import DimensionsInput as DimensionsInput
    from .dimensions_input_custom import DimensionsInputCustom as DimensionsInputCustom
    from .dimensions_input_digital import DimensionsInputDigital as DimensionsInputDigital
    from .dimensions_input_physical import DimensionsInputPhysical as DimensionsInputPhysical
    from .dimensions_physical import DimensionsPhysical as DimensionsPhysical
    from .download import Download as Download
    from .inline_details_input import InlineDetailsInput as InlineDetailsInput
    from .line_item_input import LineItemInput as LineItemInput
    from .lookup_request import LookupRequest as LookupRequest
    from .media import Media as Media
    from .media_input import MediaInput as MediaInput
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .price_summary import PriceSummary as PriceSummary
    from .product import Product as Product
    from .render import Render as Render
    from .response import Response as Response
    from .service import Service as Service
    from .shipment import Shipment as Shipment
    from .shipment_input import ShipmentInput as ShipmentInput
    from .shipment_input_type import ShipmentInputType as ShipmentInputType
    from .shipment_type import ShipmentType as ShipmentType
    from .stream import Stream as Stream
    from .type import Type as Type
    from .update_request import UpdateRequest as UpdateRequest
    from .update_response import UpdateResponse as UpdateResponse
    from .updated import Updated as Updated


_EXPORTS: dict[str, tuple[str, str]] = {
    "ActionRequest": ("inttegro.product.action_request", "ActionRequest"),
    "AddPriceRequest": ("inttegro.product.add_price_request", "AddPriceRequest"),
    "AddPriceResponse": ("inttegro.product.add_price_response", "AddPriceResponse"),
    "Attribute": ("inttegro.product.attribute", "Attribute"),
    "AttributeInput": ("inttegro.product.attribute_input", "AttributeInput"),
    "CatalogWithPriceDataInput": ("inttegro.product.catalog_with_price_data_input", "CatalogWithPriceDataInput"),
    "CatalogWithPriceReferenceInput": ("inttegro.product.catalog_with_price_reference_input", "CatalogWithPriceReferenceInput"),
    "CatalogWithCustomerSelectedPriceInput": ("inttegro.product.catalog_with_customer_selected_price_input", "CatalogWithCustomerSelectedPriceInput"),
    "CustomerSelectedPriceInput": ("inttegro.product.customer_selected_price_input", "CustomerSelectedPriceInput"),
    "CreateRequest": ("inttegro.product.create_request", "CreateRequest"),
    "Delivery": ("inttegro.product.delivery", "Delivery"),
    "DetailsInput": ("inttegro.product.details_input", "DetailsInput"),
    "Dimensions": ("inttegro.product.dimensions", "Dimensions"),
    "DimensionsCustom": ("inttegro.product.dimensions_custom", "DimensionsCustom"),
    "DimensionsDigital": ("inttegro.product.dimensions_digital", "DimensionsDigital"),
    "DimensionsInput": ("inttegro.product.dimensions_input", "DimensionsInput"),
    "DimensionsInputCustom": ("inttegro.product.dimensions_input_custom", "DimensionsInputCustom"),
    "DimensionsInputDigital": ("inttegro.product.dimensions_input_digital", "DimensionsInputDigital"),
    "DimensionsInputPhysical": ("inttegro.product.dimensions_input_physical", "DimensionsInputPhysical"),
    "DimensionsPhysical": ("inttegro.product.dimensions_physical", "DimensionsPhysical"),
    "Download": ("inttegro.product.download", "Download"),
    "InlineDetailsInput": ("inttegro.product.inline_details_input", "InlineDetailsInput"),
    "LineItemInput": ("inttegro.product.line_item_input", "LineItemInput"),
    "LookupRequest": ("inttegro.product.lookup_request", "LookupRequest"),
    "Media": ("inttegro.product.media", "Media"),
    "MediaInput": ("inttegro.product.media_input", "MediaInput"),
    "Page": ("inttegro.product.page", "Page"),
    "PageRequest": ("inttegro.product.page_request", "PageRequest"),
    "PageResponse": ("inttegro.product.page_response", "PageResponse"),
    "PriceSummary": ("inttegro.product.price_summary", "PriceSummary"),
    "Product": ("inttegro.product.product", "Product"),
    "Render": ("inttegro.product.render", "Render"),
    "Response": ("inttegro.product.response", "Response"),
    "Service": ("inttegro.product.service", "Service"),
    "Shipment": ("inttegro.product.shipment", "Shipment"),
    "ShipmentInput": ("inttegro.product.shipment_input", "ShipmentInput"),
    "ShipmentInputType": ("inttegro.product.shipment_input_type", "ShipmentInputType"),
    "ShipmentType": ("inttegro.product.shipment_type", "ShipmentType"),
    "Stream": ("inttegro.product.stream", "Stream"),
    "Type": ("inttegro.product.type", "Type"),
    "UpdateRequest": ("inttegro.product.update_request", "UpdateRequest"),
    "UpdateResponse": ("inttegro.product.update_response", "UpdateResponse"),
    "Updated": ("inttegro.product.updated", "Updated"),
}

__all__ = [
    "ActionRequest",
    "AddPriceRequest",
    "AddPriceResponse",
    "Attribute",
    "AttributeInput",
    "CatalogWithPriceDataInput",
    "CatalogWithPriceReferenceInput",
    "CatalogWithCustomerSelectedPriceInput",
    "CustomerSelectedPriceInput",
    "CreateRequest",
    "Delivery",
    "DetailsInput",
    "Dimensions",
    "DimensionsCustom",
    "DimensionsDigital",
    "DimensionsInput",
    "DimensionsInputCustom",
    "DimensionsInputDigital",
    "DimensionsInputPhysical",
    "DimensionsPhysical",
    "Download",
    "InlineDetailsInput",
    "LineItemInput",
    "LookupRequest",
    "Media",
    "MediaInput",
    "Page",
    "PageRequest",
    "PageResponse",
    "PriceSummary",
    "Product",
    "Render",
    "Response",
    "Service",
    "Shipment",
    "ShipmentInput",
    "ShipmentInputType",
    "ShipmentType",
    "Stream",
    "Type",
    "UpdateRequest",
    "UpdateResponse",
    "Updated",
]


def __getattr__(name: str) -> Any:
    """Load a public resource type on first access."""
    try:
        module_name, attribute_name = _EXPORTS[name]
    except KeyError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from None
    value = getattr(import_module(module_name), attribute_name)
    globals()[name] = value
    return value
