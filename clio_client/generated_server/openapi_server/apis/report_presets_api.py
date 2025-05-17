# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.report_presets_api_base import BaseReportPresetsApi
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
from openapi_server.models.report_preset_create_request import ReportPresetCreateRequest
from openapi_server.models.report_preset_list import ReportPresetList
from openapi_server.models.report_preset_show import ReportPresetShow
from openapi_server.models.report_preset_update_request import ReportPresetUpdateRequest
from openapi_server.models.report_show import ReportShow


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/report_presets.json",
    responses={
        201: {"model": ReportPresetShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Report Presets"],
    summary="Create a new ReportPreset",
    response_model_by_alias=True,
)
async def report_preset_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    report_preset_create_request: Annotated[Optional[ReportPresetCreateRequest], Field(description="Request Body for Report Presets")] = Body(None, description="Request Body for Report Presets"),
) -> ReportPresetShow:
    """Outlines the parameters and data fields used when creating a new ReportPreset"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_create(x_api_version, fields, report_preset_create_request)


@router.delete(
    "/report_presets/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Report Presets"],
    summary="Delete a single ReportPreset",
    response_model_by_alias=True,
)
async def report_preset_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ReportPreset.")] = Path(..., description="The unique identifier for the ReportPreset."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single ReportPreset"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_destroy(id, x_api_version)


@router.post(
    "/report_presets/{id}/generate_report.json",
    responses={
        201: {"model": ReportShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        404: {"model": Error, "description": "Not Found"},
        403: {"model": Error, "description": "Forbidden"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Report Presets"],
    summary="Generate a new report for a given preset",
    response_model_by_alias=True,
)
async def report_preset_generate_report(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ReportPreset.")] = Path(..., description="The unique identifier for the ReportPreset."),
) -> ReportShow:
    """Generate a new report for a given preset"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_generate_report(id)


@router.get(
    "/report_presets.json",
    responses={
        200: {"model": ReportPresetList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Report Presets"],
    summary="Return the data for all ReportPresets",
    response_model_by_alias=True,
)
async def report_preset_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    category: Annotated[Optional[StrictStr], Field(description="Filters ReportPreset data by category.")] = Query(None, description="Filters ReportPreset data by category.", alias="category"),
    created_since: Annotated[Optional[datetime], Field(description="Filter ReportPreset records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter ReportPreset records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    has_schedule: Annotated[Optional[StrictBool], Field(description="Filters ReportPreset records to those that have or do not have a Report Schedule.")] = Query(None, description="Filters ReportPreset records to those that have or do not have a Report Schedule.", alias="has_schedule"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter ReportPreset records to those having the specified unique identifiers.")] = Query(None, description="Filter ReportPreset records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ReportPreset records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of ReportPreset records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the ReportPreset records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the ReportPreset records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    output_format: Annotated[Optional[StrictStr], Field(description="Filters ReportPreset data by format.")] = Query(None, description="Filters ReportPreset data by format.", alias="output_format"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for ReportPreset name.")] = Query(None, description="Wildcard search for ReportPreset name.", alias="query"),
    schedule_frequency: Annotated[Optional[StrictStr], Field(description="Filters ReportPreset records to those that have a Report Schedule of the specified frequency.")] = Query(None, description="Filters ReportPreset records to those that have a Report Schedule of the specified frequency.", alias="schedule_frequency"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter ReportPreset records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter ReportPreset records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> ReportPresetList:
    """Outlines the parameters, optional and required, used when requesting the data for all ReportPresets"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_index(x_api_version, category, created_since, fields, has_schedule, ids, limit, order, output_format, page_token, query, schedule_frequency, updated_since)


@router.get(
    "/report_presets/{id}.json",
    responses={
        200: {"model": ReportPresetShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Report Presets"],
    summary="Return the data for a single ReportPreset",
    response_model_by_alias=True,
)
async def report_preset_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ReportPreset.")] = Path(..., description="The unique identifier for the ReportPreset."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> ReportPresetShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single ReportPreset"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/report_presets/{id}.json",
    responses={
        200: {"model": ReportPresetShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Report Presets"],
    summary="Update a single ReportPreset",
    response_model_by_alias=True,
)
async def report_preset_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ReportPreset.")] = Path(..., description="The unique identifier for the ReportPreset."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    report_preset_update_request: Annotated[Optional[ReportPresetUpdateRequest], Field(description="Request Body for Report Presets")] = Body(None, description="Request Body for Report Presets"),
) -> ReportPresetShow:
    """Outlines the parameters and data fields used when updating a single ReportPreset"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_update(id, if_match, x_api_version, fields, report_preset_update_request)
