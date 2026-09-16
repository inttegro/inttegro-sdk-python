"""Created in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Created(ApiModel):
    """Typed created data in the financial account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FinancialAccountCreateResponse``.
    """
    archived_at: datetime | None = field(init=False)
    """When the created was archived. Optional; nullable. Python type: ``datetime | None``; wire name: ``archived_at``; JSON type: string (date-time)"""
    created_at: datetime = field(init=False)
    """When the created was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    currency: str = field(init=False)
    """The currency associated with this created. Required. Python type: ``str``; wire name: ``currency``; JSON type: string"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    description: str | None = field(init=False)
    """Human-readable description of the created. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this created. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    institution: FinancialInstitution | None = field(init=False)
    """The institution associated with this created. Optional; nullable. Python type: ``FinancialInstitution | None``; wire name: ``institution``; JSON type: object (FinancialInstitution)"""
    label: str | None = field(init=False)
    """The label associated with this created. Optional; nullable. Python type: ``str | None``; wire name: ``label``; JSON type: string"""
    pull_configuration: FinancialAccountPullConfiguration | None = field(init=False)
    """The pull configuration associated with this created. Optional; nullable. Python type: ``FinancialAccountPullConfiguration | None``; wire name: ``pull_configuration``; JSON type: object (FinancialAccountPullConfiguration)"""
    push_configuration: FinancialAccountPushConfiguration | None = field(init=False)
    """The push configuration associated with this created. Optional; nullable. Python type: ``FinancialAccountPushConfiguration | None``; wire name: ``push_configuration``; JSON type: object (FinancialAccountPushConfiguration)"""
    reference: str | None = field(init=False)
    """Merchant-defined external reference for the created. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""
    supplied: ResourceSupply | None = field(init=False)
    """The supplied associated with this created. Optional; nullable. Python type: ``ResourceSupply | None``; wire name: ``supplied``; JSON type: object (ResourceSupply)"""
    type: Literal['wallet', 'bank_account', 'dosh_account'] = field(init=False)
    """Discriminator identifying the created type. Required. Python type: ``Literal['wallet', 'bank_account', 'dosh_account']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``wallet``, ``bank_account``, ``dosh_account``"""
    verification: dict[str, Any] | None = field(init=False)
    """The verification associated with this created. Optional; nullable. Python type: ``dict[str, Any] | None``; wire name: ``verification``; JSON type: object (FinancialAccountVerification)"""
    bank_account: FinancialAccountBankCreateResponse | None = field(init=False)
    """The bank account associated with this created. Optional; nullable. Python type: ``FinancialAccountBankCreateResponse | None``; wire name: ``bank_account``; JSON type: object (FinancialAccountBankCreateResponse)"""
    owner: FinancialAccountOwnerCreateResponse | None = field(init=False)
    """The owner associated with this created. Optional; nullable. Python type: ``FinancialAccountOwnerCreateResponse | None``; wire name: ``owner``; JSON type: object (FinancialAccountOwnerCreateResponse)"""
    wallet: FinancialAccountWallet | None = field(init=False)
    """The wallet associated with this created. Optional; nullable. Python type: ``FinancialAccountWallet | None``; wire name: ``wallet``; JSON type: object (FinancialAccountWalletResponse)"""

from inttegro.bank_account.created_bank_account import CreatedBankAccount as FinancialAccountBankCreateResponse
from inttegro.bank_account.created_owner import CreatedOwner as FinancialAccountOwnerCreateResponse
from inttegro.financial_account.pull_configuration import PullConfiguration as FinancialAccountPullConfiguration
from inttegro.financial_account.push_configuration import PushConfiguration as FinancialAccountPushConfiguration
from inttegro.wallet.wallet import Wallet as FinancialAccountWallet
from inttegro.financial_account.financial_institution import FinancialInstitution
from inttegro.shared.resource_supply import ResourceSupply
from inttegro.custom_data import CustomData
