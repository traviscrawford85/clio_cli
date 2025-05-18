# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.task_template_lists_api_base import BaseTaskTemplateListsApi
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
from clio_mock.models.task_template_list_copy_request import TaskTemplateListCopyRequest
from clio_mock.models.task_template_list_create_request import TaskTemplateListCreateRequest
from clio_mock.models.task_template_list_update_request import TaskTemplateListUpdateRequest


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/task_template_lists/{id}/copy.json",
    responses={
        404: {"model": Error, "description": "Not Found"},
        400: {"model": Error, "description": "Bad Request"},
        201: {"model": ActivityShow, "description": "Created"},
    },
    tags=["Task Template Lists"],
    summary="Copy a TaskTemplateList",
    response_model_by_alias=True,
)
async def task_template_list_copy(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    task_template_list_copy_request: Annotated[Optional[TaskTemplateListCopyRequest], Field(description="Request Body for Task Template Lists")] = Body(None, description="Request Body for Task Template Lists"),
) -> ActivityShow:
    """Creates a copy of the TaskTemplateList identified by the &#x60;id&#x60; path parameter. """
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_copy(idpath, fieldsquery, task_template_list_copy_request)


@router.post(
    "/task_template_lists.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    task_template_list_create_request: Annotated[Optional[TaskTemplateListCreateRequest], Field(description="Request Body for Task Template Lists")] = Body(None, description="Request Body for Task Template Lists"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new TaskTemplateList"""
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_create(x_api_versio_nheader, fieldsquery, task_template_list_create_request)


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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single TaskTemplateList"""
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/task_template_lists.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    emptyquery: Annotated[Optional[StrictBool], Field(description="Filter TaskTemplateList records to those that either contain at least one task template or contain none.")] = Query(None, description="Filter TaskTemplateList records to those that either contain at least one task template or contain none.", alias="emptyquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    practice_area_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single PracticeArea. The keyword `null` is not valid for this field. The list will be filtered to include only the Matter records with the matching property.")] = Query(None, description="The unique identifier for a single PracticeArea. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Matter records with the matching property.", alias="practice_area_idquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all TaskTemplateLists"""
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_index(x_api_versio_nheader, created_sincequery, emptyquery, fieldsquery, idsquery, limitquery, orderquery, page_tokenquery, practice_area_idquery, queryquery, updated_sincequery)


@router.get(
    "/task_template_lists/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single TaskTemplateList"""
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, fieldsquery)


@router.patch(
    "/task_template_lists/{id}.json",
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
    tags=["Task Template Lists"],
    summary="Update a single TaskTemplateList",
    response_model_by_alias=True,
)
async def task_template_list_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    task_template_list_update_request: Annotated[Optional[TaskTemplateListUpdateRequest], Field(description="Request Body for Task Template Lists")] = Body(None, description="Request Body for Task Template Lists"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single TaskTemplateList"""
    if not BaseTaskTemplateListsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTaskTemplateListsApi.subclasses[0]().task_template_list_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, task_template_list_update_request)
