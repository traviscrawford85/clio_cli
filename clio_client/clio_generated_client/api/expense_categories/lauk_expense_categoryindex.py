from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.lauk_expense_category_list import LaukExpenseCategoryList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[Unset, str] = UNSET,
    key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    practice_area: Union[Unset, str] = UNSET,
    region: str,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["fields"] = fields

    params["key"] = key

    params["limit"] = limit

    params["name"] = name

    params["page_token"] = page_token

    params["practice_area"] = practice_area

    params["region"] = region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lauk_expense_categories",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, LaukExpenseCategoryList]]:
    if response.status_code == 200:
        response_200 = LaukExpenseCategoryList.from_dict(response.json())

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
) -> Response[Union[Error, LaukExpenseCategoryList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    practice_area: Union[Unset, str] = UNSET,
    region: str,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, LaukExpenseCategoryList]]:
    """List Expense Categories

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukExpenseCategories

    Args:
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        page_token (Union[Unset, str]):
        practice_area (Union[Unset, str]):
        region (str):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LaukExpenseCategoryList]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        key=key,
        limit=limit,
        name=name,
        page_token=page_token,
        practice_area=practice_area,
        region=region,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    practice_area: Union[Unset, str] = UNSET,
    region: str,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, LaukExpenseCategoryList]]:
    """List Expense Categories

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukExpenseCategories

    Args:
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        page_token (Union[Unset, str]):
        practice_area (Union[Unset, str]):
        region (str):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LaukExpenseCategoryList]
    """

    return sync_detailed(
        client=client,
        fields=fields,
        key=key,
        limit=limit,
        name=name,
        page_token=page_token,
        practice_area=practice_area,
        region=region,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    practice_area: Union[Unset, str] = UNSET,
    region: str,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, LaukExpenseCategoryList]]:
    """List Expense Categories

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukExpenseCategories

    Args:
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        page_token (Union[Unset, str]):
        practice_area (Union[Unset, str]):
        region (str):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LaukExpenseCategoryList]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        key=key,
        limit=limit,
        name=name,
        page_token=page_token,
        practice_area=practice_area,
        region=region,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, str] = UNSET,
    key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    practice_area: Union[Unset, str] = UNSET,
    region: str,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, LaukExpenseCategoryList]]:
    """List Expense Categories

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukExpenseCategories

    Args:
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        page_token (Union[Unset, str]):
        practice_area (Union[Unset, str]):
        region (str):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LaukExpenseCategoryList]
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
            key=key,
            limit=limit,
            name=name,
            page_token=page_token,
            practice_area=practice_area,
            region=region,
            x_api_version=x_api_version,
        )
    ).parsed
