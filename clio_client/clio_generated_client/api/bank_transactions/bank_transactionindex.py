import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bank_transaction_list import BankTransactionList
from ...models.bank_transactionindex_type import BankTransactionindexType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bank_account_id: Union[Unset, int] = UNSET,
    client_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    type_: Union[Unset, BankTransactionindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["bank_account_id"] = bank_account_id

    params["client_id"] = client_id

    json_created_since: Union[Unset, str] = UNSET
    if not isinstance(created_since, Unset):
        json_created_since = created_since.isoformat()
    params["created_since"] = json_created_since

    params["fields"] = fields

    params["ids[]"] = ids

    params["limit"] = limit

    params["matter_id"] = matter_id

    params["order"] = order

    params["page_token"] = page_token

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/bank_transactions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BankTransactionList, Error]]:
    if response.status_code == 200:
        response_200 = BankTransactionList.from_dict(response.json())

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
) -> Response[Union[BankTransactionList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    bank_account_id: Union[Unset, int] = UNSET,
    client_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    type_: Union[Unset, BankTransactionindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[BankTransactionList, Error]]:
    """Return the data for all BankTransactions

     Outlines the parameters, optional and required, used when requesting the data for all
    BankTransactions

    Args:
        bank_account_id (Union[Unset, int]):
        client_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, str]):
        page_token (Union[Unset, str]):
        type_ (Union[Unset, BankTransactionindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BankTransactionList, Error]]
    """

    kwargs = _get_kwargs(
        bank_account_id=bank_account_id,
        client_id=client_id,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        type_=type_,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    bank_account_id: Union[Unset, int] = UNSET,
    client_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    type_: Union[Unset, BankTransactionindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[BankTransactionList, Error]]:
    """Return the data for all BankTransactions

     Outlines the parameters, optional and required, used when requesting the data for all
    BankTransactions

    Args:
        bank_account_id (Union[Unset, int]):
        client_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, str]):
        page_token (Union[Unset, str]):
        type_ (Union[Unset, BankTransactionindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BankTransactionList, Error]
    """

    return sync_detailed(
        client=client,
        bank_account_id=bank_account_id,
        client_id=client_id,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        type_=type_,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    bank_account_id: Union[Unset, int] = UNSET,
    client_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    type_: Union[Unset, BankTransactionindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[BankTransactionList, Error]]:
    """Return the data for all BankTransactions

     Outlines the parameters, optional and required, used when requesting the data for all
    BankTransactions

    Args:
        bank_account_id (Union[Unset, int]):
        client_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, str]):
        page_token (Union[Unset, str]):
        type_ (Union[Unset, BankTransactionindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BankTransactionList, Error]]
    """

    kwargs = _get_kwargs(
        bank_account_id=bank_account_id,
        client_id=client_id,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        type_=type_,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    bank_account_id: Union[Unset, int] = UNSET,
    client_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    type_: Union[Unset, BankTransactionindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[BankTransactionList, Error]]:
    """Return the data for all BankTransactions

     Outlines the parameters, optional and required, used when requesting the data for all
    BankTransactions

    Args:
        bank_account_id (Union[Unset, int]):
        client_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, str]):
        page_token (Union[Unset, str]):
        type_ (Union[Unset, BankTransactionindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BankTransactionList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            bank_account_id=bank_account_id,
            client_id=client_id,
            created_since=created_since,
            fields=fields,
            ids=ids,
            limit=limit,
            matter_id=matter_id,
            order=order,
            page_token=page_token,
            type_=type_,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
