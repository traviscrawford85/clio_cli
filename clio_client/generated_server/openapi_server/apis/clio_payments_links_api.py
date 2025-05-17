# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.clio_payments_links_api_base import BaseClioPaymentsLinksApi
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
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.clio_payments_link_create_request import ClioPaymentsLinkCreateRequest
from openapi_server.models.clio_payments_link_list import ClioPaymentsLinkList
from openapi_server.models.clio_payments_link_show import ClioPaymentsLinkShow
from openapi_server.models.clio_payments_link_update_request import ClioPaymentsLinkUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/clio_payments/links.json",
    responses={
        201: {"model": ClioPaymentsLinkShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Clio Payments Links"],
    summary="Create a new ClioPaymentsLink",
    response_model_by_alias=True,
)
async def clio_payments_link_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    clio_payments_link_create_request: Annotated[Optional[ClioPaymentsLinkCreateRequest], Field(description="Request Body for Links")] = Body(None, description="Request Body for Links"),
) -> ClioPaymentsLinkShow:
    """Outlines the parameters and data fields used when creating a new ClioPaymentsLink"""
    if not BaseClioPaymentsLinksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClioPaymentsLinksApi.subclasses[0]().clio_payments_link_create(x_api_version, fields, clio_payments_link_create_request)


@router.get(
    "/clio_payments/links.json",
    responses={
        200: {"model": ClioPaymentsLinkList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Clio Payments Links"],
    summary="Return the data for all ClioPaymentsLinks",
    response_model_by_alias=True,
)
async def clio_payments_link_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    active: Annotated[Optional[StrictBool], Field(description="Filter ClioPaymentsLink records based on whether or not they have expired.")] = Query(None, description="Filter ClioPaymentsLink records based on whether or not they have expired.", alias="active"),
    created_since: Annotated[Optional[datetime], Field(description="Filter ClioPaymentsLink records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter ClioPaymentsLink records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter ClioPaymentsLink records to those having the specified unique identifiers.")] = Query(None, description="Filter ClioPaymentsLink records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ClioPaymentsLink records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of ClioPaymentsLink records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter ClioPaymentsLink records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter ClioPaymentsLink records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> ClioPaymentsLinkList:
    """Outlines the parameters, optional and required, used when requesting the data for all ClioPaymentsLinks"""
    if not BaseClioPaymentsLinksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClioPaymentsLinksApi.subclasses[0]().clio_payments_link_index(x_api_version, active, created_since, fields, ids, limit, page_token, updated_since)


@router.get(
    "/clio_payments/links/{id}.json",
    responses={
        200: {"model": ClioPaymentsLinkShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Clio Payments Links"],
    summary="Return the data for a single ClioPaymentsLink",
    response_model_by_alias=True,
)
async def clio_payments_link_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ClioPaymentsLink.")] = Path(..., description="The unique identifier for the ClioPaymentsLink."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> ClioPaymentsLinkShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single ClioPaymentsLink"""
    if not BaseClioPaymentsLinksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClioPaymentsLinksApi.subclasses[0]().clio_payments_link_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/clio_payments/links/{id}.json",
    responses={
        200: {"model": ClioPaymentsLinkShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Clio Payments Links"],
    summary="Update a single ClioPaymentsLink",
    response_model_by_alias=True,
)
async def clio_payments_link_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ClioPaymentsLink.")] = Path(..., description="The unique identifier for the ClioPaymentsLink."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    clio_payments_link_update_request: Annotated[Optional[ClioPaymentsLinkUpdateRequest], Field(description="Request Body for Links")] = Body(None, description="Request Body for Links"),
) -> ClioPaymentsLinkShow:
    """Outlines the parameters and data fields used when updating a single ClioPaymentsLink"""
    if not BaseClioPaymentsLinksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClioPaymentsLinksApi.subclasses[0]().clio_payments_link_update(id, if_match, x_api_version, fields, clio_payments_link_update_request)
