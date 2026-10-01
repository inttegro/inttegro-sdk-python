"""Catalog product with a customer-selected price order input."""

from __future__ import annotations

from dataclasses import dataclass

from inttegro._request_base import ApiRequest
from inttegro.product.customer_selected_price_input import CustomerSelectedPriceInput


@dataclass(frozen=True, slots=True, kw_only=True)
class CatalogWithCustomerSelectedPriceInput(ApiRequest):
    """A catalog product using a selected amount from one saved price."""

    product_id: str
    customer_selected_price: CustomerSelectedPriceInput
    quantity: int
