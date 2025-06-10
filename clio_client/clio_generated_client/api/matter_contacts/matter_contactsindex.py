from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.matter_contacts_list import MatterContactsList
from ...models.matter_contactsindex_order import MatterContactsindexOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    matter_id: int,
    *,
    custom_field_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, MatterContactsindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["custom_field_ids[]"] = custom_field_ids

    params["fields"] = fields

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/matters/{matter_id}/contacts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, MatterContactsList]]:
    if response.status_code == 200:
        response_200 = MatterContactsList.from_dict(response.json())

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
) -> Response[Union[Error, MatterContactsList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    matter_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    custom_field_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, MatterContactsindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, MatterContactsList]]:
    """Return the related contact data for a single matter

     Outlines the parameters, optional and required, used when requesting the data for all MatterContacts

    Args:
        matter_id (int):
        custom_field_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        order (Union[Unset, MatterContactsindexOrder]):
        page_token (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MatterContactsList]]
    """

    kwargs = _get_kwargs(
        matter_id=matter_id,
        custom_field_ids=custom_field_ids,
        fields=fields,
        limit=limit,
        order=order,
        page_token=page_token,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    matter_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    custom_field_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, MatterContactsindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, MatterContactsList]]:
    """Return the related contact data for a single matter

     Outlines the parameters, optional and required, used when requesting the data for all MatterContacts

    Args:
        matter_id (int):
        custom_field_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        order (Union[Unset, MatterContactsindexOrder]):
        page_token (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MatterContactsList]
    """

    return sync_detailed(
        matter_id=matter_id,
        client=client,
        custom_field_ids=custom_field_ids,
        fields=fields,
        limit=limit,
        order=order,
        page_token=page_token,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    matter_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    custom_field_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, MatterContactsindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, MatterContactsList]]:
    """Return the related contact data for a single matter

     Outlines the parameters, optional and required, used when requesting the data for all MatterContacts

    Args:
        matter_id (int):
        custom_field_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        order (Union[Unset, MatterContactsindexOrder]):
        page_token (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MatterContactsList]]
    """

    kwargs = _get_kwargs(
        matter_id=matter_id,
        custom_field_ids=custom_field_ids,
        fields=fields,
        limit=limit,
        order=order,
        page_token=page_token,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    matter_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    custom_field_ids: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, MatterContactsindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, MatterContactsList]]:
    """Return the related contact data for a single matter

     Outlines the parameters, optional and required, used when requesting the data for all MatterContacts

    Args:
        matter_id (int):
        custom_field_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        order (Union[Unset, MatterContactsindexOrder]):
        page_token (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MatterContactsList]
    """

    return (
        await asyncio_detailed(
            matter_id=matter_id,
            client=client,
            custom_field_ids=custom_field_ids,
            fields=fields,
            limit=limit,
            order=order,
            page_token=page_token,
            x_api_version=x_api_version,
        )
    ).parsed
