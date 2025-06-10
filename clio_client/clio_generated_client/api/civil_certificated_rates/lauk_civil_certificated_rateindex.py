from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.lauk_civil_certificated_rate_list import LaukCivilCertificatedRateList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    activity: Union[Unset, str] = UNSET,
    activity_sub_category: Union[Unset, str] = UNSET,
    attended_several_hearings_for_multiple_clients: Union[Unset, bool] = UNSET,
    category_of_law: Union[Unset, str] = UNSET,
    change_of_solicitor: Union[Unset, bool] = UNSET,
    court: Union[Unset, str] = UNSET,
    eligible_for_sqm: Union[Unset, bool] = UNSET,
    fee_scheme: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    first_conducting_solicitor: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    number_of_clients: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    party: Union[Unset, str] = UNSET,
    post_transfer_clients_represented: Union[Unset, str] = UNSET,
    rate_type: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
    session_type: Union[Unset, str] = UNSET,
    user_type: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["activity"] = activity

    params["activity_sub_category"] = activity_sub_category

    params["attended_several_hearings_for_multiple_clients"] = attended_several_hearings_for_multiple_clients

    params["category_of_law"] = category_of_law

    params["change_of_solicitor"] = change_of_solicitor

    params["court"] = court

    params["eligible_for_sqm"] = eligible_for_sqm

    params["fee_scheme"] = fee_scheme

    params["fields"] = fields

    params["first_conducting_solicitor"] = first_conducting_solicitor

    params["key"] = key

    params["limit"] = limit

    params["number_of_clients"] = number_of_clients

    params["page_token"] = page_token

    params["party"] = party

    params["post_transfer_clients_represented"] = post_transfer_clients_represented

    params["rate_type"] = rate_type

    params["region"] = region

    params["session_type"] = session_type

    params["user_type"] = user_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lauk_civil_certificated_rates",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, LaukCivilCertificatedRateList]]:
    if response.status_code == 200:
        response_200 = LaukCivilCertificatedRateList.from_dict(response.json())

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
) -> Response[Union[Error, LaukCivilCertificatedRateList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    activity: Union[Unset, str] = UNSET,
    activity_sub_category: Union[Unset, str] = UNSET,
    attended_several_hearings_for_multiple_clients: Union[Unset, bool] = UNSET,
    category_of_law: Union[Unset, str] = UNSET,
    change_of_solicitor: Union[Unset, bool] = UNSET,
    court: Union[Unset, str] = UNSET,
    eligible_for_sqm: Union[Unset, bool] = UNSET,
    fee_scheme: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    first_conducting_solicitor: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    number_of_clients: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    party: Union[Unset, str] = UNSET,
    post_transfer_clients_represented: Union[Unset, str] = UNSET,
    rate_type: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
    session_type: Union[Unset, str] = UNSET,
    user_type: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, LaukCivilCertificatedRateList]]:
    """List Civil Certificated Rates

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukCivilCertificatedRates

    Args:
        activity (Union[Unset, str]):
        activity_sub_category (Union[Unset, str]):
        attended_several_hearings_for_multiple_clients (Union[Unset, bool]):
        category_of_law (Union[Unset, str]):
        change_of_solicitor (Union[Unset, bool]):
        court (Union[Unset, str]):
        eligible_for_sqm (Union[Unset, bool]):
        fee_scheme (Union[Unset, str]):
        fields (Union[Unset, str]):
        first_conducting_solicitor (Union[Unset, bool]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        number_of_clients (Union[Unset, str]):
        page_token (Union[Unset, str]):
        party (Union[Unset, str]):
        post_transfer_clients_represented (Union[Unset, str]):
        rate_type (Union[Unset, str]):
        region (Union[Unset, str]):
        session_type (Union[Unset, str]):
        user_type (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LaukCivilCertificatedRateList]]
    """

    kwargs = _get_kwargs(
        activity=activity,
        activity_sub_category=activity_sub_category,
        attended_several_hearings_for_multiple_clients=attended_several_hearings_for_multiple_clients,
        category_of_law=category_of_law,
        change_of_solicitor=change_of_solicitor,
        court=court,
        eligible_for_sqm=eligible_for_sqm,
        fee_scheme=fee_scheme,
        fields=fields,
        first_conducting_solicitor=first_conducting_solicitor,
        key=key,
        limit=limit,
        number_of_clients=number_of_clients,
        page_token=page_token,
        party=party,
        post_transfer_clients_represented=post_transfer_clients_represented,
        rate_type=rate_type,
        region=region,
        session_type=session_type,
        user_type=user_type,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    activity: Union[Unset, str] = UNSET,
    activity_sub_category: Union[Unset, str] = UNSET,
    attended_several_hearings_for_multiple_clients: Union[Unset, bool] = UNSET,
    category_of_law: Union[Unset, str] = UNSET,
    change_of_solicitor: Union[Unset, bool] = UNSET,
    court: Union[Unset, str] = UNSET,
    eligible_for_sqm: Union[Unset, bool] = UNSET,
    fee_scheme: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    first_conducting_solicitor: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    number_of_clients: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    party: Union[Unset, str] = UNSET,
    post_transfer_clients_represented: Union[Unset, str] = UNSET,
    rate_type: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
    session_type: Union[Unset, str] = UNSET,
    user_type: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, LaukCivilCertificatedRateList]]:
    """List Civil Certificated Rates

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukCivilCertificatedRates

    Args:
        activity (Union[Unset, str]):
        activity_sub_category (Union[Unset, str]):
        attended_several_hearings_for_multiple_clients (Union[Unset, bool]):
        category_of_law (Union[Unset, str]):
        change_of_solicitor (Union[Unset, bool]):
        court (Union[Unset, str]):
        eligible_for_sqm (Union[Unset, bool]):
        fee_scheme (Union[Unset, str]):
        fields (Union[Unset, str]):
        first_conducting_solicitor (Union[Unset, bool]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        number_of_clients (Union[Unset, str]):
        page_token (Union[Unset, str]):
        party (Union[Unset, str]):
        post_transfer_clients_represented (Union[Unset, str]):
        rate_type (Union[Unset, str]):
        region (Union[Unset, str]):
        session_type (Union[Unset, str]):
        user_type (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LaukCivilCertificatedRateList]
    """

    return sync_detailed(
        client=client,
        activity=activity,
        activity_sub_category=activity_sub_category,
        attended_several_hearings_for_multiple_clients=attended_several_hearings_for_multiple_clients,
        category_of_law=category_of_law,
        change_of_solicitor=change_of_solicitor,
        court=court,
        eligible_for_sqm=eligible_for_sqm,
        fee_scheme=fee_scheme,
        fields=fields,
        first_conducting_solicitor=first_conducting_solicitor,
        key=key,
        limit=limit,
        number_of_clients=number_of_clients,
        page_token=page_token,
        party=party,
        post_transfer_clients_represented=post_transfer_clients_represented,
        rate_type=rate_type,
        region=region,
        session_type=session_type,
        user_type=user_type,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    activity: Union[Unset, str] = UNSET,
    activity_sub_category: Union[Unset, str] = UNSET,
    attended_several_hearings_for_multiple_clients: Union[Unset, bool] = UNSET,
    category_of_law: Union[Unset, str] = UNSET,
    change_of_solicitor: Union[Unset, bool] = UNSET,
    court: Union[Unset, str] = UNSET,
    eligible_for_sqm: Union[Unset, bool] = UNSET,
    fee_scheme: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    first_conducting_solicitor: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    number_of_clients: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    party: Union[Unset, str] = UNSET,
    post_transfer_clients_represented: Union[Unset, str] = UNSET,
    rate_type: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
    session_type: Union[Unset, str] = UNSET,
    user_type: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, LaukCivilCertificatedRateList]]:
    """List Civil Certificated Rates

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukCivilCertificatedRates

    Args:
        activity (Union[Unset, str]):
        activity_sub_category (Union[Unset, str]):
        attended_several_hearings_for_multiple_clients (Union[Unset, bool]):
        category_of_law (Union[Unset, str]):
        change_of_solicitor (Union[Unset, bool]):
        court (Union[Unset, str]):
        eligible_for_sqm (Union[Unset, bool]):
        fee_scheme (Union[Unset, str]):
        fields (Union[Unset, str]):
        first_conducting_solicitor (Union[Unset, bool]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        number_of_clients (Union[Unset, str]):
        page_token (Union[Unset, str]):
        party (Union[Unset, str]):
        post_transfer_clients_represented (Union[Unset, str]):
        rate_type (Union[Unset, str]):
        region (Union[Unset, str]):
        session_type (Union[Unset, str]):
        user_type (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LaukCivilCertificatedRateList]]
    """

    kwargs = _get_kwargs(
        activity=activity,
        activity_sub_category=activity_sub_category,
        attended_several_hearings_for_multiple_clients=attended_several_hearings_for_multiple_clients,
        category_of_law=category_of_law,
        change_of_solicitor=change_of_solicitor,
        court=court,
        eligible_for_sqm=eligible_for_sqm,
        fee_scheme=fee_scheme,
        fields=fields,
        first_conducting_solicitor=first_conducting_solicitor,
        key=key,
        limit=limit,
        number_of_clients=number_of_clients,
        page_token=page_token,
        party=party,
        post_transfer_clients_represented=post_transfer_clients_represented,
        rate_type=rate_type,
        region=region,
        session_type=session_type,
        user_type=user_type,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    activity: Union[Unset, str] = UNSET,
    activity_sub_category: Union[Unset, str] = UNSET,
    attended_several_hearings_for_multiple_clients: Union[Unset, bool] = UNSET,
    category_of_law: Union[Unset, str] = UNSET,
    change_of_solicitor: Union[Unset, bool] = UNSET,
    court: Union[Unset, str] = UNSET,
    eligible_for_sqm: Union[Unset, bool] = UNSET,
    fee_scheme: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    first_conducting_solicitor: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    number_of_clients: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    party: Union[Unset, str] = UNSET,
    post_transfer_clients_represented: Union[Unset, str] = UNSET,
    rate_type: Union[Unset, str] = UNSET,
    region: Union[Unset, str] = UNSET,
    session_type: Union[Unset, str] = UNSET,
    user_type: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, LaukCivilCertificatedRateList]]:
    """List Civil Certificated Rates

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukCivilCertificatedRates

    Args:
        activity (Union[Unset, str]):
        activity_sub_category (Union[Unset, str]):
        attended_several_hearings_for_multiple_clients (Union[Unset, bool]):
        category_of_law (Union[Unset, str]):
        change_of_solicitor (Union[Unset, bool]):
        court (Union[Unset, str]):
        eligible_for_sqm (Union[Unset, bool]):
        fee_scheme (Union[Unset, str]):
        fields (Union[Unset, str]):
        first_conducting_solicitor (Union[Unset, bool]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        number_of_clients (Union[Unset, str]):
        page_token (Union[Unset, str]):
        party (Union[Unset, str]):
        post_transfer_clients_represented (Union[Unset, str]):
        rate_type (Union[Unset, str]):
        region (Union[Unset, str]):
        session_type (Union[Unset, str]):
        user_type (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LaukCivilCertificatedRateList]
    """

    return (
        await asyncio_detailed(
            client=client,
            activity=activity,
            activity_sub_category=activity_sub_category,
            attended_several_hearings_for_multiple_clients=attended_several_hearings_for_multiple_clients,
            category_of_law=category_of_law,
            change_of_solicitor=change_of_solicitor,
            court=court,
            eligible_for_sqm=eligible_for_sqm,
            fee_scheme=fee_scheme,
            fields=fields,
            first_conducting_solicitor=first_conducting_solicitor,
            key=key,
            limit=limit,
            number_of_clients=number_of_clients,
            page_token=page_token,
            party=party,
            post_transfer_clients_represented=post_transfer_clients_represented,
            rate_type=rate_type,
            region=region,
            session_type=session_type,
            user_type=user_type,
            x_api_version=x_api_version,
        )
    ).parsed
