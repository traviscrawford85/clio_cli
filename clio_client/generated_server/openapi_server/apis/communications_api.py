# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.communications_api_base import BaseCommunicationsApi
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
from openapi_server.models.communication_create_request import CommunicationCreateRequest
from openapi_server.models.communication_list import CommunicationList
from openapi_server.models.communication_show import CommunicationShow
from openapi_server.models.communication_update_request import CommunicationUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/communications.json",
    responses={
        201: {"model": CommunicationShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Communications"],
    summary="Create a new Communication",
    response_model_by_alias=True,
)
async def communication_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    communication_create_request: Annotated[Optional[CommunicationCreateRequest], Field(description="Request Body for Communications")] = Body(None, description="Request Body for Communications"),
) -> CommunicationShow:
    """Outlines the parameters and data fields used when creating a new Communication"""
    if not BaseCommunicationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommunicationsApi.subclasses[0]().communication_create(x_api_version, fields, communication_create_request)


@router.delete(
    "/communications/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Communications"],
    summary="Delete a single Communication",
    response_model_by_alias=True,
)
async def communication_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Communication.")] = Path(..., description="The unique identifier for the Communication."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Communication"""
    if not BaseCommunicationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommunicationsApi.subclasses[0]().communication_destroy(id, x_api_version)


@router.get(
    "/communications.json",
    responses={
        200: {"model": CommunicationList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Communications"],
    summary="Return the data for all Communications",
    response_model_by_alias=True,
)
async def communication_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Communication records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Communication records with the matching property.", alias="contact_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter Communication records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Communication records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    var_date: Annotated[Optional[date], Field(description="Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date).")] = Query(None, description="Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date).", alias="date"),
    external_property_name: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")] = Query(None, description="Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; ", alias="external_property_name"),
    external_property_value: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")] = Query(None, description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; ", alias="external_property_value"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    having_time_entries: Annotated[Optional[StrictBool], Field(description="Filter Communication records to those that do or do not have time entries.")] = Query(None, description="Filter Communication records to those that do or do not have time entries.", alias="having_time_entries"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Communication records to those having the specified unique identifiers.")] = Query(None, description="Filter Communication records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Communication records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Communication records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Communication. The list will be filtered to include only the Communication records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Communication. The list will be filtered to include only the Communication records with the matching property.", alias="matter_id"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Communication records by the given field. Default: `date(asc)`.")] = Query(None, description="Orders the Communication records by the given field. Default: &#x60;date(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `body` or `subject` matching a given string.")] = Query(None, description="Wildcard search for &#x60;body&#x60; or &#x60;subject&#x60; matching a given string.", alias="query"),
    received_at: Annotated[Optional[datetime], Field(description="Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date-time).")] = Query(None, description="Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date-time).", alias="received_at"),
    received_before: Annotated[Optional[datetime], Field(description="Filter Communication records to those whose `date` is on or before the date provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Communication records to those whose &#x60;date&#x60; is on or before the date provided (Expects an ISO-8601 date).", alias="received_before"),
    received_since: Annotated[Optional[datetime], Field(description="Filter Communication records to those whose `date` is on or after the date provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Communication records to those whose &#x60;date&#x60; is on or after the date provided (Expects an ISO-8601 date).", alias="received_since"),
    type: Annotated[Optional[StrictStr], Field(description="Filter Communication records to those of the specified type.")] = Query(None, description="Filter Communication records to those of the specified type.", alias="type"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Communication records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Communication records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
    user_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. The keyword `null` is not valid for this field. The list will be filtered to include only the Communication records with the matching property.")] = Query(None, description="The unique identifier for a single User. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Communication records with the matching property.", alias="user_id"),
) -> CommunicationList:
    """Outlines the parameters, optional and required, used when requesting the data for all Communications"""
    if not BaseCommunicationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommunicationsApi.subclasses[0]().communication_index(x_api_version, contact_id, created_since, var_date, external_property_name, external_property_value, fields, having_time_entries, ids, limit, matter_id, order, page_token, query, received_at, received_before, received_since, type, updated_since, user_id)


@router.get(
    "/communications/{id}.json",
    responses={
        200: {"model": CommunicationShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Communications"],
    summary="Return the data for a single Communication",
    response_model_by_alias=True,
)
async def communication_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Communication.")] = Path(..., description="The unique identifier for the Communication."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> CommunicationShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Communication"""
    if not BaseCommunicationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommunicationsApi.subclasses[0]().communication_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/communications/{id}.json",
    responses={
        200: {"model": CommunicationShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Communications"],
    summary="Update a single Communication",
    response_model_by_alias=True,
)
async def communication_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Communication.")] = Path(..., description="The unique identifier for the Communication."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    communication_update_request: Annotated[Optional[CommunicationUpdateRequest], Field(description="Request Body for Communications")] = Body(None, description="Request Body for Communications"),
) -> CommunicationShow:
    """Outlines the parameters and data fields used when updating a single Communication"""
    if not BaseCommunicationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommunicationsApi.subclasses[0]().communication_update(id, if_match, x_api_version, fields, communication_update_request)
