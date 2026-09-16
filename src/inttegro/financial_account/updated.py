"""Updated in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Updated(ApiModel):
    """Typed updated data in the financial account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FinancialAccountUpdateResponse``.
    """
    archived_at: datetime | None = field(init=False)
    """When the updated was archived. Optional; nullable. Python type: ``datetime | None``; wire name: ``archived_at``; JSON type: string (date-time)"""
    created_at: datetime = field(init=False)
    """When the updated was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    currency: str = field(init=False)
    """The currency associated with this updated. Required. Python type: ``str``; wire name: ``currency``; JSON type: string"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    description: str | None = field(init=False)
    """Human-readable description of the updated. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this updated. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    institution: FinancialInstitution | None = field(init=False)
    """The institution associated with this updated. Optional; nullable. Python type: ``FinancialInstitution | None``; wire name: ``institution``; JSON type: object (FinancialInstitution)"""
    label: str | None = field(init=False)
    """The label associated with this updated. Optional; nullable. Python type: ``str | None``; wire name: ``label``; JSON type: string"""
    pull_configuration: FinancialAccountPullConfiguration | None = field(init=False)
    """The pull configuration associated with this updated. Optional; nullable. Python type: ``FinancialAccountPullConfiguration | None``; wire name: ``pull_configuration``; JSON type: object (FinancialAccountPullConfiguration)"""
    push_configuration: FinancialAccountPushConfiguration | None = field(init=False)
    """The push configuration associated with this updated. Optional; nullable. Python type: ``FinancialAccountPushConfiguration | None``; wire name: ``push_configuration``; JSON type: object (FinancialAccountPushConfiguration)"""
    reference: str | None = field(init=False)
    """Merchant-defined external reference for the updated. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""
    supplied: ResourceSupply | None = field(init=False)
    """The supplied associated with this updated. Optional; nullable. Python type: ``ResourceSupply | None``; wire name: ``supplied``; JSON type: object (ResourceSupply)"""
    type: Literal['wallet', 'bank_account', 'dosh_account'] = field(init=False)
    """Discriminator identifying the updated type. Required. Python type: ``Literal['wallet', 'bank_account', 'dosh_account']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``wallet``, ``bank_account``, ``dosh_account``"""
    verification: dict[str, Any] | None = field(init=False)
    """The verification associated with this updated. Optional; nullable. Python type: ``dict[str, Any] | None``; wire name: ``verification``; JSON type: object (FinancialAccountVerification)"""
    bank_account: FinancialAccountBankUpdateResponse | None = field(init=False)
    """The bank account associated with this updated. Optional; nullable. Python type: ``FinancialAccountBankUpdateResponse | None``; wire name: ``bank_account``; JSON type: object (FinancialAccountBankUpdateResponse)"""
    disconnected_at: datetime | None = field(init=False)
    """Timestamp for disconnected at. Optional; nullable. Python type: ``datetime | None``; wire name: ``disconnected_at``; JSON type: string (date-time)"""
    dosh_account: dict[str, Any] | None = field(init=False)
    """Dosh account marker. Dosh credentials and internal identifiers are not supplied by callers or returned publicly. Optional; nullable. Python type: ``dict[str, Any] | None``; wire name: ``dosh_account``; JSON type: object (DoshAccount)"""
    owner: FinancialAccountOwnerUpdateResponse | None = field(init=False)
    """The owner associated with this updated. Optional; nullable. Python type: ``FinancialAccountOwnerUpdateResponse | None``; wire name: ``owner``; JSON type: object (FinancialAccountOwnerUpdateResponse)"""
    wallet: FinancialAccountWalletRawResponse | None = field(init=False)
    """Update responses currently return the wallet ID without its type prefix. Optional; nullable. Python type: ``FinancialAccountWalletRawResponse | None``; wire name: ``wallet``; JSON type: object (FinancialAccountWalletRawResponse)"""

from inttegro.bank_account.updated_bank_account import UpdatedBankAccount as FinancialAccountBankUpdateResponse
from inttegro.bank_account.updated_owner import UpdatedOwner as FinancialAccountOwnerUpdateResponse
from inttegro.financial_account.pull_configuration import PullConfiguration as FinancialAccountPullConfiguration
from inttegro.financial_account.push_configuration import PushConfiguration as FinancialAccountPushConfiguration
from inttegro.wallet.updated_wallet import UpdatedWallet as FinancialAccountWalletRawResponse
from inttegro.financial_account.financial_institution import FinancialInstitution
from inttegro.shared.resource_supply import ResourceSupply
from inttegro.custom_data import CustomData
