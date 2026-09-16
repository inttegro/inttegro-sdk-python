"""UpdateRequest in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequest(ApiRequest):
    """Parameters accepted by the update request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountUpdateRequest``.
    """
    custom_data: CustomDataPatch | UnsetType = field(default=UNSET)
    """Changes to merchant-defined data. JSON null removes a key; every other JSON value is serialized to a string. Optional. Python type: ``CustomDataPatch``; wire name: ``custom_data``; JSON type: object (CustomDataPatch)"""
    description: str | UnsetType = field(default=UNSET)
    """Human-readable description of the update request. Optional. Python type: ``str``; wire name: ``description``; JSON type: string"""
    label: str | UnsetType = field(default=UNSET)
    """The label associated with this update request. Optional. Python type: ``str``; wire name: ``label``; JSON type: string"""
    owner: FinancialAccountOwnerUpdateInput | UnsetType = field(default=UNSET)
    """The owner associated with this update request. Optional. Python type: ``FinancialAccountOwnerUpdateInput``; wire name: ``owner``; JSON type: object (FinancialAccountOwnerUpdateInput)"""
    reference: str | UnsetType = field(default=UNSET)
    """Merchant-defined external reference for the update request. Optional. Python type: ``str``; wire name: ``reference``; JSON type: string"""
    account_id: str
    """Identifier of the related account. Required. Python type: ``str``; wire name: ``account_id``; JSON type: string"""

from inttegro.bank_account.owner_update_params import OwnerUpdateParams as FinancialAccountOwnerUpdateInput
from inttegro.custom_data import CustomDataPatch
