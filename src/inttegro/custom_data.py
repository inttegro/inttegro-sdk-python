"""Semantic custom-data collections shared by generated resource models."""

from __future__ import annotations

import json
from collections.abc import Iterator, Mapping
from typing import Any, TypeVar, cast

MAX_CUSTOM_DATA_KEY_BYTES = 256
MAX_CUSTOM_DATA_BYTES = 25 * 1024

CustomDataT = TypeVar("CustomDataT", bound="_CustomDataMapping")


class _CustomDataMapping(Mapping[str, Any]):
    """Immutable JSON object with validated keys and defensive values."""

    __slots__ = ("_values",)

    def __init__(self, values: Mapping[str, Any] | None = None) -> None:
        normalized = self._normalize(values or {})
        self._validate(normalized)
        self._values = normalized

    @classmethod
    def from_mapping(
        cls: type[CustomDataT], values: Mapping[str, Any]
    ) -> CustomDataT:
        return cls(values)

    def __getitem__(self, key: str) -> Any:
        return _json_copy(self._values[key])

    def __iter__(self) -> Iterator[str]:
        return iter(self._values)

    def __len__(self) -> int:
        return len(self._values)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._values!r})"

    def to_dict(self) -> dict[str, Any]:
        return cast(dict[str, Any], _json_copy(self._values))

    def with_value(self: CustomDataT, key: str, value: Any) -> CustomDataT:
        values = self.to_dict()
        values[key] = value
        return type(self)(values)

    def without(self: CustomDataT, key: str) -> CustomDataT:
        values = self.to_dict()
        values.pop(key, None)
        return type(self)(values)

    def _normalize(self, values: Mapping[str, Any]) -> dict[str, Any]:
        return {str(key): _json_copy(value) for key, value in values.items()}

    def _validate(self, values: Mapping[str, Any]) -> None:
        for key in values:
            if len(key.encode("utf-8")) > MAX_CUSTOM_DATA_KEY_BYTES:
                raise ValueError("custom data key exceeds 256 bytes")
        encoded = json.dumps(values, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        if len(encoded) > MAX_CUSTOM_DATA_BYTES:
            raise ValueError("custom data exceeds 25 KiB")


class CustomData(_CustomDataMapping):
    """Read-only merchant-defined string values returned by the API."""

    def _normalize(self, values: Mapping[str, Any]) -> dict[str, str]:
        normalized: dict[str, str] = {}
        for key, value in values.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise TypeError("CustomData keys and values must be strings")
            normalized[key] = value
        return normalized

    def with_value(self, key: str, value: str) -> CustomData:
        return super().with_value(key, value)


class CustomDataInput(_CustomDataMapping):
    """Open-ended JSON values accepted by create and replace requests."""


class CustomDataPatch(_CustomDataMapping):
    """Merge operations where an explicit ``None`` removes a stored key."""

    def set(self, key: str, value: Any) -> CustomDataPatch:
        if value is None:
            raise ValueError("use unset() to remove a custom-data value")
        return self.with_value(key, value)

    def unset(self, key: str) -> CustomDataPatch:
        return self.with_value(key, None)

    def remove_change(self, key: str) -> CustomDataPatch:
        return self.without(key)


def _json_copy(value: Any) -> Any:
    try:
        return json.loads(json.dumps(value, ensure_ascii=False))
    except (TypeError, ValueError) as error:
        raise TypeError("custom data values must be JSON-serializable") from error
