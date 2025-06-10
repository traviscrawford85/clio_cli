import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.group_list import GroupList
from ...models.groupindex_order import GroupindexOrder
from ...models.groupindex_type import GroupindexType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: Union[Unset, bool] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    order: Union[Unset, GroupindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    type_: Union[Unset, GroupindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["archived"] = archived

    json_created_since: Union[Unset, str] = UNSET
    if not isinstance(created_since, Unset):
        json_created_since = created_since.isoformat()
    params["created_since"] = json_created_since

    params["fields"] = fields

    params["ids[]"] = ids

    params["limit"] = limit

    params["name"] = name

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["query"] = query

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
        "url": "/groups",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, GroupList]]:
    if response.status_code == 200:
        response_200 = GroupList.from_dict(response.json())

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
) -> Response[Union[Error, GroupList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    archived: Union[Unset, bool] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    order: Union[Unset, GroupindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    type_: Union[Unset, GroupindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, GroupList]]:
    """Return the data for all Groups

     Outlines the parameters, optional and required, used when requesting the data for all Groups

    Args:
        archived (Union[Unset, bool]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, GroupindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        type_ (Union[Unset, GroupindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GroupList]]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        name=name,
        order=order,
        page_token=page_token,
        query=query,
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
    archived: Union[Unset, bool] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    order: Union[Unset, GroupindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    type_: Union[Unset, GroupindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, GroupList]]:
    """Return the data for all Groups

     Outlines the parameters, optional and required, used when requesting the data for all Groups

    Args:
        archived (Union[Unset, bool]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, GroupindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        type_ (Union[Unset, GroupindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GroupList]
    """

    return sync_detailed(
        client=client,
        archived=archived,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        name=name,
        order=order,
        page_token=page_token,
        query=query,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    archived: Union[Unset, bool] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    order: Union[Unset, GroupindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    type_: Union[Unset, GroupindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, GroupList]]:
    """Return the data for all Groups

     Outlines the parameters, optional and required, used when requesting the data for all Groups

    Args:
        archived (Union[Unset, bool]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, GroupindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        type_ (Union[Unset, GroupindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GroupList]]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        name=name,
        order=order,
        page_token=page_token,
        query=query,
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
    archived: Union[Unset, bool] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    order: Union[Unset, GroupindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    type_: Union[Unset, GroupindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, GroupList]]:
    """Return the data for all Groups

     Outlines the parameters, optional and required, used when requesting the data for all Groups

    Args:
        archived (Union[Unset, bool]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, GroupindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        type_ (Union[Unset, GroupindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GroupList]
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            created_since=created_since,
            fields=fields,
            ids=ids,
            limit=limit,
            name=name,
            order=order,
            page_token=page_token,
            query=query,
            type_=type_,
            updated_since=updated_since,
            user_id=user_id,
            x_api_version=x_api_version,
        )
    ).parsed
