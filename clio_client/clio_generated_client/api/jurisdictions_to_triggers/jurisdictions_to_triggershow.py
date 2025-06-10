from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.jurisdictions_to_trigger_show import JurisdictionsToTriggerShow
from ...types import UNSET, Response, Unset


def _get_kwargs(
    jurisdiction_id: int,
    id: int,
    *,
    fields: Union[Unset, str] = UNSET,
    if_modified_since: Union[Unset, str] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_modified_since, Unset):
        headers["IF-MODIFIED-SINCE"] = if_modified_since

    if not isinstance(if_none_match, Unset):
        headers["IF-NONE-MATCH"] = if_none_match

    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/court_rules/jurisdictions/{jurisdiction_id}/triggers/{id}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error, JurisdictionsToTriggerShow]]:
    if response.status_code == 200:
        response_200 = JurisdictionsToTriggerShow.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Error, JurisdictionsToTriggerShow]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    jurisdiction_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    if_modified_since: Union[Unset, str] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Error, JurisdictionsToTriggerShow]]:
    """Return the data for the trigger

     Outlines the parameters, optional and required, used when requesting the data for a single
    JurisdictionsToTrigger

    Args:
        jurisdiction_id (int):
        id (int):
        fields (Union[Unset, str]):
        if_modified_since (Union[Unset, str]):
        if_none_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, JurisdictionsToTriggerShow]]
    """

    kwargs = _get_kwargs(
        jurisdiction_id=jurisdiction_id,
        id=id,
        fields=fields,
        if_modified_since=if_modified_since,
        if_none_match=if_none_match,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    jurisdiction_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    if_modified_since: Union[Unset, str] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Error, JurisdictionsToTriggerShow]]:
    """Return the data for the trigger

     Outlines the parameters, optional and required, used when requesting the data for a single
    JurisdictionsToTrigger

    Args:
        jurisdiction_id (int):
        id (int):
        fields (Union[Unset, str]):
        if_modified_since (Union[Unset, str]):
        if_none_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, JurisdictionsToTriggerShow]
    """

    return sync_detailed(
        jurisdiction_id=jurisdiction_id,
        id=id,
        client=client,
        fields=fields,
        if_modified_since=if_modified_since,
        if_none_match=if_none_match,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    jurisdiction_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    if_modified_since: Union[Unset, str] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Error, JurisdictionsToTriggerShow]]:
    """Return the data for the trigger

     Outlines the parameters, optional and required, used when requesting the data for a single
    JurisdictionsToTrigger

    Args:
        jurisdiction_id (int):
        id (int):
        fields (Union[Unset, str]):
        if_modified_since (Union[Unset, str]):
        if_none_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, JurisdictionsToTriggerShow]]
    """

    kwargs = _get_kwargs(
        jurisdiction_id=jurisdiction_id,
        id=id,
        fields=fields,
        if_modified_since=if_modified_since,
        if_none_match=if_none_match,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    jurisdiction_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    if_modified_since: Union[Unset, str] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Error, JurisdictionsToTriggerShow]]:
    """Return the data for the trigger

     Outlines the parameters, optional and required, used when requesting the data for a single
    JurisdictionsToTrigger

    Args:
        jurisdiction_id (int):
        id (int):
        fields (Union[Unset, str]):
        if_modified_since (Union[Unset, str]):
        if_none_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, JurisdictionsToTriggerShow]
    """

    return (
        await asyncio_detailed(
            jurisdiction_id=jurisdiction_id,
            id=id,
            client=client,
            fields=fields,
            if_modified_since=if_modified_since,
            if_none_match=if_none_match,
            x_api_version=x_api_version,
        )
    ).parsed
