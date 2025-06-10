import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_list import CalendarList
from ...models.calendarindex_order import CalendarindexOrder
from ...models.calendarindex_source import CalendarindexSource
from ...models.calendarindex_type import CalendarindexType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    filter_inactive_users: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, CalendarindexOrder] = UNSET,
    owner: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    source: Union[Unset, CalendarindexSource] = UNSET,
    type_: Union[Unset, CalendarindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    visible: Union[Unset, bool] = UNSET,
    writeable: Union[Unset, bool] = UNSET,
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

    params["filter_inactive_users"] = filter_inactive_users

    params["ids[]"] = ids

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["owner"] = owner

    params["page_token"] = page_token

    json_source: Union[Unset, str] = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params["visible"] = visible

    params["writeable"] = writeable

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/calendars",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CalendarList, Error]]:
    if response.status_code == 200:
        response_200 = CalendarList.from_dict(response.json())

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
) -> Response[Union[CalendarList, Error]]:
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
    filter_inactive_users: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, CalendarindexOrder] = UNSET,
    owner: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    source: Union[Unset, CalendarindexSource] = UNSET,
    type_: Union[Unset, CalendarindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    visible: Union[Unset, bool] = UNSET,
    writeable: Union[Unset, bool] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[CalendarList, Error]]:
    """Return the data for all Calendars

     Outlines the parameters, optional and required, used when requesting the data for all Calendars

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        filter_inactive_users (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CalendarindexOrder]):
        owner (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        source (Union[Unset, CalendarindexSource]):
        type_ (Union[Unset, CalendarindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        visible (Union[Unset, bool]):
        writeable (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CalendarList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        filter_inactive_users=filter_inactive_users,
        ids=ids,
        limit=limit,
        order=order,
        owner=owner,
        page_token=page_token,
        source=source,
        type_=type_,
        updated_since=updated_since,
        visible=visible,
        writeable=writeable,
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
    filter_inactive_users: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, CalendarindexOrder] = UNSET,
    owner: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    source: Union[Unset, CalendarindexSource] = UNSET,
    type_: Union[Unset, CalendarindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    visible: Union[Unset, bool] = UNSET,
    writeable: Union[Unset, bool] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[CalendarList, Error]]:
    """Return the data for all Calendars

     Outlines the parameters, optional and required, used when requesting the data for all Calendars

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        filter_inactive_users (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CalendarindexOrder]):
        owner (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        source (Union[Unset, CalendarindexSource]):
        type_ (Union[Unset, CalendarindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        visible (Union[Unset, bool]):
        writeable (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CalendarList, Error]
    """

    return sync_detailed(
        client=client,
        created_since=created_since,
        fields=fields,
        filter_inactive_users=filter_inactive_users,
        ids=ids,
        limit=limit,
        order=order,
        owner=owner,
        page_token=page_token,
        source=source,
        type_=type_,
        updated_since=updated_since,
        visible=visible,
        writeable=writeable,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    filter_inactive_users: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, CalendarindexOrder] = UNSET,
    owner: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    source: Union[Unset, CalendarindexSource] = UNSET,
    type_: Union[Unset, CalendarindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    visible: Union[Unset, bool] = UNSET,
    writeable: Union[Unset, bool] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[CalendarList, Error]]:
    """Return the data for all Calendars

     Outlines the parameters, optional and required, used when requesting the data for all Calendars

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        filter_inactive_users (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CalendarindexOrder]):
        owner (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        source (Union[Unset, CalendarindexSource]):
        type_ (Union[Unset, CalendarindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        visible (Union[Unset, bool]):
        writeable (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CalendarList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        filter_inactive_users=filter_inactive_users,
        ids=ids,
        limit=limit,
        order=order,
        owner=owner,
        page_token=page_token,
        source=source,
        type_=type_,
        updated_since=updated_since,
        visible=visible,
        writeable=writeable,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    filter_inactive_users: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, CalendarindexOrder] = UNSET,
    owner: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    source: Union[Unset, CalendarindexSource] = UNSET,
    type_: Union[Unset, CalendarindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    visible: Union[Unset, bool] = UNSET,
    writeable: Union[Unset, bool] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[CalendarList, Error]]:
    """Return the data for all Calendars

     Outlines the parameters, optional and required, used when requesting the data for all Calendars

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        filter_inactive_users (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CalendarindexOrder]):
        owner (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        source (Union[Unset, CalendarindexSource]):
        type_ (Union[Unset, CalendarindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        visible (Union[Unset, bool]):
        writeable (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CalendarList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_since=created_since,
            fields=fields,
            filter_inactive_users=filter_inactive_users,
            ids=ids,
            limit=limit,
            order=order,
            owner=owner,
            page_token=page_token,
            source=source,
            type_=type_,
            updated_since=updated_since,
            visible=visible,
            writeable=writeable,
            x_api_version=x_api_version,
        )
    ).parsed
