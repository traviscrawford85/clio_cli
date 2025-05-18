# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.calendars_api_base import BaseCalendarsApi
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
from clio_mock.models.calendar_create_request import CalendarCreateRequest
from clio_mock.models.calendar_update_request import CalendarUpdateRequest
from clio_mock.models.error import Error


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/calendars.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Calendars"],
    summary="Create a new Calendar",
    response_model_by_alias=True,
)
async def calendar_create(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    calendar_create_request: Annotated[Optional[CalendarCreateRequest], Field(description="Request Body for Calendars")] = Body(None, description="Request Body for Calendars"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new Calendar"""
    if not BaseCalendarsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarsApi.subclasses[0]().calendar_create(x_api_versio_nheader, fieldsquery, calendar_create_request)


@router.delete(
    "/calendars/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Calendars"],
    summary="Delete a single Calendar",
    response_model_by_alias=True,
)
async def calendar_destroy(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Calendar"""
    if not BaseCalendarsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarsApi.subclasses[0]().calendar_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/calendars.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Calendars"],
    summary="Return the data for all Calendars",
    response_model_by_alias=True,
)
async def calendar_index(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    filter_inactive_usersquery: Annotated[Optional[StrictBool], Field(description="Filter any shared UserCalendar records whose owner is inactive.")] = Query(None, description="Filter any shared UserCalendar records whose owner is inactive.", alias="filter_inactive_usersquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    ownerquery: Annotated[Optional[StrictBool], Field(description="Filter Calendar records to those that the user owns.")] = Query(None, description="Filter Calendar records to those that the user owns.", alias="ownerquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    sourcequery: Annotated[Optional[StrictStr], Field(description="Filter CalendarEntry records to those having a specific calendar visibility source (mobile, web).")] = Query(None, description="Filter CalendarEntry records to those having a specific calendar visibility source (mobile, web).", alias="sourcequery"),
    typequery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those of a specific type.")] = Query(None, description="Filter Activity records to those of a specific type.", alias="typequery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
    visiblequery: Annotated[Optional[StrictBool], Field(description="Filter CalendarEntry records to those that are visible.")] = Query(None, description="Filter CalendarEntry records to those that are visible.", alias="visiblequery"),
    writeablequery: Annotated[Optional[StrictBool], Field(description="Filter Calendar records to those which the user can write to.")] = Query(None, description="Filter Calendar records to those which the user can write to.", alias="writeablequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all Calendars"""
    if not BaseCalendarsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarsApi.subclasses[0]().calendar_index(x_api_versio_nheader, created_sincequery, fieldsquery, filter_inactive_usersquery, idsquery, limitquery, orderquery, ownerquery, page_tokenquery, sourcequery, typequery, updated_sincequery, visiblequery, writeablequery)


@router.get(
    "/calendars/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Calendars"],
    summary="Return the data for a single Calendar",
    response_model_by_alias=True,
)
async def calendar_show(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single Calendar"""
    if not BaseCalendarsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarsApi.subclasses[0]().calendar_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, fieldsquery)


@router.patch(
    "/calendars/{id}.json",
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
    tags=["Calendars"],
    summary="Update a single Calendar",
    response_model_by_alias=True,
)
async def calendar_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    calendar_update_request: Annotated[Optional[CalendarUpdateRequest], Field(description="Request Body for Calendars")] = Body(None, description="Request Body for Calendars"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single Calendar"""
    if not BaseCalendarsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarsApi.subclasses[0]().calendar_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, calendar_update_request)
