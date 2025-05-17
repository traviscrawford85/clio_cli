# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.practice_areas_api_base import BasePracticeAreasApi
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
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.practice_area_create_request import PracticeAreaCreateRequest
from openapi_server.models.practice_area_list import PracticeAreaList
from openapi_server.models.practice_area_show import PracticeAreaShow
from openapi_server.models.practice_area_update_request import PracticeAreaUpdateRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/practice_areas.json",
    responses={
        201: {"model": PracticeAreaShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Practice Areas"],
    summary="Create a new PracticeArea",
    response_model_by_alias=True,
)
async def practice_area_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    practice_area_create_request: Annotated[Optional[PracticeAreaCreateRequest], Field(description="Request Body for Practice Areas")] = Body(None, description="Request Body for Practice Areas"),
) -> PracticeAreaShow:
    """Outlines the parameters and data fields used when creating a new PracticeArea"""
    if not BasePracticeAreasApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePracticeAreasApi.subclasses[0]().practice_area_create(x_api_version, fields, practice_area_create_request)


@router.delete(
    "/practice_areas/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Practice Areas"],
    summary="Delete a single PracticeArea",
    response_model_by_alias=True,
)
async def practice_area_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the PracticeArea.")] = Path(..., description="The unique identifier for the PracticeArea."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single PracticeArea"""
    if not BasePracticeAreasApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePracticeAreasApi.subclasses[0]().practice_area_destroy(id, x_api_version)


@router.get(
    "/practice_areas.json",
    responses={
        200: {"model": PracticeAreaList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Practice Areas"],
    summary="Return the data for all PracticeAreas",
    response_model_by_alias=True,
)
async def practice_area_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    code: Annotated[Optional[StrictStr], Field(description="Filter PracticeArea records to those that match the given code.")] = Query(None, description="Filter PracticeArea records to those that match the given code.", alias="code"),
    created_since: Annotated[Optional[datetime], Field(description="Filter PracticeArea records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter PracticeArea records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter PracticeArea records to those having the specified unique identifiers.")] = Query(None, description="Filter PracticeArea records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of PracticeArea records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of PracticeArea records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="Filter PracticeArea records to exclude Legal Aid UK Practice Areas when activities exist on the matter.")] = Query(None, description="Filter PracticeArea records to exclude Legal Aid UK Practice Areas when activities exist on the matter.", alias="matter_id"),
    name: Annotated[Optional[StrictStr], Field(description="Filter PracticeArea records to those that match the given name.")] = Query(None, description="Filter PracticeArea records to those that match the given name.", alias="name"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the PracticeArea records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the PracticeArea records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter PracticeArea records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter PracticeArea records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> PracticeAreaList:
    """Outlines the parameters, optional and required, used when requesting the data for all PracticeAreas"""
    if not BasePracticeAreasApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePracticeAreasApi.subclasses[0]().practice_area_index(x_api_version, code, created_since, fields, ids, limit, matter_id, name, order, page_token, updated_since)


@router.get(
    "/practice_areas/{id}.json",
    responses={
        200: {"model": PracticeAreaShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Practice Areas"],
    summary="Return the data for a single PracticeArea",
    response_model_by_alias=True,
)
async def practice_area_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the PracticeArea.")] = Path(..., description="The unique identifier for the PracticeArea."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> PracticeAreaShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single PracticeArea"""
    if not BasePracticeAreasApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePracticeAreasApi.subclasses[0]().practice_area_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/practice_areas/{id}.json",
    responses={
        200: {"model": PracticeAreaShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Practice Areas"],
    summary="Update a single PracticeArea",
    response_model_by_alias=True,
)
async def practice_area_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the PracticeArea.")] = Path(..., description="The unique identifier for the PracticeArea."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    practice_area_update_request: Annotated[Optional[PracticeAreaUpdateRequest], Field(description="Request Body for Practice Areas")] = Body(None, description="Request Body for Practice Areas"),
) -> PracticeAreaShow:
    """Outlines the parameters and data fields used when updating a single PracticeArea"""
    if not BasePracticeAreasApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePracticeAreasApi.subclasses[0]().practice_area_update(id, if_match, x_api_version, fields, practice_area_update_request)
