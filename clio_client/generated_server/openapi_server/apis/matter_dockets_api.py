# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.matter_dockets_api_base import BaseMatterDocketsApi
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
from openapi_server.models.matter_docket_create_request import MatterDocketCreateRequest
from openapi_server.models.matter_docket_list import MatterDocketList
from openapi_server.models.matter_docket_show import MatterDocketShow


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/court_rules/matter_dockets.json",
    responses={
        201: {"model": MatterDocketShow, "description": "Created"},
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
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    matter_docket_create_request: Annotated[Optional[MatterDocketCreateRequest], Field(description="Request Body for Matter Dockets")] = Body(None, description="Request Body for Matter Dockets"),
) -> MatterDocketShow:
    """Outlines the parameters and data fields used when creating a new MatterDocket"""
    if not BaseMatterDocketsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterDocketsApi.subclasses[0]().matter_docket_create(x_api_version, fields, matter_docket_create_request)


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
    id: Annotated[StrictInt, Field(description="The unique identifier for the MatterDocket.")] = Path(..., description="The unique identifier for the MatterDocket."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single MatterDocket"""
    if not BaseMatterDocketsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterDocketsApi.subclasses[0]().matter_docket_destroy(id, x_api_version)


@router.get(
    "/court_rules/matter_dockets.json",
    responses={
        200: {"model": MatterDocketList, "description": "Ok"},
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
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter MatterDocket records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter MatterDocket records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter MatterDocket records to those having the specified unique identifiers.")] = Query(None, description="Filter MatterDocket records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of MatterDocket records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of MatterDocket records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.", alias="matter_id"),
    matter_status: Annotated[Optional[StrictStr], Field(description="Filter MatterDocket records to those with Matters having a specific status.")] = Query(None, description="Filter MatterDocket records to those with Matters having a specific status.", alias="matter_status"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the MatterDocket records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the MatterDocket records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching a given string.")] = Query(None, description="Wildcard search for &#x60;name&#x60; matching a given string.", alias="query"),
    service_type_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single ServiceType. Use the keyword `null` to match those without a MatterDocket. The list will be filtered to include only the MatterDocket records with the matching property.")] = Query(None, description="The unique identifier for a single ServiceType. Use the keyword &#x60;null&#x60; to match those without a MatterDocket. The list will be filtered to include only the MatterDocket records with the matching property.", alias="service_type_id"),
    status: Annotated[Optional[StrictStr], Field(description="Filter MatterDocket records to those having a specific status.")] = Query(None, description="Filter MatterDocket records to those having a specific status.", alias="status"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter MatterDocket records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter MatterDocket records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> MatterDocketList:
    """Outlines the parameters, optional and required, used when requesting the data for all MatterDockets"""
    if not BaseMatterDocketsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterDocketsApi.subclasses[0]().matter_docket_index(x_api_version, created_since, fields, ids, limit, matter_id, matter_status, order, page_token, query, service_type_id, status, updated_since)


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
    jurisdiction_id: Annotated[StrictInt, Field(description="The unique identifier for a single Jurisdiction. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")] = Query(None, description="The unique identifier for a single Jurisdiction. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.", alias="jurisdiction[id]"),
    service_type_id: Annotated[StrictInt, Field(description="The unique identifier for a single ServiceType. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")] = Query(None, description="The unique identifier for a single ServiceType. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.", alias="service_type[id]"),
    start_date: Annotated[datetime, Field(description="The date the MatterDocket should start. (Expects an ISO-8601 date).")] = Query(None, description="The date the MatterDocket should start. (Expects an ISO-8601 date).", alias="start_date"),
    start_time: Annotated[datetime, Field(description="The time the MatterDocket should start. (Expects an ISO-8601 timestamp).")] = Query(None, description="The time the MatterDocket should start. (Expects an ISO-8601 timestamp).", alias="start_time"),
    trigger_id: Annotated[StrictInt, Field(description="The unique identifier for a single JurisdictionsToTrigger. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")] = Query(None, description="The unique identifier for a single JurisdictionsToTrigger. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.", alias="trigger[id]"),
    event_prefix: Annotated[Optional[StrictStr], Field(description="The prefix that will be added to the beginning of all court rule event titles")] = Query(None, description="The prefix that will be added to the beginning of all court rule event titles", alias="event_prefix"),
) -> None:
    """Preview calendar dates for the docket"""
    if not BaseMatterDocketsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterDocketsApi.subclasses[0]().matter_docket_preview(jurisdiction_id, service_type_id, start_date, start_time, trigger_id, event_prefix)


@router.get(
    "/court_rules/matter_dockets/{id}.json",
    responses={
        200: {"model": MatterDocketShow, "description": "Ok"},
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
    id: Annotated[StrictInt, Field(description="The unique identifier for the MatterDocket.")] = Path(..., description="The unique identifier for the MatterDocket."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> MatterDocketShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single MatterDocket"""
    if not BaseMatterDocketsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterDocketsApi.subclasses[0]().matter_docket_show(id, if_modified_since, if_none_match, x_api_version, fields)
