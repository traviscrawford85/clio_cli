import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calendar_entry_list import CalendarEntryList
from ...models.calendar_entryindex_source import CalendarEntryindexSource
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    calendar_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    expanded: Union[Unset, bool] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    has_court_rule: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    is_all_day: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    owner_entries_across_all_users: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    source: Union[Unset, CalendarEntryindexSource] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    visible: Union[Unset, bool] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["calendar_id"] = calendar_id

    json_created_since: Union[Unset, str] = UNSET
    if not isinstance(created_since, Unset):
        json_created_since = created_since.isoformat()
    params["created_since"] = json_created_since

    params["expanded"] = expanded

    params["external_property_name"] = external_property_name

    params["external_property_value"] = external_property_value

    params["fields"] = fields

    json_from_: Union[Unset, str] = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    params["has_court_rule"] = has_court_rule

    params["ids[]"] = ids

    params["is_all_day"] = is_all_day

    params["limit"] = limit

    params["matter_id"] = matter_id

    params["owner_entries_across_all_users"] = owner_entries_across_all_users

    params["page_token"] = page_token

    params["query"] = query

    json_source: Union[Unset, str] = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    json_to: Union[Unset, str] = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params["visible"] = visible

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/calendar_entries",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CalendarEntryList, Error]]:
    if response.status_code == 200:
        response_200 = CalendarEntryList.from_dict(response.json())

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
) -> Response[Union[CalendarEntryList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    calendar_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    expanded: Union[Unset, bool] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    has_court_rule: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    is_all_day: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    owner_entries_across_all_users: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    source: Union[Unset, CalendarEntryindexSource] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    visible: Union[Unset, bool] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[CalendarEntryList, Error]]:
    """Return the data for all CalendarEntries

     Outlines the parameters, optional and required, used when requesting the data for all
    CalendarEntries

    Args:
        calendar_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        expanded (Union[Unset, bool]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        from_ (Union[Unset, datetime.datetime]):
        has_court_rule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        is_all_day (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        owner_entries_across_all_users (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, CalendarEntryindexSource]):
        to (Union[Unset, datetime.datetime]):
        updated_since (Union[Unset, datetime.datetime]):
        visible (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CalendarEntryList, Error]]
    """

    kwargs = _get_kwargs(
        calendar_id=calendar_id,
        created_since=created_since,
        expanded=expanded,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        from_=from_,
        has_court_rule=has_court_rule,
        ids=ids,
        is_all_day=is_all_day,
        limit=limit,
        matter_id=matter_id,
        owner_entries_across_all_users=owner_entries_across_all_users,
        page_token=page_token,
        query=query,
        source=source,
        to=to,
        updated_since=updated_since,
        visible=visible,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    calendar_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    expanded: Union[Unset, bool] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    has_court_rule: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    is_all_day: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    owner_entries_across_all_users: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    source: Union[Unset, CalendarEntryindexSource] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    visible: Union[Unset, bool] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[CalendarEntryList, Error]]:
    """Return the data for all CalendarEntries

     Outlines the parameters, optional and required, used when requesting the data for all
    CalendarEntries

    Args:
        calendar_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        expanded (Union[Unset, bool]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        from_ (Union[Unset, datetime.datetime]):
        has_court_rule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        is_all_day (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        owner_entries_across_all_users (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, CalendarEntryindexSource]):
        to (Union[Unset, datetime.datetime]):
        updated_since (Union[Unset, datetime.datetime]):
        visible (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CalendarEntryList, Error]
    """

    return sync_detailed(
        client=client,
        calendar_id=calendar_id,
        created_since=created_since,
        expanded=expanded,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        from_=from_,
        has_court_rule=has_court_rule,
        ids=ids,
        is_all_day=is_all_day,
        limit=limit,
        matter_id=matter_id,
        owner_entries_across_all_users=owner_entries_across_all_users,
        page_token=page_token,
        query=query,
        source=source,
        to=to,
        updated_since=updated_since,
        visible=visible,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    calendar_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    expanded: Union[Unset, bool] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    has_court_rule: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    is_all_day: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    owner_entries_across_all_users: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    source: Union[Unset, CalendarEntryindexSource] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    visible: Union[Unset, bool] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[CalendarEntryList, Error]]:
    """Return the data for all CalendarEntries

     Outlines the parameters, optional and required, used when requesting the data for all
    CalendarEntries

    Args:
        calendar_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        expanded (Union[Unset, bool]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        from_ (Union[Unset, datetime.datetime]):
        has_court_rule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        is_all_day (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        owner_entries_across_all_users (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, CalendarEntryindexSource]):
        to (Union[Unset, datetime.datetime]):
        updated_since (Union[Unset, datetime.datetime]):
        visible (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CalendarEntryList, Error]]
    """

    kwargs = _get_kwargs(
        calendar_id=calendar_id,
        created_since=created_since,
        expanded=expanded,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        from_=from_,
        has_court_rule=has_court_rule,
        ids=ids,
        is_all_day=is_all_day,
        limit=limit,
        matter_id=matter_id,
        owner_entries_across_all_users=owner_entries_across_all_users,
        page_token=page_token,
        query=query,
        source=source,
        to=to,
        updated_since=updated_since,
        visible=visible,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    calendar_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    expanded: Union[Unset, bool] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    has_court_rule: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    is_all_day: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    owner_entries_across_all_users: Union[Unset, bool] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    source: Union[Unset, CalendarEntryindexSource] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    visible: Union[Unset, bool] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[CalendarEntryList, Error]]:
    """Return the data for all CalendarEntries

     Outlines the parameters, optional and required, used when requesting the data for all
    CalendarEntries

    Args:
        calendar_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        expanded (Union[Unset, bool]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        from_ (Union[Unset, datetime.datetime]):
        has_court_rule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        is_all_day (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        owner_entries_across_all_users (Union[Unset, bool]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, CalendarEntryindexSource]):
        to (Union[Unset, datetime.datetime]):
        updated_since (Union[Unset, datetime.datetime]):
        visible (Union[Unset, bool]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CalendarEntryList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            calendar_id=calendar_id,
            created_since=created_since,
            expanded=expanded,
            external_property_name=external_property_name,
            external_property_value=external_property_value,
            fields=fields,
            from_=from_,
            has_court_rule=has_court_rule,
            ids=ids,
            is_all_day=is_all_day,
            limit=limit,
            matter_id=matter_id,
            owner_entries_across_all_users=owner_entries_across_all_users,
            page_token=page_token,
            query=query,
            source=source,
            to=to,
            updated_since=updated_since,
            visible=visible,
            x_api_version=x_api_version,
        )
    ).parsed
