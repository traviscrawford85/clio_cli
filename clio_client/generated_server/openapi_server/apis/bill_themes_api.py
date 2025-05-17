# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.bill_themes_api_base import BaseBillThemesApi
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
from openapi_server.models.bill_theme_list import BillThemeList
from openapi_server.models.bill_theme_show import BillThemeShow
from openapi_server.models.bill_theme_update_request import BillThemeUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/bill_themes.json",
    responses={
        200: {"model": BillThemeList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Bill Themes"],
    summary="Return the data for all BillThemes",
    response_model_by_alias=True,
)
async def bill_theme_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter BillTheme records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter BillTheme records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter BillTheme records to those having the specified unique identifiers.")] = Query(None, description="Filter BillTheme records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of BillTheme records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of BillTheme records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter BillTheme records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter BillTheme records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> BillThemeList:
    """Outlines the parameters, optional and required, used when requesting the data for all BillThemes"""
    if not BaseBillThemesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBillThemesApi.subclasses[0]().bill_theme_index(x_api_version, created_since, fields, ids, limit, page_token, updated_since)


@router.patch(
    "/bill_themes/{id}.json",
    responses={
        200: {"model": BillThemeShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Bill Themes"],
    summary="Update a single BillTheme",
    response_model_by_alias=True,
)
async def bill_theme_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the BillTheme.")] = Path(..., description="The unique identifier for the BillTheme."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    bill_theme_update_request: Annotated[Optional[BillThemeUpdateRequest], Field(description="Request Body for Bill Themes")] = Body(None, description="Request Body for Bill Themes"),
) -> BillThemeShow:
    """Outlines the parameters and data fields used when updating a single BillTheme"""
    if not BaseBillThemesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBillThemesApi.subclasses[0]().bill_theme_update(id, if_match, x_api_version, fields, bill_theme_update_request)
