"""Financial accounts resource for connecting payout destinations."""

from __future__ import annotations

from ..http_client import HttpClient
from inttegro.search import Page as SearchPage, Request as SearchRequest


class FinancialAccounts:
    """
    Financial accounts resource for connecting and managing payout destinations.

    Financial accounts represent bank accounts, mobile money wallets, or Dosh accounts
    where you receive payouts. Before you can receive funds from Inttegro, you must connect
    and verify at least one financial account, then configure it as a payout destination.

    The typical flow is:
    1. Connect a financial account (bank_account, mobile money, or dosh_account)
    2. Verify ownership via OTP
    3. Set as payout destination via Payouts resource
    4. Receive automatic or manual payouts

    See https://studio.inttegro.com/set-up-financial-account for detailed guides.
    """

    def __init__(self, http: HttpClient):
        """Initialize FinancialAccounts resource with HTTP client."""
        self.http = http

    def create(self, payload: dict):
        """
        Create a new financial account.

        Args:
            payload: Account creation parameters

        Returns:
            domain object with created financial account

        """
        return self.http.post("/financial_accounts/create", payload)

    def lookup(self, account_id: str):
        """
        Retrieve details of a financial account.

        Fetches information about a connected financial account including its type,
        verification status, and masked details.

        Args:
            account_id: The financial account ID (e.g., "fa_abc123")

        Returns:
            domain object containing the financial_account object

        Example:
            ```python
            result = client.financial_accounts.lookup("fa_abc123")
            account = result
            print(f"Type: {account['type']}, Verified: {account['verified']}")
            ```

        See Also:
            - connect(): Add new financial accounts
            - page(): List all financial accounts
        """
        return self.http.post("/financial_accounts/lookup", {"account_id": account_id})

    def connect(self, payload: dict):
        """
        Connect a new financial account for receiving payouts.

        Adds a bank account, mobile money wallet, or Dosh account as a payout destination.
        Financial accounts must include basic information like label, type, currency, and
        type-specific configuration. Most account types require verification before they
        can receive funds.

        Args:
            payload: Connection parameters including:
                - label: Account label (5-40 characters) (required)
                - type: Account type ("wallet", "bank_account", or "dosh_account") (required)
                - reference: External reference ID (5-40 characters) (required)
                - currency: Account currency (currently only "ghs" supported) (required)
                - description: Optional account description (0-200 characters)
                - owner: Account owner information (required):
                    - name: Owner full name
                    - address: Owner address details (name, line_1, city, region, country)
                - wallet: Wallet configuration (required if type is "wallet"):
                    - type: "mobile_money"
                    - mobile_money:
                        - account_number: Phone number (e.g., "0241234567")
                        - network: Network operator ("mtn", "vodafone", "airteltigo")
                - bank_account: Bank account configuration (required if type is "bank_account"):
                    - type: "ghana_bank_account"
                    - ghana_bank_account:
                        - number: Bank account number
                        - sort_code: Bank sort code (required if swift_code is not provided)
                        - swift_code: Bank SWIFT/BIC code (required if sort_code is not provided)
                        - holder:
                            - name: Account holder full name
                            - address:
                                - name: Address label
                                - line_1: Address line 1
                                - city: City or town
                                - region: Region or state
                                - country: Country code or name
                - push_configuration: Configuration for sending funds to this account:
                    - enabled: Whether payouts to this account are enabled (default: true)
                - pull_configuration: Configuration for collecting funds from this account:
                    - enabled: Whether pulling funds is enabled (default: false)
                    - mandate: Optional mandate parameters (created automatically using request metadata)
                - custom_data: Optional key-value metadata (string-to-string)

        Returns:
            domain object containing:
                - financial_account: Created financial account with id, type, status, etc.
                - requires_verification: Whether verification is needed before use

        Raises:
            ApiError: If parameters are invalid or connection fails

        Example:
            ```python
            # Connect mobile money wallet
            result = client.financial_accounts.connect({
                "type": "wallet",
                "currency": "ghs",
                "label": "Primary MTN Wallet",
                "description": "Main business mobile money account",
                "reference": "WALLET-MTN-001",
                "wallet": {
                    "type": "mobile_money",
                    "mobile_money": {
                        "account_number": "0241234567",
                        "network": "mtn"
                    }
                },
                "push_configuration": {
                    "enabled": True
                }
            })

            fa = result
            print(f"Financial account created: {fa['id']}")

            # Verify if needed
            if result.verification is not None:
                # Initiate verification (sends OTP)
                client.financial_accounts.verify({"account_id": fa["id"]})

                # Collect OTP from user
                otp = input("Enter OTP: ")

                # Complete verification
                client.financial_accounts.verify({
                    "account_id": fa["id"],
                    "token": otp
                })

            # Connect Vodafone wallet
            result = client.financial_accounts.connect({
                "type": "wallet",
                "currency": "ghs",
                "label": "Vodafone Cash Account",
                "reference": "WALLET-VDF-001",
                "wallet": {
                    "type": "mobile_money",
                    "mobile_money": {
                        "account_number": "0501234567",
                        "network": "vodafone"
                    }
                },
                "push_configuration": {"enabled": True}
            })
            ```

        Note:
            - Financial accounts must be verified before they can receive payouts
            - Only "ghs" currency is currently supported
            - Dosh account types are placeholders for future functionality

        See Also:
            - verify(): Verify ownership of financial account
            - Payouts.set_destinations(): Configure account as payout destination
            - https://studio.inttegro.com/set-up-financial-account
        """
        return self.http.post("/financial_accounts/connect", payload)

    def archive(self, payload: dict):
        """
        Archive a financial account to prevent future use.

        Archives a financial account, marking it inactive. Archived accounts cannot be
        used as payout destinations but remain in your account history.

        Args:
            payload: Archive parameters including account_id

        Returns:
            domain object containing the archived financial_account

        Example:
            ```python
            result = client.financial_accounts.archive({"account_id": "fa_abc123"})
            ```

        See Also:
            - connect(): Add replacement financial account
        """
        return self.http.post("/financial_accounts/archive", payload)

    def page(self, payload: dict | None = None):
        """
        List connected financial accounts with pagination and filtering.

        Retrieves a paginated list of your financial accounts with optional filtering
        by type and status.

        Args:
            payload: Optional pagination parameters and filters

        Returns:
            domain object containing data (list of accounts), has_more, and count

        Example:
            ```python
            result = client.financial_accounts.page({"limit": 20, "status": "active"})
            ```

        See Also:
            - connect(): Add new financial accounts
        """
        return self.http.post("/financial_accounts/page", payload or {})

    def search(self, payload: SearchRequest) -> SearchPage:
        """Search financial-account projections owned by the authenticated application."""
        return self.http.post("/financial_accounts/search", payload)

    def verify(self, payload: dict):
        """
        Initiate or complete verification of a financial account.

        Verification confirms ownership of the financial account. For mobile money, this
        sends an OTP that must be submitted to complete verification.

        Args:
            payload: Verification parameters including account_id and optionally token

        Returns:
            domain object containing the financial_account with updated verification status

        Example:
            ```python
            # Initiate verification
            client.financial_accounts.verify({"account_id": "fa_abc123"})
            # Complete verification
            result = client.financial_accounts.verify({
                "account_id": "fa_abc123",
                "token": "123456"
            })
            ```

        See Also:
            - connect(): Add financial accounts that need verification
        """
        return self.http.post("/financial_accounts/verify", payload)

    def update(self, payload: dict):
        """
        Update a financial account (PATCH semantics).

        All fields except account_id are optional. custom_data merges with existing data; null deletes keys.

        Args:
            payload: Update parameters including account_id and fields to change

        Returns:
            domain object containing the updated financial_account
        """
        return self.http.post("/financial_accounts/update", payload)

    def enable_push(self, account_id: str):
        """Enable push configuration for payouts.

        API endpoint: ``/financial_accounts/enable_push``.

        Args:
            account_id (str): Unique identifier of the account.

        Returns:
            ``FinancialAccount`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/financial_accounts/enable_push", {"account_id": account_id})

    def disable_push(self, account_id: str, unset_as_payout_destination: bool | None = None):
        """
        Disable push configuration for payouts.

        If the account is a payout destination, set unset_as_payout_destination to True to
        automatically remove it before disabling push.
        """
        payload = {"account_id": account_id}
        if unset_as_payout_destination is not None:
            payload["unset_as_payout_destination"] = unset_as_payout_destination
        return self.http.post("/financial_accounts/disable_push", payload)

    def disconnect(self, account_id: str, unset_as_payout_destination: bool | None = None):
        """
        Disconnect a financial account.

        If the account is a payout destination, set unset_as_payout_destination to True to
        automatically remove it before disconnecting.
        """
        payload = {"account_id": account_id}
        if unset_as_payout_destination is not None:
            payload["unset_as_payout_destination"] = unset_as_payout_destination
        return self.http.post("/financial_accounts/disconnect", payload)

    def reconnect(self, account_id: str):
        """
        Reconnect a previously disconnected financial account.

        Args:
            account_id: The financial account ID to reconnect.

        Returns:
            domain object containing the reconnected financial account.
        """
        return self.http.post("/financial_accounts/reconnect", {"account_id": account_id})

    def enable_pull(self, account_id: str):
        """Enable pull configuration for charges (creates mandate).

        API endpoint: ``/financial_accounts/enable_pull``.

        Args:
            account_id (str): Unique identifier of the account.

        Returns:
            ``FinancialAccount`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/financial_accounts/enable_pull", {"account_id": account_id})

    def disable_pull(self, account_id: str):
        """Disable pull configuration for charges.

        API endpoint: ``/financial_accounts/disable_pull``.

        Args:
            account_id (str): Unique identifier of the account.

        Returns:
            ``FinancialAccount`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/financial_accounts/disable_pull", {"account_id": account_id})
