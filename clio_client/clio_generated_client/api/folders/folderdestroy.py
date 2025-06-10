from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/folders/{id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Error]]:
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
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Error]]:
    """Delete a single Folder

     Deleting a Folder using this method will move it to the trash instead of permanently deleting it.
    Trashed Folders are permanently deleted after 30 days. The following errors may be returned:

    - `400 Bad Request`: The Folder cannot be trashed. The `type` of the error will be `DeleteFailed`
    and the `message` of the error will be one of the following:
      - `Delete failed: This folder contains more than 100,000 items and cannot be trashed. Please trash
    some of the items inside it before trying again.`
      - `Delete failed: This item contains locked items and cannot be deleted.`
      - `Delete failed: The root folder cannot be trashed`
    - `409 Conflict`: The Folder (or one of its descendants) is currently being modified by another
    request, and cannot be trashed.

    Args:
        id (int):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        id=id,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Delete a single Folder

     Deleting a Folder using this method will move it to the trash instead of permanently deleting it.
    Trashed Folders are permanently deleted after 30 days. The following errors may be returned:

    - `400 Bad Request`: The Folder cannot be trashed. The `type` of the error will be `DeleteFailed`
    and the `message` of the error will be one of the following:
      - `Delete failed: This folder contains more than 100,000 items and cannot be trashed. Please trash
    some of the items inside it before trying again.`
      - `Delete failed: This item contains locked items and cannot be deleted.`
      - `Delete failed: The root folder cannot be trashed`
    - `409 Conflict`: The Folder (or one of its descendants) is currently being modified by another
    request, and cannot be trashed.

    Args:
        id (int):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
    """

    return sync_detailed(
        id=id,
        client=client,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Error]]:
    """Delete a single Folder

     Deleting a Folder using this method will move it to the trash instead of permanently deleting it.
    Trashed Folders are permanently deleted after 30 days. The following errors may be returned:

    - `400 Bad Request`: The Folder cannot be trashed. The `type` of the error will be `DeleteFailed`
    and the `message` of the error will be one of the following:
      - `Delete failed: This folder contains more than 100,000 items and cannot be trashed. Please trash
    some of the items inside it before trying again.`
      - `Delete failed: This item contains locked items and cannot be deleted.`
      - `Delete failed: The root folder cannot be trashed`
    - `409 Conflict`: The Folder (or one of its descendants) is currently being modified by another
    request, and cannot be trashed.

    Args:
        id (int):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        id=id,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Delete a single Folder

     Deleting a Folder using this method will move it to the trash instead of permanently deleting it.
    Trashed Folders are permanently deleted after 30 days. The following errors may be returned:

    - `400 Bad Request`: The Folder cannot be trashed. The `type` of the error will be `DeleteFailed`
    and the `message` of the error will be one of the following:
      - `Delete failed: This folder contains more than 100,000 items and cannot be trashed. Please trash
    some of the items inside it before trying again.`
      - `Delete failed: This item contains locked items and cannot be deleted.`
      - `Delete failed: The root folder cannot be trashed`
    - `409 Conflict`: The Folder (or one of its descendants) is currently being modified by another
    request, and cannot be trashed.

    Args:
        id (int):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            x_api_version=x_api_version,
        )
    ).parsed
