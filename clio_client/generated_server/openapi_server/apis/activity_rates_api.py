# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.activity_rates_api_base import BaseActivityRatesApi
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
from openapi_server.models.activity_rate_create_request import ActivityRateCreateRequest
from openapi_server.models.activity_rate_list import ActivityRateList
from openapi_server.models.activity_rate_show import ActivityRateShow
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/activity_rates.json",
    responses={
        201: {"model": ActivityRateShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Activity Rates"],
    summary="Create a new ActivityRate",
    response_model_by_alias=True,
)
async def activity_rate_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    activity_rate_create_request: Annotated[Optional[ActivityRateCreateRequest], Field(description="Request Body for Activity Rates")] = Body(None, description="Request Body for Activity Rates"),
) -> ActivityRateShow:
    """Outlines the parameters and data fields used when creating a new ActivityRate"""
    if not BaseActivityRatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivityRatesApi.subclasses[0]().activity_rate_create(x_api_version, fields, activity_rate_create_request)


@router.delete(
    "/activity_rates/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Activity Rates"],
    summary="Delete a single ActivityRate",
    response_model_by_alias=True,
)
async def activity_rate_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ActivityRate.")] = Path(..., description="The unique identifier for the ActivityRate."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single ActivityRate"""
    if not BaseActivityRatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivityRatesApi.subclasses[0]().activity_rate_destroy(id, x_api_version)


@router.get(
    "/activity_rates.json",
    responses={
        200: {"model": ActivityRateList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Activity Rates"],
    summary="Return the data for all ActivityRates",
    response_model_by_alias=True,
)
async def activity_rate_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    co_counsel_contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.", alias="co_counsel_contact_id"),
    contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.", alias="contact_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter ActivityRate records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter ActivityRate records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter ActivityRate records to those having the specified unique identifiers.")] = Query(None, description="Filter ActivityRate records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ActivityRate records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of ActivityRate records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter ActivityRate records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter ActivityRate records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> ActivityRateList:
    """Outlines the parameters, optional and required, used when requesting the data for all ActivityRates"""
    if not BaseActivityRatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivityRatesApi.subclasses[0]().activity_rate_index(x_api_version, co_counsel_contact_id, contact_id, created_since, fields, ids, limit, page_token, updated_since)


@router.get(
    "/activity_rates/{id}.json",
    responses={
        200: {"model": ActivityRateShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Activity Rates"],
    summary="Return the data for a single ActivityRate",
    response_model_by_alias=True,
)
async def activity_rate_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ActivityRate.")] = Path(..., description="The unique identifier for the ActivityRate."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> ActivityRateShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single ActivityRate"""
    if not BaseActivityRatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivityRatesApi.subclasses[0]().activity_rate_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/activity_rates/{id}.json",
    responses={
        200: {"model": ActivityRateShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Activity Rates"],
    summary="Update a single ActivityRate",
    response_model_by_alias=True,
)
async def activity_rate_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ActivityRate.")] = Path(..., description="The unique identifier for the ActivityRate."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    activity_rate_create_request: Annotated[Optional[ActivityRateCreateRequest], Field(description="Request Body for Activity Rates")] = Body(None, description="Request Body for Activity Rates"),
) -> ActivityRateShow:
    """Outlines the parameters and data fields used when updating a single ActivityRate"""
    if not BaseActivityRatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseActivityRatesApi.subclasses[0]().activity_rate_update(id, if_match, x_api_version, fields, activity_rate_create_request)
