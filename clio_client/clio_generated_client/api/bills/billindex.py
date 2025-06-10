import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bill_list import BillList
from ...models.billindex_custom_field_values import BillindexCustomFieldValues
from ...models.billindex_order import BillindexOrder
from ...models.billindex_state import BillindexState
from ...models.billindex_status import BillindexStatus
from ...models.billindex_type import BillindexType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    currency_id: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, BillindexCustomFieldValues] = UNSET,
    due_after: Union[Unset, datetime.date] = UNSET,
    due_at: Union[Unset, datetime.date] = UNSET,
    due_before: Union[Unset, datetime.date] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    issued_after: Union[Unset, datetime.date] = UNSET,
    issued_before: Union[Unset, datetime.date] = UNSET,
    last_sent_end_date: Union[Unset, datetime.date] = UNSET,
    last_sent_start_date: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, BillindexOrder] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    overdue_only: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, int] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    state: Union[Unset, BillindexState] = UNSET,
    status: Union[Unset, BillindexStatus] = UNSET,
    type_: Union[Unset, BillindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["client_id"] = client_id

    json_created_since: Union[Unset, str] = UNSET
    if not isinstance(created_since, Unset):
        json_created_since = created_since.isoformat()
    params["created_since"] = json_created_since

    params["currency_id"] = currency_id

    json_custom_field_values: Union[Unset, str] = UNSET
    if not isinstance(custom_field_values, Unset):
        json_custom_field_values = custom_field_values.value

    params["custom_field_values"] = json_custom_field_values

    json_due_after: Union[Unset, str] = UNSET
    if not isinstance(due_after, Unset):
        json_due_after = due_after.isoformat()
    params["due_after"] = json_due_after

    json_due_at: Union[Unset, str] = UNSET
    if not isinstance(due_at, Unset):
        json_due_at = due_at.isoformat()
    params["due_at"] = json_due_at

    json_due_before: Union[Unset, str] = UNSET
    if not isinstance(due_before, Unset):
        json_due_before = due_before.isoformat()
    params["due_before"] = json_due_before

    params["fields"] = fields

    params["ids[]"] = ids

    json_issued_after: Union[Unset, str] = UNSET
    if not isinstance(issued_after, Unset):
        json_issued_after = issued_after.isoformat()
    params["issued_after"] = json_issued_after

    json_issued_before: Union[Unset, str] = UNSET
    if not isinstance(issued_before, Unset):
        json_issued_before = issued_before.isoformat()
    params["issued_before"] = json_issued_before

    json_last_sent_end_date: Union[Unset, str] = UNSET
    if not isinstance(last_sent_end_date, Unset):
        json_last_sent_end_date = last_sent_end_date.isoformat()
    params["last_sent_end_date"] = json_last_sent_end_date

    json_last_sent_start_date: Union[Unset, str] = UNSET
    if not isinstance(last_sent_start_date, Unset):
        json_last_sent_start_date = last_sent_start_date.isoformat()
    params["last_sent_start_date"] = json_last_sent_start_date

    params["limit"] = limit

    params["matter_id"] = matter_id

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["originating_attorney_id"] = originating_attorney_id

    params["overdue_only"] = overdue_only

    params["page_token"] = page_token

    params["query"] = query

    params["responsible_attorney_id"] = responsible_attorney_id

    json_state: Union[Unset, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

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
        "url": "/bills",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BillList, Error]]:
    if response.status_code == 200:
        response_200 = BillList.from_dict(response.json())

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
) -> Response[Union[BillList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    client_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    currency_id: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, BillindexCustomFieldValues] = UNSET,
    due_after: Union[Unset, datetime.date] = UNSET,
    due_at: Union[Unset, datetime.date] = UNSET,
    due_before: Union[Unset, datetime.date] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    issued_after: Union[Unset, datetime.date] = UNSET,
    issued_before: Union[Unset, datetime.date] = UNSET,
    last_sent_end_date: Union[Unset, datetime.date] = UNSET,
    last_sent_start_date: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, BillindexOrder] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    overdue_only: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, int] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    state: Union[Unset, BillindexState] = UNSET,
    status: Union[Unset, BillindexStatus] = UNSET,
    type_: Union[Unset, BillindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[BillList, Error]]:
    """Return the data for all Bills

     Outlines the parameters, optional and required, used when requesting the data for all Bills

    Args:
        client_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        currency_id (Union[Unset, int]):
        custom_field_values (Union[Unset, BillindexCustomFieldValues]):
        due_after (Union[Unset, datetime.date]):
        due_at (Union[Unset, datetime.date]):
        due_before (Union[Unset, datetime.date]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        issued_after (Union[Unset, datetime.date]):
        issued_before (Union[Unset, datetime.date]):
        last_sent_end_date (Union[Unset, datetime.date]):
        last_sent_start_date (Union[Unset, datetime.date]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, BillindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        overdue_only (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, int]):
        responsible_attorney_id (Union[Unset, int]):
        state (Union[Unset, BillindexState]):
        status (Union[Unset, BillindexStatus]):
        type_ (Union[Unset, BillindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillList, Error]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        created_since=created_since,
        currency_id=currency_id,
        custom_field_values=custom_field_values,
        due_after=due_after,
        due_at=due_at,
        due_before=due_before,
        fields=fields,
        ids=ids,
        issued_after=issued_after,
        issued_before=issued_before,
        last_sent_end_date=last_sent_end_date,
        last_sent_start_date=last_sent_start_date,
        limit=limit,
        matter_id=matter_id,
        order=order,
        originating_attorney_id=originating_attorney_id,
        overdue_only=overdue_only,
        page_token=page_token,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        state=state,
        status=status,
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
    client_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    currency_id: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, BillindexCustomFieldValues] = UNSET,
    due_after: Union[Unset, datetime.date] = UNSET,
    due_at: Union[Unset, datetime.date] = UNSET,
    due_before: Union[Unset, datetime.date] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    issued_after: Union[Unset, datetime.date] = UNSET,
    issued_before: Union[Unset, datetime.date] = UNSET,
    last_sent_end_date: Union[Unset, datetime.date] = UNSET,
    last_sent_start_date: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, BillindexOrder] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    overdue_only: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, int] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    state: Union[Unset, BillindexState] = UNSET,
    status: Union[Unset, BillindexStatus] = UNSET,
    type_: Union[Unset, BillindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[BillList, Error]]:
    """Return the data for all Bills

     Outlines the parameters, optional and required, used when requesting the data for all Bills

    Args:
        client_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        currency_id (Union[Unset, int]):
        custom_field_values (Union[Unset, BillindexCustomFieldValues]):
        due_after (Union[Unset, datetime.date]):
        due_at (Union[Unset, datetime.date]):
        due_before (Union[Unset, datetime.date]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        issued_after (Union[Unset, datetime.date]):
        issued_before (Union[Unset, datetime.date]):
        last_sent_end_date (Union[Unset, datetime.date]):
        last_sent_start_date (Union[Unset, datetime.date]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, BillindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        overdue_only (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, int]):
        responsible_attorney_id (Union[Unset, int]):
        state (Union[Unset, BillindexState]):
        status (Union[Unset, BillindexStatus]):
        type_ (Union[Unset, BillindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillList, Error]
    """

    return sync_detailed(
        client=client,
        client_id=client_id,
        created_since=created_since,
        currency_id=currency_id,
        custom_field_values=custom_field_values,
        due_after=due_after,
        due_at=due_at,
        due_before=due_before,
        fields=fields,
        ids=ids,
        issued_after=issued_after,
        issued_before=issued_before,
        last_sent_end_date=last_sent_end_date,
        last_sent_start_date=last_sent_start_date,
        limit=limit,
        matter_id=matter_id,
        order=order,
        originating_attorney_id=originating_attorney_id,
        overdue_only=overdue_only,
        page_token=page_token,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        state=state,
        status=status,
        type_=type_,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    client_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    currency_id: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, BillindexCustomFieldValues] = UNSET,
    due_after: Union[Unset, datetime.date] = UNSET,
    due_at: Union[Unset, datetime.date] = UNSET,
    due_before: Union[Unset, datetime.date] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    issued_after: Union[Unset, datetime.date] = UNSET,
    issued_before: Union[Unset, datetime.date] = UNSET,
    last_sent_end_date: Union[Unset, datetime.date] = UNSET,
    last_sent_start_date: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, BillindexOrder] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    overdue_only: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, int] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    state: Union[Unset, BillindexState] = UNSET,
    status: Union[Unset, BillindexStatus] = UNSET,
    type_: Union[Unset, BillindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[BillList, Error]]:
    """Return the data for all Bills

     Outlines the parameters, optional and required, used when requesting the data for all Bills

    Args:
        client_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        currency_id (Union[Unset, int]):
        custom_field_values (Union[Unset, BillindexCustomFieldValues]):
        due_after (Union[Unset, datetime.date]):
        due_at (Union[Unset, datetime.date]):
        due_before (Union[Unset, datetime.date]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        issued_after (Union[Unset, datetime.date]):
        issued_before (Union[Unset, datetime.date]):
        last_sent_end_date (Union[Unset, datetime.date]):
        last_sent_start_date (Union[Unset, datetime.date]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, BillindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        overdue_only (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, int]):
        responsible_attorney_id (Union[Unset, int]):
        state (Union[Unset, BillindexState]):
        status (Union[Unset, BillindexStatus]):
        type_ (Union[Unset, BillindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillList, Error]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        created_since=created_since,
        currency_id=currency_id,
        custom_field_values=custom_field_values,
        due_after=due_after,
        due_at=due_at,
        due_before=due_before,
        fields=fields,
        ids=ids,
        issued_after=issued_after,
        issued_before=issued_before,
        last_sent_end_date=last_sent_end_date,
        last_sent_start_date=last_sent_start_date,
        limit=limit,
        matter_id=matter_id,
        order=order,
        originating_attorney_id=originating_attorney_id,
        overdue_only=overdue_only,
        page_token=page_token,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        state=state,
        status=status,
        type_=type_,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    client_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    currency_id: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, BillindexCustomFieldValues] = UNSET,
    due_after: Union[Unset, datetime.date] = UNSET,
    due_at: Union[Unset, datetime.date] = UNSET,
    due_before: Union[Unset, datetime.date] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    issued_after: Union[Unset, datetime.date] = UNSET,
    issued_before: Union[Unset, datetime.date] = UNSET,
    last_sent_end_date: Union[Unset, datetime.date] = UNSET,
    last_sent_start_date: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, BillindexOrder] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    overdue_only: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, int] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    state: Union[Unset, BillindexState] = UNSET,
    status: Union[Unset, BillindexStatus] = UNSET,
    type_: Union[Unset, BillindexType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[BillList, Error]]:
    """Return the data for all Bills

     Outlines the parameters, optional and required, used when requesting the data for all Bills

    Args:
        client_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        currency_id (Union[Unset, int]):
        custom_field_values (Union[Unset, BillindexCustomFieldValues]):
        due_after (Union[Unset, datetime.date]):
        due_at (Union[Unset, datetime.date]):
        due_before (Union[Unset, datetime.date]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        issued_after (Union[Unset, datetime.date]):
        issued_before (Union[Unset, datetime.date]):
        last_sent_end_date (Union[Unset, datetime.date]):
        last_sent_start_date (Union[Unset, datetime.date]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, BillindexOrder]):
        originating_attorney_id (Union[Unset, int]):
        overdue_only (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, int]):
        responsible_attorney_id (Union[Unset, int]):
        state (Union[Unset, BillindexState]):
        status (Union[Unset, BillindexStatus]):
        type_ (Union[Unset, BillindexType]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            client_id=client_id,
            created_since=created_since,
            currency_id=currency_id,
            custom_field_values=custom_field_values,
            due_after=due_after,
            due_at=due_at,
            due_before=due_before,
            fields=fields,
            ids=ids,
            issued_after=issued_after,
            issued_before=issued_before,
            last_sent_end_date=last_sent_end_date,
            last_sent_start_date=last_sent_start_date,
            limit=limit,
            matter_id=matter_id,
            order=order,
            originating_attorney_id=originating_attorney_id,
            overdue_only=overdue_only,
            page_token=page_token,
            query=query,
            responsible_attorney_id=responsible_attorney_id,
            state=state,
            status=status,
            type_=type_,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
