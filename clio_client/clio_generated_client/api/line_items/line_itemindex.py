import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.line_item_list import LineItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    activity_id: Union[Unset, int] = UNSET,
    bill_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    display: Union[Unset, bool] = UNSET,
    exclude_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    group_ordering: Union[Unset, int] = UNSET,
    ids: Union[Unset, int] = UNSET,
    kind: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["activity_id"] = activity_id

    params["bill_id"] = bill_id

    json_created_since: Union[Unset, str] = UNSET
    if not isinstance(created_since, Unset):
        json_created_since = created_since.isoformat()
    params["created_since"] = json_created_since

    params["display"] = display

    params["exclude_ids[]"] = exclude_ids

    params["fields"] = fields

    params["group_ordering"] = group_ordering

    params["ids[]"] = ids

    params["kind"] = kind

    params["limit"] = limit

    params["matter_id"] = matter_id

    params["page_token"] = page_token

    params["query"] = query

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/line_items",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, LineItemList]]:
    if response.status_code == 200:
        response_200 = LineItemList.from_dict(response.json())

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
) -> Response[Union[Error, LineItemList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    activity_id: Union[Unset, int] = UNSET,
    bill_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    display: Union[Unset, bool] = UNSET,
    exclude_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    group_ordering: Union[Unset, int] = UNSET,
    ids: Union[Unset, int] = UNSET,
    kind: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, LineItemList]]:
    """Return the data for all LineItems

     Outlines the parameters, optional and required, used when requesting the data for all LineItems

    Args:
        activity_id (Union[Unset, int]):
        bill_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        display (Union[Unset, bool]):
        exclude_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        group_ordering (Union[Unset, int]):
        ids (Union[Unset, int]):
        kind (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LineItemList]]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
        bill_id=bill_id,
        created_since=created_since,
        display=display,
        exclude_ids=exclude_ids,
        fields=fields,
        group_ordering=group_ordering,
        ids=ids,
        kind=kind,
        limit=limit,
        matter_id=matter_id,
        page_token=page_token,
        query=query,
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
    activity_id: Union[Unset, int] = UNSET,
    bill_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    display: Union[Unset, bool] = UNSET,
    exclude_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    group_ordering: Union[Unset, int] = UNSET,
    ids: Union[Unset, int] = UNSET,
    kind: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, LineItemList]]:
    """Return the data for all LineItems

     Outlines the parameters, optional and required, used when requesting the data for all LineItems

    Args:
        activity_id (Union[Unset, int]):
        bill_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        display (Union[Unset, bool]):
        exclude_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        group_ordering (Union[Unset, int]):
        ids (Union[Unset, int]):
        kind (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LineItemList]
    """

    return sync_detailed(
        client=client,
        activity_id=activity_id,
        bill_id=bill_id,
        created_since=created_since,
        display=display,
        exclude_ids=exclude_ids,
        fields=fields,
        group_ordering=group_ordering,
        ids=ids,
        kind=kind,
        limit=limit,
        matter_id=matter_id,
        page_token=page_token,
        query=query,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    activity_id: Union[Unset, int] = UNSET,
    bill_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    display: Union[Unset, bool] = UNSET,
    exclude_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    group_ordering: Union[Unset, int] = UNSET,
    ids: Union[Unset, int] = UNSET,
    kind: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, LineItemList]]:
    """Return the data for all LineItems

     Outlines the parameters, optional and required, used when requesting the data for all LineItems

    Args:
        activity_id (Union[Unset, int]):
        bill_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        display (Union[Unset, bool]):
        exclude_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        group_ordering (Union[Unset, int]):
        ids (Union[Unset, int]):
        kind (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LineItemList]]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
        bill_id=bill_id,
        created_since=created_since,
        display=display,
        exclude_ids=exclude_ids,
        fields=fields,
        group_ordering=group_ordering,
        ids=ids,
        kind=kind,
        limit=limit,
        matter_id=matter_id,
        page_token=page_token,
        query=query,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    activity_id: Union[Unset, int] = UNSET,
    bill_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    display: Union[Unset, bool] = UNSET,
    exclude_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    group_ordering: Union[Unset, int] = UNSET,
    ids: Union[Unset, int] = UNSET,
    kind: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, LineItemList]]:
    """Return the data for all LineItems

     Outlines the parameters, optional and required, used when requesting the data for all LineItems

    Args:
        activity_id (Union[Unset, int]):
        bill_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        display (Union[Unset, bool]):
        exclude_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        group_ordering (Union[Unset, int]):
        ids (Union[Unset, int]):
        kind (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LineItemList]
    """

    return (
        await asyncio_detailed(
            client=client,
            activity_id=activity_id,
            bill_id=bill_id,
            created_since=created_since,
            display=display,
            exclude_ids=exclude_ids,
            fields=fields,
            group_ordering=group_ordering,
            ids=ids,
            kind=kind,
            limit=limit,
            matter_id=matter_id,
            page_token=page_token,
            query=query,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
