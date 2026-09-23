"""Models, requests, and enums for the Inttegro payout resource.

The primary returned object is ``inttegro.payout.Payout``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .balance_transaction import BalanceTransaction as BalanceTransaction
    from .cancel_request import CancelRequest as CancelRequest
    from .cancel_response import CancelResponse as CancelResponse
    from .disable_automatic_request import DisableAutomaticRequest as DisableAutomaticRequest
    from .disable_automatic_response import DisableAutomaticResponse as DisableAutomaticResponse
    from .destinations import Destinations as Destinations
    from .destinations_input import DestinationsInput as DestinationsInput
    from .enable_automatic_request import EnableAutomaticRequest as EnableAutomaticRequest
    from .enable_automatic_response import EnableAutomaticResponse as EnableAutomaticResponse
    from .error import Error as Error
    from .get_settings_request import GetSettingsRequest as GetSettingsRequest
    from .get_settings_response import GetSettingsResponse as GetSettingsResponse
    from .lookup_request import LookupRequest as LookupRequest
    from .lookup_response import LookupResponse as LookupResponse
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .payout import Payout as Payout
    from .set_destinations_request import SetDestinationsRequest as SetDestinationsRequest
    from .set_destinations_response import SetDestinationsResponse as SetDestinationsResponse
    from .settings_lookup import SettingsLookup as SettingsLookup
    from .settings_lookup_schedule import SettingsLookupSchedule as SettingsLookupSchedule
    from .settings_lookup_schedule_aging_spec import SettingsLookupScheduleAgingSpec as SettingsLookupScheduleAgingSpec
    from .settings_mutation import SettingsMutation as SettingsMutation
    from .settings_mutation_schedule import SettingsMutationSchedule as SettingsMutationSchedule
    from .settings_mutation_schedule_spec import SettingsMutationScheduleSpec as SettingsMutationScheduleSpec
    from .status import Status as Status


_EXPORTS: dict[str, tuple[str, str]] = {
    "BalanceTransaction": ("inttegro.payout.balance_transaction", "BalanceTransaction"),
    "CancelRequest": ("inttegro.payout.cancel_request", "CancelRequest"),
    "CancelResponse": ("inttegro.payout.cancel_response", "CancelResponse"),
    "DisableAutomaticRequest": ("inttegro.payout.disable_automatic_request", "DisableAutomaticRequest"),
    "DisableAutomaticResponse": ("inttegro.payout.disable_automatic_response", "DisableAutomaticResponse"),
    "Destinations": ("inttegro.payout.destinations", "Destinations"),
    "DestinationsInput": ("inttegro.payout.destinations_input", "DestinationsInput"),
    "EnableAutomaticRequest": ("inttegro.payout.enable_automatic_request", "EnableAutomaticRequest"),
    "EnableAutomaticResponse": ("inttegro.payout.enable_automatic_response", "EnableAutomaticResponse"),
    "Error": ("inttegro.payout.error", "Error"),
    "GetSettingsRequest": ("inttegro.payout.get_settings_request", "GetSettingsRequest"),
    "GetSettingsResponse": ("inttegro.payout.get_settings_response", "GetSettingsResponse"),
    "LookupRequest": ("inttegro.payout.lookup_request", "LookupRequest"),
    "LookupResponse": ("inttegro.payout.lookup_response", "LookupResponse"),
    "Page": ("inttegro.payout.page", "Page"),
    "PageRequest": ("inttegro.payout.page_request", "PageRequest"),
    "PageResponse": ("inttegro.payout.page_response", "PageResponse"),
    "Payout": ("inttegro.payout.payout", "Payout"),
    "SetDestinationsRequest": ("inttegro.payout.set_destinations_request", "SetDestinationsRequest"),
    "SetDestinationsResponse": ("inttegro.payout.set_destinations_response", "SetDestinationsResponse"),
    "SettingsLookup": ("inttegro.payout.settings_lookup", "SettingsLookup"),
    "SettingsLookupSchedule": ("inttegro.payout.settings_lookup_schedule", "SettingsLookupSchedule"),
    "SettingsLookupScheduleAgingSpec": ("inttegro.payout.settings_lookup_schedule_aging_spec", "SettingsLookupScheduleAgingSpec"),
    "SettingsMutation": ("inttegro.payout.settings_mutation", "SettingsMutation"),
    "SettingsMutationSchedule": ("inttegro.payout.settings_mutation_schedule", "SettingsMutationSchedule"),
    "SettingsMutationScheduleSpec": ("inttegro.payout.settings_mutation_schedule_spec", "SettingsMutationScheduleSpec"),
    "Status": ("inttegro.payout.status", "Status"),
}

__all__ = [
    "BalanceTransaction",
    "CancelRequest",
    "CancelResponse",
    "DisableAutomaticRequest",
    "DisableAutomaticResponse",
    "Destinations",
    "DestinationsInput",
    "EnableAutomaticRequest",
    "EnableAutomaticResponse",
    "Error",
    "GetSettingsRequest",
    "GetSettingsResponse",
    "LookupRequest",
    "LookupResponse",
    "Page",
    "PageRequest",
    "PageResponse",
    "Payout",
    "SetDestinationsRequest",
    "SetDestinationsResponse",
    "SettingsLookup",
    "SettingsLookupSchedule",
    "SettingsLookupScheduleAgingSpec",
    "SettingsMutation",
    "SettingsMutationSchedule",
    "SettingsMutationScheduleSpec",
    "Status",
]


def __getattr__(name: str) -> Any:
    """Load a public resource type on first access."""
    try:
        module_name, attribute_name = _EXPORTS[name]
    except KeyError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from None
    value = getattr(import_module(module_name), attribute_name)
    globals()[name] = value
    return value
