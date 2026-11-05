"""Operating-policy operations."""

from __future__ import annotations

from typing import cast

from ..http_client import HttpClient
from inttegro.operating_policy import (
    CreateRequest,
    LookupRequest,
    OperatingPolicy,
    Page,
    PageRequest,
    UpdateRequest,
)


class OperatingPolicies:
    """Create, look up, and version reusable operating policies."""

    def __init__(self, http: HttpClient) -> None:
        self.http = http

    def create(self, payload: CreateRequest) -> OperatingPolicy:
        """Create the first immutable version of an operating policy."""
        return cast(OperatingPolicy, self.http.post("/operating_policies/create", payload))

    def lookup(
        self,
        operating_policy_id: str | LookupRequest,
        version: int | None = None,
    ) -> OperatingPolicy:
        """Return the latest policy by default, or one exact immutable version."""
        if isinstance(operating_policy_id, LookupRequest):
            if version is not None:
                raise ValueError("version must be supplied in LookupRequest, not twice")
            payload = operating_policy_id
        else:
            payload = (
                LookupRequest(operating_policy_id=operating_policy_id)
                if version is None
                else LookupRequest(operating_policy_id=operating_policy_id, version=version)
            )
        return cast(OperatingPolicy, self.http.post("/operating_policies/lookup", payload))

    def page(self, payload: PageRequest) -> Page:
        """List immutable versions of one operating policy."""
        return cast(Page, self.http.post("/operating_policies/page", payload))

    def update(self, payload: UpdateRequest) -> OperatingPolicy:
        """Create and activate a new immutable operating-policy version."""
        return cast(OperatingPolicy, self.http.post("/operating_policies/update", payload))
