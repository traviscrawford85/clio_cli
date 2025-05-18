# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.line_items_api_base import BaseLineItemsApi
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
from datetime import datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.error import Error
from clio_mock.models.line_item_update_request import LineItemUpdateRequest


router = APIRouter()

ns_pkg = clio_mock.impl
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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """A LineItem can not be deleted if it&#39;s Bill is not editable"""
    if not BaseLineItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLineItemsApi.subclasses[0]().line_item_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/line_items.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    activity_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Activity. Use the keyword `null` to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property.")] = Query(None, description="The unique identifier for a single Activity. Use the keyword &#x60;null&#x60; to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property.", alias="activity_idquery"),
    bill_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.")] = Query(None, description="The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.", alias="bill_idquery"),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    displayquery: Annotated[Optional[StrictBool], Field(description="Set this flag to true to return only LineItems displayed on the bill.")] = Query(None, description="Set this flag to true to return only LineItems displayed on the bill.", alias="displayquery"),
    exclude_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact records to those who are not included in the given list of unique identifiers.")] = Query(None, description="Filter Contact records to those who are not included in the given list of unique identifiers.", alias="exclude_idsquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    group_orderingquery: Annotated[Optional[StrictInt], Field(description="Filters LineItem records to match given group ordering.")] = Query(None, description="Filters LineItem records to match given group ordering.", alias="group_orderingquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    kindquery: Annotated[Optional[StrictStr], Field(description="The kind of LineItem.")] = Query(None, description="The kind of LineItem.", alias="kindquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="matter_idquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all LineItems"""
    if not BaseLineItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLineItemsApi.subclasses[0]().line_item_index(x_api_versio_nheader, activity_idquery, bill_idquery, created_sincequery, displayquery, exclude_idsquery, fieldsquery, group_orderingquery, idsquery, kindquery, limitquery, matter_idquery, page_tokenquery, queryquery, updated_sincequery)


@router.patch(
    "/line_items/{id}.json",
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
    tags=["Line Items"],
    summary="Update a single LineItem",
    response_model_by_alias=True,
)
async def line_item_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    line_item_update_request: Annotated[Optional[LineItemUpdateRequest], Field(description="Request Body for Line Items")] = Body(None, description="Request Body for Line Items"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single LineItem"""
    if not BaseLineItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLineItemsApi.subclasses[0]().line_item_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, line_item_update_request)
