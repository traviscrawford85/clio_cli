# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.expense_categories_api_base import BaseExpenseCategoriesApi
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
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.expense_category_create_request import ExpenseCategoryCreateRequest
from openapi_server.models.expense_category_list import ExpenseCategoryList
from openapi_server.models.expense_category_show import ExpenseCategoryShow
from openapi_server.models.expense_category_update_request import ExpenseCategoryUpdateRequest
from openapi_server.models.lauk_expense_category_list import LaukExpenseCategoryList


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/expense_categories.json",
    responses={
        201: {"model": ExpenseCategoryShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Expense Categories"],
    summary="Create a new ExpenseCategory",
    response_model_by_alias=True,
)
async def expense_category_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    expense_category_create_request: Annotated[Optional[ExpenseCategoryCreateRequest], Field(description="Request Body for Expense Categories")] = Body(None, description="Request Body for Expense Categories"),
) -> ExpenseCategoryShow:
    """Outlines the parameters and data fields used when creating a new ExpenseCategory"""
    if not BaseExpenseCategoriesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExpenseCategoriesApi.subclasses[0]().expense_category_create(x_api_version, fields, expense_category_create_request)


@router.delete(
    "/expense_categories/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Expense Categories"],
    summary="Delete a single ExpenseCategory",
    response_model_by_alias=True,
)
async def expense_category_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ExpenseCategory.")] = Path(..., description="The unique identifier for the ExpenseCategory."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single ExpenseCategory"""
    if not BaseExpenseCategoriesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExpenseCategoriesApi.subclasses[0]().expense_category_destroy(id, x_api_version)


@router.get(
    "/expense_categories.json",
    responses={
        200: {"model": ExpenseCategoryList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Expense Categories"],
    summary="Return the data for all ExpenseCategories",
    response_model_by_alias=True,
)
async def expense_category_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter ExpenseCategory records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter ExpenseCategory records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    entry_type: Annotated[Optional[StrictStr], Field(description="Filter ExpenseCategory records to those that match the given type.")] = Query(None, description="Filter ExpenseCategory records to those that match the given type.", alias="entry_type"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ExpenseCategory records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of ExpenseCategory records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the ExpenseCategory records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the ExpenseCategory records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Allows matching search on expense category name.")] = Query(None, description="Allows matching search on expense category name.", alias="query"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter ExpenseCategory records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter ExpenseCategory records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> ExpenseCategoryList:
    """Outlines the parameters, optional and required, used when requesting the data for all ExpenseCategories"""
    if not BaseExpenseCategoriesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExpenseCategoriesApi.subclasses[0]().expense_category_index(x_api_version, created_since, entry_type, fields, limit, order, page_token, query, updated_since)


@router.get(
    "/expense_categories/{id}.json",
    responses={
        200: {"model": ExpenseCategoryShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Expense Categories"],
    summary="Return the data for a single ExpenseCategory",
    response_model_by_alias=True,
)
async def expense_category_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ExpenseCategory.")] = Path(..., description="The unique identifier for the ExpenseCategory."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> ExpenseCategoryShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single ExpenseCategory"""
    if not BaseExpenseCategoriesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExpenseCategoriesApi.subclasses[0]().expense_category_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/expense_categories/{id}.json",
    responses={
        200: {"model": ExpenseCategoryShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Expense Categories"],
    summary="Update a single ExpenseCategory",
    response_model_by_alias=True,
)
async def expense_category_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ExpenseCategory.")] = Path(..., description="The unique identifier for the ExpenseCategory."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    expense_category_update_request: Annotated[Optional[ExpenseCategoryUpdateRequest], Field(description="Request Body for Expense Categories")] = Body(None, description="Request Body for Expense Categories"),
) -> ExpenseCategoryShow:
    """Outlines the parameters and data fields used when updating a single ExpenseCategory"""
    if not BaseExpenseCategoriesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExpenseCategoriesApi.subclasses[0]().expense_category_update(id, if_match, x_api_version, fields, expense_category_update_request)


@router.get(
    "/lauk_expense_categories.json",
    responses={
        200: {"model": LaukExpenseCategoryList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Expense Categories"],
    summary="List Expense Categories",
    response_model_by_alias=True,
)
async def lauk_expense_category_index(
    region: Annotated[StrictStr, Field(description="Sets the expense rate returned based on the region. If the region is set to London, it will return the London rate; otherwise, it will return the non-London rate.")] = Query(None, description="Sets the expense rate returned based on the region. If the region is set to London, it will return the London rate; otherwise, it will return the non-London rate.", alias="region"),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    key: Annotated[Optional[StrictStr], Field(description="Filter by key.")] = Query(None, description="Filter by key.", alias="key"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of LaukExpenseCategory records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of LaukExpenseCategory records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    name: Annotated[Optional[StrictStr], Field(description="Filter by expense name.")] = Query(None, description="Filter by expense name.", alias="name"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    practice_area: Annotated[Optional[StrictStr], Field(description="Filter by expense practice area.")] = Query(None, description="Filter by expense practice area.", alias="practice_area"),
) -> LaukExpenseCategoryList:
    """Outlines the parameters, optional and required, used when requesting the data for all LaukExpenseCategories"""
    if not BaseExpenseCategoriesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExpenseCategoriesApi.subclasses[0]().lauk_expense_category_index(region, x_api_version, fields, key, limit, name, page_token, practice_area)
