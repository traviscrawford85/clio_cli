# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.jurisdictions_api_base import BaseJurisdictionsApi
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
from openapi_server.models.error import Error
from openapi_server.models.jurisdiction_list import JurisdictionList
from openapi_server.models.jurisdiction_show import JurisdictionShow


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/court_rules/jurisdictions.json",
    responses={
        200: {"model": JurisdictionList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Jurisdictions"],
    summary="Return the data for all jurisdictions",
    response_model_by_alias=True,
)
async def jurisdiction_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter Jurisdiction records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Jurisdiction records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    for_current_account: Annotated[Optional[StrictBool], Field(description="Filter Jurisdiction records to those set up for this account.")] = Query(None, description="Filter Jurisdiction records to those set up for this account.", alias="for_current_account"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Jurisdiction records to those having the specified unique identifiers.")] = Query(None, description="Filter Jurisdiction records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Jurisdiction records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Jurisdiction records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Jurisdiction records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Jurisdiction records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `description` matching a given string.")] = Query(None, description="Wildcard search for &#x60;description&#x60; matching a given string.", alias="query"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Jurisdiction records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Jurisdiction records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> JurisdictionList:
    """Outlines the parameters, optional and required, used when requesting the data for all Jurisdictions"""
    if not BaseJurisdictionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseJurisdictionsApi.subclasses[0]().jurisdiction_index(x_api_version, created_since, fields, for_current_account, ids, limit, order, page_token, query, updated_since)


@router.get(
    "/court_rules/jurisdictions/{id}.json",
    responses={
        200: {"model": JurisdictionShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Jurisdictions"],
    summary="Return the data for the jurisdiction",
    response_model_by_alias=True,
)
async def jurisdiction_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Jurisdiction.")] = Path(..., description="The unique identifier for the Jurisdiction."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> JurisdictionShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Jurisdiction"""
    if not BaseJurisdictionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseJurisdictionsApi.subclasses[0]().jurisdiction_show(id, if_modified_since, if_none_match, x_api_version, fields)
