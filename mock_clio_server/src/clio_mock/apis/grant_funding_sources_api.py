# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.grant_funding_sources_api_base import BaseGrantFundingSourcesApi
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
from datetime import datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.error import Error
from clio_mock.models.grant_funding_source_create_request import GrantFundingSourceCreateRequest


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/grant_funding_sources.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    grant_funding_source_create_request: Annotated[Optional[GrantFundingSourceCreateRequest], Field(description="Request Body for Grant Funding Sources")] = Body(None, description="Request Body for Grant Funding Sources"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new GrantFundingSource"""
    if not BaseGrantFundingSourcesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGrantFundingSourcesApi.subclasses[0]().grant_funding_source_create(x_api_versio_nheader, fieldsquery, grant_funding_source_create_request)


@router.delete(
    "/grant_funding_sources/{id}.json",
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
    tags=["Grant Funding Sources"],
    summary="Delete a single grant funding source",
    response_model_by_alias=True,
)
async def grant_funding_source_destroy(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    grant_funding_source_create_request: Annotated[Optional[GrantFundingSourceCreateRequest], Field(description="Request Body for Grant Funding Sources")] = Body(None, description="Request Body for Grant Funding Sources"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single GrantFundingSource"""
    if not BaseGrantFundingSourcesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGrantFundingSourcesApi.subclasses[0]().grant_funding_source_destroy(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, grant_funding_source_create_request)


@router.get(
    "/grant_funding_sources.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    namequery: Annotated[Optional[StrictStr], Field(description="Filter Grant records to those that match the given name.")] = Query(None, description="Filter Grant records to those that match the given name.", alias="namequery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all GrantFundingSources"""
    if not BaseGrantFundingSourcesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGrantFundingSourcesApi.subclasses[0]().grant_funding_source_index(x_api_versio_nheader, created_sincequery, fieldsquery, idsquery, limitquery, namequery, page_tokenquery, updated_sincequery)


@router.patch(
    "/grant_funding_sources/{id}.json",
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
    tags=["Grant Funding Sources"],
    summary="Update a single grant funding source",
    response_model_by_alias=True,
)
async def grant_funding_source_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    grant_funding_source_create_request: Annotated[Optional[GrantFundingSourceCreateRequest], Field(description="Request Body for Grant Funding Sources")] = Body(None, description="Request Body for Grant Funding Sources"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single GrantFundingSource"""
    if not BaseGrantFundingSourcesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGrantFundingSourcesApi.subclasses[0]().grant_funding_source_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, grant_funding_source_create_request)
