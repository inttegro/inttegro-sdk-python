"""Endpoint-to-domain-model registry used to hide HTTP response envelopes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from inttegro.app.app import App as Application
from inttegro.balance.balance import Balance as BalanceSnapshot
from inttegro.balance_transaction.balance_transaction import BalanceTransaction
from inttegro.balance_transaction.page import Page as BalanceTransactionPage
from inttegro.broadcast.creation_detail import CreationDetail as BroadcastCreationDetail
from inttegro.broadcast.broadcast import Broadcast as BroadcastDetail
from inttegro.price.price import Price as CatalogPrice
from inttegro.chime.chime import Chime
from inttegro.chime.page import Page as ChimePage
from inttegro.shared.country_specification import CountrySpecification
from inttegro.customer.customer import Customer
from inttegro.customer.page import Page as CustomerPage
from inttegro.file.file import File
from inttegro.file_link.file_link import FileLink
from inttegro.file_link.creation import Creation as FileLinkCreation
from inttegro.file_link.page import Page as FileLinkPage
from inttegro.file.page import Page as FilePage
from inttegro.file_reference.reconciliation import Reconciliation as FileReferenceReconciliation
from inttegro.financial_account.financial_account import FinancialAccount
from inttegro.financial_account.page import Page as FinancialAccountPage
from inttegro.secret_key.generated import Generated as GeneratedSecretKey
from inttegro.message_template.message_template import MessageTemplate
from inttegro.message_template.preview import Preview as MessageTemplatePreview
from inttegro.message_template.page import Page as MessageTemplatesPage
from inttegro.otp.transaction import Transaction as OTPTransaction
from inttegro.otp.verification import Verification as OTPVerification
from inttegro.order.order import Order
from inttegro.order.document_delivery_result import DocumentDeliveryResult as OrderDocumentDeliveryResult
from inttegro.order.page import Page as OrderPage
from inttegro.payment_method.payment_method import PaymentMethod
from inttegro.payment_method.deletion import Deletion as PaymentMethodDeletion
from inttegro.payment_method.page import Page as PaymentMethodPage
from inttegro.payment_method.settings import Settings as PaymentMethodSettings
from inttegro.payment_method.verification_session import VerificationSession as PaymentMethodVerificationSession
from inttegro.payout.payout import Payout
from inttegro.payout.page import Page as PayoutPage
from inttegro.payout.settings_lookup import SettingsLookup as PayoutSettingsLookup
from inttegro.payout.settings_mutation import SettingsMutation as PayoutSettingsMutation
from inttegro.price.page import Page as PricePage
from inttegro.product.product import Product
from inttegro.product.page import Page as ProductPage
from inttegro.purchase_intent.purchase_intent import PurchaseIntent
from inttegro.purchase_intent.page import Page as PurchaseIntentPage
from inttegro.refund.refund import Refund
from inttegro.refund.page import Page as RefundPage
from inttegro.schedule.cancel_detail import CancelDetail as ScheduleCancelDetail
from inttegro.schedule.creation_detail import CreationDetail as ScheduleCreationDetail
from inttegro.schedule.schedule import Schedule as ScheduleDetail
from inttegro.search import Page as ResourceSearchPage
from inttegro.secret_key.secret_key import SecretKey
from inttegro.secret_key.page import Page as SecretKeyPage
from inttegro.secret_key.usage import Usage as SecretKeyUsage
from inttegro.shared.upload_fulfillment import UploadFulfillment
from inttegro.upload_request.upload_request import UploadRequest
from inttegro.upload_request.page import Page as UploadRequestPage


@dataclass(frozen=True, slots=True)
class ResponseShape:
    model: Any
    field: str | None = None


def _resource(model: Any, field: str) -> ResponseShape:
    return ResponseShape(model=model, field=field)


RESPONSE_TYPES_BY_PATH: dict[str, ResponseShape] = {
    '/apps/create': _resource(Application, 'app'), '/apps/lookup': _resource(Application, 'app'), '/apps/update': _resource(Application, 'app'),
    '/balance_transactions/lookup': _resource(BalanceTransaction, 'transaction'), '/balance_transactions/page': _resource(BalanceTransactionPage, 'page'), '/balances': _resource(BalanceSnapshot, 'balances'),
    '/broadcasts/cancel': _resource(BroadcastDetail, 'broadcast'), '/broadcasts/lookup': _resource(BroadcastDetail, 'broadcast'),
    '/chimes/broadcast': _resource(BroadcastCreationDetail, 'broadcast'), '/chimes/lookup': _resource(Chime, 'chime'), '/chimes/page': _resource(ChimePage, 'page'), '/chimes/schedule': _resource(ScheduleCreationDetail, 'scheduled_chime'), '/chimes/send': _resource(Chime, 'chime'),
    '/customers/create': _resource(Customer, 'customer'), '/customers/lookup': _resource(Customer, 'customer'), '/customers/page': _resource(CustomerPage, 'page'), '/customers/update': _resource(Customer, 'customer'),
    '/customers/search': _resource(ResourceSearchPage, 'search'),
    '/file_links/create': ResponseShape(FileLinkCreation), '/file_links/lookup': _resource(FileLink, 'file_link'), '/file_links/page': _resource(FileLinkPage, 'page'), '/file_links/revoke': _resource(FileLink, 'file_link'),
    '/file_references/reconcile': ResponseShape(FileReferenceReconciliation), '/files/create': _resource(File, 'file'), '/files/delete': _resource(File, 'file'), '/files/lookup': _resource(File, 'file'), '/files/page': _resource(FilePage, 'page'),
    '/financial_accounts/archive': _resource(FinancialAccount, 'account'), '/financial_accounts/connect': _resource(FinancialAccount, 'account'), '/financial_accounts/create': _resource(FinancialAccount, 'account'),
    '/financial_accounts/disable_pull': _resource(FinancialAccount, 'account'), '/financial_accounts/disable_push': _resource(FinancialAccount, 'account'), '/financial_accounts/disconnect': _resource(FinancialAccount, 'account'),
    '/financial_accounts/enable_pull': _resource(FinancialAccount, 'account'), '/financial_accounts/enable_push': _resource(FinancialAccount, 'account'), '/financial_accounts/lookup': _resource(FinancialAccount, 'account'),
    '/financial_accounts/page': _resource(FinancialAccountPage, 'page'), '/financial_accounts/reconnect': _resource(FinancialAccount, 'account'), '/financial_accounts/update': _resource(FinancialAccount, 'account'), '/financial_accounts/verify': _resource(FinancialAccount, 'account'),
    '/financial_accounts/search': _resource(ResourceSearchPage, 'search'),
    '/keys/destroy': _resource(SecretKey, 'key'), '/keys/generate': _resource(GeneratedSecretKey, 'key'), '/keys/lookup': _resource(SecretKey, 'key'), '/keys/page': _resource(SecretKeyPage, 'page'), '/keys/update': _resource(SecretKey, 'key'), '/keys/usage': ResponseShape(SecretKeyUsage),
    '/message_templates/archive': _resource(MessageTemplate, 'message_template'), '/message_templates/create': _resource(MessageTemplate, 'message_template'), '/message_templates/lookup': _resource(MessageTemplate, 'message_template'),
    '/message_templates/page': _resource(MessageTemplatesPage, 'page'), '/message_templates/publish': _resource(MessageTemplate, 'message_template'), '/message_templates/render_preview': ResponseShape(MessageTemplatePreview), '/message_templates/update': _resource(MessageTemplate, 'message_template'),
    '/orders/cancel': _resource(Order, 'order'), '/orders/complete': _resource(Order, 'order'), '/orders/confirm_payment': _resource(Order, 'order'), '/orders/create': _resource(Order, 'order'), '/orders/finalize': _resource(Order, 'order'),
    '/orders/lookup': _resource(Order, 'order'), '/orders/page': _resource(OrderPage, 'page'), '/orders/pay': _resource(Order, 'order'),
    '/orders/search': _resource(ResourceSearchPage, 'search'),
    '/orders/request_confirmation': _resource(Order, 'order'), '/orders/send_invoice': ResponseShape(OrderDocumentDeliveryResult), '/orders/send_receipt': ResponseShape(OrderDocumentDeliveryResult), '/orders/update': _resource(Order, 'order'),
    '/otp/cancel': _resource(OTPTransaction, 'transaction'), '/otp/initiate': _resource(OTPTransaction, 'transaction'), '/otp/lookup': _resource(OTPTransaction, 'transaction'), '/otp/verify': ResponseShape(OTPVerification),
    '/payment_methods/activate': _resource(PaymentMethod, 'payment_method'), '/payment_methods/archive': _resource(PaymentMethod, 'payment_method'), '/payment_methods/confirm_verification': _resource(PaymentMethod, 'payment_method'),
    '/payment_methods/delete': ResponseShape(PaymentMethodDeletion), '/payment_methods/disactivate': _resource(PaymentMethod, 'payment_method'), '/payment_methods/lookup': _resource(PaymentMethod, 'payment_method'),
    '/payment_methods/page': _resource(PaymentMethodPage, 'page'), '/payment_methods/settings': _resource(PaymentMethodSettings, 'settings'), '/payment_methods/tokenize': _resource(PaymentMethod, 'payment_method'),
    '/payment_methods/unarchive': _resource(PaymentMethod, 'payment_method'), '/payment_methods/update': _resource(PaymentMethod, 'payment_method'), '/payment_methods/verify': _resource(PaymentMethodVerificationSession, 'verification'),
    '/payouts/cancel': _resource(Payout, 'payout'), '/payouts/disable': _resource(PayoutSettingsMutation, 'settings'), '/payouts/disable_fx': _resource(PayoutSettingsMutation, 'settings'),
    '/payouts/enable': _resource(PayoutSettingsMutation, 'settings'), '/payouts/enable_fx': _resource(PayoutSettingsMutation, 'settings'), '/payouts/lookup': _resource(Payout, 'payout'), '/payouts/page': _resource(PayoutPage, 'page'),
    '/payouts/search': _resource(ResourceSearchPage, 'search'),
    '/payouts/schedule': _resource(Payout, 'payout'), '/payouts/set_destinations': _resource(PayoutSettingsMutation, 'settings'), '/payouts/settings': _resource(PayoutSettingsLookup, 'settings'),
    '/prices/activate': _resource(CatalogPrice, 'price'), '/prices/archive': _resource(CatalogPrice, 'price'), '/prices/create': _resource(CatalogPrice, 'price'), '/prices/deactivate': _resource(CatalogPrice, 'price'), '/prices/lookup': _resource(CatalogPrice, 'price'), '/prices/page': _resource(PricePage, 'page'), '/prices/update': _resource(CatalogPrice, 'price'),
    '/products/add_price': _resource(CatalogPrice, 'price'), '/products/archive': _resource(Product, 'product'), '/products/create': _resource(Product, 'product'), '/products/lookup': _resource(Product, 'product'),
    '/products/page': _resource(ProductPage, 'page'), '/products/publish': _resource(Product, 'product'), '/products/set_default_unit_price': _resource(Product, 'product'), '/products/unpublish': _resource(Product, 'product'), '/products/update': _resource(Product, 'product'),
    '/products/search': _resource(ResourceSearchPage, 'search'),
    '/purchase_intents/cancel': _resource(PurchaseIntent, 'purchase_intent'), '/purchase_intents/create': _resource(PurchaseIntent, 'purchase_intent'), '/purchase_intents/lookup': _resource(PurchaseIntent, 'purchase_intent'), '/purchase_intents/page': _resource(PurchaseIntentPage, 'page'), '/purchase_intents/update': _resource(PurchaseIntent, 'purchase_intent'),
    '/refunds/cancel': _resource(Refund, 'refund'), '/refunds/create': _resource(Refund, 'refund'), '/refunds/lookup': _resource(Refund, 'refund'), '/refunds/page': _resource(RefundPage, 'page'),
    '/schedules/cancel': _resource(ScheduleCancelDetail, 'scheduled_chime'), '/schedules/lookup': _resource(ScheduleDetail, 'scheduled_chime'), '/spec/countries': _resource(dict[str, CountrySpecification], 'countries'),
    '/upload_requests/cancel': _resource(UploadRequest, 'upload_request'), '/upload_requests/create': _resource(UploadRequest, 'upload_request'), '/upload_requests/lookup': _resource(UploadRequest, 'upload_request'),
    '/upload_requests/page': _resource(UploadRequestPage, 'page'), '/upload_requests/review': _resource(UploadRequest, 'upload_request'), '/upload_requests/upload': ResponseShape(UploadFulfillment),
}


def response_type_for_path(path: str) -> ResponseShape | None:
    return RESPONSE_TYPES_BY_PATH.get(path)
