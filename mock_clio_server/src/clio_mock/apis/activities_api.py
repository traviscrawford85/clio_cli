# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.activities_api_base import BaseActivitiesApi
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
from clio_mock.models.activity_create_request import ActivityCreateRequest
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.activity_update_request import ActivityUpdateRequest
from clio_mock.models.error import Error


router = APIRouter()

ns_pkg = clio_mock.impl
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    activity_create_request: Annotated[Optional[ActivityCreateRequest], Field(description="Request Body for Activities")] = Body(None, description="Request Body for Activities"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new Activity"""
    if not BaseActivitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivitiesApi.subclasses[0]().activity_create(x_api_versio_nheader, fieldsquery, activity_create_request)


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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Activity"""
    if not BaseActivitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivitiesApi.subclasses[0]().activity_destroy(idpath, x_api_versio_nheader)


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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    activity_description_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single ActivityDescription. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single ActivityDescription. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="activity_description_idquery"),
    calendar_entry_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single CalendarEntry. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single CalendarEntry. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="calendar_entry_idquery"),
    communication_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Communication. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Communication. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="communication_idquery"),
    contact_note_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Note. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Note. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="contact_note_idquery"),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    end_datequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those whose `date` is on or before the date provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Activity records to those whose &#x60;date&#x60; is on or before the date provided (Expects an ISO-8601 date).", alias="end_datequery"),
    expense_category_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single ExpenseCategory. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single ExpenseCategory. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="expense_category_idquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    flat_ratequery: Annotated[Optional[StrictBool], Field(description="Filter Activity TimeEntry records to those that have a flat rate, or not.")] = Query(None, description="Filter Activity TimeEntry records to those that have a flat rate, or not.", alias="flat_ratequery"),
    grant_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Grant. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Grant. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="grant_idquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="matter_idquery"),
    matter_note_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Note. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Note. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="matter_note_idquery"),
    only_unaccounted_forquery: Annotated[Optional[StrictBool], Field(description="Only unaccounted for activities.")] = Query(None, description="Only unaccounted for activities.", alias="only_unaccounted_forquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    start_datequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those whose `date` is on or after the date provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Activity records to those whose &#x60;date&#x60; is on or after the date provided (Expects an ISO-8601 date).", alias="start_datequery"),
    statusquery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those that are draft, billed, unbilled or non-billable.")] = Query(None, description="Filter Activity records to those that are draft, billed, unbilled or non-billable.", alias="statusquery"),
    task_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Task. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Task. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="task_idquery"),
    typequery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those of a specific type.")] = Query(None, description="Filter Activity records to those of a specific type.", alias="typequery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
    user_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="user_idquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all Activities"""
    if not BaseActivitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivitiesApi.subclasses[0]().activity_index(x_api_versio_nheader, activity_description_idquery, calendar_entry_idquery, communication_idquery, contact_note_idquery, created_sincequery, end_datequery, expense_category_idquery, fieldsquery, flat_ratequery, grant_idquery, idsquery, limitquery, matter_idquery, matter_note_idquery, only_unaccounted_forquery, orderquery, page_tokenquery, queryquery, start_datequery, statusquery, task_idquery, typequery, updated_sincequery, user_idquery)


@router.get(
    "/activities/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single Activity"""
    if not BaseActivitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivitiesApi.subclasses[0]().activity_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, fieldsquery)


@router.patch(
    "/activities/{id}.json",
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
    tags=["Activities"],
    summary="Update a single Activity",
    response_model_by_alias=True,
)
async def activity_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    activity_update_request: Annotated[Optional[ActivityUpdateRequest], Field(description="Request Body for Activities")] = Body(None, description="Request Body for Activities"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single Activity"""
    if not BaseActivitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivitiesApi.subclasses[0]().activity_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, activity_update_request)
