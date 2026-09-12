"""PurchaseIntent in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntent(ApiModel):
    """Typed purchase intent data in the purchase intent resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    allow_variants: bool = field(init=False)
    """Whether the intent was configured with a variant set. Required. Python type: ``bool``; wire name: ``allow_variants``; JSON type: boolean"""
    created_at: datetime = field(init=False)
    """Creation timestamp. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    expires_at: datetime | None = field(init=False)
    """Timestamp at or after which the Buy link is expired. Optional; nullable. Python type: ``datetime | None``; wire name: ``expires_at``; JSON type: string (date-time)"""
    id: str = field(init=False)
    """Unique purchase intent identifier with sale_ prefix. Append it to https://pages.inttegro.com/buy/ to build the hosted Buy link. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    inactive_at: datetime | None = field(init=False)
    """When the Buy link was explicitly canceled. Optional; nullable. Python type: ``datetime | None``; wire name: ``inactive_at``; JSON type: string (date-time)"""
    merchant: PurchaseIntentMerchant | None = field(init=False)
    """Merchant identity captured for the hosted checkout. Individual fields are omitted when unavailable. Optional; nullable. Python type: ``PurchaseIntentMerchant | None``; wire name: ``merchant``; JSON type: object (PurchaseIntentMerchant)"""
    price: PurchaseIntentPrice | None = field(init=False)
    """The price associated with this purchase intent. Optional; nullable. Python type: ``PurchaseIntentPrice | None``; wire name: ``price``; JSON type: object (PurchaseIntentPrice)"""
    product: PurchaseIntentProduct | None = field(init=False)
    """The product associated with this purchase intent. Optional; nullable. Python type: ``PurchaseIntentProduct | None``; wire name: ``product``; JSON type: object (PurchaseIntentProduct)"""
    quantity: PurchaseIntentQuantity = field(init=False)
    """Quantity bounds enforced by the hosted checkout. max is omitted when the offer has no upper bound. Required. Python type: ``PurchaseIntentQuantity``; wire name: ``quantity``; JSON type: object"""
    status: Literal['active', 'expired', 'inactive', 'used'] = field(init=False)
    """Effective lifecycle state derived from expiry, cancellation, and single-use order creation. Required. Python type: ``Literal['active', 'expired', 'inactive', 'used']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``active``, ``expired``, ``inactive``, ``used``"""
    updated_at: datetime | None = field(init=False)
    """Last mutation timestamp. Optional; nullable. Python type: ``datetime | None``; wire name: ``updated_at``; JSON type: string (date-time)"""
    usage: PurchaseIntentUsage = field(init=False)
    """Exactly one of multi_use or single_use is returned as true. Order is present after a single-use intent is consumed. Required. Python type: ``PurchaseIntentUsage``; wire name: ``usage``; JSON type: object (PurchaseIntentUsage)"""
    variant_set: PurchaseIntentVariantSet | None = field(init=False)
    """The variant set associated with this purchase intent. Optional; nullable. Python type: ``PurchaseIntentVariantSet | None``; wire name: ``variant_set``; JSON type: object (PurchaseIntentVariantSet)"""

    def is_active(self) -> bool:
        """Whether the purchase intent is currently active."""
        return self.status == "active"

    def is_single_use(self) -> bool:
        """Whether the purchase intent can create at most one order."""
        return getattr(self.usage, "single_use", False) is True

    def used_order_id(self) -> str | None:
        """Return the order ID that consumed a single-use purchase intent."""
        if not self.is_single_use():
            return None
        order = getattr(self.usage, "order", None)
        order_id = getattr(order, "id", None)
        return order_id if order_id else None

from inttegro.purchase_intent.merchant import Merchant as PurchaseIntentMerchant
from inttegro.purchase_intent.price import Price as PurchaseIntentPrice
from inttegro.purchase_intent.product import Product as PurchaseIntentProduct
from inttegro.purchase_intent.quantity import Quantity as PurchaseIntentQuantity
from inttegro.purchase_intent.usage import Usage as PurchaseIntentUsage
from inttegro.purchase_intent.variant_set import VariantSet as PurchaseIntentVariantSet
