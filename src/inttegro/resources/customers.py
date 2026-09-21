"""Customers resource for creating and managing customer records."""

from __future__ import annotations

from ..http_client import HttpClient
from inttegro.search import Page as SearchPage, Request as SearchRequest


class Customers:
    """Customers resource for creating, updating, looking up, and paging customers.

    Access this service as ``InttegroClient.customers``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict):
        """Create a customer record.

        API endpoint: ``/customers/create``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Customer`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/customers/create", payload)

    def lookup(self, customer_id: str):
        """Lookup a customer by ID.

        API endpoint: ``/customers/lookup``.

        Args:
            customer_id (str): Unique identifier of the customer.

        Returns:
            ``Customer`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/customers/lookup", {"customer_id": customer_id})

    def update(self, payload: dict, idempotency_key: str | None = None):
        """Update supplied fields on a customer record.

        API endpoint: ``/customers/update``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.
            idempotency_key (str | None): Optional stable key to reuse when retrying the same logical write.

        Returns:
            ``Customer`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/customers/update", payload, headers)

    def page(self, payload: dict | None = None):
        """Page through customers.

        API endpoint: ``/customers/page``.

        Args:
            payload (dict | None): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Page`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/customers/page", payload or {})

    def search(self, payload: SearchRequest) -> SearchPage:
        """Search customer projections owned by the authenticated application."""
        return self.http.post("/customers/search", payload)
