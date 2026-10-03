"""CreateRequest in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequest(ApiRequest):
    """Parameters accepted by the create request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreatePurchaseIntentRequest``.
    """
    product: CreatePurchaseIntentRequestProduct | UnsetType = field(default=UNSET)
    """Product selection with optional variant-set configuration. Use this instead of product_id. Optional. Python type: ``CreatePurchaseIntentRequestProduct``; wire name: ``product``; JSON type: object"""
    product_id: str | UnsetType = field(default=UNSET)
    """App-owned product ID to sell through the Buy link when not using product. Optional. Python type: ``str``; wire name: ``product_id``; JSON type: string"""
    price: CreatePurchaseIntentRequestPrice | UnsetType = field(default=UNSET)
    """Price selection for the Buy link. Send exactly one of id or nominal and at most one of original or original_id. Optional. Python type: ``CreatePurchaseIntentRequestPrice``; wire name: ``price``; JSON type: object"""
    price_id: str | UnsetType = field(default=UNSET)
    """Active, unarchived app-owned price ID that belongs to the selected product. Optional. Python type: ``str``; wire name: ``price_id``; JSON type: string"""
    usage: CreatePurchaseIntentRequestUsage | UnsetType = field(default=UNSET)
    """Optional link-use policy. Omit to create a reusable Buy link. Optional. Python type: ``CreatePurchaseIntentRequestUsage``; wire name: ``usage``; JSON type: object"""
    expires_at: datetime | UnsetType = field(default=UNSET)
    """Future RFC3339 timestamp after which the Buy link stops accepting purchases. Optional. Python type: ``datetime``; wire name: ``expires_at``; JSON type: string (date-time)"""
    presentation: CreatePurchaseIntentRequestPresentation | UnsetType = field(default=UNSET)
    """Optional merchant-authored copy for the hosted Buy page. Optional. Python type: ``CreatePurchaseIntentRequestPresentation``; wire name: ``presentation``; JSON type: object"""
    quantity: CreatePurchaseIntentRequestQuantity
    """Quantity bounds the Buy link should enforce. Omit max when the Buy link has no upper quantity bound. When present, max must be greater than or equal to min. Required. Python type: ``CreatePurchaseIntentRequestQuantity``; wire name: ``quantity``; JSON type: object"""

from inttegro.purchase_intent.create_request_price import CreateRequestPrice as CreatePurchaseIntentRequestPrice
from inttegro.purchase_intent.create_request_product import CreateRequestProduct as CreatePurchaseIntentRequestProduct
from inttegro.purchase_intent.create_request_quantity import CreateRequestQuantity as CreatePurchaseIntentRequestQuantity
from inttegro.purchase_intent.create_request_usage import CreateRequestUsage as CreatePurchaseIntentRequestUsage
from inttegro.purchase_intent.create_request_presentation import CreateRequestPresentation as CreatePurchaseIntentRequestPresentation
