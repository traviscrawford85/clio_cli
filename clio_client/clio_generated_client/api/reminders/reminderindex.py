import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.reminder_list import ReminderList
from ...models.reminderindex_order import ReminderindexOrder
from ...models.reminderindex_state import ReminderindexState
from ...models.reminderindex_subject_type import ReminderindexSubjectType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    notification_method_id: Union[Unset, int] = UNSET,
    order: Union[Unset, ReminderindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    state: Union[Unset, ReminderindexState] = UNSET,
    subject_id: Union[Unset, int] = UNSET,
    subject_type: Union[Unset, ReminderindexSubjectType] = UNSET,
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

    params["notification_method_id"] = notification_method_id

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    json_state: Union[Unset, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params["subject_id"] = subject_id

    json_subject_type: Union[Unset, str] = UNSET
    if not isinstance(subject_type, Unset):
        json_subject_type = subject_type.value

    params["subject_type"] = json_subject_type

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/reminders",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ReminderList]]:
    if response.status_code == 200:
        response_200 = ReminderList.from_dict(response.json())

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
) -> Response[Union[Error, ReminderList]]:
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
    notification_method_id: Union[Unset, int] = UNSET,
    order: Union[Unset, ReminderindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    state: Union[Unset, ReminderindexState] = UNSET,
    subject_id: Union[Unset, int] = UNSET,
    subject_type: Union[Unset, ReminderindexSubjectType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, ReminderList]]:
    """Return the data for all Reminders

     Outlines the parameters, optional and required, used when requesting the data for all Reminders

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        notification_method_id (Union[Unset, int]):
        order (Union[Unset, ReminderindexOrder]):
        page_token (Union[Unset, str]):
        state (Union[Unset, ReminderindexState]):
        subject_id (Union[Unset, int]):
        subject_type (Union[Unset, ReminderindexSubjectType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReminderList]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        notification_method_id=notification_method_id,
        order=order,
        page_token=page_token,
        state=state,
        subject_id=subject_id,
        subject_type=subject_type,
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
    notification_method_id: Union[Unset, int] = UNSET,
    order: Union[Unset, ReminderindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    state: Union[Unset, ReminderindexState] = UNSET,
    subject_id: Union[Unset, int] = UNSET,
    subject_type: Union[Unset, ReminderindexSubjectType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, ReminderList]]:
    """Return the data for all Reminders

     Outlines the parameters, optional and required, used when requesting the data for all Reminders

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        notification_method_id (Union[Unset, int]):
        order (Union[Unset, ReminderindexOrder]):
        page_token (Union[Unset, str]):
        state (Union[Unset, ReminderindexState]):
        subject_id (Union[Unset, int]):
        subject_type (Union[Unset, ReminderindexSubjectType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReminderList]
    """

    return sync_detailed(
        client=client,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        notification_method_id=notification_method_id,
        order=order,
        page_token=page_token,
        state=state,
        subject_id=subject_id,
        subject_type=subject_type,
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
    notification_method_id: Union[Unset, int] = UNSET,
    order: Union[Unset, ReminderindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    state: Union[Unset, ReminderindexState] = UNSET,
    subject_id: Union[Unset, int] = UNSET,
    subject_type: Union[Unset, ReminderindexSubjectType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, ReminderList]]:
    """Return the data for all Reminders

     Outlines the parameters, optional and required, used when requesting the data for all Reminders

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        notification_method_id (Union[Unset, int]):
        order (Union[Unset, ReminderindexOrder]):
        page_token (Union[Unset, str]):
        state (Union[Unset, ReminderindexState]):
        subject_id (Union[Unset, int]):
        subject_type (Union[Unset, ReminderindexSubjectType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReminderList]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        notification_method_id=notification_method_id,
        order=order,
        page_token=page_token,
        state=state,
        subject_id=subject_id,
        subject_type=subject_type,
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
    notification_method_id: Union[Unset, int] = UNSET,
    order: Union[Unset, ReminderindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    state: Union[Unset, ReminderindexState] = UNSET,
    subject_id: Union[Unset, int] = UNSET,
    subject_type: Union[Unset, ReminderindexSubjectType] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, ReminderList]]:
    """Return the data for all Reminders

     Outlines the parameters, optional and required, used when requesting the data for all Reminders

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        notification_method_id (Union[Unset, int]):
        order (Union[Unset, ReminderindexOrder]):
        page_token (Union[Unset, str]):
        state (Union[Unset, ReminderindexState]):
        subject_id (Union[Unset, int]):
        subject_type (Union[Unset, ReminderindexSubjectType]):
        updated_since (Union[Unset, datetime.datetime]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReminderList]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_since=created_since,
            fields=fields,
            ids=ids,
            limit=limit,
            notification_method_id=notification_method_id,
            order=order,
            page_token=page_token,
            state=state,
            subject_id=subject_id,
            subject_type=subject_type,
            updated_since=updated_since,
            user_id=user_id,
            x_api_version=x_api_version,
        )
    ).parsed
