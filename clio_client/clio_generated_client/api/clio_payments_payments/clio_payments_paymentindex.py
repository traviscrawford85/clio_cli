from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clio_payments_payment_list import ClioPaymentsPaymentList
from ...models.clio_payments_paymentindex_state import ClioPaymentsPaymentindexState
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bill_id: Union[Unset, int] = UNSET,
    contact_id: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    state: Union[Unset, ClioPaymentsPaymentindexState] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["bill_id"] = bill_id

    params["contact_id"] = contact_id

    params["fields"] = fields

    params["ids[]"] = ids

    params["limit"] = limit

    params["page_token"] = page_token

    json_state: Union[Unset, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clio_payments/payments",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClioPaymentsPaymentList, Error]]:
    if response.status_code == 200:
        response_200 = ClioPaymentsPaymentList.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ClioPaymentsPaymentList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    bill_id: Union[Unset, int] = UNSET,
    contact_id: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    state: Union[Unset, ClioPaymentsPaymentindexState] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[ClioPaymentsPaymentList, Error]]:
    """Return the data for all ClioPaymentsPayments

     Outlines the parameters, optional and required, used when requesting the data for all
    ClioPaymentsPayments

    Args:
        bill_id (Union[Unset, int]):
        contact_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        state (Union[Unset, ClioPaymentsPaymentindexState]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClioPaymentsPaymentList, Error]]
    """

    kwargs = _get_kwargs(
        bill_id=bill_id,
        contact_id=contact_id,
        fields=fields,
        ids=ids,
        limit=limit,
        page_token=page_token,
        state=state,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    bill_id: Union[Unset, int] = UNSET,
    contact_id: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    state: Union[Unset, ClioPaymentsPaymentindexState] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ClioPaymentsPaymentList, Error]]:
    """Return the data for all ClioPaymentsPayments

     Outlines the parameters, optional and required, used when requesting the data for all
    ClioPaymentsPayments

    Args:
        bill_id (Union[Unset, int]):
        contact_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        state (Union[Unset, ClioPaymentsPaymentindexState]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClioPaymentsPaymentList, Error]
    """

    return sync_detailed(
        client=client,
        bill_id=bill_id,
        contact_id=contact_id,
        fields=fields,
        ids=ids,
        limit=limit,
        page_token=page_token,
        state=state,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    bill_id: Union[Unset, int] = UNSET,
    contact_id: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    state: Union[Unset, ClioPaymentsPaymentindexState] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[ClioPaymentsPaymentList, Error]]:
    """Return the data for all ClioPaymentsPayments

     Outlines the parameters, optional and required, used when requesting the data for all
    ClioPaymentsPayments

    Args:
        bill_id (Union[Unset, int]):
        contact_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        state (Union[Unset, ClioPaymentsPaymentindexState]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClioPaymentsPaymentList, Error]]
    """

    kwargs = _get_kwargs(
        bill_id=bill_id,
        contact_id=contact_id,
        fields=fields,
        ids=ids,
        limit=limit,
        page_token=page_token,
        state=state,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    bill_id: Union[Unset, int] = UNSET,
    contact_id: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    state: Union[Unset, ClioPaymentsPaymentindexState] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ClioPaymentsPaymentList, Error]]:
    """Return the data for all ClioPaymentsPayments

     Outlines the parameters, optional and required, used when requesting the data for all
    ClioPaymentsPayments

    Args:
        bill_id (Union[Unset, int]):
        contact_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        state (Union[Unset, ClioPaymentsPaymentindexState]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClioPaymentsPaymentList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            bill_id=bill_id,
            contact_id=contact_id,
            fields=fields,
            ids=ids,
            limit=limit,
            page_token=page_token,
            state=state,
            x_api_version=x_api_version,
        )
    ).parsed
