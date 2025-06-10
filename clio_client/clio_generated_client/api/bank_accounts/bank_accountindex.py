import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bank_account_list import BankAccountList
from ...models.bank_accountindex_order import BankAccountindexOrder
from ...models.bank_accountindex_type import BankAccountindexType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, BankAccountindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    show_empty_accounts: Union[Unset, bool] = UNSET,
    type_: Union[Unset, BankAccountindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    json_created_since: Union[Unset, str] = UNSET
    if not isinstance(created_since, Unset):
        json_created_since = created_since.isoformat()
    params["created_since"] = json_created_since

    params["fields"] = fields

    params["ids[]"] = ids

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["show_empty_accounts"] = show_empty_accounts

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/bank_accounts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BankAccountList, Error]]:
    if response.status_code == 200:
        response_200 = BankAccountList.from_dict(response.json())

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
) -> Response[Union[BankAccountList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, BankAccountindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    show_empty_accounts: Union[Unset, bool] = UNSET,
    type_: Union[Unset, BankAccountindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[BankAccountList, Error]]:
    """Return the data for all BankAccounts

     Outlines the parameters, optional and required, used when requesting the data for all BankAccounts

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, BankAccountindexOrder]):
        page_token (Union[Unset, str]):
        show_empty_accounts (Union[Unset, bool]):
        type_ (Union[Unset, BankAccountindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BankAccountList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        show_empty_accounts=show_empty_accounts,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, BankAccountindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    show_empty_accounts: Union[Unset, bool] = UNSET,
    type_: Union[Unset, BankAccountindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[BankAccountList, Error]]:
    """Return the data for all BankAccounts

     Outlines the parameters, optional and required, used when requesting the data for all BankAccounts

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, BankAccountindexOrder]):
        page_token (Union[Unset, str]):
        show_empty_accounts (Union[Unset, bool]):
        type_ (Union[Unset, BankAccountindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BankAccountList, Error]
    """

    return sync_detailed(
        client=client,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        show_empty_accounts=show_empty_accounts,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, BankAccountindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    show_empty_accounts: Union[Unset, bool] = UNSET,
    type_: Union[Unset, BankAccountindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[BankAccountList, Error]]:
    """Return the data for all BankAccounts

     Outlines the parameters, optional and required, used when requesting the data for all BankAccounts

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, BankAccountindexOrder]):
        page_token (Union[Unset, str]):
        show_empty_accounts (Union[Unset, bool]):
        type_ (Union[Unset, BankAccountindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BankAccountList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        show_empty_accounts=show_empty_accounts,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, BankAccountindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    show_empty_accounts: Union[Unset, bool] = UNSET,
    type_: Union[Unset, BankAccountindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[BankAccountList, Error]]:
    """Return the data for all BankAccounts

     Outlines the parameters, optional and required, used when requesting the data for all BankAccounts

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, BankAccountindexOrder]):
        page_token (Union[Unset, str]):
        show_empty_accounts (Union[Unset, bool]):
        type_ (Union[Unset, BankAccountindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BankAccountList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_since=created_since,
            fields=fields,
            ids=ids,
            limit=limit,
            order=order,
            page_token=page_token,
            show_empty_accounts=show_empty_accounts,
            type_=type_,
            updated_since=updated_since,
            user_id=user_id,
            x_api_version=x_api_version,
        )
    ).parsed
