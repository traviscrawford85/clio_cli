# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.trust_line_items_api_base import BaseTrustLineItemsApi
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
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.trust_line_item_list import TrustLineItemList
from openapi_server.models.trust_line_item_show import TrustLineItemShow
from openapi_server.models.trust_line_item_update_request import TrustLineItemUpdateRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/trust_line_items.json",
    responses={
        200: {"model": TrustLineItemList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Trust Line Items"],
    summary="Return the data for all TrustLineItems",
    response_model_by_alias=True,
)
async def trust_line_item_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    bill_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the TrustLineItem records with the matching property.")] = Query(None, description="The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the TrustLineItem records with the matching property.", alias="bill_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter TrustLineItem records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter TrustLineItem records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter TrustLineItem records to those having the specified unique identifiers.")] = Query(None, description="Filter TrustLineItem records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of TrustLineItem records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of TrustLineItem records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a TrustLineItem. The list will be filtered to include only the TrustLineItem records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a TrustLineItem. The list will be filtered to include only the TrustLineItem records with the matching property.", alias="matter_id"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the TrustLineItem records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the TrustLineItem records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter TrustLineItem records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter TrustLineItem records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> TrustLineItemList:
    """Outlines the parameters, optional and required, used when requesting the data for all TrustLineItems"""
    if not BaseTrustLineItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTrustLineItemsApi.subclasses[0]().trust_line_item_index(x_api_version, bill_id, created_since, fields, ids, limit, matter_id, order, page_token, updated_since)


@router.patch(
    "/trust_line_items/{id}.json",
    responses={
        200: {"model": TrustLineItemShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Trust Line Items"],
    summary="Update a single TrustLineItem",
    response_model_by_alias=True,
)
async def trust_line_item_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the TrustLineItem.")] = Path(..., description="The unique identifier for the TrustLineItem."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    trust_line_item_update_request: Annotated[Optional[TrustLineItemUpdateRequest], Field(description="Request Body for Trust Line Items")] = Body(None, description="Request Body for Trust Line Items"),
) -> TrustLineItemShow:
    """Outlines the parameters and data fields used when updating a single TrustLineItem"""
    if not BaseTrustLineItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTrustLineItemsApi.subclasses[0]().trust_line_item_update(id, if_match, x_api_version, fields, trust_line_item_update_request)
