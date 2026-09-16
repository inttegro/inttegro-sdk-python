"""UpdateRequest in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequest(ApiRequest):
    """A tokenized payment instrument tied to a customer.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdatePaymentMethodRequest``.
    """
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    active: bool | UnsetType = field(default=UNSET)
    """Whether this payment method is active and reusable in new payment flows. Optional. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    archived: bool | UnsetType = field(default=UNSET)
    """Whether archived. Optional. Python type: ``bool``; wire name: ``archived``; JSON type: boolean"""
    owner: UpdatePaymentMethodRequestOwner | UnsetType = field(default=UNSET)
    """Owner identity captured during tokenization when provided. Optional. Python type: ``UpdatePaymentMethodRequestOwner``; wire name: ``owner``; JSON type: object"""
    payment_method_id: str
    """Identifier of the related payment method. Required. Python type: ``str``; wire name: ``payment_method_id``; JSON type: string"""

from inttegro.payment_method.update_request_owner import UpdateRequestOwner as UpdatePaymentMethodRequestOwner
from inttegro.custom_data import CustomData
