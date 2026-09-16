"""Customer in the ``inttegro.customer`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Customer(ApiModel):
    """Typed customer data in the customer resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    balance: dict[str, CustomerBalanceValue] = field(init=False)
    """Available customer balances keyed by lowercase currency code. Required. Python type: ``dict[str, CustomerBalanceValue]``; wire name: ``balance``; JSON type: object (CustomerBalance)"""
    billing_address: CustomerAddress | None = field(init=False)
    """The billing address associated with this customer. Optional; nullable. Python type: ``CustomerAddress | None``; wire name: ``billing_address``; JSON type: object (CustomerAddress)"""
    created_at: datetime = field(init=False)
    """When the customer was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    custom_data: CustomData | None = field(init=False)
    """Merchant-defined string values attached to a resource. SDKs expose this as a semantic collection rather than a raw map. Optional; nullable. Python type: ``CustomData | None``; wire name: ``custom_data``; JSON type: object (CustomData)"""
    email_address: str | None = field(init=False)
    """Customer or recipient email address. Optional; nullable. Python type: ``str | None``; wire name: ``email_address``; JSON type: string"""
    guest: bool = field(init=False)
    """Whether guest. Required. Python type: ``bool``; wire name: ``guest``; JSON type: boolean"""
    id: str = field(init=False)
    """Unique identifier for this customer. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    name: str = field(init=False)
    """Human-readable name of the customer. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    phone_number: str | None = field(init=False)
    """Customer or recipient phone number in international form. Optional; nullable. Python type: ``str | None``; wire name: ``phone_number``; JSON type: string"""
    reference: str | None = field(init=False)
    """Merchant-defined external reference for the customer. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""
    shipping_address: CustomerAddress | None = field(init=False)
    """The shipping address associated with this customer. Optional; nullable. Python type: ``CustomerAddress | None``; wire name: ``shipping_address``; JSON type: object (CustomerAddress)"""
    suffix: str | None = field(init=False)
    """The suffix associated with this customer. Optional; nullable. Python type: ``str | None``; wire name: ``suffix``; JSON type: string"""
    title: str | None = field(init=False)
    """The title associated with this customer. Optional; nullable. Python type: ``str | None``; wire name: ``title``; JSON type: string"""
    updated_at: datetime | None = field(init=False)
    """When the customer was last updated. Optional; nullable. Python type: ``datetime | None``; wire name: ``updated_at``; JSON type: string (date-time)"""

from inttegro.customer.address import Address as CustomerAddress
from inttegro.customer.balance_value import BalanceValue as CustomerBalanceValue
from inttegro.custom_data import CustomData
