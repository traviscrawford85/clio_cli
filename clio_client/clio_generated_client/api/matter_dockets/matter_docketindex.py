import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.matter_docket_list import MatterDocketList
from ...models.matter_docketindex_matter_status import MatterDocketindexMatterStatus
from ...models.matter_docketindex_order import MatterDocketindexOrder
from ...models.matter_docketindex_status import MatterDocketindexStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    matter_status: Union[Unset, MatterDocketindexMatterStatus] = UNSET,
    order: Union[Unset, MatterDocketindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    service_type_id: Union[Unset, int] = UNSET,
    status: Union[Unset, MatterDocketindexStatus] = UNSET,
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

    params["fields"] = fields

    params["ids[]"] = ids

    params["limit"] = limit

    params["matter_id"] = matter_id

    json_matter_status: Union[Unset, str] = UNSET
    if not isinstance(matter_status, Unset):
        json_matter_status = matter_status.value

    params["matter_status"] = json_matter_status

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["query"] = query

    params["service_type_id"] = service_type_id

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/court_rules/matter_dockets",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, MatterDocketList]]:
    if response.status_code == 200:
        response_200 = MatterDocketList.from_dict(response.json())

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
) -> Response[Union[Error, MatterDocketList]]:
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
    matter_id: Union[Unset, int] = UNSET,
    matter_status: Union[Unset, MatterDocketindexMatterStatus] = UNSET,
    order: Union[Unset, MatterDocketindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    service_type_id: Union[Unset, int] = UNSET,
    status: Union[Unset, MatterDocketindexStatus] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, MatterDocketList]]:
    """Return the data for all matter dockets

     Outlines the parameters, optional and required, used when requesting the data for all MatterDockets

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        matter_status (Union[Unset, MatterDocketindexMatterStatus]):
        order (Union[Unset, MatterDocketindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        service_type_id (Union[Unset, int]):
        status (Union[Unset, MatterDocketindexStatus]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MatterDocketList]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        matter_status=matter_status,
        order=order,
        page_token=page_token,
        query=query,
        service_type_id=service_type_id,
        status=status,
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
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    matter_status: Union[Unset, MatterDocketindexMatterStatus] = UNSET,
    order: Union[Unset, MatterDocketindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    service_type_id: Union[Unset, int] = UNSET,
    status: Union[Unset, MatterDocketindexStatus] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, MatterDocketList]]:
    """Return the data for all matter dockets

     Outlines the parameters, optional and required, used when requesting the data for all MatterDockets

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        matter_status (Union[Unset, MatterDocketindexMatterStatus]):
        order (Union[Unset, MatterDocketindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        service_type_id (Union[Unset, int]):
        status (Union[Unset, MatterDocketindexStatus]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MatterDocketList]
    """

    return sync_detailed(
        client=client,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        matter_status=matter_status,
        order=order,
        page_token=page_token,
        query=query,
        service_type_id=service_type_id,
        status=status,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    matter_status: Union[Unset, MatterDocketindexMatterStatus] = UNSET,
    order: Union[Unset, MatterDocketindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    service_type_id: Union[Unset, int] = UNSET,
    status: Union[Unset, MatterDocketindexStatus] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, MatterDocketList]]:
    """Return the data for all matter dockets

     Outlines the parameters, optional and required, used when requesting the data for all MatterDockets

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        matter_status (Union[Unset, MatterDocketindexMatterStatus]):
        order (Union[Unset, MatterDocketindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        service_type_id (Union[Unset, int]):
        status (Union[Unset, MatterDocketindexStatus]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MatterDocketList]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        matter_status=matter_status,
        order=order,
        page_token=page_token,
        query=query,
        service_type_id=service_type_id,
        status=status,
        updated_since=updated_since,
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
    matter_id: Union[Unset, int] = UNSET,
    matter_status: Union[Unset, MatterDocketindexMatterStatus] = UNSET,
    order: Union[Unset, MatterDocketindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    service_type_id: Union[Unset, int] = UNSET,
    status: Union[Unset, MatterDocketindexStatus] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, MatterDocketList]]:
    """Return the data for all matter dockets

     Outlines the parameters, optional and required, used when requesting the data for all MatterDockets

    Args:
        created_since (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        matter_status (Union[Unset, MatterDocketindexMatterStatus]):
        order (Union[Unset, MatterDocketindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        service_type_id (Union[Unset, int]):
        status (Union[Unset, MatterDocketindexStatus]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MatterDocketList]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_since=created_since,
            fields=fields,
            ids=ids,
            limit=limit,
            matter_id=matter_id,
            matter_status=matter_status,
            order=order,
            page_token=page_token,
            query=query,
            service_type_id=service_type_id,
            status=status,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
