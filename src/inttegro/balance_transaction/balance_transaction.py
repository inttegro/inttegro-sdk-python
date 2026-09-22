"""BalanceTransaction in the ``inttegro.balance_transaction`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BalanceTransaction(ApiModel):
    """Merchant balance entry caused by a payment or refund. `type` describes the semantic source, not direction. A payment transaction contains `payment_id`; a refund transaction contains `refund_id`. Exactly one matching reference is present.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    amount: BalanceTransactionAmount = field(init=False)
    """Monetary amount, represented by a currency and an integer minor-unit value. Required. Python type: ``BalanceTransactionAmount``; wire name: ``amount``; JSON type: object (BalanceTransactionAmount)"""
    available_at: datetime | None = field(init=False)
    """Timestamp for available at. Optional; nullable. Python type: ``datetime | None``; wire name: ``available_at``; JSON type: string (date-time)"""
    claimed_at: datetime | None = field(init=False)
    """Timestamp for claimed at. Optional; nullable. Python type: ``datetime | None``; wire name: ``claimed_at``; JSON type: string (date-time)"""
    created_at: datetime = field(init=False)
    """When the balance transaction was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    id: str = field(init=False)
    """Unique identifier for this balance transaction. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    order_id: str = field(init=False)
    """Identifier of the related order. Required. Python type: ``str``; wire name: ``order_id``; JSON type: string"""
    paid_at: datetime | None = field(init=False)
    """When payment completed successfully. Optional; nullable. Python type: ``datetime | None``; wire name: ``paid_at``; JSON type: string (date-time)"""
    payment_id: str | None = field(init=False)
    """Present when `type` is `payment`; omitted when `type` is `refund`. Optional; nullable. Python type: ``str | None``; wire name: ``payment_id``; JSON type: string"""
    payout_id: str | None = field(init=False)
    """Identifier of the related payout. Optional; nullable. Python type: ``str | None``; wire name: ``payout_id``; JSON type: string"""
    refund_id: str | None = field(init=False)
    """Present when `type` is `refund`; omitted when `type` is `payment`. Optional; nullable. Python type: ``str | None``; wire name: ``refund_id``; JSON type: string"""
    type: Literal['payment', 'refund'] = field(init=False)
    """Semantic source or cause of the transaction, not its direction. Required. Python type: ``Literal['payment', 'refund']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``payment``, ``refund``"""
    payout_configuration: PaymentPayoutConfiguration | None = field(init=False)
    """The payout configuration associated with this balance transaction. Optional; nullable. Python type: ``PaymentPayoutConfiguration | None``; wire name: ``payout_configuration``; JSON type: object"""
    allocations: list[BalanceTransactionAllocation] | None = field(init=False)
    """All current pending and completed allocations. Released allocations are omitted. Python type: ``list[BalanceTransactionAllocation] | None``; wire name: ``allocations``; JSON type: array"""
    available_amount: BalanceTransactionAmount | None = field(init=False)
    """Amount still available for a refund or payout. Python type: ``BalanceTransactionAmount | None``; wire name: ``available_amount``; JSON type: object"""
    pending_amount: BalanceTransactionAmount | None = field(init=False)
    """Amount reserved by unresolved refunds and payouts. Python type: ``BalanceTransactionAmount | None``; wire name: ``pending_amount``; JSON type: object"""
    spent_amount: BalanceTransactionAmount | None = field(init=False)
    """Amount permanently consumed by completed allocations. Python type: ``BalanceTransactionAmount | None``; wire name: ``spent_amount``; JSON type: object"""

from inttegro.balance_transaction.amount import Amount as BalanceTransactionAmount
from inttegro.balance_transaction.allocation import Allocation as BalanceTransactionAllocation
from inttegro.payment.payout_configuration import PayoutConfiguration as PaymentPayoutConfiguration
