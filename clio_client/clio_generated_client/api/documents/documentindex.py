import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_list import DocumentList
from ...models.documentindex_order import DocumentindexOrder
from ...models.documentindex_scope import DocumentindexScope
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    document_category_id: Union[Unset, int] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, DocumentindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    scope: Union[Unset, DocumentindexScope] = UNSET,
    show_uncompleted: Union[Unset, bool] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
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

    params["document_category_id"] = document_category_id

    params["external_property_name"] = external_property_name

    params["external_property_value"] = external_property_value

    params["fields"] = fields

    params["ids[]"] = ids

    params["include_deleted"] = include_deleted

    params["limit"] = limit

    params["matter_id"] = matter_id

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["parent_id"] = parent_id

    params["query"] = query

    json_scope: Union[Unset, str] = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope.value

    params["scope"] = json_scope

    params["show_uncompleted"] = show_uncompleted

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DocumentList, Error]]:
    if response.status_code == 200:
        response_200 = DocumentList.from_dict(response.json())

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
) -> Response[Union[DocumentList, Error]]:
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
    document_category_id: Union[Unset, int] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, DocumentindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    scope: Union[Unset, DocumentindexScope] = UNSET,
    show_uncompleted: Union[Unset, bool] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[DocumentList, Error]]:
    """Return the data for all Documents

     Outlines the parameters, optional and required, used when requesting the data for all Documents

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        document_category_id (Union[Unset, int]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_deleted (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, DocumentindexOrder]):
        page_token (Union[Unset, str]):
        parent_id (Union[Unset, int]):
        query (Union[Unset, str]):
        scope (Union[Unset, DocumentindexScope]):
        show_uncompleted (Union[Unset, bool]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentList, Error]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        created_since=created_since,
        document_category_id=document_category_id,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        ids=ids,
        include_deleted=include_deleted,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        parent_id=parent_id,
        query=query,
        scope=scope,
        show_uncompleted=show_uncompleted,
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
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    document_category_id: Union[Unset, int] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, DocumentindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    scope: Union[Unset, DocumentindexScope] = UNSET,
    show_uncompleted: Union[Unset, bool] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[DocumentList, Error]]:
    """Return the data for all Documents

     Outlines the parameters, optional and required, used when requesting the data for all Documents

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        document_category_id (Union[Unset, int]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_deleted (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, DocumentindexOrder]):
        page_token (Union[Unset, str]):
        parent_id (Union[Unset, int]):
        query (Union[Unset, str]):
        scope (Union[Unset, DocumentindexScope]):
        show_uncompleted (Union[Unset, bool]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentList, Error]
    """

    return sync_detailed(
        client=client,
        contact_id=contact_id,
        created_since=created_since,
        document_category_id=document_category_id,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        ids=ids,
        include_deleted=include_deleted,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        parent_id=parent_id,
        query=query,
        scope=scope,
        show_uncompleted=show_uncompleted,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    document_category_id: Union[Unset, int] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, DocumentindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    scope: Union[Unset, DocumentindexScope] = UNSET,
    show_uncompleted: Union[Unset, bool] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[DocumentList, Error]]:
    """Return the data for all Documents

     Outlines the parameters, optional and required, used when requesting the data for all Documents

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        document_category_id (Union[Unset, int]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_deleted (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, DocumentindexOrder]):
        page_token (Union[Unset, str]):
        parent_id (Union[Unset, int]):
        query (Union[Unset, str]):
        scope (Union[Unset, DocumentindexScope]):
        show_uncompleted (Union[Unset, bool]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentList, Error]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        created_since=created_since,
        document_category_id=document_category_id,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        ids=ids,
        include_deleted=include_deleted,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        parent_id=parent_id,
        query=query,
        scope=scope,
        show_uncompleted=show_uncompleted,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, datetime.datetime] = UNSET,
    document_category_id: Union[Unset, int] = UNSET,
    external_property_name: Union[Unset, str] = UNSET,
    external_property_value: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, DocumentindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    scope: Union[Unset, DocumentindexScope] = UNSET,
    show_uncompleted: Union[Unset, bool] = UNSET,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[DocumentList, Error]]:
    """Return the data for all Documents

     Outlines the parameters, optional and required, used when requesting the data for all Documents

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, datetime.datetime]):
        document_category_id (Union[Unset, int]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_deleted (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, DocumentindexOrder]):
        page_token (Union[Unset, str]):
        parent_id (Union[Unset, int]):
        query (Union[Unset, str]):
        scope (Union[Unset, DocumentindexScope]):
        show_uncompleted (Union[Unset, bool]):
        updated_since (Union[Unset, datetime.datetime]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            contact_id=contact_id,
            created_since=created_since,
            document_category_id=document_category_id,
            external_property_name=external_property_name,
            external_property_value=external_property_value,
            fields=fields,
            ids=ids,
            include_deleted=include_deleted,
            limit=limit,
            matter_id=matter_id,
            order=order,
            page_token=page_token,
            parent_id=parent_id,
            query=query,
            scope=scope,
            show_uncompleted=show_uncompleted,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
