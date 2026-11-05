"""Typed children-policy response models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from inttegro._model_base import ApiModel
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class LookupRequest(ApiRequest):
    """Optionally selects one exact children-policy version."""
    version: int | UnsetType = field(default=UNSET)

    def __post_init__(self) -> None:
        if isinstance(self.version, int) and self.version < 1:
            raise ValueError("version must be greater than or equal to 1")


@dataclass(frozen=True, slots=True, kw_only=True)
class PageRequest(ApiRequest):
    """Controls children-policy version pagination."""
    number: int | UnsetType = field(default=UNSET)
    size: int | UnsetType = field(default=UNSET)


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
    version: int = field(init=False)
    active_version: int = field(init=False)
    name: str = field(init=False)
    description: str | None = field(init=False)
    capabilities: Capabilities = field(init=False)
    created_at: datetime = field(init=False)
    updated_at: datetime = field(init=False)
    version_created_at: datetime = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Page(ApiModel):
    """One page of immutable children-policy versions, ordered newest first."""
    number: int = field(init=False)
    size: int = field(init=False)
    count: int = field(init=False)
    total: int = field(init=False)
    has_more: bool = field(init=False)
    versions: list[ChildrenPolicy] = field(init=False)
