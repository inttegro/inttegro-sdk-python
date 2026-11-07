"""Typed preferences for an Inttegro API response."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from inttegro._request_base import ApiRequest
from inttegro.request.selection import PropertySelection


@dataclass(frozen=True, slots=True, kw_only=True)
class Response(ApiRequest):
    """Select public response properties by endpoint-defined resource name.

    Resources omitted from ``projection`` keep their complete caller-visible
    representation. The endpoint reference defines valid resource names and
    property paths.
    """

    projection: Mapping[str, PropertySelection]
