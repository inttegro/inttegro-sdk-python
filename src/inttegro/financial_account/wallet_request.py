"""WalletRequest in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class WalletRequest(ApiRequest):
    """Parameters accepted by the wallet request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountWalletRequest``.
    """
    custom_data: CustomDataInput | UnsetType = field(default=UNSET)
    """Merchant-defined values accepted on resource creation. Values are serialized to strings before storage. Optional. Python type: ``CustomDataInput``; wire name: ``custom_data``; JSON type: object (CustomDataInput)"""
    description: str | UnsetType = field(default=UNSET)
    """Human-readable description of the wallet request. Optional. Python type: ``str``; wire name: ``description``; JSON type: string. Constraints: maximum length 200"""
    pull_configuration: FinancialAccountWalletRequestPullConfiguration | UnsetType = field(default=UNSET)
    """The pull configuration associated with this wallet request. Optional. Python type: ``FinancialAccountWalletRequestPullConfiguration``; wire name: ``pull_configuration``; JSON type: object"""
    push_configuration: FinancialAccountWalletRequestPushConfiguration | UnsetType = field(default=UNSET)
    """The push configuration associated with this wallet request. Optional. Python type: ``FinancialAccountWalletRequestPushConfiguration``; wire name: ``push_configuration``; JSON type: object"""
    currency: str
    """Supported lowercase currency code. Required. Python type: ``str``; wire name: ``currency``; JSON type: string"""
    label: str
    """The label associated with this wallet request. Required. Python type: ``str``; wire name: ``label``; JSON type: string. Constraints: minimum length 5; maximum length 40"""
    owner: FinancialAccountOwnerInput
    """The owner associated with this wallet request. Required. Python type: ``FinancialAccountOwnerInput``; wire name: ``owner``; JSON type: object (FinancialAccountOwnerInput)"""
    reference: str
    """Merchant-defined external reference for the wallet request. Required. Python type: ``str``; wire name: ``reference``; JSON type: string. Constraints: minimum length 5; maximum length 40"""
    type: Literal['wallet', FinancialAccountType.WALLET]
    """Discriminator identifying the wallet request type. Required. Python type: ``Literal['wallet', FinancialAccountType.WALLET]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``wallet``"""
    wallet: FinancialAccountWalletRequestWallet
    """The wallet associated with this wallet request. Required. Python type: ``FinancialAccountWalletRequestWallet``; wire name: ``wallet``; JSON type: object"""

from inttegro.bank_account.owner_params import OwnerParams as FinancialAccountOwnerInput
from inttegro.financial_account.type import Type as FinancialAccountType
from inttegro.financial_account.wallet_request_pull_configuration import WalletRequestPullConfiguration as FinancialAccountWalletRequestPullConfiguration
from inttegro.financial_account.wallet_request_push_configuration import WalletRequestPushConfiguration as FinancialAccountWalletRequestPushConfiguration
from inttegro.wallet.params import Params as FinancialAccountWalletRequestWallet
from inttegro.custom_data import CustomDataInput
