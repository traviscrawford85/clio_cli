# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.calendar_visibilities_api_base import BaseCalendarVisibilitiesApi
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
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.calendar_visibility_list import CalendarVisibilityList
from openapi_server.models.calendar_visibility_show import CalendarVisibilityShow
from openapi_server.models.calendar_visibility_update_request import CalendarVisibilityUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/task_calendars.json",
    responses={
        200: {"model": CalendarVisibilityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Calendar Visibilities"],
    summary="Return the data for all CalendarVisibilities",
    response_model_by_alias=True,
)
async def calendar_visibility_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter CalendarVisibility records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter CalendarVisibility records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter CalendarVisibility records to those having the specified unique identifiers.")] = Query(None, description="Filter CalendarVisibility records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of CalendarVisibility records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of CalendarVisibility records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter CalendarVisibility records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter CalendarVisibility records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> CalendarVisibilityList:
    """Outlines the parameters, optional and required, used when requesting the data for all CalendarVisibilities"""
    if not BaseCalendarVisibilitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarVisibilitiesApi.subclasses[0]().calendar_visibility_index(x_api_version, created_since, fields, ids, limit, page_token, updated_since)


@router.get(
    "/task_calendars/{id}.json",
    responses={
        200: {"model": CalendarVisibilityShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Calendar Visibilities"],
    summary="Return the data for a single CalendarVisibility",
    response_model_by_alias=True,
)
async def calendar_visibility_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the CalendarVisibility.")] = Path(..., description="The unique identifier for the CalendarVisibility."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> CalendarVisibilityShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single CalendarVisibility"""
    if not BaseCalendarVisibilitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarVisibilitiesApi.subclasses[0]().calendar_visibility_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/task_calendars/{id}.json",
    responses={
        200: {"model": CalendarVisibilityShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Calendar Visibilities"],
    summary="Update a single CalendarVisibility",
    response_model_by_alias=True,
)
async def calendar_visibility_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the CalendarVisibility.")] = Path(..., description="The unique identifier for the CalendarVisibility."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    calendar_visibility_update_request: Annotated[Optional[CalendarVisibilityUpdateRequest], Field(description="Request Body for Task Calendars")] = Body(None, description="Request Body for Task Calendars"),
) -> CalendarVisibilityShow:
    """Outlines the parameters and data fields used when updating a single CalendarVisibility"""
    if not BaseCalendarVisibilitiesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCalendarVisibilitiesApi.subclasses[0]().calendar_visibility_update(id, if_match, x_api_version, fields, calendar_visibility_update_request)
