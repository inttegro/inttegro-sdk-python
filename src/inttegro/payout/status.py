"""Status in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Status(WireEnum):
    """Current payout lifecycle state.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``PayoutStatus``.
    """
    INITIALIZED = "initialized"
    """Wire value ``initialized`` (initialized) for current payout lifecycle state"""
    SCHEDULED = "scheduled"
    """Wire value ``scheduled`` (scheduled) for current payout lifecycle state"""
    PROCESSING = "processing"
    """Wire value ``processing`` (processing) for current payout lifecycle state"""
    EXECUTING = "executing"
    """Wire value ``executing`` (executing) for current payout lifecycle state"""
    SUCCEEDED = "succeeded"
    """Wire value ``succeeded`` (succeeded) for current payout lifecycle state"""
    FAILED = "failed"
    """Wire value ``failed`` (failed) for current payout lifecycle state"""
    CANCELED = "canceled"
    """Wire value ``canceled`` (canceled) for current payout lifecycle state"""
