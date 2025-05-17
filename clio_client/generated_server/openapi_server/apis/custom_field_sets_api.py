# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.custom_field_sets_api_base import BaseCustomFieldSetsApi
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
from openapi_server.models.custom_field_set_create_request import CustomFieldSetCreateRequest
from openapi_server.models.custom_field_set_list import CustomFieldSetList
from openapi_server.models.custom_field_set_show import CustomFieldSetShow
from openapi_server.models.custom_field_set_update_request import CustomFieldSetUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/custom_field_sets.json",
    responses={
        201: {"model": CustomFieldSetShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Custom Field Sets"],
    summary="Create a new CustomFieldSet",
    response_model_by_alias=True,
)
async def custom_field_set_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    custom_field_set_create_request: Annotated[Optional[CustomFieldSetCreateRequest], Field(description="Request Body for Custom Field Sets")] = Body(None, description="Request Body for Custom Field Sets"),
) -> CustomFieldSetShow:
    """Outlines the parameters and data fields used when creating a new CustomFieldSet"""
    if not BaseCustomFieldSetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCustomFieldSetsApi.subclasses[0]().custom_field_set_create(x_api_version, fields, custom_field_set_create_request)


@router.delete(
    "/custom_field_sets/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Custom Field Sets"],
    summary="Delete a single CustomFieldSet",
    response_model_by_alias=True,
)
async def custom_field_set_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the CustomFieldSet.")] = Path(..., description="The unique identifier for the CustomFieldSet."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single CustomFieldSet"""
    if not BaseCustomFieldSetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCustomFieldSetsApi.subclasses[0]().custom_field_set_destroy(id, x_api_version)


@router.get(
    "/custom_field_sets.json",
    responses={
        200: {"model": CustomFieldSetList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Custom Field Sets"],
    summary="Return the data for all CustomFieldSets",
    response_model_by_alias=True,
)
async def custom_field_set_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter CustomFieldSet records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter CustomFieldSet records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    displayed: Annotated[Optional[StrictBool], Field(description="Filter CustomFieldSet records to those that should be displayed by default.")] = Query(None, description="Filter CustomFieldSet records to those that should be displayed by default.", alias="displayed"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter CustomFieldSet records to those having the specified unique identifiers.")] = Query(None, description="Filter CustomFieldSet records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of CustomFieldSet records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of CustomFieldSet records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the CustomFieldSet records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the CustomFieldSet records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    parent_type: Annotated[Optional[StrictStr], Field(description="Filter CustomFieldSet records to those that have the specified `parent_type`.")] = Query(None, description="Filter CustomFieldSet records to those that have the specified &#x60;parent_type&#x60;.", alias="parent_type"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching a given string.")] = Query(None, description="Wildcard search for &#x60;name&#x60; matching a given string.", alias="query"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter CustomFieldSet records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter CustomFieldSet records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> CustomFieldSetList:
    """Outlines the parameters, optional and required, used when requesting the data for all CustomFieldSets"""
    if not BaseCustomFieldSetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCustomFieldSetsApi.subclasses[0]().custom_field_set_index(x_api_version, created_since, displayed, fields, ids, limit, order, page_token, parent_type, query, updated_since)


@router.get(
    "/custom_field_sets/{id}.json",
    responses={
        200: {"model": CustomFieldSetShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Custom Field Sets"],
    summary="Return the data for a single CustomFieldSet",
    response_model_by_alias=True,
)
async def custom_field_set_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the CustomFieldSet.")] = Path(..., description="The unique identifier for the CustomFieldSet."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> CustomFieldSetShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single CustomFieldSet"""
    if not BaseCustomFieldSetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCustomFieldSetsApi.subclasses[0]().custom_field_set_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/custom_field_sets/{id}.json",
    responses={
        200: {"model": CustomFieldSetShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Custom Field Sets"],
    summary="Update a single CustomFieldSet",
    response_model_by_alias=True,
)
async def custom_field_set_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the CustomFieldSet.")] = Path(..., description="The unique identifier for the CustomFieldSet."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    custom_field_set_update_request: Annotated[Optional[CustomFieldSetUpdateRequest], Field(description="Request Body for Custom Field Sets")] = Body(None, description="Request Body for Custom Field Sets"),
) -> CustomFieldSetShow:
    """Outlines the parameters and data fields used when updating a single CustomFieldSet"""
    if not BaseCustomFieldSetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCustomFieldSetsApi.subclasses[0]().custom_field_set_update(id, if_match, x_api_version, fields, custom_field_set_update_request)
