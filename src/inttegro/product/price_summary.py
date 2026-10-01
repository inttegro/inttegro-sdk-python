"""PriceSummary in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.money import Amount
from inttegro.price.customer_selected_amount import CustomerSelectedAmount
from inttegro.price.type import Type as PriceType


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PriceSummary(ApiModel):
    """Typed price summary data in the product resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ProductPriceSummary``.
    """
    id: str = field(init=False)
    """Unique price identifier with pr_ prefix. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    active: bool = field(init=False)
    """Whether this price is active and usable in new flows. Required. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    label: str | None = field(init=False)
    """Short label for this price. Optional; nullable. Python type: ``str | None``; wire name: ``label``; JSON type: string"""
    type: PriceType = field(init=False)
    """Price definition discriminator. Required. Python type: ``PriceType``; wire name: ``type``; JSON type: string (PriceType)"""
    nominal: Amount | None = field(init=False)
    """Deprecated fixed-price compatibility alias. Present only for fixed prices. Python type: ``Amount | None``; wire name: ``nominal``; JSON type: object (Amount)"""
    fixed_amount: Amount | None = field(init=False)
    """Fixed amount present only for fixed prices. Python type: ``Amount | None``; wire name: ``fixed_amount``; JSON type: object (Amount)"""
    customer_selected_amount: CustomerSelectedAmount | None = field(init=False)
    """Selection policy present only for customer-selected prices. Python type: ``CustomerSelectedAmount | None``; wire name: ``customer_selected_amount``; JSON type: object (CustomerSelectedAmount)"""
