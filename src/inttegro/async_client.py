from __future__ import annotations

from typing import TYPE_CHECKING

from .async_http_client import AsyncHTTPClient, AsyncHttpClient, AsyncTransport
from .async_resources.apps import AsyncApps
from .async_resources.children_policies import AsyncChildrenPolicies
from .async_resources.operating_policies import AsyncOperatingPolicies
from .async_resources.balance_transactions import AsyncBalanceTransactions
from .async_resources.balances import AsyncBalances
from .async_resources.broadcasts import AsyncBroadcasts
from .async_resources.chimes import AsyncChimes
from .async_resources.customers import AsyncCustomers
from .async_resources.file_links import AsyncFileLinks
from .async_resources.file_references import AsyncFileReferences
from .async_resources.files import AsyncFiles
from .async_resources.financial_accounts import AsyncFinancialAccounts
from .async_resources.keys import AsyncKeys
from .async_resources.message_templates import AsyncMessageTemplates
from .async_resources.orders import AsyncOrders
from .async_resources.otp import AsyncOtp
from .async_resources.payment_methods import AsyncPaymentMethods
from .async_resources.payouts import AsyncPayouts
from .async_resources.prices import AsyncPrices
from .async_resources.products import AsyncProducts
from .async_resources.purchase_intents import AsyncPurchaseIntents
from .async_resources.refunds import AsyncRefunds
from .async_resources.schedules import AsyncSchedules
from .async_resources.spec import AsyncSpec
from .async_resources.upload_requests import AsyncUploadRequests
from .error_reporting import ErrorReporter, ErrorReportingPolicy

if TYPE_CHECKING:
    from opentelemetry.trace import TracerProvider


class AsyncInttegroClient:
    """Asynchronous Inttegro API client for event-loop based applications.

    Use one long-lived client per application and close it during shutdown, or
    use ``async with`` for a bounded lifecycle. Every resource operation must
    be awaited. ``InttegroClient`` remains available for synchronous programs.

    Example::

        async with AsyncInttegroClient(api_key="sk_live_...") as client:
            order = await client.orders.create({...})
    """

    http: AsyncHttpClient
    orders: AsyncOrders
    payment_methods: AsyncPaymentMethods
    payouts: AsyncPayouts
    balance_transactions: AsyncBalanceTransactions
    financial_accounts: AsyncFinancialAccounts
    files: AsyncFiles
    file_links: AsyncFileLinks
    file_references: AsyncFileReferences
    customers: AsyncCustomers
    products: AsyncProducts
    prices: AsyncPrices
    purchase_intents: AsyncPurchaseIntents
    refunds: AsyncRefunds
    chimes: AsyncChimes
    schedules: AsyncSchedules
    broadcasts: AsyncBroadcasts
    message_templates: AsyncMessageTemplates
    otp: AsyncOtp
    apps: AsyncApps
    keys: AsyncKeys
    spec: AsyncSpec
    balances: AsyncBalances
    upload_requests: AsyncUploadRequests
    children_policies: AsyncChildrenPolicies
    operating_policies: AsyncOperatingPolicies

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.inttegro.com",
        timeout: float = 30.0,
        transport: AsyncTransport | None = None,
        telemetry_enabled: bool = True,
        tracer_provider: TracerProvider | None = None,
        error_reporter: ErrorReporter | None = None,
        error_reporting_policy: ErrorReportingPolicy = "unexpected",
        http_client: AsyncHTTPClient | None = None,
    ) -> None:
        """Initialize a non-blocking client and its shared connection pool.

        ``transport`` is the lightweight SDK test/adapter seam. Use
        ``http_client`` to supply an application-owned ``httpx.AsyncClient``
        with custom proxy, TLS, limits, or retry configuration. Do not pass
        both unless the transport deliberately replaces network I/O.
        """

        self.http = AsyncHttpClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            transport=transport,
            telemetry_enabled=telemetry_enabled,
            tracer_provider=tracer_provider,
            error_reporter=error_reporter,
            error_reporting_policy=error_reporting_policy,
            http_client=http_client,
        )
        self.orders = AsyncOrders(self.http)
        self.payment_methods = AsyncPaymentMethods(self.http)
        self.payouts = AsyncPayouts(self.http)
        self.balance_transactions = AsyncBalanceTransactions(self.http)
        self.financial_accounts = AsyncFinancialAccounts(self.http)
        self.files = AsyncFiles(self.http)
        self.file_links = AsyncFileLinks(self.http)
        self.file_references = AsyncFileReferences(self.http)
        self.customers = AsyncCustomers(self.http)
        self.products = AsyncProducts(self.http)
        self.prices = AsyncPrices(self.http)
        self.purchase_intents = AsyncPurchaseIntents(self.http)
        self.refunds = AsyncRefunds(self.http)
        self.chimes = AsyncChimes(self.http)
        self.schedules = AsyncSchedules(self.http)
        self.broadcasts = AsyncBroadcasts(self.http)
        self.message_templates = AsyncMessageTemplates(self.http)
        self.otp = AsyncOtp(self.http)
        self.apps = AsyncApps(self.http)
        self.keys = AsyncKeys(self.http)
        self.spec = AsyncSpec(self.http)
        self.balances = AsyncBalances(self.http)
        self.upload_requests = AsyncUploadRequests(self.http)
        self.children_policies = AsyncChildrenPolicies(self.http)
        self.operating_policies = AsyncOperatingPolicies(self.http)

    async def __aenter__(self) -> AsyncInttegroClient:
        return self

    async def __aexit__(self, exc_type: object, exc: object, traceback: object) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        """Close the SDK-owned connection pool."""

        await self.http.aclose()
