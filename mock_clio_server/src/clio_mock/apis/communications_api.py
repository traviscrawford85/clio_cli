# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.communications_api_base import BaseCommunicationsApi
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
from clio_mock.models.communication_create_request import CommunicationCreateRequest
from clio_mock.models.communication_update_request import CommunicationUpdateRequest
from clio_mock.models.error import Error


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/communications.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    communication_create_request: Annotated[Optional[CommunicationCreateRequest], Field(description="Request Body for Communications")] = Body(None, description="Request Body for Communications"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new Communication"""
    if not BaseCommunicationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommunicationsApi.subclasses[0]().communication_create(x_api_versio_nheader, fieldsquery, communication_create_request)


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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Communication"""
    if not BaseCommunicationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommunicationsApi.subclasses[0]().communication_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/communications.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    contact_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.", alias="contact_idquery"),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    datequery: Annotated[Optional[date], Field(description="Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date).")] = Query(None, description="Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date).", alias="datequery"),
    external_property_namequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")] = Query(None, description="Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; ", alias="external_property_namequery"),
    external_property_valuequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")] = Query(None, description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; ", alias="external_property_valuequery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    having_time_entriesquery: Annotated[Optional[StrictBool], Field(description="Filter Communication records to those that do or do not have time entries.")] = Query(None, description="Filter Communication records to those that do or do not have time entries.", alias="having_time_entriesquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="matter_idquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    received_atquery: Annotated[Optional[datetime], Field(description="Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date-time).")] = Query(None, description="Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date-time).", alias="received_atquery"),
    received_beforequery: Annotated[Optional[datetime], Field(description="Filter Communication records to those whose `date` is on or before the date provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Communication records to those whose &#x60;date&#x60; is on or before the date provided (Expects an ISO-8601 date).", alias="received_beforequery"),
    received_sincequery: Annotated[Optional[datetime], Field(description="Filter Communication records to those whose `date` is on or after the date provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Communication records to those whose &#x60;date&#x60; is on or after the date provided (Expects an ISO-8601 date).", alias="received_sincequery"),
    typequery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those of a specific type.")] = Query(None, description="Filter Activity records to those of a specific type.", alias="typequery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
    user_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="user_idquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all Communications"""
    if not BaseCommunicationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommunicationsApi.subclasses[0]().communication_index(x_api_versio_nheader, contact_idquery, created_sincequery, datequery, external_property_namequery, external_property_valuequery, fieldsquery, having_time_entriesquery, idsquery, limitquery, matter_idquery, orderquery, page_tokenquery, queryquery, received_atquery, received_beforequery, received_sincequery, typequery, updated_sincequery, user_idquery)


@router.get(
    "/communications/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single Communication"""
    if not BaseCommunicationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommunicationsApi.subclasses[0]().communication_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, fieldsquery)


@router.patch(
    "/communications/{id}.json",
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
    tags=["Communications"],
    summary="Update a single Communication",
    response_model_by_alias=True,
)
async def communication_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    communication_update_request: Annotated[Optional[CommunicationUpdateRequest], Field(description="Request Body for Communications")] = Body(None, description="Request Body for Communications"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single Communication"""
    if not BaseCommunicationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommunicationsApi.subclasses[0]().communication_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, communication_update_request)
