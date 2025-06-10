import datetime
from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    event_prefix: Union[Unset, str] = UNSET,
    jurisdictionid: int,
    service_typeid: int,
    start_date: datetime.datetime,
    start_time: datetime.datetime,
    triggerid: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["event_prefix"] = event_prefix

    params["jurisdiction[id]"] = jurisdictionid

    params["service_type[id]"] = service_typeid

    json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_start_time = start_time.isoformat()
    params["start_time"] = json_start_time

    params["trigger[id]"] = triggerid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/court_rules/matter_dockets/preview",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error]]:
    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
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
    *,
    client: Union[AuthenticatedClient, Client],
    event_prefix: Union[Unset, str] = UNSET,
    jurisdictionid: int,
    service_typeid: int,
    start_date: datetime.datetime,
    start_time: datetime.datetime,
    triggerid: int,
) -> Response[Union[Any, Error]]:
    """Preview calendar dates for the docket

     Preview calendar dates for the docket

    Args:
        event_prefix (Union[Unset, str]):
        jurisdictionid (int):
        service_typeid (int):
        start_date (datetime.datetime):
        start_time (datetime.datetime):
        triggerid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        event_prefix=event_prefix,
        jurisdictionid=jurisdictionid,
        service_typeid=service_typeid,
        start_date=start_date,
        start_time=start_time,
        triggerid=triggerid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    event_prefix: Union[Unset, str] = UNSET,
    jurisdictionid: int,
    service_typeid: int,
    start_date: datetime.datetime,
    start_time: datetime.datetime,
    triggerid: int,
) -> Optional[Union[Any, Error]]:
    """Preview calendar dates for the docket

     Preview calendar dates for the docket

    Args:
        event_prefix (Union[Unset, str]):
        jurisdictionid (int):
        service_typeid (int):
        start_date (datetime.datetime):
        start_time (datetime.datetime):
        triggerid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
    """

    return sync_detailed(
        client=client,
        event_prefix=event_prefix,
        jurisdictionid=jurisdictionid,
        service_typeid=service_typeid,
        start_date=start_date,
        start_time=start_time,
        triggerid=triggerid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    event_prefix: Union[Unset, str] = UNSET,
    jurisdictionid: int,
    service_typeid: int,
    start_date: datetime.datetime,
    start_time: datetime.datetime,
    triggerid: int,
) -> Response[Union[Any, Error]]:
    """Preview calendar dates for the docket

     Preview calendar dates for the docket

    Args:
        event_prefix (Union[Unset, str]):
        jurisdictionid (int):
        service_typeid (int):
        start_date (datetime.datetime):
        start_time (datetime.datetime):
        triggerid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        event_prefix=event_prefix,
        jurisdictionid=jurisdictionid,
        service_typeid=service_typeid,
        start_date=start_date,
        start_time=start_time,
        triggerid=triggerid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    event_prefix: Union[Unset, str] = UNSET,
    jurisdictionid: int,
    service_typeid: int,
    start_date: datetime.datetime,
    start_time: datetime.datetime,
    triggerid: int,
) -> Optional[Union[Any, Error]]:
    """Preview calendar dates for the docket

     Preview calendar dates for the docket

    Args:
        event_prefix (Union[Unset, str]):
        jurisdictionid (int):
        service_typeid (int):
        start_date (datetime.datetime):
        start_time (datetime.datetime):
        triggerid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            event_prefix=event_prefix,
            jurisdictionid=jurisdictionid,
            service_typeid=service_typeid,
            start_date=start_date,
            start_time=start_time,
            triggerid=triggerid,
        )
    ).parsed
