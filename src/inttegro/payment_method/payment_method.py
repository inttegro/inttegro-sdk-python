"""PaymentMethod in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethod(ApiModel):
    """A tokenized payment instrument tied to a customer.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    active: bool = field(init=False)
    """Whether this payment method is active and reusable in new payment flows. Required. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    archived_at: datetime | None = field(init=False)
    """Timestamp when the payment method was archived. Omitted while unarchived. Optional; nullable. Python type: ``datetime | None``; wire name: ``archived_at``; JSON type: string (date-time)"""
    bank_account: PaymentMethodBankAccount | None = field(init=False)
    """Bank account details (present when type is bank_account). Optional; nullable. Python type: ``PaymentMethodBankAccount | None``; wire name: ``bank_account``; JSON type: object"""
    card: PaymentMethodCard | None = field(init=False)
    """Card marker. Nested card credentials are not returned. Optional; nullable. Python type: ``PaymentMethodCard | None``; wire name: ``card``; JSON type: object (PaymentMethodCard)"""
    created_at: datetime = field(init=False)
    """When this payment method was tokenized. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    customer_id: str = field(init=False)
    """Customer who owns this payment method. Required. Python type: ``str``; wire name: ``customer_id``; JSON type: string"""
    ephemeral: bool | None = field(init=False)
    """Whether the method is limited to its originating flow and cannot be reused. Optional; nullable. Python type: ``bool | None``; wire name: ``ephemeral``; JSON type: boolean"""
    expires_on: datetime | None = field(init=False)
    """When this payment method expires. Omitted when no expiry is available. Optional; nullable. Python type: ``datetime | None``; wire name: ``expires_on``; JSON type: string (date-time)"""
    fingerprint: str = field(init=False)
    """App-customer-local fingerprint. Required; empty when unavailable. Python type: ``str``; wire name: ``fingerprint``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this payment method. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    mobile_money: PaymentMethodMobileMoney | None = field(init=False)
    """Masked mobile-money wallet details (present when type is mobile_money). Optional; nullable. Python type: ``PaymentMethodMobileMoney | None``; wire name: ``mobile_money``; JSON type: object"""
    owner: PaymentMethodOwner | None = field(init=False)
    """Owner identity captured during tokenization when provided. Optional; nullable. Python type: ``PaymentMethodOwner | None``; wire name: ``owner``; JSON type: object"""
    type: Literal['mobile_money', 'bank_account', 'card', 'motito'] = field(init=False)
    """Payment rail type. Required. Python type: ``Literal['mobile_money', 'bank_account', 'card', 'motito']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``mobile_money``, ``bank_account``, ``card``, ``motito``"""
    supplied: PaymentMethodSupplied | None = field(init=False)
    """Public provenance for how the payment method was supplied. Optional; nullable. Python type: ``PaymentMethodSupplied | None``; wire name: ``supplied``; JSON type: object"""
    verification: PaymentMethodVerification | None = field(init=False)
    """Most recent verification record when the payment method has entered a verification flow. Optional; nullable. Python type: ``PaymentMethodVerification | None``; wire name: ``verification``; JSON type: object"""
    verified_at: datetime | None = field(init=False)
    """When ownership verification was completed. Optional; nullable. Python type: ``datetime | None``; wire name: ``verified_at``; JSON type: string (date-time)"""

    def is_archived(self) -> bool:
        """Whether the payment method is archived."""
        return getattr(self, "archived_at", None) is not None

    def is_verified(self) -> bool:
        """Whether payment-method ownership has been verified."""
        return getattr(self, "verified_at", None) is not None

    def is_reusable(self) -> bool:
        """Whether the payment method may be reused in new payment flows."""
        return self.active and not self.is_archived() and getattr(self, "ephemeral", False) is not True

from inttegro.payment_method.bank_account import BankAccount as PaymentMethodBankAccount
from inttegro.payment_method.card import Card as PaymentMethodCard
from inttegro.payment_method.mobile_money import MobileMoney as PaymentMethodMobileMoney
from inttegro.payment_method.owner import Owner as PaymentMethodOwner
from inttegro.payment_method.supplied import Supplied as PaymentMethodSupplied
from inttegro.payment_method.verification import Verification as PaymentMethodVerification
from inttegro.custom_data import CustomData
