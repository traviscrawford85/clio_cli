import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.communication_list import CommunicationList
from ...models.communicationindex_order import CommunicationindexOrder
from ...models.communicationindex_type import CommunicationindexType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    having_time_entries: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, CommunicationindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    received_at: Union[Unset, datetime.datetime] = UNSET,
    received_before: Union[Unset, datetime.datetime] = UNSET,
    received_since: Union[Unset, datetime.datetime] = UNSET,
    type_: Union[Unset, CommunicationindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["contact_id"] = contact_id

    json_created_since: Union[Unset, str] = UNSET
    if not isinstance(created_since, Unset):
        json_created_since = created_since.isoformat()
    params["created_since"] = json_created_since

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["external_property_name"] = external_property_name

    params["external_property_value"] = external_property_value

    params["fields"] = fields

    params["having_time_entries"] = having_time_entries

    params["ids[]"] = ids

    params["limit"] = limit

    params["matter_id"] = matter_id

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["query"] = query

    json_received_at: Union[Unset, str] = UNSET
    if not isinstance(received_at, Unset):
        json_received_at = received_at.isoformat()
    params["received_at"] = json_received_at

    json_received_before: Union[Unset, str] = UNSET
    if not isinstance(received_before, Unset):
        json_received_before = received_before.isoformat()
    params["received_before"] = json_received_before

    json_received_since: Union[Unset, str] = UNSET
    if not isinstance(received_since, Unset):
        json_received_since = received_since.isoformat()
    params["received_since"] = json_received_since

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
        "url": "/communications",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommunicationList, Error]]:
    if response.status_code == 200:
        response_200 = CommunicationList.from_dict(response.json())

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
) -> Response[Union[CommunicationList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    having_time_entries: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, CommunicationindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    received_at: Union[Unset, datetime.datetime] = UNSET,
    received_before: Union[Unset, datetime.datetime] = UNSET,
    received_since: Union[Unset, datetime.datetime] = UNSET,
    type_: Union[Unset, CommunicationindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[CommunicationList, Error]]:
    """Return the data for all Communications

     Outlines the parameters, optional and required, used when requesting the data for all Communications

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        date (Union[Unset, datetime.date]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        having_time_entries (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, CommunicationindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        received_at (Union[Unset, datetime.datetime]):
        received_before (Union[Unset, datetime.datetime]):
        received_since (Union[Unset, datetime.datetime]):
        type_ (Union[Unset, CommunicationindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommunicationList, Error]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        created_since=created_since,
        date=date,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        having_time_entries=having_time_entries,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        query=query,
        received_at=received_at,
        received_before=received_before,
        received_since=received_since,
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
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    having_time_entries: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, CommunicationindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    received_at: Union[Unset, datetime.datetime] = UNSET,
    received_before: Union[Unset, datetime.datetime] = UNSET,
    received_since: Union[Unset, datetime.datetime] = UNSET,
    type_: Union[Unset, CommunicationindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[CommunicationList, Error]]:
    """Return the data for all Communications

     Outlines the parameters, optional and required, used when requesting the data for all Communications

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        date (Union[Unset, datetime.date]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        having_time_entries (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, CommunicationindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        received_at (Union[Unset, datetime.datetime]):
        received_before (Union[Unset, datetime.datetime]):
        received_since (Union[Unset, datetime.datetime]):
        type_ (Union[Unset, CommunicationindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommunicationList, Error]
    """

    return sync_detailed(
        client=client,
        contact_id=contact_id,
        created_since=created_since,
        date=date,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        having_time_entries=having_time_entries,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        query=query,
        received_at=received_at,
        received_before=received_before,
        received_since=received_since,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    having_time_entries: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, CommunicationindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    received_at: Union[Unset, datetime.datetime] = UNSET,
    received_before: Union[Unset, datetime.datetime] = UNSET,
    received_since: Union[Unset, datetime.datetime] = UNSET,
    type_: Union[Unset, CommunicationindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[CommunicationList, Error]]:
    """Return the data for all Communications

     Outlines the parameters, optional and required, used when requesting the data for all Communications

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        date (Union[Unset, datetime.date]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        having_time_entries (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, CommunicationindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        received_at (Union[Unset, datetime.datetime]):
        received_before (Union[Unset, datetime.datetime]):
        received_since (Union[Unset, datetime.datetime]):
        type_ (Union[Unset, CommunicationindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommunicationList, Error]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        created_since=created_since,
        date=date,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        having_time_entries=having_time_entries,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        query=query,
        received_at=received_at,
        received_before=received_before,
        received_since=received_since,
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
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    having_time_entries: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, CommunicationindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    received_at: Union[Unset, datetime.datetime] = UNSET,
    received_before: Union[Unset, datetime.datetime] = UNSET,
    received_since: Union[Unset, datetime.datetime] = UNSET,
    type_: Union[Unset, CommunicationindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[CommunicationList, Error]]:
    """Return the data for all Communications

     Outlines the parameters, optional and required, used when requesting the data for all Communications

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        date (Union[Unset, datetime.date]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        having_time_entries (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, CommunicationindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        received_at (Union[Unset, datetime.datetime]):
        received_before (Union[Unset, datetime.datetime]):
        received_since (Union[Unset, datetime.datetime]):
        type_ (Union[Unset, CommunicationindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommunicationList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            contact_id=contact_id,
            created_since=created_since,
            date=date,
            external_property_name=external_property_name,
            external_property_value=external_property_value,
            fields=fields,
            having_time_entries=having_time_entries,
            ids=ids,
            limit=limit,
            matter_id=matter_id,
            order=order,
            page_token=page_token,
            query=query,
            received_at=received_at,
            received_before=received_before,
            received_since=received_since,
            type_=type_,
            updated_since=updated_since,
            user_id=user_id,
            x_api_version=x_api_version,
        )
    ).parsed
