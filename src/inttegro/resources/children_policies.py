"""Children-policy operations."""

from __future__ import annotations

from ..http_client import HttpClient
from inttegro.children_policy import ChildrenPolicy


class ChildrenPolicies:
    """Look up the authenticated application's active children policy."""

    def __init__(self, http: HttpClient) -> None:
        self.http = http

    def lookup(self) -> ChildrenPolicy:
        """Return the authenticated application's latest active children policy."""
        return self.http.post("/children_policies/lookup", {})
