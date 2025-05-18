# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.tasks_api_base import BaseTasksApi
import clio_mock.impl

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

from clio_mock.models.extra_models import TokenModel  # noqa: F401
from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.error import Error
from clio_mock.models.task_create_request import TaskCreateRequest
from clio_mock.models.task_update_request import TaskUpdateRequest


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/tasks.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    task_create_request: Annotated[Optional[TaskCreateRequest], Field(description="Request Body for Tasks")] = Body(None, description="Request Body for Tasks"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new Task"""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().task_create(x_api_versio_nheader, fieldsquery, task_create_request)


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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Task"""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().task_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/tasks.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    assignee_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User or Contact. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")] = Query(None, description="The unique identifier for a single User or Contact. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.", alias="assignee_idquery"),
    assignee_typequery: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with a specific assignee. Must be passed if filtering by assignee.")] = Query(None, description="Filter Task records to those with a specific assignee. Must be passed if filtering by assignee.", alias="assignee_typequery"),
    assigner_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.", alias="assigner_idquery"),
    cascading_source_idquery: Annotated[Optional[StrictInt], Field(description="Filter Task records to those with a parent task that has the specified ID.")] = Query(None, description="Filter Task records to those with a parent task that has the specified ID.", alias="cascading_source_idquery"),
    client_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.", alias="client_idquery"),
    completequery: Annotated[Optional[StrictBool], Field(description="Filter Task records to those which are complete or not.")] = Query(None, description="Filter Task records to those which are complete or not.", alias="completequery"),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    due_at_fromquery: Annotated[Optional[date], Field(description="Start of date range when querying by due_at in a range. (Expects an ISO-8601 date).")] = Query(None, description="Start of date range when querying by due_at in a range. (Expects an ISO-8601 date).", alias="due_at_fromquery"),
    due_at_presentquery: Annotated[Optional[StrictBool], Field(description="Filter Task records to those that have a due date specified, or not.")] = Query(None, description="Filter Task records to those that have a due date specified, or not.", alias="due_at_presentquery"),
    due_at_toquery: Annotated[Optional[date], Field(description="End of date range when querying by due_at in a range. (Expects an ISO-8601 date).")] = Query(None, description="End of date range when querying by due_at in a range. (Expects an ISO-8601 date).", alias="due_at_toquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="matter_idquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    permissionquery: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given permission. Returns all tasks by default.")] = Query(None, description="Filter Task records to those with the given permission. Returns all tasks by default.", alias="permissionquery"),
    priorityquery: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given priority.")] = Query(None, description="Filter Task records to those with the given priority.", alias="priorityquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    responsible_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.", alias="responsible_attorney_idquery"),
    statusquery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those that are draft, billed, unbilled or non-billable.")] = Query(None, description="Filter Activity records to those that are draft, billed, unbilled or non-billable.", alias="statusquery"),
    statusesquery: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given statuses. Users without advanced tasks enabled may only specify 'complete' or 'pending'.")] = Query(None, description="Filter Task records to those with the given statuses. Users without advanced tasks enabled may only specify &#39;complete&#39; or &#39;pending&#39;.", alias="statusesquery"),
    statute_of_limitationsquery: Annotated[Optional[StrictBool], Field(description="Filter Task records to those which are a statute of limitations or not.")] = Query(None, description="Filter Task records to those which are a statute of limitations or not.", alias="statute_of_limitationsquery"),
    task_type_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single TaskType. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")] = Query(None, description="The unique identifier for a single TaskType. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.", alias="task_type_idquery"),
    time_entries_presentquery: Annotated[Optional[StrictBool], Field(description="Filter Task records to those that have associated time entries, or not.")] = Query(None, description="Filter Task records to those that have associated time entries, or not.", alias="time_entries_presentquery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all Tasks"""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().task_index(x_api_versio_nheader, assignee_idquery, assignee_typequery, assigner_idquery, cascading_source_idquery, client_idquery, completequery, created_sincequery, due_at_fromquery, due_at_presentquery, due_at_toquery, fieldsquery, idsquery, limitquery, matter_idquery, orderquery, page_tokenquery, permissionquery, priorityquery, queryquery, responsible_attorney_idquery, statusquery, statusesquery, statute_of_limitationsquery, task_type_idquery, time_entries_presentquery, updated_sincequery)


@router.get(
    "/tasks/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single Task"""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().task_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, fieldsquery)


@router.patch(
    "/tasks/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    task_update_request: Annotated[Optional[TaskUpdateRequest], Field(description="Request Body for Tasks")] = Body(None, description="Request Body for Tasks"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single Task"""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().task_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, task_update_request)
