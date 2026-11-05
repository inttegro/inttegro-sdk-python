"""Typed operating-policy request and response models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal, TypeAlias

from inttegro._model_base import ApiModel
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class AmountRangeInput(ApiRequest):
    """Inclusive amount bounds accepted in a policy request."""
    min: int
    max: int


@dataclass(frozen=True, slots=True, kw_only=True)
class LimitsInput(ApiRequest):
    """Amount limits accepted in a policy request."""
    amount: AmountRangeInput


@dataclass(frozen=True, slots=True, kw_only=True)
class BTAgingSpecReference(ApiRequest):
    """Caller-selectable platform aging-specification identifier."""
    id: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PaymentsCapabilitiesInput(ApiRequest):
    """Payment settings accepted in a policy request."""
    currencies: list[str] | UnsetType = field(default=UNSET)
    limits: LimitsInput | UnsetType = field(default=UNSET)


@dataclass(frozen=True, slots=True, kw_only=True)
class PayoutsCapabilitiesInput(ApiRequest):
    """Payout settings accepted in a policy request."""
    enabled: bool | UnsetType = field(default=UNSET)
    limits: LimitsInput | UnsetType = field(default=UNSET)
    bt_aging_spec: BTAgingSpecReference | UnsetType = field(default=UNSET)


@dataclass(frozen=True, slots=True, kw_only=True)
class PaymentMethodCapabilitiesInput(ApiRequest):
    """Configuration accepted for one payment method."""
    enabled: bool
    confirms_use: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class PaymentMethodsCapabilitiesInput(ApiRequest):
    """Payment-method settings accepted in a policy request."""
    mobile_money: PaymentMethodCapabilitiesInput | UnsetType = field(default=UNSET)
    bank_account: PaymentMethodCapabilitiesInput | UnsetType = field(default=UNSET)
    motito: PaymentMethodCapabilitiesInput | UnsetType = field(default=UNSET)
    card: PaymentMethodCapabilitiesInput | UnsetType = field(default=UNSET)


@dataclass(frozen=True, slots=True, kw_only=True)
class CapabilitiesInput(ApiRequest):
    """Complete operating configuration accepted by policy operations."""
    payments: PaymentsCapabilitiesInput | UnsetType = field(default=UNSET)
    payouts: PayoutsCapabilitiesInput | UnsetType = field(default=UNSET)
    payment_methods: PaymentMethodsCapabilitiesInput | UnsetType = field(default=UNSET)


@dataclass(frozen=True, slots=True, kw_only=True)
class IDSelection(ApiRequest):
    """Selects a reusable operating policy by identifier."""
    id: str


@dataclass(frozen=True, slots=True, kw_only=True)
class InlineSelection(ApiRequest):
    """Selects an inline operating-policy configuration."""
    capabilities: CapabilitiesInput


Selection: TypeAlias = IDSelection | InlineSelection

# This module is an implementation detail; the package initializer re-exports
# the public selection alias explicitly.
__all__ = ("Selection",)


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequest(ApiRequest):
    """Parameters for creating the first operating-policy version."""
    name: str
    capabilities: CapabilitiesInput
    description: str | UnsetType = field(default=UNSET)


@dataclass(frozen=True, slots=True, kw_only=True)
class LookupRequest(ApiRequest):
    """Parameters for looking up an operating policy."""
    operating_policy_id: str
    version: int | UnsetType = field(default=UNSET)

    def __post_init__(self) -> None:
        if isinstance(self.version, int) and self.version < 1:
            raise ValueError("version must be greater than or equal to 1")


@dataclass(frozen=True, slots=True, kw_only=True)
class PageRequest(ApiRequest):
    """Selects one operating policy and controls version pagination."""
    operating_policy_id: str
    number: int | UnsetType = field(default=UNSET)
    size: int | UnsetType = field(default=UNSET)


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequest(ApiRequest):
    """Parameters for creating a new operating-policy version."""
    operating_policy_id: str
    expected_version: int
    name: str | UnsetType = field(default=UNSET)
    description: str | UnsetType = field(default=UNSET)
    capabilities: CapabilitiesInput | UnsetType = field(default=UNSET)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class AmountRange(ApiModel):
    """Inclusive resolved amount bounds in minor currency units."""
    min: int = field(init=False)
    max: int = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Limits(ApiModel):
    """Resolved amount limits."""
    amount: AmountRange = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BTAgingSpec(ApiModel):
    """Platform-resolved balance-transaction aging configuration."""
    public_id: str = field(init=False)
    t_plus: str = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentsCapabilities(ApiModel):
    """Resolved payment configuration selected for an application."""
    currencies: list[str] = field(init=False)
    limits: Limits = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutsCapabilities(ApiModel):
    """Resolved payout configuration selected for an application."""
    enabled: bool = field(init=False)
    limits: Limits = field(init=False)
    bt_aging_spec: BTAgingSpec = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodCapabilities(ApiModel):
    """Resolved configuration for one payment method."""
    enabled: bool = field(init=False)
    confirms_use: bool = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodsCapabilities(ApiModel):
    """Resolved payment-method configuration."""
    mobile_money: PaymentMethodCapabilities = field(init=False)
    bank_account: PaymentMethodCapabilities = field(init=False)
    motito: PaymentMethodCapabilities = field(init=False)
    card: PaymentMethodCapabilities = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Capabilities(ApiModel):
    """Complete resolved operating configuration."""
    payments: PaymentsCapabilities = field(init=False)
    payouts: PayoutsCapabilities = field(init=False)
    payment_methods: PaymentMethodsCapabilities = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Source(ApiModel):
    """Provenance for a policy snapshot applied to an application."""
    type: Literal["inline", "template"] = field(init=False)
    id: str | None = field(init=False)
    version: int | None = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Snapshot(ApiModel):
    """Immutable operating-policy snapshot applied to an application."""
    capabilities: Capabilities = field(init=False)
    source: Source = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OperatingPolicy(ApiModel):
    """Latest active immutable version of a reusable operating policy."""
    id: str = field(init=False)
    version: int = field(init=False)
    active_version: int = field(init=False)
    name: str = field(init=False)
    description: str | None = field(init=False)
    capabilities: Capabilities = field(init=False)
    children_policy_id: str = field(init=False)
    children_policy_version: int = field(init=False)
    created_at: datetime = field(init=False)
    updated_at: datetime = field(init=False)
    version_created_at: datetime = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Page(ApiModel):
    """One page of immutable operating-policy versions, ordered newest first."""
    number: int = field(init=False)
    size: int = field(init=False)
    count: int = field(init=False)
    total: int = field(init=False)
    has_more: bool = field(init=False)
    versions: list[OperatingPolicy] = field(init=False)
