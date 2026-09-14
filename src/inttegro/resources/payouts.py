"""Typed payout operations for transfers from an Inttegro balance."""

from __future__ import annotations

from ..http_client import HttpClient
from inttegro.payout.destinations_input import DestinationsInput
from inttegro.payout.page import Page
from inttegro.payout.page_request import PageRequest
from inttegro.payout.payout import Payout
from inttegro.payout.set_destinations_request import SetDestinationsRequest
from inttegro.payout.settings_lookup import SettingsLookup
from inttegro.payout.settings_mutation import SettingsMutation
from inttegro.schedule.payout_request import PayoutRequest


class Payouts:
    """Configure payout routing and inspect payout lifecycle state.

    Access this resource through :attr:`inttegro.Client.payouts`. Successful
    responses are decoded into the payout models named in each return annotation;
    callers do not need to traverse response envelopes or parse timestamps.
    """

    def __init__(self, http: HttpClient) -> None:
        """Create the resource with the client's authenticated HTTP transport."""
        self.http = http

    def set_destinations(
        self,
        destinations: SetDestinationsRequest | DestinationsInput,
    ) -> SettingsMutation:
        """Assign the financial account that receives GHS payouts.

        Pass :class:`DestinationsInput` for the concise form, or a complete
        :class:`SetDestinationsRequest`. An empty ``ghs`` string removes the
        existing assignment. The returned :class:`SettingsMutation` exposes the
        updated ``destinations`` directly.

        Example::

            settings = client.payouts.set_destinations(
                DestinationsInput(ghs="fa_123")
            )
            print(settings.destinations.ghs)
        """
        if isinstance(destinations, SetDestinationsRequest):
            return self.http.post("/payouts/set_destinations", destinations)
        return self.http.post(
            "/payouts/set_destinations",
            SetDestinationsRequest(destinations=destinations),
        )

    def settings(self) -> SettingsLookup:
        """Return the complete payout settings read model.

        ``destinations`` is a typed object with a ``ghs`` attribute. ``schedule``
        exposes its interval, execution day, and nested aging specification; it is
        ``None`` when no schedule is configured.
        """
        return self.http.post("/payouts/settings", {})

    def schedule(self, payload: PayoutRequest) -> Payout:
        """Schedule a payout using typed destination, limit, reference, and time fields.

        ``execute_after`` accepts a timezone-aware :class:`datetime.datetime` and
        is serialized by the request model. The response is a :class:`Payout`
        whose timestamp fields are parsed as datetimes.
        """
        return self.http.post("/payouts/schedule", payload)

    def lookup(self, payout_id: str) -> Payout:
        """Retrieve one payout by its ``po_`` identifier."""
        return self.http.post("/payouts/lookup", {"payout_id": payout_id})

    def disable_automatic(self) -> SettingsMutation:
        """Switch to manual payout scheduling and return the changed settings."""
        return self.http.post("/payouts/disable", {})

    def enable_automatic(self) -> SettingsMutation:
        """Restore automatic payout scheduling and return the changed settings."""
        return self.http.post("/payouts/enable", {})

    def enable_fx(self) -> SettingsMutation:
        """Enable payout currency conversion and return the changed settings."""
        return self.http.post("/payouts/enable_fx", {})

    def disable_fx(self) -> SettingsMutation:
        """Disable payout currency conversion and return the changed settings."""
        return self.http.post("/payouts/disable_fx", {})

    def page(self, payload: PageRequest) -> Page:
        """Return a typed page of payouts in reverse chronological order.

        ``page_number`` is one-based and required. ``page_size`` is optional and
        limited to 256. Each item is a :class:`Payout`, not a dictionary.

        Example::

            page = client.payouts.page(PageRequest(page_number=1, page_size=50))
            for payout in page.payouts or []:
                print(payout.id, payout.status, payout.initiated_at)
        """
        return self.http.post("/payouts/page", payload)

    def cancel(self, payout_id: str) -> Payout:
        """Cancel a scheduled payout and return its updated typed representation."""
        return self.http.post("/payouts/cancel", {"payout_id": payout_id})
