"""Typed delivery aggregates for invoice and receipt documents."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DocumentDeliveryChannelSummary(ApiModel):
    """Accepted deliveries aggregated for one channel."""

    count: int = field(init=False)
    latest_sent_at: datetime = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DocumentDeliverySummaryChannels(ApiModel):
    """Accepted delivery totals grouped by channel."""

    email: DocumentDeliveryChannelSummary | None = field(init=False)
    sms: DocumentDeliveryChannelSummary | None = field(init=False)


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DocumentDeliverySummary(ApiModel):
    """Accepted invoice or receipt deliveries aggregated across channels."""

    channels: DocumentDeliverySummaryChannels = field(init=False)
    latest_sent_at: datetime = field(init=False)
    total_count: int = field(init=False)
