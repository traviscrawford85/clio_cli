import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.user_list import UserList
from ...models.userindex_order import UserindexOrder
from ...models.userindex_role import UserindexRole
from ...models.userindex_subscription_type import UserindexSubscriptionType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    include_co_counsel: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    order: Union[Unset, UserindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    pending_setup: Union[Unset, bool] = UNSET,
    role: Union[Unset, UserindexRole] = UNSET,
    subscription_type: Union[Unset, UserindexSubscriptionType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
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

    params["enabled"] = enabled

    params["fields"] = fields

    params["ids[]"] = ids

    params["include_co_counsel"] = include_co_counsel

    params["limit"] = limit

    params["name"] = name

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["pending_setup"] = pending_setup

    json_role: Union[Unset, str] = UNSET
    if not isinstance(role, Unset):
        json_role = role.value

    params["role"] = json_role

    json_subscription_type: Union[Unset, str] = UNSET
    if not isinstance(subscription_type, Unset):
        json_subscription_type = subscription_type.value

    params["subscription_type"] = json_subscription_type

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, UserList]]:
    if response.status_code == 200:
        response_200 = UserList.from_dict(response.json())

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
) -> Response[Union[Error, UserList]]:
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
    enabled: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    include_co_counsel: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    order: Union[Unset, UserindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    pending_setup: Union[Unset, bool] = UNSET,
    role: Union[Unset, UserindexRole] = UNSET,
    subscription_type: Union[Unset, UserindexSubscriptionType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, UserList]]:
    """Return the data for all Users

     Outlines the parameters, optional and required, used when requesting the data for all Users

    Args:
        created_since (Union[Unset, datetime.datetime]):
        enabled (Union[Unset, bool]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_co_counsel (Union[Unset, bool]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, UserindexOrder]):
        page_token (Union[Unset, str]):
        pending_setup (Union[Unset, bool]):
        role (Union[Unset, UserindexRole]):
        subscription_type (Union[Unset, UserindexSubscriptionType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UserList]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        enabled=enabled,
        fields=fields,
        ids=ids,
        include_co_counsel=include_co_counsel,
        limit=limit,
        name=name,
        order=order,
        page_token=page_token,
        pending_setup=pending_setup,
        role=role,
        subscription_type=subscription_type,
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
    created_since: Union[Unset, datetime.datetime] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    include_co_counsel: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    order: Union[Unset, UserindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    pending_setup: Union[Unset, bool] = UNSET,
    role: Union[Unset, UserindexRole] = UNSET,
    subscription_type: Union[Unset, UserindexSubscriptionType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, UserList]]:
    """Return the data for all Users

     Outlines the parameters, optional and required, used when requesting the data for all Users

    Args:
        created_since (Union[Unset, datetime.datetime]):
        enabled (Union[Unset, bool]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_co_counsel (Union[Unset, bool]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, UserindexOrder]):
        page_token (Union[Unset, str]):
        pending_setup (Union[Unset, bool]):
        role (Union[Unset, UserindexRole]):
        subscription_type (Union[Unset, UserindexSubscriptionType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UserList]
    """

    return sync_detailed(
        client=client,
        created_since=created_since,
        enabled=enabled,
        fields=fields,
        ids=ids,
        include_co_counsel=include_co_counsel,
        limit=limit,
        name=name,
        order=order,
        page_token=page_token,
        pending_setup=pending_setup,
        role=role,
        subscription_type=subscription_type,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, datetime.datetime] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    include_co_counsel: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    order: Union[Unset, UserindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    pending_setup: Union[Unset, bool] = UNSET,
    role: Union[Unset, UserindexRole] = UNSET,
    subscription_type: Union[Unset, UserindexSubscriptionType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, UserList]]:
    """Return the data for all Users

     Outlines the parameters, optional and required, used when requesting the data for all Users

    Args:
        created_since (Union[Unset, datetime.datetime]):
        enabled (Union[Unset, bool]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_co_counsel (Union[Unset, bool]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, UserindexOrder]):
        page_token (Union[Unset, str]):
        pending_setup (Union[Unset, bool]):
        role (Union[Unset, UserindexRole]):
        subscription_type (Union[Unset, UserindexSubscriptionType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UserList]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        enabled=enabled,
        fields=fields,
        ids=ids,
        include_co_counsel=include_co_counsel,
        limit=limit,
        name=name,
        order=order,
        page_token=page_token,
        pending_setup=pending_setup,
        role=role,
        subscription_type=subscription_type,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, datetime.datetime] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    include_co_counsel: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    order: Union[Unset, UserindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    pending_setup: Union[Unset, bool] = UNSET,
    role: Union[Unset, UserindexRole] = UNSET,
    subscription_type: Union[Unset, UserindexSubscriptionType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, UserList]]:
    """Return the data for all Users

     Outlines the parameters, optional and required, used when requesting the data for all Users

    Args:
        created_since (Union[Unset, datetime.datetime]):
        enabled (Union[Unset, bool]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_co_counsel (Union[Unset, bool]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, UserindexOrder]):
        page_token (Union[Unset, str]):
        pending_setup (Union[Unset, bool]):
        role (Union[Unset, UserindexRole]):
        subscription_type (Union[Unset, UserindexSubscriptionType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UserList]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_since=created_since,
            enabled=enabled,
            fields=fields,
            ids=ids,
            include_co_counsel=include_co_counsel,
            limit=limit,
            name=name,
            order=order,
            page_token=page_token,
            pending_setup=pending_setup,
            role=role,
            subscription_type=subscription_type,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
