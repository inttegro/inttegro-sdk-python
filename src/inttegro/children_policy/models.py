"""Typed children-policy response models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class AmountRange(ApiModel):
    """Inclusive amount bounds in minor currency units."""
    min: int = field(init=False)
    max: int = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Limits(ApiModel):
    """Amount limits granted by a children policy."""
    amount: AmountRange = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BTAgingSpec(ApiModel):
    """Platform-owned balance-transaction aging option."""
    public_id: str = field(init=False)
    t_plus: str = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentsCapabilities(ApiModel):
    """Payment choices and bounds available to child applications."""
    currencies: list[str] = field(init=False)
    limits: Limits = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutsCapabilities(ApiModel):
    """Payout choices, bounds, and aging options available to children."""
    enabled: list[bool] = field(init=False)
    limits: Limits = field(init=False)
    bt_aging_spec: list[BTAgingSpec] = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodCapabilities(ApiModel):
    """Allowed state combinations for one child payment method."""
    enabled: list[bool] = field(init=False)
    confirms_use: list[bool] = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodsCapabilities(ApiModel):
    """Payment-method choices available to child applications."""
    mobile_money: PaymentMethodCapabilities = field(init=False)
    bank_account: PaymentMethodCapabilities = field(init=False)
    motito: PaymentMethodCapabilities = field(init=False)
    card: PaymentMethodCapabilities = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Capabilities(ApiModel):
    """Complete authority granted by a children policy."""
    payments: PaymentsCapabilities = field(init=False)
    payouts: PayoutsCapabilities = field(init=False)
    payment_methods: PaymentMethodsCapabilities = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChildrenPolicy(ApiModel):
    """Latest active children policy assigned to an application."""
    id: str = field(init=False)
    owner_application_id: str = field(init=False)
    version: int = field(init=False)
    active_version: int = field(init=False)
    name: str = field(init=False)
    description: str | None = field(init=False)
    capabilities: Capabilities = field(init=False)
    created_at: datetime = field(init=False)
    updated_at: datetime = field(init=False)
    version_created_at: datetime = field(init=False)
