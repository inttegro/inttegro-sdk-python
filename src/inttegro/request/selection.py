"""Typed public-property selections for an Inttegro API response."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class Pick(ApiRequest):
    """Include only the named public property paths for one response resource.

    Ancestors needed to contain a selected descendant remain present. Selecting
    a parent includes its complete caller-visible subtree.
    """

    pick: Sequence[str]

    def __post_init__(self) -> None:
        object.__setattr__(self, "pick", _property_paths("pick", self.pick))


@dataclass(frozen=True, slots=True, kw_only=True)
class Omit(ApiRequest):
    """Exclude the named public property paths from one response resource.

    Omitting a property also omits all of its descendants.
    """

    omit: Sequence[str]

    def __post_init__(self) -> None:
        object.__setattr__(self, "omit", _property_paths("omit", self.omit))


PropertySelection = Pick | Omit
"""Exactly one ``pick`` or ``omit`` selection for a response resource."""


def _property_paths(mode: str, values: Sequence[str]) -> tuple[str, ...]:
    paths = tuple(values)
    if not paths:
        raise ValueError(f"{mode} must contain at least one property path")
    if any(not isinstance(path, str) or not path.strip() for path in paths):
        raise ValueError(f"{mode} property paths must be non-blank strings")
    return paths
