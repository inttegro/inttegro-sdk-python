import inttegro
from inttegro import (
    AsyncInttegroClient,
    CustomData,
    CustomDataInput,
    CustomDataPatch,
    InttegroClient,
)
from inttegro.refund import Refund


def custom_data(
    response: CustomData,
    request: CustomDataInput,
    patch: CustomDataPatch,
) -> None:
    return None


def refund(client: InttegroClient) -> tuple[str, int]:
    request = inttegro.refund.CreateRequest(
        order_id="or_0123456789abcdefghijklmnopqrstuvwxyzABCD",
        reason=inttegro.refund.Reason.REQUESTED_BY_CUSTOMER,
        line_items=[
            inttegro.refund.CreateLineItemInput(
                order_line_item_id="oli_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN",
                refund_amount=inttegro.money.AmountParams(
                    currency=inttegro.money.Currency.GHS,
                    value=2500,
                ),
            )
        ],
    )
    response: Refund = client.refunds.create(request)
    invalid_request = inttegro.refund.CreateRequest(  # type: ignore[call-arg]
        order_id="or_0123456789abcdefghijklmnopqrstuvwxyzABCD",
    )
    wrong_response: str = client.refunds.create(request)  # type: ignore[assignment]
    wrong_total: str = response.total.value  # type: ignore[assignment]
    del invalid_request, wrong_response, wrong_total
    return response.id, response.total.value


def create_order(client: InttegroClient) -> str:
    request = inttegro.order.CreateNewCustomerInput(
        customer_data=inttegro.customer.DataInput(
            name="Akua Mensah",
            email_address="akua@example.com",
            phone_number="+233544998605",
        ),
        payment_method_data=inttegro.payment_method.DataInput(
            type=inttegro.payment_method.Type.MOBILE_MONEY,
            mobile_money=inttegro.payment_method.DataInputMobileMoney(
                network=inttegro.payment_method.MobileMoneyNetwork.MTN,
                account_number="0544998605",
            ),
        ),
        line_items=[
            inttegro.product.LineItemInput(
                type=inttegro.order.LineItemType.PRODUCT,
                product=inttegro.product.InlineDetailsInput(
                    name="Monthly subscription",
                    price=inttegro.price.InlineParams(
                        currency=inttegro.money.Currency.GHS,
                        value=5000,
                    ),
                    quantity=1,
                    type=inttegro.product.Type.DIGITAL,
                ),
            )
        ],
    )
    return client.orders.create(request).id


async def create_order_async(client: AsyncInttegroClient) -> str:
    request = inttegro.order.CreateNewCustomerInput(
        customer_data=inttegro.customer.DataInput(
            name="Akua Mensah",
            email_address="akua@example.com",
            phone_number="+233544998605",
        ),
        line_items=[
            inttegro.product.LineItemInput(
                type=inttegro.order.LineItemType.PRODUCT,
                product=inttegro.product.InlineDetailsInput(
                    name="Monthly subscription",
                    price=inttegro.price.InlineParams(
                        currency=inttegro.money.Currency.GHS,
                        value=5000,
                    ),
                    quantity=1,
                    type=inttegro.product.Type.DIGITAL,
                ),
            )
        ],
    )
    return (await client.orders.create(request)).id
