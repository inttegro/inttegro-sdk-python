"""Public Dosh-account marker."""

from dataclasses import dataclass

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DoshAccount(ApiModel):
    """Marks a Dosh account without exposing credentials or internal IDs."""
