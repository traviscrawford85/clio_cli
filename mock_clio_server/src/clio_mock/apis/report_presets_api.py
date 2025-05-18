# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.report_presets_api_base import BaseReportPresetsApi
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
from clio_mock.models.error import Error
from clio_mock.models.report_preset_create_request import ReportPresetCreateRequest
from clio_mock.models.report_preset_update_request import ReportPresetUpdateRequest


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/report_presets.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    report_preset_create_request: Annotated[Optional[ReportPresetCreateRequest], Field(description="Request Body for Report Presets")] = Body(None, description="Request Body for Report Presets"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new ReportPreset"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_create(x_api_versio_nheader, fieldsquery, report_preset_create_request)


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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single ReportPreset"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_destroy(idpath, x_api_versio_nheader)


@router.post(
    "/report_presets/{id}/generate_report.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
) -> ActivityShow:
    """Generate a new report for a given preset"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_generate_report(idpath)


@router.get(
    "/report_presets.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    categoryquery: Annotated[Optional[StrictStr], Field(description="Filters Report data by category.")] = Query(None, description="Filters Report data by category.", alias="categoryquery"),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    has_schedulequery: Annotated[Optional[StrictBool], Field(description="Filters ReportPreset records to those that have or do not have a Report Schedule.")] = Query(None, description="Filters ReportPreset records to those that have or do not have a Report Schedule.", alias="has_schedulequery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    output_formatquery: Annotated[Optional[StrictStr], Field(description="Filters Report data by format.")] = Query(None, description="Filters Report data by format.", alias="output_formatquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    schedule_frequencyquery: Annotated[Optional[StrictStr], Field(description="Filters ReportPreset records to those that have a Report Schedule of the specified frequency.")] = Query(None, description="Filters ReportPreset records to those that have a Report Schedule of the specified frequency.", alias="schedule_frequencyquery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all ReportPresets"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_index(x_api_versio_nheader, categoryquery, created_sincequery, fieldsquery, has_schedulequery, idsquery, limitquery, orderquery, output_formatquery, page_tokenquery, queryquery, schedule_frequencyquery, updated_sincequery)


@router.get(
    "/report_presets/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single ReportPreset"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, fieldsquery)


@router.patch(
    "/report_presets/{id}.json",
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
    tags=["Report Presets"],
    summary="Update a single ReportPreset",
    response_model_by_alias=True,
)
async def report_preset_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    report_preset_update_request: Annotated[Optional[ReportPresetUpdateRequest], Field(description="Request Body for Report Presets")] = Body(None, description="Request Body for Report Presets"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single ReportPreset"""
    if not BaseReportPresetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReportPresetsApi.subclasses[0]().report_preset_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, report_preset_update_request)
