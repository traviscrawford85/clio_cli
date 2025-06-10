from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_version_list import DocumentVersionList
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id_path: int,
    *,
    fields: Union[Unset, str] = UNSET,
    fully_uploaded: Union[Unset, bool] = UNSET,
    id_query: int,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["fields"] = fields

    params["fully_uploaded"] = fully_uploaded

    params["id"] = id_query

    params["limit"] = limit

    params["page_token"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/documents/{id_path}/versions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DocumentVersionList, Error]]:
    if response.status_code == 200:
        response_200 = DocumentVersionList.from_dict(response.json())

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
) -> Response[Union[DocumentVersionList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id_path: int,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    fully_uploaded: Union[Unset, bool] = UNSET,
    id_query: int,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[DocumentVersionList, Error]]:
    """Return the data for all DocumentVersions

     Outlines the parameters, optional and required, used when requesting the data for all
    DocumentVersions

    Args:
        id_path (int):
        fields (Union[Unset, str]):
        fully_uploaded (Union[Unset, bool]):
        id_query (int):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentVersionList, Error]]
    """

    kwargs = _get_kwargs(
        id_path=id_path,
        fields=fields,
        fully_uploaded=fully_uploaded,
        id_query=id_query,
        limit=limit,
        page_token=page_token,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id_path: int,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    fully_uploaded: Union[Unset, bool] = UNSET,
    id_query: int,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[DocumentVersionList, Error]]:
    """Return the data for all DocumentVersions

     Outlines the parameters, optional and required, used when requesting the data for all
    DocumentVersions

    Args:
        id_path (int):
        fields (Union[Unset, str]):
        fully_uploaded (Union[Unset, bool]):
        id_query (int):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentVersionList, Error]
    """

    return sync_detailed(
        id_path=id_path,
        client=client,
        fields=fields,
        fully_uploaded=fully_uploaded,
        id_query=id_query,
        limit=limit,
        page_token=page_token,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    id_path: int,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    fully_uploaded: Union[Unset, bool] = UNSET,
    id_query: int,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[DocumentVersionList, Error]]:
    """Return the data for all DocumentVersions

     Outlines the parameters, optional and required, used when requesting the data for all
    DocumentVersions

    Args:
        id_path (int):
        fields (Union[Unset, str]):
        fully_uploaded (Union[Unset, bool]):
        id_query (int):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentVersionList, Error]]
    """

    kwargs = _get_kwargs(
        id_path=id_path,
        fields=fields,
        fully_uploaded=fully_uploaded,
        id_query=id_query,
        limit=limit,
        page_token=page_token,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id_path: int,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    fully_uploaded: Union[Unset, bool] = UNSET,
    id_query: int,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[DocumentVersionList, Error]]:
    """Return the data for all DocumentVersions

     Outlines the parameters, optional and required, used when requesting the data for all
    DocumentVersions

    Args:
        id_path (int):
        fields (Union[Unset, str]):
        fully_uploaded (Union[Unset, bool]):
        id_query (int):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentVersionList, Error]
    """

    return (
        await asyncio_detailed(
            id_path=id_path,
            client=client,
            fields=fields,
            fully_uploaded=fully_uploaded,
            id_query=id_query,
            limit=limit,
            page_token=page_token,
            x_api_version=x_api_version,
        )
    ).parsed
