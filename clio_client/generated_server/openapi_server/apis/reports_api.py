# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.reports_api_base import BaseReportsApi
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
from openapi_server.models.report_create_request import ReportCreateRequest
from openapi_server.models.report_list import ReportList
from openapi_server.models.report_show import ReportShow


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/reports.json",
    responses={
        201: {"model": ReportShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Reports"],
    summary="Create a new Report",
    response_model_by_alias=True,
)
async def report_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    report_create_request: Annotated[Optional[ReportCreateRequest], Field(description="Request Body for Reports")] = Body(None, description="Request Body for Reports"),
) -> ReportShow:
    """Outlines the parameters and data fields used when creating a new Report"""
    if not BaseReportsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportsApi.subclasses[0]().report_create(x_api_version, fields, report_create_request)


@router.get(
    "/reports/{id}/download.json",
    responses={
        303: {"description": "See Other"},
        400: {"model": Error, "description": "Bad Request"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Reports"],
    summary="Download the completed Report",
    response_model_by_alias=True,
)
async def report_download(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Report.")] = Path(..., description="The unique identifier for the Report."),
) -> None:
    """Download the completed Report"""
    if not BaseReportsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportsApi.subclasses[0]().report_download(id)


@router.get(
    "/reports.json",
    responses={
        200: {"model": ReportList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Reports"],
    summary="Return the data for all Reports",
    response_model_by_alias=True,
)
async def report_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    category: Annotated[Optional[StrictStr], Field(description="Filters Report data by category.")] = Query(None, description="Filters Report data by category.", alias="category"),
    created_before: Annotated[Optional[datetime], Field(description="Filters Report data by date. (Expects an ISO-8601 date).")] = Query(None, description="Filters Report data by date. (Expects an ISO-8601 date).", alias="created_before"),
    created_since: Annotated[Optional[datetime], Field(description="Filter Report records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Report records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Report records to those having the specified unique identifiers.")] = Query(None, description="Filter Report records to those having the specified unique identifiers.", alias="ids[]"),
    kind: Annotated[Optional[StrictStr], Field(description="Filters Report data by kind.")] = Query(None, description="Filters Report data by kind.", alias="kind"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Report records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Report records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    output_format: Annotated[Optional[StrictStr], Field(description="Filters Report data by format.")] = Query(None, description="Filters Report data by format.", alias="output_format"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for Report name.")] = Query(None, description="Wildcard search for Report name.", alias="query"),
    source: Annotated[Optional[StrictStr], Field(description="Filters Report data by source.")] = Query(None, description="Filters Report data by source.", alias="source"),
    state: Annotated[Optional[StrictStr], Field(description="Filters Report data by state.")] = Query(None, description="Filters Report data by state.", alias="state"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Report records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Report records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> ReportList:
    """Outlines the parameters, optional and required, used when requesting the data for all Reports"""
    if not BaseReportsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportsApi.subclasses[0]().report_index(x_api_version, category, created_before, created_since, fields, ids, kind, limit, output_format, page_token, query, source, state, updated_since)


@router.get(
    "/reports/{id}.json",
    responses={
        200: {"model": ReportShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Reports"],
    summary="Return the data for a single Report",
    response_model_by_alias=True,
)
async def report_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Report.")] = Path(..., description="The unique identifier for the Report."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> ReportShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Report"""
    if not BaseReportsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportsApi.subclasses[0]().report_show(id, if_modified_since, if_none_match, x_api_version, fields)
