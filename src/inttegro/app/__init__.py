"""Models, requests, and enums for the Inttegro app resource.

The primary returned object is ``inttegro.app.App``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .app import App as App
    from .capabilities import Capabilities as Capabilities
    from .capabilities import Capability as Capability
    from .capabilities import CapabilityRequirement as CapabilityRequirement
    from .capabilities import CapabilityRequirements as CapabilityRequirements
    from .create_request import CreateRequest as CreateRequest
    from .create_request_relationship_policy import CreateRequestRelationshipPolicy as CreateRequestRelationshipPolicy
    from .create_response import CreateResponse as CreateResponse
    from .credential_owner import CredentialOwner as CredentialOwner
    from .lookup_response import LookupResponse as LookupResponse
    from .lookup_response_app import LookupResponseApp as LookupResponseApp
    from .management_role import ManagementRole as ManagementRole
    from .relationship import Relationship as Relationship
    from .relationship_kind import RelationshipKind as RelationshipKind
    from .relationship_policy import RelationshipPolicy as RelationshipPolicy
    from .relationship_status import RelationshipStatus as RelationshipStatus
    from .secret_key import SecretKey as SecretKey
    from .update_request import UpdateRequest as UpdateRequest
    from .update_response import UpdateResponse as UpdateResponse
    from .update_response_app import UpdateResponseApp as UpdateResponseApp


_EXPORTS: dict[str, tuple[str, str]] = {
    "App": ("inttegro.app.app", "App"),
    "Capabilities": ("inttegro.app.capabilities", "Capabilities"),
    "Capability": ("inttegro.app.capabilities", "Capability"),
    "CapabilityRequirement": ("inttegro.app.capabilities", "CapabilityRequirement"),
    "CapabilityRequirements": ("inttegro.app.capabilities", "CapabilityRequirements"),
    "CreateRequest": ("inttegro.app.create_request", "CreateRequest"),
    "CreateRequestRelationshipPolicy": ("inttegro.app.create_request_relationship_policy", "CreateRequestRelationshipPolicy"),
    "CreateResponse": ("inttegro.app.create_response", "CreateResponse"),
    "CredentialOwner": ("inttegro.app.credential_owner", "CredentialOwner"),
    "LookupResponse": ("inttegro.app.lookup_response", "LookupResponse"),
    "LookupResponseApp": ("inttegro.app.lookup_response_app", "LookupResponseApp"),
    "ManagementRole": ("inttegro.app.management_role", "ManagementRole"),
    "Relationship": ("inttegro.app.relationship", "Relationship"),
    "RelationshipKind": ("inttegro.app.relationship_kind", "RelationshipKind"),
    "RelationshipPolicy": ("inttegro.app.relationship_policy", "RelationshipPolicy"),
    "RelationshipStatus": ("inttegro.app.relationship_status", "RelationshipStatus"),
    "SecretKey": ("inttegro.app.secret_key", "SecretKey"),
    "UpdateRequest": ("inttegro.app.update_request", "UpdateRequest"),
    "UpdateResponse": ("inttegro.app.update_response", "UpdateResponse"),
    "UpdateResponseApp": ("inttegro.app.update_response_app", "UpdateResponseApp"),
}

__all__ = [
    "App",
    "Capabilities",
    "Capability",
    "CapabilityRequirement",
    "CapabilityRequirements",
    "CreateRequest",
    "CreateRequestRelationshipPolicy",
    "CreateResponse",
    "CredentialOwner",
    "LookupResponse",
    "LookupResponseApp",
    "ManagementRole",
    "Relationship",
    "RelationshipKind",
    "RelationshipPolicy",
    "RelationshipStatus",
    "SecretKey",
    "UpdateRequest",
    "UpdateResponse",
    "UpdateResponseApp",
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
