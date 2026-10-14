"""Apps resource for managing the authenticated Inttegro application."""

from __future__ import annotations

from ..http_client import HttpClient
from inttegro.app.capabilities import Capabilities


class Apps:
    """Application creation, lookup, and update operations.

    Access this service as ``InttegroClient.apps``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict):
        """Create a Inttegro application.

        API endpoint: ``/apps/create``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``App`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/apps/create", payload)

    def lookup(self):
        """Retrieve the application associated with the configured API key.

        API endpoint: ``/apps/lookup``.

        Returns:
            ``App`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/apps/lookup", {})

    def capabilities(self) -> Capabilities:
        """Return the authenticated application's payment and payout capabilities."""
        return self.http.post("/apps/capabilities", {})

    def update(self, payload: dict):
        """Update one or more attributes of the configured API key's application.

        API endpoint: ``/apps/update``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``App`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/apps/update", payload)
