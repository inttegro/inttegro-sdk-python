"""BankRequest in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class BankRequest(ApiRequest):
    """Parameters accepted by the bank request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountBankRequest``.
    """
    custom_data: CustomDataInput | UnsetType = field(default=UNSET)
    """Merchant-defined values accepted on resource creation. Values are serialized to strings before storage. Optional. Python type: ``CustomDataInput``; wire name: ``custom_data``; JSON type: object (CustomDataInput)"""
    description: str | UnsetType = field(default=UNSET)
    """Human-readable description of the bank request. Optional. Python type: ``str``; wire name: ``description``; JSON type: string. Constraints: maximum length 200"""
    owner: FinancialAccountOwnerInput | UnsetType = field(default=UNSET)
    """The owner associated with this bank request. Optional. Python type: ``FinancialAccountOwnerInput``; wire name: ``owner``; JSON type: object (FinancialAccountOwnerInput)"""
    pull_configuration: FinancialAccountBankRequestPullConfiguration | UnsetType = field(default=UNSET)
    """The pull configuration associated with this bank request. Optional. Python type: ``FinancialAccountBankRequestPullConfiguration``; wire name: ``pull_configuration``; JSON type: object"""
    push_configuration: FinancialAccountBankRequestPushConfiguration | UnsetType = field(default=UNSET)
    """The push configuration associated with this bank request. Optional. Python type: ``FinancialAccountBankRequestPushConfiguration``; wire name: ``push_configuration``; JSON type: object"""
    currency: str
    """Supported lowercase currency code. Required. Python type: ``str``; wire name: ``currency``; JSON type: string"""
    label: str
    """The label associated with this bank request. Required. Python type: ``str``; wire name: ``label``; JSON type: string. Constraints: minimum length 5; maximum length 40"""
    reference: str
    """Merchant-defined external reference for the bank request. Required. Python type: ``str``; wire name: ``reference``; JSON type: string. Constraints: minimum length 5; maximum length 40"""
    type: Literal['bank_account', FinancialAccountType.BANK_ACCOUNT]
    """Discriminator identifying the bank request type. Required. Python type: ``Literal['bank_account', FinancialAccountType.BANK_ACCOUNT]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``bank_account``"""
    bank_account: FinancialAccountBankRequestBankAccount
    """The bank account associated with this bank request. Required. Python type: ``FinancialAccountBankRequestBankAccount``; wire name: ``bank_account``; JSON type: object"""

from inttegro.bank_account.params import Params as FinancialAccountBankRequestBankAccount
from inttegro.financial_account.bank_request_pull_configuration import BankRequestPullConfiguration as FinancialAccountBankRequestPullConfiguration
from inttegro.financial_account.bank_request_push_configuration import BankRequestPushConfiguration as FinancialAccountBankRequestPushConfiguration
from inttegro.bank_account.owner_params import OwnerParams as FinancialAccountOwnerInput
from inttegro.financial_account.type import Type as FinancialAccountType
from inttegro.custom_data import CustomDataInput
