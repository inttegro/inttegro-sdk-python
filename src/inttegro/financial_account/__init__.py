"""Models, requests, and enums for the Inttegro financial account resource.

The primary returned object is ``inttegro.financial_account.FinancialAccount``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .bank_request import BankRequest as BankRequest
    from .bank_request_pull_configuration import BankRequestPullConfiguration as BankRequestPullConfiguration
    from .bank_request_push_configuration import BankRequestPushConfiguration as BankRequestPushConfiguration
    from .compact_response import CompactResponse as CompactResponse
    from .connect_response import ConnectResponse as ConnectResponse
    from .connected_response import ConnectedResponse as ConnectedResponse
    from .create_request import CreateRequest as CreateRequest
    from .create_response import CreateResponse as CreateResponse
    from .created import Created as Created
    from .disable_pull_response import DisablePullResponse as DisablePullResponse
    from .disable_push_response import DisablePushResponse as DisablePushResponse
    from .disable_request import DisableRequest as DisableRequest
    from .disconnect_response import DisconnectResponse as DisconnectResponse
    from .dosh_request import DoshRequest as DoshRequest
    from .dosh_account import DoshAccount as DoshAccount
    from .dosh_request_pull_configuration import DoshRequestPullConfiguration as DoshRequestPullConfiguration
    from .dosh_request_push_configuration import DoshRequestPushConfiguration as DoshRequestPushConfiguration
    from .enable_pull_request import EnablePullRequest as EnablePullRequest
    from .enable_pull_response import EnablePullResponse as EnablePullResponse
    from .enable_push_response import EnablePushResponse as EnablePushResponse
    from .financial_account import FinancialAccount as FinancialAccount
    from .financial_institution import FinancialInstitution as FinancialInstitution
    from .financial_institution_bank import FinancialInstitutionBank as FinancialInstitutionBank
    from .financial_institution_bank_branch import FinancialInstitutionBankBranch as FinancialInstitutionBankBranch
    from .financial_institution_mobile_money_provider import FinancialInstitutionMobileMoneyProvider as FinancialInstitutionMobileMoneyProvider
    from .id_request import IDRequest as IDRequest
    from .lookup_response import LookupResponse as LookupResponse
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .pull_configuration import PullConfiguration as PullConfiguration
    from .pull_configuration_mandate import PullConfigurationMandate as PullConfigurationMandate
    from .push_configuration import PushConfiguration as PushConfiguration
    from .reconnect_response import ReconnectResponse as ReconnectResponse
    from .type import Type as Type
    from .update_request import UpdateRequest as UpdateRequest
    from .update_response import UpdateResponse as UpdateResponse
    from .updated import Updated as Updated
    from .verification import Verification as Verification
    from .verification import VerificationRequest as VerificationRequest
    from .wallet_request import WalletRequest as WalletRequest
    from .wallet_request_pull_configuration import WalletRequestPullConfiguration as WalletRequestPullConfiguration
    from .wallet_request_push_configuration import WalletRequestPushConfiguration as WalletRequestPushConfiguration


_EXPORTS: dict[str, tuple[str, str]] = {
    "BankRequest": ("inttegro.financial_account.bank_request", "BankRequest"),
    "BankRequestPullConfiguration": ("inttegro.financial_account.bank_request_pull_configuration", "BankRequestPullConfiguration"),
    "BankRequestPushConfiguration": ("inttegro.financial_account.bank_request_push_configuration", "BankRequestPushConfiguration"),
    "CompactResponse": ("inttegro.financial_account.compact_response", "CompactResponse"),
    "ConnectResponse": ("inttegro.financial_account.connect_response", "ConnectResponse"),
    "ConnectedResponse": ("inttegro.financial_account.connected_response", "ConnectedResponse"),
    "CreateRequest": ("inttegro.financial_account.create_request", "CreateRequest"),
    "CreateResponse": ("inttegro.financial_account.create_response", "CreateResponse"),
    "Created": ("inttegro.financial_account.created", "Created"),
    "DisablePullResponse": ("inttegro.financial_account.disable_pull_response", "DisablePullResponse"),
    "DisablePushResponse": ("inttegro.financial_account.disable_push_response", "DisablePushResponse"),
    "DisableRequest": ("inttegro.financial_account.disable_request", "DisableRequest"),
    "DisconnectResponse": ("inttegro.financial_account.disconnect_response", "DisconnectResponse"),
    "DoshRequest": ("inttegro.financial_account.dosh_request", "DoshRequest"),
    "DoshAccount": ("inttegro.financial_account.dosh_account", "DoshAccount"),
    "DoshRequestPullConfiguration": ("inttegro.financial_account.dosh_request_pull_configuration", "DoshRequestPullConfiguration"),
    "DoshRequestPushConfiguration": ("inttegro.financial_account.dosh_request_push_configuration", "DoshRequestPushConfiguration"),
    "EnablePullRequest": ("inttegro.financial_account.enable_pull_request", "EnablePullRequest"),
    "EnablePullResponse": ("inttegro.financial_account.enable_pull_response", "EnablePullResponse"),
    "EnablePushResponse": ("inttegro.financial_account.enable_push_response", "EnablePushResponse"),
    "FinancialAccount": ("inttegro.financial_account.financial_account", "FinancialAccount"),
    "FinancialInstitution": ("inttegro.financial_account.financial_institution", "FinancialInstitution"),
    "FinancialInstitutionBank": ("inttegro.financial_account.financial_institution_bank", "FinancialInstitutionBank"),
    "FinancialInstitutionBankBranch": ("inttegro.financial_account.financial_institution_bank_branch", "FinancialInstitutionBankBranch"),
    "FinancialInstitutionMobileMoneyProvider": ("inttegro.financial_account.financial_institution_mobile_money_provider", "FinancialInstitutionMobileMoneyProvider"),
    "IDRequest": ("inttegro.financial_account.id_request", "IDRequest"),
    "LookupResponse": ("inttegro.financial_account.lookup_response", "LookupResponse"),
    "Page": ("inttegro.financial_account.page", "Page"),
    "PageRequest": ("inttegro.financial_account.page_request", "PageRequest"),
    "PageResponse": ("inttegro.financial_account.page_response", "PageResponse"),
    "PullConfiguration": ("inttegro.financial_account.pull_configuration", "PullConfiguration"),
    "PullConfigurationMandate": ("inttegro.financial_account.pull_configuration_mandate", "PullConfigurationMandate"),
    "PushConfiguration": ("inttegro.financial_account.push_configuration", "PushConfiguration"),
    "ReconnectResponse": ("inttegro.financial_account.reconnect_response", "ReconnectResponse"),
    "Type": ("inttegro.financial_account.type", "Type"),
    "UpdateRequest": ("inttegro.financial_account.update_request", "UpdateRequest"),
    "UpdateResponse": ("inttegro.financial_account.update_response", "UpdateResponse"),
    "Updated": ("inttegro.financial_account.updated", "Updated"),
    "Verification": ("inttegro.financial_account.verification", "Verification"),
    "VerificationRequest": ("inttegro.financial_account.verification", "VerificationRequest"),
    "WalletRequest": ("inttegro.financial_account.wallet_request", "WalletRequest"),
    "WalletRequestPullConfiguration": ("inttegro.financial_account.wallet_request_pull_configuration", "WalletRequestPullConfiguration"),
    "WalletRequestPushConfiguration": ("inttegro.financial_account.wallet_request_push_configuration", "WalletRequestPushConfiguration"),
}

__all__ = [
    "BankRequest",
    "BankRequestPullConfiguration",
    "BankRequestPushConfiguration",
    "CompactResponse",
    "ConnectResponse",
    "ConnectedResponse",
    "CreateRequest",
    "CreateResponse",
    "Created",
    "DisablePullResponse",
    "DisablePushResponse",
    "DisableRequest",
    "DisconnectResponse",
    "DoshRequest",
    "DoshAccount",
    "DoshRequestPullConfiguration",
    "DoshRequestPushConfiguration",
    "EnablePullRequest",
    "EnablePullResponse",
    "EnablePushResponse",
    "FinancialAccount",
    "FinancialInstitution",
    "FinancialInstitutionBank",
    "FinancialInstitutionBankBranch",
    "FinancialInstitutionMobileMoneyProvider",
    "IDRequest",
    "LookupResponse",
    "Page",
    "PageRequest",
    "PageResponse",
    "PullConfiguration",
    "PullConfigurationMandate",
    "PushConfiguration",
    "ReconnectResponse",
    "Type",
    "UpdateRequest",
    "UpdateResponse",
    "Updated",
    "Verification",
    "VerificationRequest",
    "WalletRequest",
    "WalletRequestPullConfiguration",
    "WalletRequestPushConfiguration",
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
