"""UpdateRequest in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequest(ApiRequest):
    """Parameters accepted by the update request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdateOrderRequest``.
    """
    clear_payment_method: bool | UnsetType = field(default=UNSET)
    """Whether clear payment method. Optional. Python type: ``bool``; wire name: ``clear_payment_method``; JSON type: boolean"""
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    invoice_settings: InvoiceSettingsInput | UnsetType = field(default=UNSET)
    """Order-level invoice rendering data. Pages uses this data when rendering invoice web and download views. Optional. Python type: ``InvoiceSettingsInput``; wire name: ``invoice_settings``; JSON type: object (InvoiceSettings)"""
    finalize: bool | UnsetType = field(default=UNSET)
    """Whether to explicitly finalize the order. When true, the order is finalized regardless of payment state. When false or omitted, finalization follows default heuristics (finalize if payment is executable). Optional. Python type: ``bool``; wire name: ``finalize``; JSON type: boolean"""
    line_items: list[LineItemInput] | UnsetType = field(default=UNSET)
    """Items included in the order. Product line items may use inline product data, `product_id` with explicit `price`, or `product_id` with `price_id`. Optional. Python type: ``list[LineItemInput]``; wire name: ``line_items``; JSON type: array of object (LineItem) values. Constraints: minimum items 1"""
    number: str | UnsetType = field(default=UNSET)
    """Optional order number for reference. When omitted, Inttegro uses the generated order ID. Optional. Python type: ``str``; wire name: ``number``; JSON type: string"""
    receipt_number: str | UnsetType = field(default=UNSET)
    """Optional receipt number for downstream reconciliation. Uses the same length rules as `number`. Optional. Python type: ``str``; wire name: ``receipt_number``; JSON type: string"""
    payment_method_data: UpdateOrderRequestPaymentMethodData | UnsetType = field(default=UNSET)
    """New payment instrument details to use when executing payment for the order. Optional. Python type: ``UpdateOrderRequestPaymentMethodData``; wire name: ``payment_method_data``; JSON type: object (PaymentMethodData)"""
    payment_method_id: str | UnsetType = field(default=UNSET)
    """Identifier of the related payment method. Optional. Python type: ``str``; wire name: ``payment_method_id``; JSON type: string"""
    statement_descriptor: str | UnsetType = field(default=UNSET)
    """Optional statement descriptor shown on the customer's bank statement. Optional. Python type: ``str``; wire name: ``statement_descriptor``; JSON type: string. Constraints: maximum length 22"""
    statement_descriptor_prefix: str | UnsetType = field(default=UNSET)
    """Optional static prefix used to build the statement descriptor as `prefix*order_id`. Mutually exclusive with `statement_descriptor`. Optional. Python type: ``str``; wire name: ``statement_descriptor_prefix``; JSON type: string. Constraints: minimum length 2; maximum length 10"""
    order_id: str
    """Identifier of the related order. Required. Python type: ``str``; wire name: ``order_id``; JSON type: string"""

from inttegro.order.invoice_settings_input import InvoiceSettingsInput
from inttegro.shared.line_item_input import LineItemInput
from inttegro.order.update_request_payment_method_data import UpdateRequestPaymentMethodData as UpdateOrderRequestPaymentMethodData
from inttegro.custom_data import CustomData
