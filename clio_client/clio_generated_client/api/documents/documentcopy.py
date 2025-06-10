from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_show import DocumentShow
from ...models.documentcopy_data_body import DocumentcopyDataBody
from ...models.documentcopy_files_body import DocumentcopyFilesBody
from ...models.documentcopy_json_body import DocumentcopyJsonBody
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: Union[
        DocumentcopyJsonBody,
        DocumentcopyDataBody,
        DocumentcopyFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/documents/{id}/copy",
        "params": params,
    }

    if isinstance(body, DocumentcopyJsonBody):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, DocumentcopyDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, DocumentcopyFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DocumentShow, Error]]:
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 201:
        response_201 = DocumentShow.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DocumentShow, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        DocumentcopyJsonBody,
        DocumentcopyDataBody,
        DocumentcopyFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
) -> Response[Union[DocumentShow, Error]]:
    """Copy a Document

     Copies the latest document version of a Document into a new Document. The parameters `filename` and
    `name` will be copied from the source Document if none are provided.

    Args:
        id (int):
        fields (Union[Unset, str]):
        body (DocumentcopyJsonBody):
        body (DocumentcopyDataBody):
        body (DocumentcopyFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentShow, Error]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        DocumentcopyJsonBody,
        DocumentcopyDataBody,
        DocumentcopyFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
) -> Optional[Union[DocumentShow, Error]]:
    """Copy a Document

     Copies the latest document version of a Document into a new Document. The parameters `filename` and
    `name` will be copied from the source Document if none are provided.

    Args:
        id (int):
        fields (Union[Unset, str]):
        body (DocumentcopyJsonBody):
        body (DocumentcopyDataBody):
        body (DocumentcopyFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentShow, Error]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        DocumentcopyJsonBody,
        DocumentcopyDataBody,
        DocumentcopyFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
) -> Response[Union[DocumentShow, Error]]:
    """Copy a Document

     Copies the latest document version of a Document into a new Document. The parameters `filename` and
    `name` will be copied from the source Document if none are provided.

    Args:
        id (int):
        fields (Union[Unset, str]):
        body (DocumentcopyJsonBody):
        body (DocumentcopyDataBody):
        body (DocumentcopyFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentShow, Error]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        DocumentcopyJsonBody,
        DocumentcopyDataBody,
        DocumentcopyFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
) -> Optional[Union[DocumentShow, Error]]:
    """Copy a Document

     Copies the latest document version of a Document into a new Document. The parameters `filename` and
    `name` will be copied from the source Document if none are provided.

    Args:
        id (int):
        fields (Union[Unset, str]):
        body (DocumentcopyJsonBody):
        body (DocumentcopyDataBody):
        body (DocumentcopyFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentShow, Error]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            fields=fields,
        )
    ).parsed
