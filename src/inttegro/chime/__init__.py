"""Models, requests, and enums for the Inttegro chime resource.

The primary returned object is ``inttegro.chime.Chime``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .chime import Chime as Chime
    from .email_mailbox import EmailMailbox as EmailMailbox
    from .email_mailbox_input import EmailMailboxInput as EmailMailboxInput
    from .email_message import EmailMessage as EmailMessage
    from .email_message_input import EmailMessageInput as EmailMessageInput
    from .email_safety_result import EmailSafetyResult as EmailSafetyResult
    from .email_scanned_link import EmailScannedLink as EmailScannedLink
    from .email_schema_kind import EmailSchemaKind as EmailSchemaKind
    from .email_schema_markup import EmailSchemaMarkup as EmailSchemaMarkup
    from .inline_recipient_input import InlineRecipientInput as InlineRecipientInput
    from .inline_recipient_input_variant1 import InlineRecipientInputVariant1 as InlineRecipientInputVariant1
    from .inline_recipient_input_variant1_phone import InlineRecipientInputVariant1Phone as InlineRecipientInputVariant1Phone
    from .inline_recipient_input_variant2 import InlineRecipientInputVariant2 as InlineRecipientInputVariant2
    from .inline_recipient_input_variant2_email import InlineRecipientInputVariant2Email as InlineRecipientInputVariant2Email
    from .lookup_request import LookupRequest as LookupRequest
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .recipient import Recipient as Recipient
    from .recipient_email import RecipientEmail as RecipientEmail
    from .recipient_input import RecipientInput as RecipientInput
    from .recipient_phone import RecipientPhone as RecipientPhone
    from .recipient_type import RecipientType as RecipientType
    from .response import Response as Response
    from .saved_customer_recipient_input import SavedCustomerRecipientInput as SavedCustomerRecipientInput
    from .send_request import SendRequest as SendRequest
    from .send_request_request_meta import SendRequestRequestMeta as SendRequestRequestMeta
    from .settings import EmailSettings as EmailSettings
    from .settings import Settings as Settings
    from .settings import SMSSettings as SMSSettings
    from .transmission import Transmission as Transmission
    from .transport import Transport as Transport


_EXPORTS: dict[str, tuple[str, str]] = {
    "Chime": ("inttegro.chime.chime", "Chime"),
    "EmailMailbox": ("inttegro.chime.email_mailbox", "EmailMailbox"),
    "EmailMailboxInput": ("inttegro.chime.email_mailbox_input", "EmailMailboxInput"),
    "EmailMessage": ("inttegro.chime.email_message", "EmailMessage"),
    "EmailMessageInput": ("inttegro.chime.email_message_input", "EmailMessageInput"),
    "EmailSafetyResult": ("inttegro.chime.email_safety_result", "EmailSafetyResult"),
    "EmailScannedLink": ("inttegro.chime.email_scanned_link", "EmailScannedLink"),
    "EmailSchemaKind": ("inttegro.chime.email_schema_kind", "EmailSchemaKind"),
    "EmailSchemaMarkup": ("inttegro.chime.email_schema_markup", "EmailSchemaMarkup"),
    "InlineRecipientInput": ("inttegro.chime.inline_recipient_input", "InlineRecipientInput"),
    "InlineRecipientInputVariant1": ("inttegro.chime.inline_recipient_input_variant1", "InlineRecipientInputVariant1"),
    "InlineRecipientInputVariant1Phone": ("inttegro.chime.inline_recipient_input_variant1_phone", "InlineRecipientInputVariant1Phone"),
    "InlineRecipientInputVariant2": ("inttegro.chime.inline_recipient_input_variant2", "InlineRecipientInputVariant2"),
    "InlineRecipientInputVariant2Email": ("inttegro.chime.inline_recipient_input_variant2_email", "InlineRecipientInputVariant2Email"),
    "LookupRequest": ("inttegro.chime.lookup_request", "LookupRequest"),
    "Page": ("inttegro.chime.page", "Page"),
    "PageRequest": ("inttegro.chime.page_request", "PageRequest"),
    "PageResponse": ("inttegro.chime.page_response", "PageResponse"),
    "Recipient": ("inttegro.chime.recipient", "Recipient"),
    "RecipientEmail": ("inttegro.chime.recipient_email", "RecipientEmail"),
    "RecipientInput": ("inttegro.chime.recipient_input", "RecipientInput"),
    "RecipientPhone": ("inttegro.chime.recipient_phone", "RecipientPhone"),
    "RecipientType": ("inttegro.chime.recipient_type", "RecipientType"),
    "Response": ("inttegro.chime.response", "Response"),
    "SavedCustomerRecipientInput": ("inttegro.chime.saved_customer_recipient_input", "SavedCustomerRecipientInput"),
    "SendRequest": ("inttegro.chime.send_request", "SendRequest"),
    "SendRequestRequestMeta": ("inttegro.chime.send_request_request_meta", "SendRequestRequestMeta"),
    "EmailSettings": ("inttegro.chime.settings", "EmailSettings"),
    "Settings": ("inttegro.chime.settings", "Settings"),
    "SMSSettings": ("inttegro.chime.settings", "SMSSettings"),
    "Transmission": ("inttegro.chime.transmission", "Transmission"),
    "Transport": ("inttegro.chime.transport", "Transport"),
}

__all__ = [
    "Chime",
    "EmailMailbox",
    "EmailMailboxInput",
    "EmailMessage",
    "EmailMessageInput",
    "EmailSafetyResult",
    "EmailScannedLink",
    "EmailSchemaKind",
    "EmailSchemaMarkup",
    "InlineRecipientInput",
    "InlineRecipientInputVariant1",
    "InlineRecipientInputVariant1Phone",
    "InlineRecipientInputVariant2",
    "InlineRecipientInputVariant2Email",
    "LookupRequest",
    "Page",
    "PageRequest",
    "PageResponse",
    "Recipient",
    "RecipientEmail",
    "RecipientInput",
    "RecipientPhone",
    "RecipientType",
    "Response",
    "SavedCustomerRecipientInput",
    "SendRequest",
    "SendRequestRequestMeta",
    "EmailSettings",
    "Settings",
    "SMSSettings",
    "Transmission",
    "Transport",
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
