"""Children-policy operations."""

from __future__ import annotations

from typing import cast

from ..http_client import HttpClient
from inttegro.children_policy import ChildrenPolicy, LookupRequest, Page, PageRequest


class ChildrenPolicies:
    """Look up the authenticated application's active children policy."""

    def __init__(self, http: HttpClient) -> None:
        self.http = http

    def lookup(self, version: int | LookupRequest | None = None) -> ChildrenPolicy:
        """Return the latest policy by default, or one exact immutable version."""
        if isinstance(version, LookupRequest):
            payload = version
        elif version is None:
            payload = LookupRequest()
        else:
            payload = LookupRequest(version=version)
        return cast(ChildrenPolicy, self.http.post("/children_policies/lookup", payload))

    def page(self, payload: PageRequest | None = None) -> Page:
        """List immutable versions of the authenticated application's policy."""
        return cast(Page, self.http.post("/children_policies/page", payload or PageRequest()))
