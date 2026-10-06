"""Models, requests, and enums for the Inttegro order resource.

The primary returned object is ``inttegro.order.Order``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .address import Address as Address
    from .cancel_request import CancelRequest as CancelRequest
    from .checkout_settings import CheckoutSettings as CheckoutSettings
    from .complete_envelope import CompleteEnvelope as CompleteEnvelope
    from .complete_request import CompleteRequest as CompleteRequest
    from .create_existing_customer_input import CreateExistingCustomerInput as CreateExistingCustomerInput
    from .create_existing_customer_input_checkout_settings import CreateExistingCustomerInputCheckoutSettings as CreateExistingCustomerInputCheckoutSettings
    from .create_existing_customer_input_request_meta import CreateExistingCustomerInputRequestMeta as CreateExistingCustomerInputRequestMeta
    from .create_new_customer_input import CreateNewCustomerInput as CreateNewCustomerInput
    from .create_new_customer_input_checkout_settings import CreateNewCustomerInputCheckoutSettings as CreateNewCustomerInputCheckoutSettings
    from .create_new_customer_input_request_meta import CreateNewCustomerInputRequestMeta as CreateNewCustomerInputRequestMeta
    from .create_request import CreateRequest as CreateRequest
    from .created_from import CreatedFrom as CreatedFrom
    from .created_from_resource_type import CreatedFromResourceType as CreatedFromResourceType
    from .customer import Customer as Customer
    from .delivery_channel import DeliveryChannel as DeliveryChannel
    from .discount_line_item import DiscountLineItem as DiscountLineItem
    from .discount_line_item_discount import DiscountLineItemDiscount as DiscountLineItemDiscount
    from .document_delivery import DocumentDelivery as DocumentDelivery
    from .document_delivery_attempt import DocumentDeliveryAttempt as DocumentDeliveryAttempt
    from .document_delivery_failure import DocumentDeliveryFailure as DocumentDeliveryFailure
    from .document_delivery_request import DocumentDeliveryRequest as DocumentDeliveryRequest
    from .document_delivery_result import DocumentDeliveryResult as DocumentDeliveryResult
    from .document_format import DocumentFormat as DocumentFormat
    from .document_kind import DocumentKind as DocumentKind
    from .envelope import Envelope as Envelope
    from .fee_line_item import FeeLineItem as FeeLineItem
    from .fee_line_item_fee import FeeLineItemFee as FeeLineItemFee
    from .finalize_envelope import FinalizeEnvelope as FinalizeEnvelope
    from .finalize_request import FinalizeRequest as FinalizeRequest
    from .invoice import Invoice as Invoice
    from .invoice_format import InvoiceFormat as InvoiceFormat
    from .invoice_settings import InvoiceSettings as InvoiceSettings
    from .invoice_settings_input import InvoiceSettingsInput as InvoiceSettingsInput
    from .line_item import LineItem as LineItem
    from .line_item_group import LineItemGroup as LineItemGroup
    from .line_item_type import LineItemType as LineItemType
    from .lookup_request import LookupRequest as LookupRequest
    from .order import Order as Order
    from .page import Page as Page
    from .page_envelope import PageEnvelope as PageEnvelope
    from .page_request import PageRequest as PageRequest
    from .pay_request import PayRequest as PayRequest
    from .payout_settings_request import PayoutSettingsRequest as PayoutSettingsRequest
    from .payout_settings_request_destination import PayoutSettingsRequestDestination as PayoutSettingsRequestDestination
    from .product_line_item import ProductLineItem as ProductLineItem
    from .product_line_item_product import ProductLineItemProduct as ProductLineItemProduct
    from .receipt import Receipt as Receipt
    from .receipt_format import ReceiptFormat as ReceiptFormat
    from .shipping_line_item import ShippingLineItem as ShippingLineItem
    from .shipping_line_item_shipping import ShippingLineItemShipping as ShippingLineItemShipping
    from .status import Status as Status
    from .update_request import UpdateRequest as UpdateRequest
    from .update_request_payment_method_data import UpdateRequestPaymentMethodData as UpdateRequestPaymentMethodData
    from .update_request_payment_method_data_mobile_money import UpdateRequestPaymentMethodDataMobileMoney as UpdateRequestPaymentMethodDataMobileMoney


_EXPORTS: dict[str, tuple[str, str]] = {
    "Address": ("inttegro.order.address", "Address"),
    "CancelRequest": ("inttegro.order.cancel_request", "CancelRequest"),
    "CheckoutSettings": ("inttegro.order.checkout_settings", "CheckoutSettings"),
    "CompleteEnvelope": ("inttegro.order.complete_envelope", "CompleteEnvelope"),
    "CompleteRequest": ("inttegro.order.complete_request", "CompleteRequest"),
    "CreateExistingCustomerInput": ("inttegro.order.create_existing_customer_input", "CreateExistingCustomerInput"),
    "CreateExistingCustomerInputCheckoutSettings": ("inttegro.order.create_existing_customer_input_checkout_settings", "CreateExistingCustomerInputCheckoutSettings"),
    "CreateExistingCustomerInputRequestMeta": ("inttegro.order.create_existing_customer_input_request_meta", "CreateExistingCustomerInputRequestMeta"),
    "CreateNewCustomerInput": ("inttegro.order.create_new_customer_input", "CreateNewCustomerInput"),
    "CreateNewCustomerInputCheckoutSettings": ("inttegro.order.create_new_customer_input_checkout_settings", "CreateNewCustomerInputCheckoutSettings"),
    "CreateNewCustomerInputRequestMeta": ("inttegro.order.create_new_customer_input_request_meta", "CreateNewCustomerInputRequestMeta"),
    "CreateRequest": ("inttegro.order.create_request", "CreateRequest"),
    "CreatedFrom": ("inttegro.order.created_from", "CreatedFrom"),
    "CreatedFromResourceType": ("inttegro.order.created_from_resource_type", "CreatedFromResourceType"),
    "Customer": ("inttegro.order.customer", "Customer"),
    "DeliveryChannel": ("inttegro.order.delivery_channel", "DeliveryChannel"),
    "DiscountLineItem": ("inttegro.order.discount_line_item", "DiscountLineItem"),
    "DiscountLineItemDiscount": ("inttegro.order.discount_line_item_discount", "DiscountLineItemDiscount"),
    "DocumentDelivery": ("inttegro.order.document_delivery", "DocumentDelivery"),
    "DocumentDeliveryAttempt": ("inttegro.order.document_delivery_attempt", "DocumentDeliveryAttempt"),
    "DocumentDeliveryFailure": ("inttegro.order.document_delivery_failure", "DocumentDeliveryFailure"),
    "DocumentDeliveryRequest": ("inttegro.order.document_delivery_request", "DocumentDeliveryRequest"),
    "DocumentDeliveryResult": ("inttegro.order.document_delivery_result", "DocumentDeliveryResult"),
    "DocumentFormat": ("inttegro.order.document_format", "DocumentFormat"),
    "DocumentKind": ("inttegro.order.document_kind", "DocumentKind"),
    "Envelope": ("inttegro.order.envelope", "Envelope"),
    "FeeLineItem": ("inttegro.order.fee_line_item", "FeeLineItem"),
    "FeeLineItemFee": ("inttegro.order.fee_line_item_fee", "FeeLineItemFee"),
    "FinalizeEnvelope": ("inttegro.order.finalize_envelope", "FinalizeEnvelope"),
    "FinalizeRequest": ("inttegro.order.finalize_request", "FinalizeRequest"),
    "Invoice": ("inttegro.order.invoice", "Invoice"),
    "InvoiceFormat": ("inttegro.order.invoice_format", "InvoiceFormat"),
    "InvoiceSettings": ("inttegro.order.invoice_settings", "InvoiceSettings"),
    "InvoiceSettingsInput": ("inttegro.order.invoice_settings_input", "InvoiceSettingsInput"),
    "LineItem": ("inttegro.order.line_item", "LineItem"),
    "LineItemGroup": ("inttegro.order.line_item_group", "LineItemGroup"),
    "LineItemType": ("inttegro.order.line_item_type", "LineItemType"),
    "LookupRequest": ("inttegro.order.lookup_request", "LookupRequest"),
    "Order": ("inttegro.order.order", "Order"),
    "Page": ("inttegro.order.page", "Page"),
    "PageEnvelope": ("inttegro.order.page_envelope", "PageEnvelope"),
    "PageRequest": ("inttegro.order.page_request", "PageRequest"),
    "PayRequest": ("inttegro.order.pay_request", "PayRequest"),
    "PayoutSettingsRequest": ("inttegro.order.payout_settings_request", "PayoutSettingsRequest"),
    "PayoutSettingsRequestDestination": ("inttegro.order.payout_settings_request_destination", "PayoutSettingsRequestDestination"),
    "ProductLineItem": ("inttegro.order.product_line_item", "ProductLineItem"),
    "ProductLineItemProduct": ("inttegro.order.product_line_item_product", "ProductLineItemProduct"),
    "Receipt": ("inttegro.order.receipt", "Receipt"),
    "ReceiptFormat": ("inttegro.order.receipt_format", "ReceiptFormat"),
    "ShippingLineItem": ("inttegro.order.shipping_line_item", "ShippingLineItem"),
    "ShippingLineItemShipping": ("inttegro.order.shipping_line_item_shipping", "ShippingLineItemShipping"),
    "Status": ("inttegro.order.status", "Status"),
    "UpdateRequest": ("inttegro.order.update_request", "UpdateRequest"),
    "UpdateRequestPaymentMethodData": ("inttegro.order.update_request_payment_method_data", "UpdateRequestPaymentMethodData"),
    "UpdateRequestPaymentMethodDataMobileMoney": ("inttegro.order.update_request_payment_method_data_mobile_money", "UpdateRequestPaymentMethodDataMobileMoney"),
}

__all__ = [
    "Address",
    "CancelRequest",
    "CheckoutSettings",
    "CompleteEnvelope",
    "CompleteRequest",
    "CreateExistingCustomerInput",
    "CreateExistingCustomerInputCheckoutSettings",
    "CreateExistingCustomerInputRequestMeta",
    "CreateNewCustomerInput",
    "CreateNewCustomerInputCheckoutSettings",
    "CreateNewCustomerInputRequestMeta",
    "CreateRequest",
    "CreatedFrom",
    "CreatedFromResourceType",
    "Customer",
    "DeliveryChannel",
    "DiscountLineItem",
    "DiscountLineItemDiscount",
    "DocumentDelivery",
    "DocumentDeliveryAttempt",
    "DocumentDeliveryFailure",
    "DocumentDeliveryRequest",
    "DocumentDeliveryResult",
    "DocumentFormat",
    "DocumentKind",
    "Envelope",
    "FeeLineItem",
    "FeeLineItemFee",
    "FinalizeEnvelope",
    "FinalizeRequest",
    "Invoice",
    "InvoiceFormat",
    "InvoiceSettings",
    "InvoiceSettingsInput",
    "LineItem",
    "LineItemGroup",
    "LineItemType",
    "LookupRequest",
    "Order",
    "Page",
    "PageEnvelope",
    "PageRequest",
    "PayRequest",
    "PayoutSettingsRequest",
    "PayoutSettingsRequestDestination",
    "ProductLineItem",
    "ProductLineItemProduct",
    "Receipt",
    "ReceiptFormat",
    "ShippingLineItem",
    "ShippingLineItemShipping",
    "Status",
    "UpdateRequest",
    "UpdateRequestPaymentMethodData",
    "UpdateRequestPaymentMethodDataMobileMoney",
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
