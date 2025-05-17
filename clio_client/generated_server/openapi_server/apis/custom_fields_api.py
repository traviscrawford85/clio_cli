# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.custom_fields_api_base import BaseCustomFieldsApi
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
from openapi_server.models.custom_field_create_request import CustomFieldCreateRequest
from openapi_server.models.custom_field_list import CustomFieldList
from openapi_server.models.custom_field_show import CustomFieldShow
from openapi_server.models.custom_field_update_request import CustomFieldUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/custom_fields.json",
    responses={
        201: {"model": CustomFieldShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Custom Fields"],
    summary="Create a new CustomField",
    response_model_by_alias=True,
)
async def custom_field_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    custom_field_create_request: Annotated[Optional[CustomFieldCreateRequest], Field(description="Request Body for Custom Fields")] = Body(None, description="Request Body for Custom Fields"),
) -> CustomFieldShow:
    """Outlines the parameters and data fields used when creating a new CustomField"""
    if not BaseCustomFieldsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCustomFieldsApi.subclasses[0]().custom_field_create(x_api_version, fields, custom_field_create_request)


@router.delete(
    "/custom_fields/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Custom Fields"],
    summary="Delete a single CustomField",
    response_model_by_alias=True,
)
async def custom_field_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the CustomField.")] = Path(..., description="The unique identifier for the CustomField."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single CustomField"""
    if not BaseCustomFieldsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCustomFieldsApi.subclasses[0]().custom_field_destroy(id, x_api_version)


@router.get(
    "/custom_fields.json",
    responses={
        200: {"model": CustomFieldList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Custom Fields"],
    summary="Return the data for all CustomFields",
    response_model_by_alias=True,
)
async def custom_field_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter CustomField records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter CustomField records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    deleted: Annotated[Optional[StrictBool], Field(description="Filter CustomField records to those that have been deleted for future use.")] = Query(None, description="Filter CustomField records to those that have been deleted for future use.", alias="deleted"),
    field_type: Annotated[Optional[StrictStr], Field(description="Field type of this custom field")] = Query(None, description="Field type of this custom field", alias="field_type"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter CustomField records to those having the specified unique identifiers.")] = Query(None, description="Filter CustomField records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of CustomField records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of CustomField records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the CustomField records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the CustomField records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    parent_type: Annotated[Optional[StrictStr], Field(description="Filter CustomField records to those that have the specified `parent_type`.")] = Query(None, description="Filter CustomField records to those that have the specified &#x60;parent_type&#x60;.", alias="parent_type"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching a given string.")] = Query(None, description="Wildcard search for &#x60;name&#x60; matching a given string.", alias="query"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter CustomField records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter CustomField records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
    visible_and_required: Annotated[Optional[StrictBool], Field(description="Filter CustomField records to those that are visible and required.")] = Query(None, description="Filter CustomField records to those that are visible and required.", alias="visible_and_required"),
) -> CustomFieldList:
    """Outlines the parameters, optional and required, used when requesting the data for all CustomFields"""
    if not BaseCustomFieldsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCustomFieldsApi.subclasses[0]().custom_field_index(x_api_version, created_since, deleted, field_type, fields, ids, limit, order, page_token, parent_type, query, updated_since, visible_and_required)


@router.get(
    "/custom_fields/{id}.json",
    responses={
        200: {"model": CustomFieldShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Custom Fields"],
    summary="Return the data for a single CustomField",
    response_model_by_alias=True,
)
async def custom_field_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the CustomField.")] = Path(..., description="The unique identifier for the CustomField."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> CustomFieldShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single CustomField"""
    if not BaseCustomFieldsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCustomFieldsApi.subclasses[0]().custom_field_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/custom_fields/{id}.json",
    responses={
        200: {"model": CustomFieldShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Custom Fields"],
    summary="Update a single CustomField",
    response_model_by_alias=True,
)
async def custom_field_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the CustomField.")] = Path(..., description="The unique identifier for the CustomField."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    custom_field_update_request: Annotated[Optional[CustomFieldUpdateRequest], Field(description="Request Body for Custom Fields")] = Body(None, description="Request Body for Custom Fields"),
) -> CustomFieldShow:
    """Outlines the parameters and data fields used when updating a single CustomField"""
    if not BaseCustomFieldsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCustomFieldsApi.subclasses[0]().custom_field_update(id, if_match, x_api_version, fields, custom_field_update_request)
