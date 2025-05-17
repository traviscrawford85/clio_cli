# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.bank_accounts_api_base import BaseBankAccountsApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.bank_account_create_request import BankAccountCreateRequest
from openapi_server.models.bank_account_list import BankAccountList
from openapi_server.models.bank_account_show import BankAccountShow
from openapi_server.models.bank_account_update_request import BankAccountUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/bank_accounts.json",
    responses={
        201: {"model": BankAccountShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Bank Accounts"],
    summary="Create a new BankAccount",
    response_model_by_alias=True,
)
async def bank_account_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    bank_account_create_request: Annotated[Optional[BankAccountCreateRequest], Field(description="Request Body for Bank Accounts")] = Body(None, description="Request Body for Bank Accounts"),
) -> BankAccountShow:
    """Outlines the parameters and data fields used when creating a new BankAccount"""
    if not BaseBankAccountsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBankAccountsApi.subclasses[0]().bank_account_create(x_api_version, fields, bank_account_create_request)


@router.delete(
    "/bank_accounts/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Bank Accounts"],
    summary="Delete a single BankAccount",
    response_model_by_alias=True,
)
async def bank_account_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the BankAccount.")] = Path(..., description="The unique identifier for the BankAccount."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single BankAccount"""
    if not BaseBankAccountsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBankAccountsApi.subclasses[0]().bank_account_destroy(id, x_api_version)


@router.get(
    "/bank_accounts.json",
    responses={
        200: {"model": BankAccountList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Bank Accounts"],
    summary="Return the data for all BankAccounts",
    response_model_by_alias=True,
)
async def bank_account_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter BankAccount records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter BankAccount records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter BankAccount records to those having the specified unique identifiers.")] = Query(None, description="Filter BankAccount records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of BankAccount records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of BankAccount records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the BankAccount records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the BankAccount records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    show_empty_accounts: Annotated[Optional[StrictBool], Field(description="Filter BankAccount records to those having a zero or non zero balance.")] = Query(None, description="Filter BankAccount records to those having a zero or non zero balance.", alias="show_empty_accounts"),
    type: Annotated[Optional[StrictStr], Field(description="Filter BankAccount records to those having a specific type.")] = Query(None, description="Filter BankAccount records to those having a specific type.", alias="type"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter BankAccount records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter BankAccount records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
    user_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BankAccount. The list will be filtered to include only the BankAccount records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BankAccount. The list will be filtered to include only the BankAccount records with the matching property.", alias="user_id"),
) -> BankAccountList:
    """Outlines the parameters, optional and required, used when requesting the data for all BankAccounts"""
    if not BaseBankAccountsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBankAccountsApi.subclasses[0]().bank_account_index(x_api_version, created_since, fields, ids, limit, order, page_token, show_empty_accounts, type, updated_since, user_id)


@router.get(
    "/bank_accounts/{id}.json",
    responses={
        200: {"model": BankAccountShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Bank Accounts"],
    summary="Return the data for a single BankAccount",
    response_model_by_alias=True,
)
async def bank_account_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the BankAccount.")] = Path(..., description="The unique identifier for the BankAccount."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> BankAccountShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single BankAccount"""
    if not BaseBankAccountsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBankAccountsApi.subclasses[0]().bank_account_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/bank_accounts/{id}.json",
    responses={
        200: {"model": BankAccountShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Bank Accounts"],
    summary="Update a single BankAccount",
    response_model_by_alias=True,
)
async def bank_account_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the BankAccount.")] = Path(..., description="The unique identifier for the BankAccount."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    bank_account_update_request: Annotated[Optional[BankAccountUpdateRequest], Field(description="Request Body for Bank Accounts")] = Body(None, description="Request Body for Bank Accounts"),
) -> BankAccountShow:
    """Outlines the parameters and data fields used when updating a single BankAccount"""
    if not BaseBankAccountsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBankAccountsApi.subclasses[0]().bank_account_update(id, if_match, x_api_version, fields, bank_account_update_request)
