# Inttegro Python SDK

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/inttegro/inttegro-sdk-python/badge)](https://scorecard.dev/viewer/?uri=github.com/inttegro/inttegro-sdk-python)

The official Python client for building server-side Inttegro integrations, with
native asynchronous and synchronous clients.

[API documentation](https://python.inttegro.dev/) · [Integration guides](https://studio.inttegro.com/sdks/python)

> **Fastest, most modern path:** connect an agent to [Inttegro MCP](https://studio.inttegro.com/inttegro-mcp) at `https://mcp.inttegro.com`, then ask it to run `design_integration`. It will produce an implementation and test plan for your application. Use this SDK when you are ready to connect that plan to your Python service.

All official Inttegro SDKs expose the same API capabilities. This package adds Python-specific data access, transports, and test seams.

## Install

Requires Python 3.10 or newer.

```bash
pip install inttegro
```

Store your secret key in the server environment:

```bash
export INTTEGRO_API_KEY="your_secret_key"
```

Never put the key in browser code, a mobile app, or source control. The client uses `https://api.inttegro.com` by default.

## Choose a client

`AsyncInttegroClient` is the default shown in new integration examples. Use it
in FastAPI, Starlette, Quart, async Django views,
Python Workers, and other event-loop applications. Its HTTP requests are
non-blocking and share one connection pool:

```python
import os

from inttegro import AsyncInttegroClient

async with AsyncInttegroClient(api_key=os.environ["INTTEGRO_API_KEY"]) as client:
    order = await client.orders.lookup("or_...")
```

Create one long-lived client during application startup and call `aclose()`
during shutdown. An `async with` block is useful for scripts and jobs. Every
resource operation on the async client is awaited.

Use `InttegroClient` in synchronous Django views, Flask, command-line tools, or
other code without an event loop:

```python
import os

from inttegro import InttegroClient

client = InttegroClient(api_key=os.environ["INTTEGRO_API_KEY"])
order = client.orders.lookup("or_...")
```

The two clients expose the same resources, request types, returned domain
models, errors, idempotency behavior, and telemetry contract. Do not call the
synchronous client directly from an async request handler because it blocks
the event loop. The distinct class names make the concurrency model explicit:
choose `AsyncInttegroClient` for an event loop and `InttegroClient` for a
genuinely synchronous application.

## Create a hosted checkout

Create and finalize an order, then send the customer to its hosted invoice URL:

```python
import os

import inttegro
from inttegro import APIError, customer, money, order, price, product

async def create_checkout() -> str:
    request = order.CreateNewCustomerInput(
        request_meta=order.CreateNewCustomerInputRequestMeta(
            idempotency_key="checkout-cart-123",
        ),
        customer_data=customer.DataInput(
            name="Akua Mensah",
            email_address="akua@example.com",
            phone_number="+233544998605",
        ),
        finalize=True,
        checkout_settings=order.CreateNewCustomerInputCheckoutSettings(
            redirect_url="https://example.com/orders/complete",
            cancel_url="https://example.com/cart",
        ),
        line_items=[
            product.LineItemInput(
                type=order.LineItemType.PRODUCT,
                product=product.InlineDetailsInput(
                    type=product.Type.DIGITAL,
                    name="Monthly subscription",
                    quantity=1,
                    price=price.InlineParams(currency=money.Currency.GHS, value=5000),
                ),
            ),
        ],
    )
    try:
        async with inttegro.AsyncInttegroClient(
            api_key=os.environ["INTTEGRO_API_KEY"],
        ) as client:
            order = await client.orders.create(request)
            return order.invoice.format.web.url
    except APIError as error:
        print(error.code, error.detail or str(error))
        raise
```

Amounts use integer minor units: `5000` GHS is GHS 50.00. Reuse the same idempotency key when retrying the same logical write. If you omit one, the SDK generates a UUIDv7 key for mutating calls.

## Observe SDK operations

The SDK emits vendor-neutral OpenTelemetry spans through your application's provider. It never configures an exporter or sends telemetry by itself. Configure OpenTelemetry at application startup; the global provider is used automatically, or pass `tracer_provider` explicitly:

```python
client = inttegro.AsyncInttegroClient(
    api_key=os.environ["INTTEGRO_API_KEY"],
    tracer_provider=tracer_provider,
)
```

Spans are named after logical operations such as `inttegro.orders.create`. HTTP attempts, response receipt, and decoding are span events. API keys, bodies, resource IDs, dynamic URLs, and exception messages are never recorded. See [SDK observability](https://studio.inttegro.com/sdk-observability) for the complete contract and set `telemetry_enabled=False` when needed.

### Report SDK failures

Provide an application-owned reporter to receive one immutable, typed, privacy-safe report after an SDK operation finally fails. The default `"unexpected"` policy reports transport, timeout, decoding, SDK, `unknown_error`, and server-side failures while leaving normal 4xx API errors alone:

```python
client = inttegro.InttegroClient(
    api_key=os.environ["INTTEGRO_API_KEY"],
    error_reporter=error_collector.enqueue,
)
```

Use `error_reporting_policy="all"` to include expected API failures; cancellations are never reported. Call `report.to_dict()` when a collector needs a JSON-serializable value. Reports contain the logical operation, static route, server host, status and request IDs when available, duration, safe API error codes, SDK identity, stable fingerprint, exception type, and trace IDs when tracing is active. They exclude credentials, headers, bodies, resource IDs, dynamic URLs, exception messages, and stack traces. Reporter failures are isolated and the original SDK error is still raised.

Error reporting is completely opt-in. Without `error_reporter`, the SDK does not calculate report metadata, create an event ID or timestamp, allocate a report, or serialize a payload.

## Work with the API

The SDK covers orders and checkout, customers, products and prices, purchase intents, payment methods, balances, payouts and refunds, notifications, files, application settings, keys, and country specifications. Resources use snake-case attributes such as `purchase_intents` and `payment_methods`.

Python-specific features:

- Native async HTTP transport powered by HTTPX, plus a dependency-light synchronous standard-library transport.
- OpenAPI-generated, immutable request and domain dataclasses with fully typed nested fields.
- Singular resource namespaces keep the public API navigable: `inttegro.product.Product`, `inttegro.payment.Payment`, and `inttegro.order.CreateRequest`.
- Mapping-style lookup and `to_dict()` conversion on every returned domain object.
- Dictionary request payloads remain available when an integration cannot construct typed request objects.
- JSON-compatible string enums for public API values.
- Configurable timeout, base URL, and injectable transport for tests or custom networking.
- Structured authentication, rate-limit, network, timeout, and API exceptions.

The namespace name identifies the resource and its same-named class is the
primary returned object. Related request objects, nested shapes, and enums live
beside it, so editors and code-reading agents can discover the full surface
without searching a monolithic model module:

```python
from inttegro import payment, product

def summarize(value: payment.Payment) -> str:
    if value.requires_action():
        return "customer action required"
    return f"{value.status}: {value.amount.value} {value.amount.currency.value.upper()}"

item: product.Product
```

Request and returned domain fields are available to editors, Pyright, and mypy without plugins:

```python
import os

import inttegro
from inttegro import money, refund

client = inttegro.AsyncInttegroClient(api_key=os.environ["INTTEGRO_API_KEY"])

request = refund.CreateRequest(
    order_id="or_0123456789abcdefghijklmnopqrstuvwxyzABCD",
    reason=refund.Reason.REQUESTED_BY_CUSTOMER,
    line_items=[
        refund.CreateLineItemInput(
            order_line_item_id="oli_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN",
            refund_amount=money.AmountParams(currency=money.Currency.GHS, value=2500),
        ),
    ],
)

created_refund: refund.Refund = await client.refunds.create(request)
print(created_refund.id, created_refund.total.value)
```

See the [API reference](https://studio.inttegro.com/api-reference) for request fields and lifecycle rules, [errors](https://studio.inttegro.com/errors) for recovery guidance, and [idempotency](https://studio.inttegro.com/idempotency) for safe retries.

## Verify a release

The GitHub release for each version is the canonical record. It contains the exact wheel and source distribution uploaded to PyPI, SHA-256 checksums, and a Sigstore attestation tied to the source commit and release workflow.

```bash
sha256sum --check SHA256SUMS
gh attestation verify inttegro-7.0.0-py3-none-any.whl \
  --repo inttegro/inttegro-sdk-python
```

## Develop

```bash
poetry install
poetry run python scripts/generate_async_resources.py --check
poetry run python -m unittest discover -s tests -p "test_*.py"
poetry run mypy src
poetry run pyright
```
