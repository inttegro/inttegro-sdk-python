"""Typed request and response models shared by resource search endpoints."""

from __future__ import annotations

from dataclasses import dataclass, field as dataclass_field
from datetime import datetime

from inttegro._enum_base import WireEnum
from inttegro._model_base import ApiModel
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.money import Amount


class Operator(WireEnum):
    """Comparison supported by a resource search filter."""
    EQ = "eq"
    IN = "in"


class SortField(WireEnum):
    """Supported ordering field for resource search."""
    RELEVANCE = "relevance"
    UPDATED_AT = "updated_at"
    PUBLISHED_AT = "published_at"


class SortDirection(WireEnum):
    """Direction applied to the selected search ordering."""
    ASC = "asc"
    DESC = "desc"


class ResourceType(WireEnum):
    """Resource type represented by a search projection."""
    CUSTOMER = "customer"
    FINANCIAL_ACCOUNT = "financial_account"
    ORDER = "order"
    PAYOUT = "payout"
    PRODUCT = "product"


class TotalRelation(WireEnum):
    """Whether a returned total is exact or a lower bound."""
    EXACT = "exact"
    LOWER_BOUND = "lower_bound"


class FreshnessState(WireEnum):
    """Freshness of the search projection relative to canonical resources."""
    CURRENT = "current"
    DELAYED = "delayed"
    PARTIAL = "partial"
    UNKNOWN = "unknown"
    UNAVAILABLE = "unavailable"


@dataclass(frozen=True, slots=True, kw_only=True)
class Filter(ApiRequest):
    """A route-local field constraint."""
    field: str
    operator: Operator
    values: list[str]


@dataclass(frozen=True, slots=True, kw_only=True)
class Facet(ApiRequest):
    """A route-local field to group and count."""
    field: str
    limit: int | UnsetType = dataclass_field(default=UNSET)


@dataclass(frozen=True, slots=True, kw_only=True)
class Sort(ApiRequest):
    """Typed search ordering."""
    field: SortField
    direction: SortDirection


@dataclass(frozen=True, slots=True, kw_only=True)
class Request(ApiRequest):
    """A typed resource-local search request."""

    text: str | UnsetType = dataclass_field(default=UNSET)
    filters: list[Filter] | UnsetType = dataclass_field(default=UNSET)
    facets: list[Facet] | UnsetType = dataclass_field(default=UNSET)
    sort: Sort | UnsetType = dataclass_field(default=UNSET)
    page_size: int | UnsetType = dataclass_field(default=UNSET)
    cursor: str | UnsetType = dataclass_field(default=UNSET)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Total(ApiModel):
    """The result count and whether it is exact."""

    value: int = dataclass_field(init=False)
    relation: TotalRelation = dataclass_field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ResourceTotal(ApiModel):
    """A per-resource result count."""

    resource_type: ResourceType = dataclass_field(init=False)
    value: int = dataclass_field(init=False)
    relation: TotalRelation = dataclass_field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ResourceReference(ApiModel):
    """The canonical type and identifier for a search result."""

    type: ResourceType = dataclass_field(init=False)
    id: str = dataclass_field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Result(ApiModel):
    """A discovery projection for a canonical resource."""

    resource: ResourceReference = dataclass_field(init=False)
    title: str = dataclass_field(init=False)
    summary: str | None = dataclass_field(init=False)
    status: str | None = dataclass_field(init=False)
    customer_name: str | None = dataclass_field(init=False)
    amount: Amount | None = dataclass_field(init=False)
    url: str | None = dataclass_field(init=False)
    updated_at: datetime = dataclass_field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FacetBucket(ApiModel):
    """One value and count in a requested facet."""

    value: str = dataclass_field(init=False)
    count: int = dataclass_field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FacetResult(ApiModel):
    """The buckets returned for one requested field."""

    field: str = dataclass_field(init=False)
    buckets: list[FacetBucket] = dataclass_field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ResourceFreshness(ApiModel):
    """Freshness information for the searched resource type."""

    resource_type: ResourceType = dataclass_field(init=False)
    state: FreshnessState = dataclass_field(init=False)
    observed_at: datetime | None = dataclass_field(init=False)
    last_indexed_at: datetime | None = dataclass_field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Freshness(ApiModel):
    """Overall and resource-specific search index freshness."""

    state: FreshnessState = dataclass_field(init=False)
    observed_at: datetime | None = dataclass_field(init=False)
    resources: list[ResourceFreshness] | None = dataclass_field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Page(ApiModel):
    """Search projections and continuation metadata."""

    resource_types: list[ResourceType] = dataclass_field(init=False)
    sort: SortResult = dataclass_field(init=False)
    page_size: int = dataclass_field(init=False)
    result_count: int = dataclass_field(init=False)
    has_more: bool = dataclass_field(init=False)
    total: Total = dataclass_field(init=False)
    resource_totals: list[ResourceTotal] = dataclass_field(init=False)
    results: list[Result] = dataclass_field(init=False)
    facets: list[FacetResult] = dataclass_field(init=False)
    next_cursor: str | None = dataclass_field(init=False)
    freshness: Freshness = dataclass_field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SortResult(ApiModel):
    """Ordering echoed by a search response."""

    field: SortField = dataclass_field(init=False)
    direction: SortDirection = dataclass_field(init=False)
