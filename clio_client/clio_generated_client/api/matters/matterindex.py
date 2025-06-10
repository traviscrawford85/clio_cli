import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.matter_list import MatterList
from ...models.matterindex_close_date import MatterindexCloseDate
from ...models.matterindex_custom_field_values import MatterindexCustomFieldValues
from ...models.matterindex_open_date import MatterindexOpenDate
from ...models.matterindex_order import MatterindexOrder
from ...models.matterindex_pending_date import MatterindexPendingDate
from ...models.matterindex_status import MatterindexStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    billable: Union[Unset, bool] = UNSET,
    client_id: Union[Unset, int] = UNSET,
    close_date: Union[Unset, MatterindexCloseDate] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    custom_field_ids: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, MatterindexCustomFieldValues] = UNSET,
    fields: Union[Unset, str] = UNSET,
    grant_id: Union[Unset, int] = UNSET,
    group_id: Union[Unset, int] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    notification_event_subscriber_user_id: Union[Unset, int] = UNSET,
    open_date: Union[Unset, MatterindexOpenDate] = UNSET,
    order: Union[Unset, MatterindexOrder] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    pending_date: Union[Unset, MatterindexPendingDate] = UNSET,
    practice_area_id: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    responsible_staff_id: Union[Unset, int] = UNSET,
    status: Union[Unset, MatterindexStatus] = UNSET,
    subscriber_user_id: Union[Unset, int] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["billable"] = billable

    params["client_id"] = client_id

    json_close_date: Union[Unset, str] = UNSET
    if not isinstance(close_date, Unset):
        json_close_date = close_date.value

    params["close_date[]"] = json_close_date

    json_created_since: Union[Unset, str] = UNSET
    if not isinstance(created_since, Unset):
        json_created_since = created_since.isoformat()
    params["created_since"] = json_created_since

    params["custom_field_ids[]"] = custom_field_ids

    json_custom_field_values: Union[Unset, str] = UNSET
    if not isinstance(custom_field_values, Unset):
        json_custom_field_values = custom_field_values.value

    params["custom_field_values"] = json_custom_field_values

    params["fields"] = fields

    params["grant_id"] = grant_id

    params["group_id"] = group_id

    params["ids[]"] = ids

    params["limit"] = limit

    params["notification_event_subscriber_user_id"] = notification_event_subscriber_user_id

    json_open_date: Union[Unset, str] = UNSET
    if not isinstance(open_date, Unset):
        json_open_date = open_date.value

    params["open_date[]"] = json_open_date

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["originating_attorney_id"] = originating_attorney_id

    params["page_token"] = page_token

    json_pending_date: Union[Unset, str] = UNSET
    if not isinstance(pending_date, Unset):
        json_pending_date = pending_date.value

    params["pending_date[]"] = json_pending_date

    params["practice_area_id"] = practice_area_id

    params["query"] = query

    params["responsible_attorney_id"] = responsible_attorney_id

    params["responsible_staff_id"] = responsible_staff_id

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["subscriber_user_id"] = subscriber_user_id

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/matters",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, MatterList]]:
    if response.status_code == 200:
        response_200 = MatterList.from_dict(response.json())

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
) -> Response[Union[Error, MatterList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billable: Union[Unset, bool] = UNSET,
    client_id: Union[Unset, int] = UNSET,
    close_date: Union[Unset, MatterindexCloseDate] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    custom_field_ids: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, MatterindexCustomFieldValues] = UNSET,
    fields: Union[Unset, str] = UNSET,
    grant_id: Union[Unset, int] = UNSET,
    group_id: Union[Unset, int] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    notification_event_subscriber_user_id: Union[Unset, int] = UNSET,
    open_date: Union[Unset, MatterindexOpenDate] = UNSET,
    order: Union[Unset, MatterindexOrder] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    pending_date: Union[Unset, MatterindexPendingDate] = UNSET,
    practice_area_id: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    responsible_staff_id: Union[Unset, int] = UNSET,
    status: Union[Unset, MatterindexStatus] = UNSET,
    subscriber_user_id: Union[Unset, int] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, MatterList]]:
    """Return the data for all Matters

     Outlines the parameters, optional and required, used when requesting the data for all Matters

    Args:
        billable (Union[Unset, bool]):
        client_id (Union[Unset, int]):
        close_date (Union[Unset, MatterindexCloseDate]):
        created_since (Union[Unset, datetime.datetime]):
        custom_field_ids (Union[Unset, int]):
        custom_field_values (Union[Unset, MatterindexCustomFieldValues]):
        fields (Union[Unset, str]):
        grant_id (Union[Unset, int]):
        group_id (Union[Unset, int]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        notification_event_subscriber_user_id (Union[Unset, int]):
        open_date (Union[Unset, MatterindexOpenDate]):
        order (Union[Unset, MatterindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        pending_date (Union[Unset, MatterindexPendingDate]):
        practice_area_id (Union[Unset, int]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        responsible_staff_id (Union[Unset, int]):
        status (Union[Unset, MatterindexStatus]):
        subscriber_user_id (Union[Unset, int]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MatterList]]
    """

    kwargs = _get_kwargs(
        billable=billable,
        client_id=client_id,
        close_date=close_date,
        created_since=created_since,
        custom_field_ids=custom_field_ids,
        custom_field_values=custom_field_values,
        fields=fields,
        grant_id=grant_id,
        group_id=group_id,
        ids=ids,
        limit=limit,
        notification_event_subscriber_user_id=notification_event_subscriber_user_id,
        open_date=open_date,
        order=order,
        originating_attorney_id=originating_attorney_id,
        page_token=page_token,
        pending_date=pending_date,
        practice_area_id=practice_area_id,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        responsible_staff_id=responsible_staff_id,
        status=status,
        subscriber_user_id=subscriber_user_id,
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
    billable: Union[Unset, bool] = UNSET,
    client_id: Union[Unset, int] = UNSET,
    close_date: Union[Unset, MatterindexCloseDate] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    custom_field_ids: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, MatterindexCustomFieldValues] = UNSET,
    fields: Union[Unset, str] = UNSET,
    grant_id: Union[Unset, int] = UNSET,
    group_id: Union[Unset, int] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    notification_event_subscriber_user_id: Union[Unset, int] = UNSET,
    open_date: Union[Unset, MatterindexOpenDate] = UNSET,
    order: Union[Unset, MatterindexOrder] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    pending_date: Union[Unset, MatterindexPendingDate] = UNSET,
    practice_area_id: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    responsible_staff_id: Union[Unset, int] = UNSET,
    status: Union[Unset, MatterindexStatus] = UNSET,
    subscriber_user_id: Union[Unset, int] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, MatterList]]:
    """Return the data for all Matters

     Outlines the parameters, optional and required, used when requesting the data for all Matters

    Args:
        billable (Union[Unset, bool]):
        client_id (Union[Unset, int]):
        close_date (Union[Unset, MatterindexCloseDate]):
        created_since (Union[Unset, datetime.datetime]):
        custom_field_ids (Union[Unset, int]):
        custom_field_values (Union[Unset, MatterindexCustomFieldValues]):
        fields (Union[Unset, str]):
        grant_id (Union[Unset, int]):
        group_id (Union[Unset, int]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        notification_event_subscriber_user_id (Union[Unset, int]):
        open_date (Union[Unset, MatterindexOpenDate]):
        order (Union[Unset, MatterindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        pending_date (Union[Unset, MatterindexPendingDate]):
        practice_area_id (Union[Unset, int]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        responsible_staff_id (Union[Unset, int]):
        status (Union[Unset, MatterindexStatus]):
        subscriber_user_id (Union[Unset, int]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MatterList]
    """

    return sync_detailed(
        client=client,
        billable=billable,
        client_id=client_id,
        close_date=close_date,
        created_since=created_since,
        custom_field_ids=custom_field_ids,
        custom_field_values=custom_field_values,
        fields=fields,
        grant_id=grant_id,
        group_id=group_id,
        ids=ids,
        limit=limit,
        notification_event_subscriber_user_id=notification_event_subscriber_user_id,
        open_date=open_date,
        order=order,
        originating_attorney_id=originating_attorney_id,
        page_token=page_token,
        pending_date=pending_date,
        practice_area_id=practice_area_id,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        responsible_staff_id=responsible_staff_id,
        status=status,
        subscriber_user_id=subscriber_user_id,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billable: Union[Unset, bool] = UNSET,
    client_id: Union[Unset, int] = UNSET,
    close_date: Union[Unset, MatterindexCloseDate] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    custom_field_ids: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, MatterindexCustomFieldValues] = UNSET,
    fields: Union[Unset, str] = UNSET,
    grant_id: Union[Unset, int] = UNSET,
    group_id: Union[Unset, int] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    notification_event_subscriber_user_id: Union[Unset, int] = UNSET,
    open_date: Union[Unset, MatterindexOpenDate] = UNSET,
    order: Union[Unset, MatterindexOrder] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    pending_date: Union[Unset, MatterindexPendingDate] = UNSET,
    practice_area_id: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    responsible_staff_id: Union[Unset, int] = UNSET,
    status: Union[Unset, MatterindexStatus] = UNSET,
    subscriber_user_id: Union[Unset, int] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, MatterList]]:
    """Return the data for all Matters

     Outlines the parameters, optional and required, used when requesting the data for all Matters

    Args:
        billable (Union[Unset, bool]):
        client_id (Union[Unset, int]):
        close_date (Union[Unset, MatterindexCloseDate]):
        created_since (Union[Unset, datetime.datetime]):
        custom_field_ids (Union[Unset, int]):
        custom_field_values (Union[Unset, MatterindexCustomFieldValues]):
        fields (Union[Unset, str]):
        grant_id (Union[Unset, int]):
        group_id (Union[Unset, int]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        notification_event_subscriber_user_id (Union[Unset, int]):
        open_date (Union[Unset, MatterindexOpenDate]):
        order (Union[Unset, MatterindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        pending_date (Union[Unset, MatterindexPendingDate]):
        practice_area_id (Union[Unset, int]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        responsible_staff_id (Union[Unset, int]):
        status (Union[Unset, MatterindexStatus]):
        subscriber_user_id (Union[Unset, int]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MatterList]]
    """

    kwargs = _get_kwargs(
        billable=billable,
        client_id=client_id,
        close_date=close_date,
        created_since=created_since,
        custom_field_ids=custom_field_ids,
        custom_field_values=custom_field_values,
        fields=fields,
        grant_id=grant_id,
        group_id=group_id,
        ids=ids,
        limit=limit,
        notification_event_subscriber_user_id=notification_event_subscriber_user_id,
        open_date=open_date,
        order=order,
        originating_attorney_id=originating_attorney_id,
        page_token=page_token,
        pending_date=pending_date,
        practice_area_id=practice_area_id,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        responsible_staff_id=responsible_staff_id,
        status=status,
        subscriber_user_id=subscriber_user_id,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    billable: Union[Unset, bool] = UNSET,
    client_id: Union[Unset, int] = UNSET,
    close_date: Union[Unset, MatterindexCloseDate] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    custom_field_ids: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, MatterindexCustomFieldValues] = UNSET,
    fields: Union[Unset, str] = UNSET,
    grant_id: Union[Unset, int] = UNSET,
    group_id: Union[Unset, int] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    notification_event_subscriber_user_id: Union[Unset, int] = UNSET,
    open_date: Union[Unset, MatterindexOpenDate] = UNSET,
    order: Union[Unset, MatterindexOrder] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    pending_date: Union[Unset, MatterindexPendingDate] = UNSET,
    practice_area_id: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    responsible_staff_id: Union[Unset, int] = UNSET,
    status: Union[Unset, MatterindexStatus] = UNSET,
    subscriber_user_id: Union[Unset, int] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, MatterList]]:
    """Return the data for all Matters

     Outlines the parameters, optional and required, used when requesting the data for all Matters

    Args:
        billable (Union[Unset, bool]):
        client_id (Union[Unset, int]):
        close_date (Union[Unset, MatterindexCloseDate]):
        created_since (Union[Unset, datetime.datetime]):
        custom_field_ids (Union[Unset, int]):
        custom_field_values (Union[Unset, MatterindexCustomFieldValues]):
        fields (Union[Unset, str]):
        grant_id (Union[Unset, int]):
        group_id (Union[Unset, int]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        notification_event_subscriber_user_id (Union[Unset, int]):
        open_date (Union[Unset, MatterindexOpenDate]):
        order (Union[Unset, MatterindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        pending_date (Union[Unset, MatterindexPendingDate]):
        practice_area_id (Union[Unset, int]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        responsible_staff_id (Union[Unset, int]):
        status (Union[Unset, MatterindexStatus]):
        subscriber_user_id (Union[Unset, int]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MatterList]
    """

    return (
        await asyncio_detailed(
            client=client,
            billable=billable,
            client_id=client_id,
            close_date=close_date,
            created_since=created_since,
            custom_field_ids=custom_field_ids,
            custom_field_values=custom_field_values,
            fields=fields,
            grant_id=grant_id,
            group_id=group_id,
            ids=ids,
            limit=limit,
            notification_event_subscriber_user_id=notification_event_subscriber_user_id,
            open_date=open_date,
            order=order,
            originating_attorney_id=originating_attorney_id,
            page_token=page_token,
            pending_date=pending_date,
            practice_area_id=practice_area_id,
            query=query,
            responsible_attorney_id=responsible_attorney_id,
            responsible_staff_id=responsible_staff_id,
            status=status,
            subscriber_user_id=subscriber_user_id,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
