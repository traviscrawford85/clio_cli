# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.tasks_api_base import BaseTasksApi
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
from openapi_server.models.task_create_request import TaskCreateRequest
from openapi_server.models.task_list import TaskList
from openapi_server.models.task_show import TaskShow
from openapi_server.models.task_update_request import TaskUpdateRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/tasks.json",
    responses={
        201: {"model": TaskShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Tasks"],
    summary="Create a new Task",
    response_model_by_alias=True,
)
async def task_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    task_create_request: Annotated[Optional[TaskCreateRequest], Field(description="Request Body for Tasks")] = Body(None, description="Request Body for Tasks"),
) -> TaskShow:
    """Outlines the parameters and data fields used when creating a new Task"""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().task_create(x_api_version, fields, task_create_request)


@router.delete(
    "/tasks/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Tasks"],
    summary="Delete a single Task",
    response_model_by_alias=True,
)
async def task_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Task.")] = Path(..., description="The unique identifier for the Task."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Task"""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().task_destroy(id, x_api_version)


@router.get(
    "/tasks.json",
    responses={
        200: {"model": TaskList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Tasks"],
    summary="Return the data for all Tasks",
    response_model_by_alias=True,
)
async def task_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    assignee_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User or Contact. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")] = Query(None, description="The unique identifier for a single User or Contact. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.", alias="assignee_id"),
    assignee_type: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with a specific assignee. Must be passed if filtering by assignee.")] = Query(None, description="Filter Task records to those with a specific assignee. Must be passed if filtering by assignee.", alias="assignee_type"),
    assigner_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.", alias="assigner_id"),
    cascading_source_id: Annotated[Optional[StrictInt], Field(description="Filter Task records to those with a parent task that has the specified ID.")] = Query(None, description="Filter Task records to those with a parent task that has the specified ID.", alias="cascading_source_id"),
    client_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.", alias="client_id"),
    complete: Annotated[Optional[StrictBool], Field(description="Filter Task records to those which are complete or not.")] = Query(None, description="Filter Task records to those which are complete or not.", alias="complete"),
    created_since: Annotated[Optional[datetime], Field(description="Filter Task records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Task records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    due_at_from: Annotated[Optional[date], Field(description="Start of date range when querying by due_at in a range. (Expects an ISO-8601 date).")] = Query(None, description="Start of date range when querying by due_at in a range. (Expects an ISO-8601 date).", alias="due_at_from"),
    due_at_present: Annotated[Optional[StrictBool], Field(description="Filter Task records to those that have a due date specified, or not.")] = Query(None, description="Filter Task records to those that have a due date specified, or not.", alias="due_at_present"),
    due_at_to: Annotated[Optional[date], Field(description="End of date range when querying by due_at in a range. (Expects an ISO-8601 date).")] = Query(None, description="End of date range when querying by due_at in a range. (Expects an ISO-8601 date).", alias="due_at_to"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Task records to those having the specified unique identifiers.")] = Query(None, description="Filter Task records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Task records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Task records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.", alias="matter_id"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Task records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Task records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    permission: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given permission. Returns all tasks by default.")] = Query(None, description="Filter Task records to those with the given permission. Returns all tasks by default.", alias="permission"),
    priority: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given priority.")] = Query(None, description="Filter Task records to those with the given priority.", alias="priority"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` or `description` matching a given string.")] = Query(None, description="Wildcard search for &#x60;name&#x60; or &#x60;description&#x60; matching a given string.", alias="query"),
    responsible_attorney_id: Annotated[Optional[StrictInt], Field(description="Filter Task records to those that have an associated matter with a responsible attorney ID.")] = Query(None, description="Filter Task records to those that have an associated matter with a responsible attorney ID.", alias="responsible_attorney_id"),
    status: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given status. Users without advanced tasks enabled may only specify 'complete' or 'pending'.")] = Query(None, description="Filter Task records to those with the given status. Users without advanced tasks enabled may only specify &#39;complete&#39; or &#39;pending&#39;.", alias="status"),
    statuses: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given statuses. Users without advanced tasks enabled may only specify 'complete' or 'pending'.")] = Query(None, description="Filter Task records to those with the given statuses. Users without advanced tasks enabled may only specify &#39;complete&#39; or &#39;pending&#39;.", alias="statuses[]"),
    statute_of_limitations: Annotated[Optional[StrictBool], Field(description="Filter Task records to those which are a statute of limitations or not.")] = Query(None, description="Filter Task records to those which are a statute of limitations or not.", alias="statute_of_limitations"),
    task_type_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single TaskType. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")] = Query(None, description="The unique identifier for a single TaskType. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.", alias="task_type_id"),
    time_entries_present: Annotated[Optional[StrictBool], Field(description="Filter Task records to those that have associated time entries, or not.")] = Query(None, description="Filter Task records to those that have associated time entries, or not.", alias="time_entries_present"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Task records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Task records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> TaskList:
    """Outlines the parameters, optional and required, used when requesting the data for all Tasks"""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().task_index(x_api_version, assignee_id, assignee_type, assigner_id, cascading_source_id, client_id, complete, created_since, due_at_from, due_at_present, due_at_to, fields, ids, limit, matter_id, order, page_token, permission, priority, query, responsible_attorney_id, status, statuses, statute_of_limitations, task_type_id, time_entries_present, updated_since)


@router.get(
    "/tasks/{id}.json",
    responses={
        200: {"model": TaskShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Tasks"],
    summary="Return the data for a single Task",
    response_model_by_alias=True,
)
async def task_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Task.")] = Path(..., description="The unique identifier for the Task."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> TaskShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Task"""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().task_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/tasks/{id}.json",
    responses={
        200: {"model": TaskShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Tasks"],
    summary="Update a single Task",
    response_model_by_alias=True,
)
async def task_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Task.")] = Path(..., description="The unique identifier for the Task."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    task_update_request: Annotated[Optional[TaskUpdateRequest], Field(description="Request Body for Tasks")] = Body(None, description="Request Body for Tasks"),
) -> TaskShow:
    """Outlines the parameters and data fields used when updating a single Task"""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().task_update(id, if_match, x_api_version, fields, task_update_request)
