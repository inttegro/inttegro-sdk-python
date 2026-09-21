"""Products resource for managing catalog products."""

from __future__ import annotations

from ..http_client import HttpClient
from inttegro.search import Page as SearchPage, Request as SearchRequest


class Products:
    """Products resource for creating, updating, and managing products.

    Access this service as ``InttegroClient.products``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict):
        """Create a product.

        API endpoint: ``/products/create``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Product`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/products/create", payload)

    def add_price(self, payload: dict):
        """Add a price to a product.

        API endpoint: ``/products/add_price``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Price`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/products/add_price", payload)

    def set_default_unit_price(self, payload: dict):
        """Set a product's default unit price.

        API endpoint: ``/products/set_default_unit_price``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Product`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/products/set_default_unit_price", payload)

    def lookup(self, product_id: str):
        """Lookup a product by ID.

        API endpoint: ``/products/lookup``.

        Args:
            product_id (str): Unique identifier of the product.

        Returns:
            ``Product`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/products/lookup", {"product_id": product_id})

    def update(self, payload: dict):
        """Update a product.

        API endpoint: ``/products/update``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Product`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/products/update", payload)

    def publish(self, product_id: str):
        """Publish a product.

        API endpoint: ``/products/publish``.

        Args:
            product_id (str): Unique identifier of the product.

        Returns:
            ``Product`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/products/publish", {"product_id": product_id})

    def unpublish(self, product_id: str):
        """Unpublish a product.

        API endpoint: ``/products/unpublish``.

        Args:
            product_id (str): Unique identifier of the product.

        Returns:
            ``Product`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/products/unpublish", {"product_id": product_id})

    def archive(self, product_id: str):
        """Archive a product.

        API endpoint: ``/products/archive``.

        Args:
            product_id (str): Unique identifier of the product.

        Returns:
            ``Product`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/products/archive", {"product_id": product_id})

    def page(self, payload: dict | None = None):
        """Page through products.

        API endpoint: ``/products/page``.

        Args:
            payload (dict | None): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Page`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/products/page", payload or {})

    def search(self, payload: SearchRequest) -> SearchPage:
        """Search product projections owned by the authenticated application."""
        return self.http.post("/products/search", payload)
