## [Unreleased]

## [10.0.0] - 2026-09-16

- Breaking: replaced generic custom-data dictionaries with immutable
  `CustomData`, `CustomDataInput`, and `CustomDataPatch` mappings.
- Preserved open-ended JSON request values while making replacement and merge
  behavior explicit and validating custom-data size and key limits.
- Kept customer billing and shipping addresses represented by their native
  typed request and response models throughout serialization.

## [9.0.0] - 2026-09-14

- Breaking: replaced payout dictionaries and generic payloads with named
  request, response, settings, page, error, and destination models.
- Made `ghs` the explicit supported payout-destination attribute and exposed
  payout timestamps as timezone-aware `datetime` values.
- Removed server-internal purchase-intent activity response models and exposed
  refund order and cancellation context.

## [8.1.0] - 2026-09-12

- Added opt-in response envelopes that expose status, headers, request IDs,
  retry hints, and response metadata without changing existing resource return
  values.

## [8.0.0] - 2026-09-11

- Breaking: moved resource models and enums from the `inttegro` root into singular resource packages such as `inttegro.payment.Payment`, with one public type per file.
- Breaking: removed the obsolete flat and plural-package compatibility aliases.
- Added focused question and accessor methods for common resource state, actionability, amounts, customers, and payment methods.
- Expanded and automatically verified the API documentation for resource types, enum values, and synchronous and asynchronous client operations.

## [7.0.0] - 2026-09-10

- Breaking: replaced generic dictionaries with named models for balances, purchase intents, products, payment methods, payments, and orders.
- Breaking: exposed API timestamps as timezone-aware `datetime` values and accepted them in timestamp request fields.

## [6.3.1] - 2026-09-08

- Tightened financial-account and payment-method response models to exclude internal platform fields.

## [6.2.0] - 2026-09-06

- Added opt-in, typed error reporting to application-owned collectors with privacy-safe payloads, stable fingerprints, isolated reporter failures, and no reporting work when unconfigured.

## [6.1.2] - 2026-09-04

- Restored a 100% Pyright public type-completeness score by explicitly typing the OpenTelemetry tracer.

## [6.1.1] - 2026-09-04

- Fixed the release version check so it does not import runtime dependencies before installation.

## [6.1.0] - 2026-09-04

- Added vendor-neutral OpenTelemetry spans for logical SDK operations, HTTP attempts, response receipt, decoding, and safe failure categories.
- Added W3C trace-context propagation plus global or per-client tracer-provider configuration.
- Kept request bodies, credentials, resource identifiers, dynamic URLs, and exception details out of telemetry.

## [6.0.0] - 2026-09-03

- Breaking: moved wallet-specific types into `inttegro.wallets`.
- Breaking: moved financial-account bank types into `inttegro.bank_accounts`.
- Kept financial-account lifecycle requests in `inttegro.financial_accounts`.
- Added a typed `bank_accounts.GhanaBankAccountParams` request dataclass instead of exposing the nested bank payload as `Any`.

## [5.0.0] - 2026-09-03

- Breaking: made the catch-all enum implementation private and removed `WireEnum` from the public API.
- Re-exported enum types from their owning domain modules, including `payments`, `chimes`, `orders`, and `products`.

- Normalize legacy uppercase currency values when decoding typed amount responses while keeping lowercase wire values for requests.

## [4.0.0] - 2026-09-03

- Breaking: renamed order-prefixed payment models to semantic `Payment`, `PaymentAttempt`, `PaymentMethodSnapshot`, and `PaymentPayoutConfiguration` types.
- Added focused `inttegro.payments`, `inttegro.chimes`, and `inttegro.money` modules for related domain and request objects.
- Separated request and response amount and price dataclasses while preserving typed dictionary serialization at the transport boundary.

## [3.0.1] - 2026-09-03

- Corrected README examples and terminology to show direct domain return values.

## [3.0.0] - 2026-09-03

- Breaking: every documented resource method now returns an immutable domain dataclass or page directly.
- Internalized the dynamic fallback value and removed the public response wrapper module.
- Renamed `PaymentResponseStatus` to `PaymentResultStatus`.

## [2.1.0] - 2026-09-03

- Replaced dictionary-shaped request contracts with immutable, keyword-only request dataclasses.
- Added resource request namespaces such as `inttegro.orders.CreateRequest` and recursively serialize nested request objects.
- Preserved dictionary payload support for backwards compatibility.

## [2.0.0] - 2026-09-02

- Made the generated model module private; public types are imported directly from `inttegro`.
- Added OpenAPI-generated immutable dataclass response models and typed nested fields.
- Added generated `TypedDict` request contracts and endpoint-specific resource return types.
- Added PEP 561 package metadata plus strict mypy and Pyright checks in CI.
- Preserved attribute access, mapping access, `to_dict()`, and unknown response fields.

## [1.0.0] - 2026-09-01

- Breaking: renamed the distribution, import package, client, and base exception to `inttegro`, `InttegroClient`, and `InttegroError`.
- Aligned package metadata, examples, and the transport user agent with the public Inttegro service name.
