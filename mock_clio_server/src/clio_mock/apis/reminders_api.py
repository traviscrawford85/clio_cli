# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.reminders_api_base import BaseRemindersApi
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
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.error import Error
from clio_mock.models.reminder_create_request import ReminderCreateRequest
from clio_mock.models.reminder_update_request import ReminderUpdateRequest


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/reminders.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Reminders"],
    summary="Create a new Reminder",
    response_model_by_alias=True,
)
async def reminder_create(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    reminder_create_request: Annotated[Optional[ReminderCreateRequest], Field(description="Request Body for Reminders")] = Body(None, description="Request Body for Reminders"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new Reminder"""
    if not BaseRemindersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRemindersApi.subclasses[0]().reminder_create(x_api_versio_nheader, fieldsquery, reminder_create_request)


@router.delete(
    "/reminders/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Reminders"],
    summary="Delete a single Reminder",
    response_model_by_alias=True,
)
async def reminder_destroy(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Reminder"""
    if not BaseRemindersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRemindersApi.subclasses[0]().reminder_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/reminders.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Reminders"],
    summary="Return the data for all Reminders",
    response_model_by_alias=True,
)
async def reminder_index(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    notification_method_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single NotificationMethod. The keyword `null` is not valid for this field. The list will be filtered to include only the Reminder records with the matching property.")] = Query(None, description="The unique identifier for a single NotificationMethod. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Reminder records with the matching property.", alias="notification_method_idquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    statequery: Annotated[Optional[StrictStr], Field(description="Filter Bill records to those in a given state.")] = Query(None, description="Filter Bill records to those in a given state.", alias="statequery"),
    subject_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single CalendarEntry or Task. The keyword `null` is not valid for this field. The list will be filtered to include only the Reminder records with the matching property.")] = Query(None, description="The unique identifier for a single CalendarEntry or Task. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Reminder records with the matching property.", alias="subject_idquery"),
    subject_typequery: Annotated[Optional[StrictStr], Field(description="Filter Reminder records to those of a given subject type, required if using subject_id.")] = Query(None, description="Filter Reminder records to those of a given subject type, required if using subject_id.", alias="subject_typequery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
    user_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="user_idquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all Reminders"""
    if not BaseRemindersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRemindersApi.subclasses[0]().reminder_index(x_api_versio_nheader, created_sincequery, fieldsquery, idsquery, limitquery, notification_method_idquery, orderquery, page_tokenquery, statequery, subject_idquery, subject_typequery, updated_sincequery, user_idquery)


@router.get(
    "/reminders/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Reminders"],
    summary="Return the data for a single Reminder",
    response_model_by_alias=True,
)
async def reminder_show(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single Reminder"""
    if not BaseRemindersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRemindersApi.subclasses[0]().reminder_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, fieldsquery)


@router.patch(
    "/reminders/{id}.json",
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
    tags=["Reminders"],
    summary="Update a single Reminder",
    response_model_by_alias=True,
)
async def reminder_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    reminder_update_request: Annotated[Optional[ReminderUpdateRequest], Field(description="Request Body for Reminders")] = Body(None, description="Request Body for Reminders"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single Reminder"""
    if not BaseRemindersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRemindersApi.subclasses[0]().reminder_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, reminder_update_request)
