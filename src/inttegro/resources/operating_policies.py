"""Operating-policy operations."""

from __future__ import annotations

from ..http_client import HttpClient
from inttegro.operating_policy import CreateRequest, LookupRequest, OperatingPolicy, UpdateRequest


class OperatingPolicies:
    """Create, look up, and version reusable operating policies."""

    def __init__(self, http: HttpClient) -> None:
        self.http = http

    def create(self, payload: CreateRequest) -> OperatingPolicy:
        """Create the first immutable version of an operating policy."""
        return self.http.post("/operating_policies/create", payload)

    def lookup(self, operating_policy_id: str | LookupRequest) -> OperatingPolicy:
        """Return the latest active version of an operating policy."""
        payload = (
            operating_policy_id
            if isinstance(operating_policy_id, LookupRequest)
            else LookupRequest(operating_policy_id=operating_policy_id)
        )
        return self.http.post("/operating_policies/lookup", payload)

    def update(self, payload: UpdateRequest) -> OperatingPolicy:
        """Create and activate a new immutable operating-policy version."""
        return self.http.post("/operating_policies/update", payload)
