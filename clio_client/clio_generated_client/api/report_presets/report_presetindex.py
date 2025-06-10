import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.report_preset_list import ReportPresetList
from ...models.report_presetindex_category import ReportPresetindexCategory
from ...models.report_presetindex_order import ReportPresetindexOrder
from ...models.report_presetindex_schedule_frequency import ReportPresetindexScheduleFrequency
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: Union[Unset, ReportPresetindexCategory] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    has_schedule: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ReportPresetindexOrder] = UNSET,
    output_format: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    schedule_frequency: Union[Unset, ReportPresetindexScheduleFrequency] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    json_category: Union[Unset, str] = UNSET
    if not isinstance(category, Unset):
        json_category = category.value

    params["category"] = json_category

    json_created_since: Union[Unset, str] = UNSET
    if not isinstance(created_since, Unset):
        json_created_since = created_since.isoformat()
    params["created_since"] = json_created_since

    params["fields"] = fields

    params["has_schedule"] = has_schedule

    params["ids[]"] = ids

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["output_format"] = output_format

    params["page_token"] = page_token

    params["query"] = query

    json_schedule_frequency: Union[Unset, str] = UNSET
    if not isinstance(schedule_frequency, Unset):
        json_schedule_frequency = schedule_frequency.value

    params["schedule_frequency"] = json_schedule_frequency

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/report_presets",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ReportPresetList]]:
    if response.status_code == 200:
        response_200 = ReportPresetList.from_dict(response.json())

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
) -> Response[Union[Error, ReportPresetList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, ReportPresetindexCategory] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    has_schedule: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ReportPresetindexOrder] = UNSET,
    output_format: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    schedule_frequency: Union[Unset, ReportPresetindexScheduleFrequency] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, ReportPresetList]]:
    """Return the data for all ReportPresets

     Outlines the parameters, optional and required, used when requesting the data for all ReportPresets

    Args:
        category (Union[Unset, ReportPresetindexCategory]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        has_schedule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, ReportPresetindexOrder]):
        output_format (Union[Unset, str]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        schedule_frequency (Union[Unset, ReportPresetindexScheduleFrequency]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReportPresetList]]
    """

    kwargs = _get_kwargs(
        category=category,
        created_since=created_since,
        fields=fields,
        has_schedule=has_schedule,
        ids=ids,
        limit=limit,
        order=order,
        output_format=output_format,
        page_token=page_token,
        query=query,
        schedule_frequency=schedule_frequency,
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
    category: Union[Unset, ReportPresetindexCategory] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    has_schedule: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ReportPresetindexOrder] = UNSET,
    output_format: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    schedule_frequency: Union[Unset, ReportPresetindexScheduleFrequency] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, ReportPresetList]]:
    """Return the data for all ReportPresets

     Outlines the parameters, optional and required, used when requesting the data for all ReportPresets

    Args:
        category (Union[Unset, ReportPresetindexCategory]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        has_schedule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, ReportPresetindexOrder]):
        output_format (Union[Unset, str]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        schedule_frequency (Union[Unset, ReportPresetindexScheduleFrequency]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReportPresetList]
    """

    return sync_detailed(
        client=client,
        category=category,
        created_since=created_since,
        fields=fields,
        has_schedule=has_schedule,
        ids=ids,
        limit=limit,
        order=order,
        output_format=output_format,
        page_token=page_token,
        query=query,
        schedule_frequency=schedule_frequency,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, ReportPresetindexCategory] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    has_schedule: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ReportPresetindexOrder] = UNSET,
    output_format: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    schedule_frequency: Union[Unset, ReportPresetindexScheduleFrequency] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, ReportPresetList]]:
    """Return the data for all ReportPresets

     Outlines the parameters, optional and required, used when requesting the data for all ReportPresets

    Args:
        category (Union[Unset, ReportPresetindexCategory]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        has_schedule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, ReportPresetindexOrder]):
        output_format (Union[Unset, str]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        schedule_frequency (Union[Unset, ReportPresetindexScheduleFrequency]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReportPresetList]]
    """

    kwargs = _get_kwargs(
        category=category,
        created_since=created_since,
        fields=fields,
        has_schedule=has_schedule,
        ids=ids,
        limit=limit,
        order=order,
        output_format=output_format,
        page_token=page_token,
        query=query,
        schedule_frequency=schedule_frequency,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, ReportPresetindexCategory] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    has_schedule: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ReportPresetindexOrder] = UNSET,
    output_format: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    schedule_frequency: Union[Unset, ReportPresetindexScheduleFrequency] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, ReportPresetList]]:
    """Return the data for all ReportPresets

     Outlines the parameters, optional and required, used when requesting the data for all ReportPresets

    Args:
        category (Union[Unset, ReportPresetindexCategory]):
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        has_schedule (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, ReportPresetindexOrder]):
        output_format (Union[Unset, str]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        schedule_frequency (Union[Unset, ReportPresetindexScheduleFrequency]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReportPresetList]
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            created_since=created_since,
            fields=fields,
            has_schedule=has_schedule,
            ids=ids,
            limit=limit,
            order=order,
            output_format=output_format,
            page_token=page_token,
            query=query,
            schedule_frequency=schedule_frequency,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
