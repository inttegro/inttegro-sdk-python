"""UpdateRequest in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequest(ApiRequest):
    """Parameters accepted by the update request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdatePurchaseIntentRequest``.
    """
    expires_at: datetime | None | UnsetType = field(default=UNSET)
    """RFC3339 expiry timestamp, including a past time for immediate expiry, or null to clear expiry. Optional; nullable. Python type: ``datetime | None``; wire name: ``expires_at``; JSON type: string (date-time)"""
    id: str | UnsetType = field(default=UNSET)
    """Purchase intent ID to update. Send this or purchase_intent_id. Optional. Python type: ``str``; wire name: ``id``; JSON type: string. Constraints: minimum length 1"""
    quantity: UpdatePurchaseIntentRequestQuantity | UnsetType = field(default=UNSET)
    """Replacement quantity bounds. Omit the object to preserve the current bounds. Within the object, min is required and omitting max removes the upper bound. When present, max must be greater than or equal to min. Optional. Python type: ``UpdatePurchaseIntentRequestQuantity``; wire name: ``quantity``; JSON type: object"""
    purchase_intent_id: str | UnsetType = field(default=UNSET)
    """Alias for id. If both are present, this value takes precedence. Optional. Python type: ``str``; wire name: ``purchase_intent_id``; JSON type: string. Constraints: minimum length 1"""
    reactivate: bool | UnsetType = field(default=UNSET)
    """Clears the state that prevents new purchases. For canceled Buy links this removes inactive_at. For expired Buy links this clears an existing elapsed expires_at value. It does not remove the order claim from a used single-use intent. Optional. Python type: ``bool``; wire name: ``reactivate``; JSON type: boolean"""
    presentation: UpdatePurchaseIntentRequestPresentation | UnsetType = field(default=UNSET)
    """Sparse hosted Buy page copy update. Optional. Python type: ``UpdatePurchaseIntentRequestPresentation``; wire name: ``presentation``; JSON type: object"""

from inttegro.purchase_intent.update_request_quantity import UpdateRequestQuantity as UpdatePurchaseIntentRequestQuantity
from inttegro.purchase_intent.update_request_presentation import UpdateRequestPresentation as UpdatePurchaseIntentRequestPresentation
