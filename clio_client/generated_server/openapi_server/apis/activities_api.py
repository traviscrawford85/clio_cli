# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.activities_api_base import BaseActivitiesApi
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
from openapi_server.models.activity_create_request import ActivityCreateRequest
from openapi_server.models.activity_list import ActivityList
from openapi_server.models.activity_show import ActivityShow
from openapi_server.models.activity_update_request import ActivityUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/activities.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Activities"],
    summary="Create a new Activity",
    response_model_by_alias=True,
)
async def activity_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    activity_create_request: Annotated[Optional[ActivityCreateRequest], Field(description="Request Body for Activities")] = Body(None, description="Request Body for Activities"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new Activity"""
    if not BaseActivitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivitiesApi.subclasses[0]().activity_create(x_api_version, fields, activity_create_request)


@router.delete(
    "/activities/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Activities"],
    summary="Delete a single Activity",
    response_model_by_alias=True,
)
async def activity_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Activity"""
    if not BaseActivitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivitiesApi.subclasses[0]().activity_destroy(id, x_api_version)


@router.get(
    "/activities.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Activities"],
    summary="Return the data for all Activities",
    response_model_by_alias=True,
)
async def activity_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    activity_description_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single ActivityDescription. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single ActivityDescription. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="activity_description_id"),
    calendar_entry_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single CalendarEntry. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single CalendarEntry. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="calendar_entry_id"),
    communication_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Communication. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Communication. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="communication_id"),
    contact_note_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Note. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Note. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="contact_note_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    end_date: Annotated[Optional[datetime], Field(description="Filter Activity records to those whose `date` is on or before the date provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Activity records to those whose &#x60;date&#x60; is on or before the date provided (Expects an ISO-8601 date).", alias="end_date"),
    expense_category_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single ExpenseCategory. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single ExpenseCategory. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="expense_category_id"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    flat_rate: Annotated[Optional[StrictBool], Field(description="Filter Activity TimeEntry records to those that have a flat rate, or not.")] = Query(None, description="Filter Activity TimeEntry records to those that have a flat rate, or not.", alias="flat_rate"),
    grant_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Grant. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Grant. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="grant_id"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="matter_id"),
    matter_note_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Note. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Note. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="matter_note_id"),
    only_unaccounted_for: Annotated[Optional[StrictBool], Field(description="Only unaccounted for activities.")] = Query(None, description="Only unaccounted for activities.", alias="only_unaccounted_for"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="query"),
    start_date: Annotated[Optional[datetime], Field(description="Filter Activity records to those whose `date` is on or after the date provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Activity records to those whose &#x60;date&#x60; is on or after the date provided (Expects an ISO-8601 date).", alias="start_date"),
    status: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those that are draft, billed, unbilled or non-billable.")] = Query(None, description="Filter Activity records to those that are draft, billed, unbilled or non-billable.", alias="status"),
    task_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Task. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Task. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="task_id"),
    type: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those of a specific type.")] = Query(None, description="Filter Activity records to those of a specific type.", alias="type"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
    user_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="user_id"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all Activities"""
    if not BaseActivitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivitiesApi.subclasses[0]().activity_index(x_api_version, activity_description_id, calendar_entry_id, communication_id, contact_note_id, created_since, end_date, expense_category_id, fields, flat_rate, grant_id, ids, limit, matter_id, matter_note_id, only_unaccounted_for, order, page_token, query, start_date, status, task_id, type, updated_since, user_id)


@router.get(
    "/activities/{id}.json",
    responses={
        200: {"model": ActivityShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Activities"],
    summary="Return the data for a single Activity",
    response_model_by_alias=True,
)
async def activity_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> ActivityShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Activity"""
    if not BaseActivitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivitiesApi.subclasses[0]().activity_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/activities/{id}.json",
    responses={
        200: {"model": ActivityShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Activities"],
    summary="Update a single Activity",
    response_model_by_alias=True,
)
async def activity_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    activity_update_request: Annotated[Optional[ActivityUpdateRequest], Field(description="Request Body for Activities")] = Body(None, description="Request Body for Activities"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when updating a single Activity"""
    if not BaseActivitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivitiesApi.subclasses[0]().activity_update(id, if_match, x_api_version, fields, activity_update_request)
