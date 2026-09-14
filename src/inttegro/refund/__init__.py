"""Models, requests, and enums for the Inttegro refund resource.

The primary returned object is ``inttegro.refund.Refund``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .cancel_request import CancelRequest as CancelRequest
    from .create_line_item_input import CreateLineItemInput as CreateLineItemInput
    from .create_request import CreateRequest as CreateRequest
    from .failure import Failure as Failure
    from .failure_reason import FailureReason as FailureReason
    from .line_item import LineItem as LineItem
    from .lookup_request import LookupRequest as LookupRequest
    from .offline_settlement import OfflineSettlement as OfflineSettlement
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .payment_method_settlement import PaymentMethodSettlement as PaymentMethodSettlement
    from .reason import Reason as Reason
    from .reason_input import ReasonInput as ReasonInput
    from .reason_value import ReasonValue as ReasonValue
    from .refund import Refund as Refund
    from .request_meta_input import RequestMetaInput as RequestMetaInput
    from .response import Response as Response
    from .settlement import Settlement as Settlement
    from .settlement_bank_account import SettlementBankAccount as SettlementBankAccount
    from .settlement_bank_account_payment_method import SettlementBankAccountPaymentMethod as SettlementBankAccountPaymentMethod
    from .settlement_ghana_bank_account import SettlementGhanaBankAccount as SettlementGhanaBankAccount
    from .settlement_mobile_money import SettlementMobileMoney as SettlementMobileMoney
    from .settlement_mobile_money_payment_method import SettlementMobileMoneyPaymentMethod as SettlementMobileMoneyPaymentMethod
    from .settlement_payment_method import SettlementPaymentMethod as SettlementPaymentMethod
    from .status import Status as Status


_EXPORTS: dict[str, tuple[str, str]] = {
    "CancelRequest": ("inttegro.refund.cancel_request", "CancelRequest"),
    "CreateLineItemInput": ("inttegro.refund.create_line_item_input", "CreateLineItemInput"),
    "CreateRequest": ("inttegro.refund.create_request", "CreateRequest"),
    "Failure": ("inttegro.refund.failure", "Failure"),
    "FailureReason": ("inttegro.refund.failure_reason", "FailureReason"),
    "LineItem": ("inttegro.refund.line_item", "LineItem"),
    "LookupRequest": ("inttegro.refund.lookup_request", "LookupRequest"),
    "OfflineSettlement": ("inttegro.refund.offline_settlement", "OfflineSettlement"),
    "Page": ("inttegro.refund.page", "Page"),
    "PageRequest": ("inttegro.refund.page_request", "PageRequest"),
    "PageResponse": ("inttegro.refund.page_response", "PageResponse"),
    "PaymentMethodSettlement": ("inttegro.refund.payment_method_settlement", "PaymentMethodSettlement"),
    "Reason": ("inttegro.refund.reason", "Reason"),
    "ReasonInput": ("inttegro.refund.reason_input", "ReasonInput"),
    "ReasonValue": ("inttegro.refund.reason_value", "ReasonValue"),
    "Refund": ("inttegro.refund.refund", "Refund"),
    "RequestMetaInput": ("inttegro.refund.request_meta_input", "RequestMetaInput"),
    "Response": ("inttegro.refund.response", "Response"),
    "Settlement": ("inttegro.refund.settlement", "Settlement"),
    "SettlementBankAccount": ("inttegro.refund.settlement_bank_account", "SettlementBankAccount"),
    "SettlementBankAccountPaymentMethod": ("inttegro.refund.settlement_bank_account_payment_method", "SettlementBankAccountPaymentMethod"),
    "SettlementGhanaBankAccount": ("inttegro.refund.settlement_ghana_bank_account", "SettlementGhanaBankAccount"),
    "SettlementMobileMoney": ("inttegro.refund.settlement_mobile_money", "SettlementMobileMoney"),
    "SettlementMobileMoneyPaymentMethod": ("inttegro.refund.settlement_mobile_money_payment_method", "SettlementMobileMoneyPaymentMethod"),
    "SettlementPaymentMethod": ("inttegro.refund.settlement_payment_method", "SettlementPaymentMethod"),
    "Status": ("inttegro.refund.status", "Status"),
}

__all__ = [
    "CancelRequest",
    "CreateLineItemInput",
    "CreateRequest",
    "Failure",
    "FailureReason",
    "LineItem",
    "LookupRequest",
    "OfflineSettlement",
    "Page",
    "PageRequest",
    "PageResponse",
    "PaymentMethodSettlement",
    "Reason",
    "ReasonInput",
    "ReasonValue",
    "Refund",
    "RequestMetaInput",
    "Response",
    "Settlement",
    "SettlementBankAccount",
    "SettlementBankAccountPaymentMethod",
    "SettlementGhanaBankAccount",
    "SettlementMobileMoney",
    "SettlementMobileMoneyPaymentMethod",
    "SettlementPaymentMethod",
    "Status",
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
