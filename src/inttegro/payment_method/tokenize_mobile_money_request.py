"""TokenizeMobileMoneyRequest in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class TokenizeMobileMoneyRequest(ApiRequest):
    """Parameters accepted by the tokenize mobile money request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``TokenizeMobileMoneyPaymentMethodRequest``.
    """
    custom_data: CustomData | UnsetType = field(default=UNSET)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional. Python type: ``CustomData``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    customer_id: str
    """Existing customer in the authenticated application who will own the payment method. Required. Python type: ``str``; wire name: ``customer_id``; JSON type: string. Constraints: minimum length 1"""
    type: Literal['mobile_money', PaymentMethodType.MOBILE_MONEY]
    """Discriminator identifying the tokenize mobile money request type. Required. Python type: ``Literal['mobile_money', PaymentMethodType.MOBILE_MONEY]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``mobile_money``"""
    mobile_money: TokenizeMobileMoneyPaymentMethodRequestMobileMoney
    """The mobile money associated with this tokenize mobile money request. Required. Python type: ``TokenizeMobileMoneyPaymentMethodRequestMobileMoney``; wire name: ``mobile_money``; JSON type: object"""
    owner: PaymentMethodOwnerInput
    """The owner associated with this tokenize mobile money request. Required. Python type: ``PaymentMethodOwnerInput``; wire name: ``owner``; JSON type: object (PaymentMethodOwnerInput)"""

from inttegro.payment_method.owner_input import OwnerInput as PaymentMethodOwnerInput
from inttegro.payment_method.type import Type as PaymentMethodType
from inttegro.payment_method.tokenize_mobile_money_request_mobile_money import TokenizeMobileMoneyRequestMobileMoney as TokenizeMobileMoneyPaymentMethodRequestMobileMoney
from inttegro.custom_data import CustomData
