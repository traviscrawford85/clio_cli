# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.task_template_lists_api_base import BaseTaskTemplateListsApi
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
from openapi_server.models.error import Error
from openapi_server.models.task_template_list_copy_request import TaskTemplateListCopyRequest
from openapi_server.models.task_template_list_create_request import TaskTemplateListCreateRequest
from openapi_server.models.task_template_list_list import TaskTemplateListList
from openapi_server.models.task_template_list_show import TaskTemplateListShow
from openapi_server.models.task_template_list_update_request import TaskTemplateListUpdateRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/task_template_lists/{id}/copy.json",
    responses={
        404: {"model": Error, "description": "Not Found"},
        400: {"model": Error, "description": "Bad Request"},
        201: {"model": TaskTemplateListShow, "description": "Created"},
    },
    tags=["Task Template Lists"],
    summary="Copy a TaskTemplateList",
    response_model_by_alias=True,
)
async def task_template_list_copy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the TaskTemplateList.")] = Path(..., description="The unique identifier for the TaskTemplateList."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    task_template_list_copy_request: Annotated[Optional[TaskTemplateListCopyRequest], Field(description="Request Body for Task Template Lists")] = Body(None, description="Request Body for Task Template Lists"),
) -> TaskTemplateListShow:
    """Creates a copy of the TaskTemplateList identified by the &#x60;id&#x60; path parameter. """
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_copy(id, fields, task_template_list_copy_request)


@router.post(
    "/task_template_lists.json",
    responses={
        201: {"model": TaskTemplateListShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Task Template Lists"],
    summary="Create a new TaskTemplateList",
    response_model_by_alias=True,
)
async def task_template_list_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    task_template_list_create_request: Annotated[Optional[TaskTemplateListCreateRequest], Field(description="Request Body for Task Template Lists")] = Body(None, description="Request Body for Task Template Lists"),
) -> TaskTemplateListShow:
    """Outlines the parameters and data fields used when creating a new TaskTemplateList"""
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_create(x_api_version, fields, task_template_list_create_request)


@router.delete(
    "/task_template_lists/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Task Template Lists"],
    summary="Delete a single TaskTemplateList",
    response_model_by_alias=True,
)
async def task_template_list_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the TaskTemplateList.")] = Path(..., description="The unique identifier for the TaskTemplateList."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single TaskTemplateList"""
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_destroy(id, x_api_version)


@router.get(
    "/task_template_lists.json",
    responses={
        200: {"model": TaskTemplateListList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Task Template Lists"],
    summary="Return the data for all TaskTemplateLists",
    response_model_by_alias=True,
)
async def task_template_list_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter TaskTemplateList records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter TaskTemplateList records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    empty: Annotated[Optional[StrictBool], Field(description="Filter TaskTemplateList records to those that either contain at least one task template or contain none.")] = Query(None, description="Filter TaskTemplateList records to those that either contain at least one task template or contain none.", alias="empty"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter TaskTemplateList records to those having the specified unique identifiers.")] = Query(None, description="Filter TaskTemplateList records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of TaskTemplateList records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of TaskTemplateList records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the TaskTemplateList records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the TaskTemplateList records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    practice_area_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single PracticeArea. Use the keyword `null` to match those without a TaskTemplateList. The list will be filtered to include only the TaskTemplateList records with the matching property.")] = Query(None, description="The unique identifier for a single PracticeArea. Use the keyword &#x60;null&#x60; to match those without a TaskTemplateList. The list will be filtered to include only the TaskTemplateList records with the matching property.", alias="practice_area_id"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching a given string.")] = Query(None, description="Wildcard search for &#x60;name&#x60; matching a given string.", alias="query"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter TaskTemplateList records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter TaskTemplateList records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> TaskTemplateListList:
    """Outlines the parameters, optional and required, used when requesting the data for all TaskTemplateLists"""
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_index(x_api_version, created_since, empty, fields, ids, limit, order, page_token, practice_area_id, query, updated_since)


@router.get(
    "/task_template_lists/{id}.json",
    responses={
        200: {"model": TaskTemplateListShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Task Template Lists"],
    summary="Return the data for a single TaskTemplateList",
    response_model_by_alias=True,
)
async def task_template_list_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the TaskTemplateList.")] = Path(..., description="The unique identifier for the TaskTemplateList."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> TaskTemplateListShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single TaskTemplateList"""
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/task_template_lists/{id}.json",
    responses={
        200: {"model": TaskTemplateListShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Task Template Lists"],
    summary="Update a single TaskTemplateList",
    response_model_by_alias=True,
)
async def task_template_list_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the TaskTemplateList.")] = Path(..., description="The unique identifier for the TaskTemplateList."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    task_template_list_update_request: Annotated[Optional[TaskTemplateListUpdateRequest], Field(description="Request Body for Task Template Lists")] = Body(None, description="Request Body for Task Template Lists"),
) -> TaskTemplateListShow:
    """Outlines the parameters and data fields used when updating a single TaskTemplateList"""
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_update(id, if_match, x_api_version, fields, task_template_list_update_request)
