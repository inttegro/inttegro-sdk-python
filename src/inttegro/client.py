from __future__ import annotations

from typing import TYPE_CHECKING

from .http_client import HttpClient, Transport
from .resources.balance_transactions import BalanceTransactions
from .resources.chimes import Chimes
from .resources.customers import Customers
from .resources.schedules import Schedules
from .resources.broadcasts import Broadcasts
from .resources.message_templates import MessageTemplates
from .resources.financial_accounts import FinancialAccounts
from .resources.files import Files
from .resources.file_links import FileLinks
from .resources.file_references import FileReferences
from .resources.keys import Keys
from .resources.otp import Otp
from .resources.orders import Orders
from .resources.payment_methods import PaymentMethods
from .resources.payouts import Payouts
from .resources.products import Products
from .resources.prices import Prices
from .resources.purchase_intents import PurchaseIntents
from .resources.refunds import Refunds
from .resources.spec import Spec
from .resources.balances import Balances
from .resources.upload_requests import UploadRequests
from .resources.apps import Apps
from .resources.children_policies import ChildrenPolicies
from .resources.operating_policies import OperatingPolicies
from .error_reporting import ErrorReporter, ErrorReportingPolicy

if TYPE_CHECKING:
    from opentelemetry.trace import TracerProvider


class InttegroClient:
    """
    Main SDK client for the Inttegro API.

    The Inttegro client provides access to all API resources including orders,
    payment methods, payouts, financial accounts, and more. Initialize with
    your API key from the Inttegro dashboard.

    Attributes:
        orders: Orders resource for creating and managing orders, processing payments
        payment_methods: Payment methods resource for tokenizing and managing payment instruments
        payouts: Payouts resource for scheduling and managing fund transfers
        balance_transactions: Balance transactions resource for viewing account activity
        financial_accounts: Financial accounts resource for connecting bank and mobile money accounts
        customers: Customers resource for creating and managing customers
        products: Products resource for managing catalog products
        prices: Prices resource for managing catalog prices
        refunds: Refunds resource for creating and managing refunds
        chimes: Chimes resource for sending transactional notifications
        schedules: Schedules resource for looking up and canceling scheduled chimes
        broadcasts: Broadcasts resource for looking up and canceling broadcasts
        otp: OTP resource for one-time password verification
        apps: Apps resource for creating, looking up, and updating applications
        spec: Spec resource for retrieving supported countries and currencies

    Example:
        ```python
        import os
        from inttegro import InttegroClient

        # Initialize client with API key
        client = InttegroClient(api_key=os.environ["INTTEGRO_API_KEY"])

        # Create and process an order
        result = client.orders.create({
            "customer_data": {
                "name": "Akua Asantewaa",
                "phone_number": "+233541234567",
                "email_address": "akua@example.com"
            },
            "line_items": [{
                "type": "product",
                "product": {
                    "type": "digital",
                    "name": "Premium Subscription",
                    "quantity": 1,
                    "price": {"currency": "ghs", "value": 5000}
                }
            }],
            "billing_details": {
                "name": "Akua Asantewaa",
                "phone_number": "+233541234567"
            },
            "execute_payment": True
        })
        ```

    Thread Safety:
        The client is thread-safe after initialization and can be safely shared
        across multiple threads.
    """

    http: HttpClient
    orders: Orders
    payment_methods: PaymentMethods
    payouts: Payouts
    balance_transactions: BalanceTransactions
    financial_accounts: FinancialAccounts
    files: Files
    file_links: FileLinks
    file_references: FileReferences
    customers: Customers
    products: Products
    prices: Prices
    purchase_intents: PurchaseIntents
    refunds: Refunds
    chimes: Chimes
    schedules: Schedules
    broadcasts: Broadcasts
    message_templates: MessageTemplates
    otp: Otp
    apps: Apps
    keys: Keys
    spec: Spec
    balances: Balances
    upload_requests: UploadRequests
    children_policies: ChildrenPolicies
    operating_policies: OperatingPolicies

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.inttegro.com",
        timeout: float = 30.0,
        transport: Transport | None = None,
        telemetry_enabled: bool = True,
        tracer_provider: TracerProvider | None = None,
        error_reporter: ErrorReporter | None = None,
        error_reporting_policy: ErrorReportingPolicy = "unexpected",
    ) -> None:
        """
        Initialize a new Inttegro client.

        Args:
            api_key: Your Inttegro API key (required). Get this from your dashboard
                at https://studio.inttegro.com/settings/keys. Use test keys (sk_test_...)
                for development and live keys (sk_live_...) for production.
            base_url: API base URL. Defaults to production (https://api.inttegro.com).
                Override for testing or staging environments.
            timeout: Request timeout in seconds. Defaults to 30.0. Increase for
                long-running operations or slow networks.
            transport: Custom HTTP transport adapter. Pass a requests.Session or
                custom transport for connection pooling, retries, or proxies.
            telemetry_enabled: Emit spans to the configured OpenTelemetry provider.
                Defaults to True. The SDK never configures an exporter.
            tracer_provider: Optional OpenTelemetry tracer provider override.
            error_reporter: Optional application-owned callback for privacy-safe final-failure reports.
            error_reporting_policy: Report unexpected failures by default, or use ``"all"``.

        Raises:
            ValueError: If api_key is empty or invalid

        Example:
            ```python
            # Production usage
            client = InttegroClient(api_key="sk_live_...")

            # Development with custom timeout
            client = InttegroClient(
                api_key="sk_test_...",
                timeout=60.0
            )

            # Testing with mock server
            client = InttegroClient(
                api_key="sk_test_...",
                base_url="http://localhost:8080"
            )
            ```
        """
        self.http = HttpClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            transport=transport,
            telemetry_enabled=telemetry_enabled,
            tracer_provider=tracer_provider,
            error_reporter=error_reporter,
            error_reporting_policy=error_reporting_policy,
        )

        self.orders = Orders(self.http)
        self.payment_methods = PaymentMethods(self.http)
        self.payouts = Payouts(self.http)
        self.balance_transactions = BalanceTransactions(self.http)
        self.financial_accounts = FinancialAccounts(self.http)
        self.files = Files(self.http)
        self.file_links = FileLinks(self.http)
        self.file_references = FileReferences(self.http)
        self.customers = Customers(self.http)
        self.products = Products(self.http)
        self.prices = Prices(self.http)
        self.purchase_intents = PurchaseIntents(self.http)
        self.refunds = Refunds(self.http)
        self.chimes = Chimes(self.http)
        self.schedules = Schedules(self.http)
        self.broadcasts = Broadcasts(self.http)
        self.message_templates = MessageTemplates(self.http)
        self.otp = Otp(self.http)
        self.apps = Apps(self.http)
        self.keys = Keys(self.http)
        self.spec = Spec(self.http)
        self.balances = Balances(self.http)
        self.upload_requests = UploadRequests(self.http)
        self.children_policies = ChildrenPolicies(self.http)
        self.operating_policies = OperatingPolicies(self.http)
