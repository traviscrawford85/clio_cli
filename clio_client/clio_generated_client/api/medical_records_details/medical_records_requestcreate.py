from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.medical_records_request_show import MedicalRecordsRequestShow
from ...models.medical_records_requestcreate_data_body import MedicalRecordsRequestcreateDataBody
from ...models.medical_records_requestcreate_files_body import MedicalRecordsRequestcreateFilesBody
from ...models.medical_records_requestcreate_json_body import MedicalRecordsRequestcreateJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        MedicalRecordsRequestcreateJsonBody,
        MedicalRecordsRequestcreateDataBody,
        MedicalRecordsRequestcreateFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/medical_records_details",
        "params": params,
    }

    if isinstance(body, MedicalRecordsRequestcreateJsonBody):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, MedicalRecordsRequestcreateDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, MedicalRecordsRequestcreateFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, MedicalRecordsRequestShow]]:
    if response.status_code == 201:
        response_201 = MedicalRecordsRequestShow.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422
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
) -> Response[Union[Error, MedicalRecordsRequestShow]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        MedicalRecordsRequestcreateJsonBody,
        MedicalRecordsRequestcreateDataBody,
        MedicalRecordsRequestcreateFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, MedicalRecordsRequestShow]]:
    """Creating a Medical Records Detail, Medical Records and Medical Bills

     This endpoint allows a creation of a Medical Records Detail, multiple Medical Records and Medical
    Bills.
    Medical Liens can also be created as a property under Medical Bills.

    Reference the payload to see how the records are being passed in.

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (MedicalRecordsRequestcreateJsonBody):
        body (MedicalRecordsRequestcreateDataBody):
        body (MedicalRecordsRequestcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MedicalRecordsRequestShow]]
    """

    kwargs = _get_kwargs(
        body=body,
        fields=fields,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        MedicalRecordsRequestcreateJsonBody,
        MedicalRecordsRequestcreateDataBody,
        MedicalRecordsRequestcreateFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, MedicalRecordsRequestShow]]:
    """Creating a Medical Records Detail, Medical Records and Medical Bills

     This endpoint allows a creation of a Medical Records Detail, multiple Medical Records and Medical
    Bills.
    Medical Liens can also be created as a property under Medical Bills.

    Reference the payload to see how the records are being passed in.

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (MedicalRecordsRequestcreateJsonBody):
        body (MedicalRecordsRequestcreateDataBody):
        body (MedicalRecordsRequestcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MedicalRecordsRequestShow]
    """

    return sync_detailed(
        client=client,
        body=body,
        fields=fields,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        MedicalRecordsRequestcreateJsonBody,
        MedicalRecordsRequestcreateDataBody,
        MedicalRecordsRequestcreateFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, MedicalRecordsRequestShow]]:
    """Creating a Medical Records Detail, Medical Records and Medical Bills

     This endpoint allows a creation of a Medical Records Detail, multiple Medical Records and Medical
    Bills.
    Medical Liens can also be created as a property under Medical Bills.

    Reference the payload to see how the records are being passed in.

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (MedicalRecordsRequestcreateJsonBody):
        body (MedicalRecordsRequestcreateDataBody):
        body (MedicalRecordsRequestcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MedicalRecordsRequestShow]]
    """

    kwargs = _get_kwargs(
        body=body,
        fields=fields,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        MedicalRecordsRequestcreateJsonBody,
        MedicalRecordsRequestcreateDataBody,
        MedicalRecordsRequestcreateFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, MedicalRecordsRequestShow]]:
    """Creating a Medical Records Detail, Medical Records and Medical Bills

     This endpoint allows a creation of a Medical Records Detail, multiple Medical Records and Medical
    Bills.
    Medical Liens can also be created as a property under Medical Bills.

    Reference the payload to see how the records are being passed in.

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (MedicalRecordsRequestcreateJsonBody):
        body (MedicalRecordsRequestcreateDataBody):
        body (MedicalRecordsRequestcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MedicalRecordsRequestShow]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            fields=fields,
            x_api_version=x_api_version,
        )
    ).parsed
