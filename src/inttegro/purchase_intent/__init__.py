"""Models, requests, and enums for the Inttegro purchase intent resource.

The primary returned object is ``inttegro.purchase_intent.PurchaseIntent``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .cancel_request import CancelRequest as CancelRequest
    from .create_request import CreateRequest as CreateRequest
    from .create_request_price import CreateRequestPrice as CreateRequestPrice
    from .create_request_price_original import CreateRequestPriceOriginal as CreateRequestPriceOriginal
    from .create_request_product import CreateRequestProduct as CreateRequestProduct
    from .create_request_quantity import CreateRequestQuantity as CreateRequestQuantity
    from .create_request_usage import CreateRequestUsage as CreateRequestUsage
    from .lookup_request import LookupRequest as LookupRequest
    from .merchant import Merchant as Merchant
    from .original_price import OriginalPrice as OriginalPrice
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .price import Price as Price
    from .product import Product as Product
    from .product_attributes_item import ProductAttributesItem as ProductAttributesItem
    from .purchase_intent import PurchaseIntent as PurchaseIntent
    from .quantity import Quantity as Quantity
    from .response import Response as Response
    from .status import Status as Status
    from .update_request import UpdateRequest as UpdateRequest
    from .update_request_quantity import UpdateRequestQuantity as UpdateRequestQuantity
    from .usage import Usage as Usage
    from .usage_order import UsageOrder as UsageOrder
    from .variant import Variant as Variant
    from .variant_axis import VariantAxis as VariantAxis
    from .variant_set import VariantSet as VariantSet


_EXPORTS: dict[str, tuple[str, str]] = {
    "CancelRequest": ("inttegro.purchase_intent.cancel_request", "CancelRequest"),
    "CreateRequest": ("inttegro.purchase_intent.create_request", "CreateRequest"),
    "CreateRequestPrice": ("inttegro.purchase_intent.create_request_price", "CreateRequestPrice"),
    "CreateRequestPriceOriginal": ("inttegro.purchase_intent.create_request_price_original", "CreateRequestPriceOriginal"),
    "CreateRequestProduct": ("inttegro.purchase_intent.create_request_product", "CreateRequestProduct"),
    "CreateRequestQuantity": ("inttegro.purchase_intent.create_request_quantity", "CreateRequestQuantity"),
    "CreateRequestUsage": ("inttegro.purchase_intent.create_request_usage", "CreateRequestUsage"),
    "LookupRequest": ("inttegro.purchase_intent.lookup_request", "LookupRequest"),
    "Merchant": ("inttegro.purchase_intent.merchant", "Merchant"),
    "OriginalPrice": ("inttegro.purchase_intent.original_price", "OriginalPrice"),
    "Page": ("inttegro.purchase_intent.page", "Page"),
    "PageRequest": ("inttegro.purchase_intent.page_request", "PageRequest"),
    "PageResponse": ("inttegro.purchase_intent.page_response", "PageResponse"),
    "Price": ("inttegro.purchase_intent.price", "Price"),
    "Product": ("inttegro.purchase_intent.product", "Product"),
    "ProductAttributesItem": ("inttegro.purchase_intent.product_attributes_item", "ProductAttributesItem"),
    "PurchaseIntent": ("inttegro.purchase_intent.purchase_intent", "PurchaseIntent"),
    "Quantity": ("inttegro.purchase_intent.quantity", "Quantity"),
    "Response": ("inttegro.purchase_intent.response", "Response"),
    "Status": ("inttegro.purchase_intent.status", "Status"),
    "UpdateRequest": ("inttegro.purchase_intent.update_request", "UpdateRequest"),
    "UpdateRequestQuantity": ("inttegro.purchase_intent.update_request_quantity", "UpdateRequestQuantity"),
    "Usage": ("inttegro.purchase_intent.usage", "Usage"),
    "UsageOrder": ("inttegro.purchase_intent.usage_order", "UsageOrder"),
    "Variant": ("inttegro.purchase_intent.variant", "Variant"),
    "VariantAxis": ("inttegro.purchase_intent.variant_axis", "VariantAxis"),
    "VariantSet": ("inttegro.purchase_intent.variant_set", "VariantSet"),
}

__all__ = [
    "CancelRequest",
    "CreateRequest",
    "CreateRequestPrice",
    "CreateRequestPriceOriginal",
    "CreateRequestProduct",
    "CreateRequestQuantity",
    "CreateRequestUsage",
    "LookupRequest",
    "Merchant",
    "OriginalPrice",
    "Page",
    "PageRequest",
    "PageResponse",
    "Price",
    "Product",
    "ProductAttributesItem",
    "PurchaseIntent",
    "Quantity",
    "Response",
    "Status",
    "UpdateRequest",
    "UpdateRequestQuantity",
    "Usage",
    "UsageOrder",
    "Variant",
    "VariantAxis",
    "VariantSet",
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
