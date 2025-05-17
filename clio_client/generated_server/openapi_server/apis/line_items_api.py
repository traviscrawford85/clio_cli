# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.line_items_api_base import BaseLineItemsApi
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
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.line_item_list import LineItemList
from openapi_server.models.line_item_show import LineItemShow
from openapi_server.models.line_item_update_request import LineItemUpdateRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/line_items/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Line Items"],
    summary="Delete a single LineItem",
    response_model_by_alias=True,
)
async def line_item_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the LineItem.")] = Path(..., description="The unique identifier for the LineItem."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """A LineItem can not be deleted if it&#39;s Bill is not editable"""
    if not BaseLineItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLineItemsApi.subclasses[0]().line_item_destroy(id, x_api_version)


@router.get(
    "/line_items.json",
    responses={
        200: {"model": LineItemList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Line Items"],
    summary="Return the data for all LineItems",
    response_model_by_alias=True,
)
async def line_item_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    activity_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Activity. Use the keyword `null` to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property.")] = Query(None, description="The unique identifier for a single Activity. Use the keyword &#x60;null&#x60; to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property.", alias="activity_id"),
    bill_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the LineItem records with the matching property.")] = Query(None, description="The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the LineItem records with the matching property.", alias="bill_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter LineItem records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter LineItem records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    display: Annotated[Optional[StrictBool], Field(description="Set this flag to true to return only LineItems displayed on the bill.")] = Query(None, description="Set this flag to true to return only LineItems displayed on the bill.", alias="display"),
    exclude_ids: Annotated[Optional[StrictInt], Field(description="Array containing LineItem identifiers that should be excluded from the query.")] = Query(None, description="Array containing LineItem identifiers that should be excluded from the query.", alias="exclude_ids[]"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    group_ordering: Annotated[Optional[StrictInt], Field(description="Filters LineItem records to match given group ordering.")] = Query(None, description="Filters LineItem records to match given group ordering.", alias="group_ordering"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter LineItem records to those having the specified unique identifiers.")] = Query(None, description="Filter LineItem records to those having the specified unique identifiers.", alias="ids[]"),
    kind: Annotated[Optional[StrictStr], Field(description="The kind of LineItem.")] = Query(None, description="The kind of LineItem.", alias="kind"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of LineItem records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of LineItem records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property.", alias="matter_id"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `description` or `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;description&#x60; or &#x60;note&#x60; matching a given string.", alias="query"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter LineItem records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter LineItem records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> LineItemList:
    """Outlines the parameters, optional and required, used when requesting the data for all LineItems"""
    if not BaseLineItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLineItemsApi.subclasses[0]().line_item_index(x_api_version, activity_id, bill_id, created_since, display, exclude_ids, fields, group_ordering, ids, kind, limit, matter_id, page_token, query, updated_since)


@router.patch(
    "/line_items/{id}.json",
    responses={
        200: {"model": LineItemShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Line Items"],
    summary="Update a single LineItem",
    response_model_by_alias=True,
)
async def line_item_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the LineItem.")] = Path(..., description="The unique identifier for the LineItem."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    line_item_update_request: Annotated[Optional[LineItemUpdateRequest], Field(description="Request Body for Line Items")] = Body(None, description="Request Body for Line Items"),
) -> LineItemShow:
    """Outlines the parameters and data fields used when updating a single LineItem"""
    if not BaseLineItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLineItemsApi.subclasses[0]().line_item_update(id, if_match, x_api_version, fields, line_item_update_request)
