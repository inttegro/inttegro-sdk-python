"""CreateNewCustomerInput in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateNewCustomerInput(ApiRequest):
    """Parameters accepted by the create new customer input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreateOrderNewCustomerInput``.
    """
    number: str | UnsetType = field(default=UNSET)
    """Optional order number for reference. When omitted, Inttegro uses the generated order ID. Optional. Python type: ``str``; wire name: ``number``; JSON type: string"""
    receipt_number: str | UnsetType = field(default=UNSET)
    """Optional receipt number for downstream reconciliation. Uses the same length rules as `number`. Optional. Python type: ``str``; wire name: ``receipt_number``; JSON type: string"""
    statement_descriptor: str | UnsetType = field(default=UNSET)
    """Optional statement descriptor shown on the customer's bank statement. Optional. Python type: ``str``; wire name: ``statement_descriptor``; JSON type: string. Constraints: maximum length 22"""
    statement_descriptor_prefix: str | UnsetType = field(default=UNSET)
    """Optional static prefix used to build the statement descriptor as `prefix*order_id`. Mutually exclusive with `statement_descriptor`. Optional. Python type: ``str``; wire name: ``statement_descriptor_prefix``; JSON type: string. Constraints: minimum length 2; maximum length 10"""
    execute_payment: bool | UnsetType = field(default=UNSET)
    """Whether to execute payment immediately after order creation. Optional. Python type: ``bool``; wire name: ``execute_payment``; JSON type: boolean"""
    finalize: bool | UnsetType = field(default=UNSET)
    """Whether to explicitly finalize the order. When true, the order is finalized regardless of payment state. When false or omitted, finalization follows default heuristics (finalize if payment is executable). Optional. Python type: ``bool``; wire name: ``finalize``; JSON type: boolean"""
    request_meta: CreateOrderNewCustomerInputRequestMeta | UnsetType = field(default=UNSET)
    """Optional metadata controlling request processing. Optional. Python type: ``CreateOrderNewCustomerInputRequestMeta``; wire name: ``request_meta``; JSON type: object"""
    checkout_settings: CreateOrderNewCustomerInputCheckoutSettings | UnsetType = field(default=UNSET)
    """Checkout and payment flow configuration. Strongly recommended to provide both redirect_url and cancel_url for a delightful customer experience. Optional. Python type: ``CreateOrderNewCustomerInputCheckoutSettings``; wire name: ``checkout_settings``; JSON type: object"""
    invoice_settings: InvoiceSettingsInput | UnsetType = field(default=UNSET)
    """Order-level invoice rendering data. Pages uses this data when rendering invoice web and download views. Optional. Python type: ``InvoiceSettingsInput``; wire name: ``invoice_settings``; JSON type: object (InvoiceSettings)"""
    payout_settings: OrderPayoutSettingsRequest | UnsetType = field(default=UNSET)
    """The payout settings associated with this create new customer input. Optional. Python type: ``OrderPayoutSettingsRequest``; wire name: ``payout_settings``; JSON type: object (OrderPayoutSettingsRequest)"""
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    billing_details: BillingDetailsInput | UnsetType = field(default=UNSET)
    """The billing details associated with this create new customer input. Optional. Python type: ``BillingDetailsInput``; wire name: ``billing_details``; JSON type: object (BillingDetails)"""
    shipping: ShippingInput | UnsetType = field(default=UNSET)
    """The shipping associated with this create new customer input. Optional. Python type: ``ShippingInput``; wire name: ``shipping``; JSON type: object (Shipping)"""
    payment_method_data: PaymentMethodDataInput | UnsetType = field(default=UNSET)
    """New payment instrument details to use when executing payment for the order. Optional. Python type: ``PaymentMethodDataInput``; wire name: ``payment_method_data``; JSON type: object (PaymentMethodData)"""
    customer_data: CustomerDataInput
    """The customer data associated with this create new customer input. Required. Python type: ``CustomerDataInput``; wire name: ``customer_data``; JSON type: object (CustomerData)"""
    line_items: list[LineItemInput]
    """Items included in the order. Product line items may use inline product data, `product_id` with explicit `price`, or `product_id` with `price_id`. Required. Python type: ``list[LineItemInput]``; wire name: ``line_items``; JSON type: array of object (LineItem) values. Constraints: minimum items 1"""

from inttegro.shared.billing_details_input import BillingDetailsInput
from inttegro.order.create_new_customer_input_checkout_settings import CreateNewCustomerInputCheckoutSettings as CreateOrderNewCustomerInputCheckoutSettings
from inttegro.order.create_new_customer_input_request_meta import CreateNewCustomerInputRequestMeta as CreateOrderNewCustomerInputRequestMeta
from inttegro.customer.data_input import DataInput as CustomerDataInput
from inttegro.order.invoice_settings_input import InvoiceSettingsInput
from inttegro.shared.line_item_input import LineItemInput
from inttegro.order.payout_settings_request import PayoutSettingsRequest as OrderPayoutSettingsRequest
from inttegro.payment_method.data_input import DataInput as PaymentMethodDataInput
from inttegro.shared.shipping_input import ShippingInput
from inttegro.custom_data import CustomData
