# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.calendars_api_base import BaseCalendarsApi
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
from openapi_server.models.calendar_create_request import CalendarCreateRequest
from openapi_server.models.calendar_list import CalendarList
from openapi_server.models.calendar_show import CalendarShow
from openapi_server.models.calendar_update_request import CalendarUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/calendars.json",
    responses={
        201: {"model": CalendarShow, "description": "Created"},
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
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    calendar_create_request: Annotated[Optional[CalendarCreateRequest], Field(description="Request Body for Calendars")] = Body(None, description="Request Body for Calendars"),
) -> CalendarShow:
    """Outlines the parameters and data fields used when creating a new Calendar"""
    if not BaseCalendarsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarsApi.subclasses[0]().calendar_create(x_api_version, fields, calendar_create_request)


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
    id: Annotated[StrictInt, Field(description="The unique identifier for the Calendar.")] = Path(..., description="The unique identifier for the Calendar."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Calendar"""
    if not BaseCalendarsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarsApi.subclasses[0]().calendar_destroy(id, x_api_version)


@router.get(
    "/calendars.json",
    responses={
        200: {"model": CalendarList, "description": "Ok"},
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
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter Calendar records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Calendar records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    filter_inactive_users: Annotated[Optional[StrictBool], Field(description="Filter any shared UserCalendar records whose owner is inactive.")] = Query(None, description="Filter any shared UserCalendar records whose owner is inactive.", alias="filter_inactive_users"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Calendar records to those having the specified unique identifiers.")] = Query(None, description="Filter Calendar records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Calendar records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Calendar records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Calendar records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Calendar records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    owner: Annotated[Optional[StrictBool], Field(description="Filter Calendar records to those that the user owns.")] = Query(None, description="Filter Calendar records to those that the user owns.", alias="owner"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    source: Annotated[Optional[StrictStr], Field(description="Filter Calendar records to those having a specific calendar visibility source (mobile, web).")] = Query(None, description="Filter Calendar records to those having a specific calendar visibility source (mobile, web).", alias="source"),
    type: Annotated[Optional[StrictStr], Field(description="Filter Calendar records to those of the specified type.")] = Query(None, description="Filter Calendar records to those of the specified type.", alias="type"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Calendar records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Calendar records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
    visible: Annotated[Optional[StrictBool], Field(description="Filter Calendar records to those that are visible.")] = Query(None, description="Filter Calendar records to those that are visible.", alias="visible"),
    writeable: Annotated[Optional[StrictBool], Field(description="Filter Calendar records to those which the user can write to.")] = Query(None, description="Filter Calendar records to those which the user can write to.", alias="writeable"),
) -> CalendarList:
    """Outlines the parameters, optional and required, used when requesting the data for all Calendars"""
    if not BaseCalendarsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarsApi.subclasses[0]().calendar_index(x_api_version, created_since, fields, filter_inactive_users, ids, limit, order, owner, page_token, source, type, updated_since, visible, writeable)


@router.get(
    "/calendars/{id}.json",
    responses={
        200: {"model": CalendarShow, "description": "Ok"},
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
    id: Annotated[StrictInt, Field(description="The unique identifier for the Calendar.")] = Path(..., description="The unique identifier for the Calendar."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> CalendarShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Calendar"""
    if not BaseCalendarsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarsApi.subclasses[0]().calendar_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/calendars/{id}.json",
    responses={
        200: {"model": CalendarShow, "description": "Ok"},
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
    id: Annotated[StrictInt, Field(description="The unique identifier for the Calendar.")] = Path(..., description="The unique identifier for the Calendar."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    calendar_update_request: Annotated[Optional[CalendarUpdateRequest], Field(description="Request Body for Calendars")] = Body(None, description="Request Body for Calendars"),
) -> CalendarShow:
    """Outlines the parameters and data fields used when updating a single Calendar"""
    if not BaseCalendarsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarsApi.subclasses[0]().calendar_update(id, if_match, x_api_version, fields, calendar_update_request)
