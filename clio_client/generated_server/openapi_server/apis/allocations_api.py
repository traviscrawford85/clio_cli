# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.allocations_api_base import BaseAllocationsApi
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
from openapi_server.models.allocation_list import AllocationList
from openapi_server.models.allocation_show import AllocationShow
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/allocations.json",
    responses={
        200: {"model": AllocationList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Allocations"],
    summary="Return the data for all Allocations",
    response_model_by_alias=True,
)
async def allocation_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    bill_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.")] = Query(None, description="The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.", alias="bill_id"),
    contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.", alias="contact_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter Allocation records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Allocation records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Allocation records to those having the specified unique identifiers.")] = Query(None, description="Filter Allocation records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Allocation records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Allocation records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.", alias="matter_id"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Allocation records by the given field. Default: `date(asc)`.")] = Query(None, description="Orders the Allocation records by the given field. Default: &#x60;date(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    parent_id: Annotated[Optional[StrictInt], Field(description="ID of parent (either a Payment or CreditMemo) this allocation belongs to")] = Query(None, description="ID of parent (either a Payment or CreditMemo) this allocation belongs to", alias="parent_id"),
    parent_type: Annotated[Optional[StrictInt], Field(description="Filter Allocation records based on whether the parent is a CreditMemo or a Payment.")] = Query(None, description="Filter Allocation records based on whether the parent is a CreditMemo or a Payment.", alias="parent_type"),
    status: Annotated[Optional[StrictStr], Field(description="Filter Allocation records to only those that are voided (`\"invalid\"`) or not voided (`\"valid\"`).")] = Query(None, description="Filter Allocation records to only those that are voided (&#x60;\&quot;invalid\&quot;&#x60;) or not voided (&#x60;\&quot;valid\&quot;&#x60;).", alias="status"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Allocation records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Allocation records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> AllocationList:
    """Outlines the parameters, optional and required, used when requesting the data for all Allocations"""
    if not BaseAllocationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAllocationsApi.subclasses[0]().allocation_index(x_api_version, bill_id, contact_id, created_since, fields, ids, limit, matter_id, order, page_token, parent_id, parent_type, status, updated_since)


@router.get(
    "/allocations/{id}.json",
    responses={
        200: {"model": AllocationShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Allocations"],
    summary="Return the data for a single Allocation",
    response_model_by_alias=True,
)
async def allocation_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Allocation.")] = Path(..., description="The unique identifier for the Allocation."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> AllocationShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Allocation"""
    if not BaseAllocationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAllocationsApi.subclasses[0]().allocation_show(id, if_modified_since, if_none_match, x_api_version, fields)
