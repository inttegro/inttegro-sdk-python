"""DetailsInput in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias
from inttegro.product.catalog_with_price_data_input import CatalogWithPriceDataInput as CatalogProductWithPriceDataInput
from inttegro.product.catalog_with_price_reference_input import CatalogWithPriceReferenceInput as CatalogProductWithPriceReferenceInput
from inttegro.product.catalog_with_customer_selected_price_input import CatalogWithCustomerSelectedPriceInput as CatalogProductWithCustomerSelectedPriceInput
from inttegro.product.inline_details_input import InlineDetailsInput as InlineProductDetailsInput


DetailsInput: TypeAlias = InlineProductDetailsInput | CatalogProductWithPriceDataInput | CatalogProductWithPriceReferenceInput | CatalogProductWithCustomerSelectedPriceInput
"""Product details for an order line item. Customer-selected prices are accepted only with a catalog ``product_id`` and tightly couple ``price_id`` with ``selected_amount``."""
