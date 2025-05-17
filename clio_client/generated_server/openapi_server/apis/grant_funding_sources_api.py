# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.grant_funding_sources_api_base import BaseGrantFundingSourcesApi
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
from datetime import datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.grant_funding_source_create_request import GrantFundingSourceCreateRequest
from openapi_server.models.grant_funding_source_list import GrantFundingSourceList
from openapi_server.models.grant_funding_source_show import GrantFundingSourceShow


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/grant_funding_sources.json",
    responses={
        201: {"model": GrantFundingSourceShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Grant Funding Sources"],
    summary="Create a new grant funding source",
    response_model_by_alias=True,
)
async def grant_funding_source_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    grant_funding_source_create_request: Annotated[Optional[GrantFundingSourceCreateRequest], Field(description="Request Body for Grant Funding Sources")] = Body(None, description="Request Body for Grant Funding Sources"),
) -> GrantFundingSourceShow:
    """Outlines the parameters and data fields used when creating a new GrantFundingSource"""
    if not BaseGrantFundingSourcesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGrantFundingSourcesApi.subclasses[0]().grant_funding_source_create(x_api_version, fields, grant_funding_source_create_request)


@router.delete(
    "/grant_funding_sources/{id}.json",
    responses={
        200: {"model": GrantFundingSourceShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Grant Funding Sources"],
    summary="Delete a single grant funding source",
    response_model_by_alias=True,
)
async def grant_funding_source_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the GrantFundingSource.")] = Path(..., description="The unique identifier for the GrantFundingSource."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    grant_funding_source_create_request: Annotated[Optional[GrantFundingSourceCreateRequest], Field(description="Request Body for Grant Funding Sources")] = Body(None, description="Request Body for Grant Funding Sources"),
) -> GrantFundingSourceShow:
    """Outlines the parameters and data fields used when updating a single GrantFundingSource"""
    if not BaseGrantFundingSourcesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGrantFundingSourcesApi.subclasses[0]().grant_funding_source_destroy(id, if_match, x_api_version, fields, grant_funding_source_create_request)


@router.get(
    "/grant_funding_sources.json",
    responses={
        200: {"model": GrantFundingSourceList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Grant Funding Sources"],
    summary="Return the data for all grant funding sources",
    response_model_by_alias=True,
)
async def grant_funding_source_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter GrantFundingSource records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter GrantFundingSource records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter GrantFundingSource records to those having the specified unique identifiers.")] = Query(None, description="Filter GrantFundingSource records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of GrantFundingSource records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of GrantFundingSource records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    name: Annotated[Optional[StrictStr], Field(description="Filter GrantFundingSource records to those that match the given name.")] = Query(None, description="Filter GrantFundingSource records to those that match the given name.", alias="name"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter GrantFundingSource records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter GrantFundingSource records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> GrantFundingSourceList:
    """Outlines the parameters, optional and required, used when requesting the data for all GrantFundingSources"""
    if not BaseGrantFundingSourcesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGrantFundingSourcesApi.subclasses[0]().grant_funding_source_index(x_api_version, created_since, fields, ids, limit, name, page_token, updated_since)


@router.patch(
    "/grant_funding_sources/{id}.json",
    responses={
        200: {"model": GrantFundingSourceShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Grant Funding Sources"],
    summary="Update a single grant funding source",
    response_model_by_alias=True,
)
async def grant_funding_source_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the GrantFundingSource.")] = Path(..., description="The unique identifier for the GrantFundingSource."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    grant_funding_source_create_request: Annotated[Optional[GrantFundingSourceCreateRequest], Field(description="Request Body for Grant Funding Sources")] = Body(None, description="Request Body for Grant Funding Sources"),
) -> GrantFundingSourceShow:
    """Outlines the parameters and data fields used when updating a single GrantFundingSource"""
    if not BaseGrantFundingSourcesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGrantFundingSourcesApi.subclasses[0]().grant_funding_source_update(id, if_match, x_api_version, fields, grant_funding_source_create_request)
