# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.matter_dockets_api_base import BaseMatterDocketsApi
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
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.error import Error
from clio_mock.models.matter_docket_create_request import MatterDocketCreateRequest


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/court_rules/matter_dockets.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Matter Dockets"],
    summary="Creates a matter docket",
    response_model_by_alias=True,
)
async def matter_docket_create(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    matter_docket_create_request: Annotated[Optional[MatterDocketCreateRequest], Field(description="Request Body for Matter Dockets")] = Body(None, description="Request Body for Matter Dockets"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new MatterDocket"""
    if not BaseMatterDocketsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterDocketsApi.subclasses[0]().matter_docket_create(x_api_versio_nheader, fieldsquery, matter_docket_create_request)


@router.delete(
    "/court_rules/matter_dockets/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Matter Dockets"],
    summary="Deletes the requested matter docket",
    response_model_by_alias=True,
)
async def matter_docket_destroy(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single MatterDocket"""
    if not BaseMatterDocketsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterDocketsApi.subclasses[0]().matter_docket_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/court_rules/matter_dockets.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Matter Dockets"],
    summary="Return the data for all matter dockets",
    response_model_by_alias=True,
)
async def matter_docket_index(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="matter_idquery"),
    matter_statusquery: Annotated[Optional[StrictStr], Field(description="Filter MatterDocket records to those with Matters having a specific status.")] = Query(None, description="Filter MatterDocket records to those with Matters having a specific status.", alias="matter_statusquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    service_type_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single ServiceType. Use the keyword `null` to match those without a MatterDocket. The list will be filtered to include only the MatterDocket records with the matching property.")] = Query(None, description="The unique identifier for a single ServiceType. Use the keyword &#x60;null&#x60; to match those without a MatterDocket. The list will be filtered to include only the MatterDocket records with the matching property.", alias="service_type_idquery"),
    statusquery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those that are draft, billed, unbilled or non-billable.")] = Query(None, description="Filter Activity records to those that are draft, billed, unbilled or non-billable.", alias="statusquery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all MatterDockets"""
    if not BaseMatterDocketsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterDocketsApi.subclasses[0]().matter_docket_index(x_api_versio_nheader, created_sincequery, fieldsquery, idsquery, limitquery, matter_idquery, matter_statusquery, orderquery, page_tokenquery, queryquery, service_type_idquery, statusquery, updated_sincequery)


@router.get(
    "/court_rules/matter_dockets/preview.json",
    responses={
        303: {"description": "See Other"},
        400: {"model": Error, "description": "Bad Request"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Matter Dockets"],
    summary="Preview calendar dates for the docket",
    response_model_by_alias=True,
)
async def matter_docket_preview(
    jurisdictionidquery: Annotated[StrictInt, Field(description="The unique identifier for a single Jurisdiction. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")] = Query(None, description="The unique identifier for a single Jurisdiction. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.", alias="jurisdictionidquery"),
    service_typeidquery: Annotated[StrictInt, Field(description="The unique identifier for a single ServiceType. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")] = Query(None, description="The unique identifier for a single ServiceType. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.", alias="service_typeidquery"),
    start_timequery: Annotated[datetime, Field(description="The time the MatterDocket should start. (Expects an ISO-8601 timestamp).")] = Query(None, description="The time the MatterDocket should start. (Expects an ISO-8601 timestamp).", alias="start_timequery"),
    triggeridquery: Annotated[StrictInt, Field(description="The unique identifier for a single JurisdictionsToTrigger. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")] = Query(None, description="The unique identifier for a single JurisdictionsToTrigger. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.", alias="triggeridquery"),
    event_prefixquery: Annotated[Optional[StrictStr], Field(description="The prefix that will be added to the beginning of all court rule event titles")] = Query(None, description="The prefix that will be added to the beginning of all court rule event titles", alias="event_prefixquery"),
    start_datequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those whose `date` is on or after the date provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Activity records to those whose &#x60;date&#x60; is on or after the date provided (Expects an ISO-8601 date).", alias="start_datequery"),
) -> None:
    """Preview calendar dates for the docket"""
    if not BaseMatterDocketsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterDocketsApi.subclasses[0]().matter_docket_preview(jurisdictionidquery, service_typeidquery, start_timequery, triggeridquery, event_prefixquery, start_datequery)


@router.get(
    "/court_rules/matter_dockets/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Matter Dockets"],
    summary="Return the data for the matter docket",
    response_model_by_alias=True,
)
async def matter_docket_show(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single MatterDocket"""
    if not BaseMatterDocketsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterDocketsApi.subclasses[0]().matter_docket_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, fieldsquery)
