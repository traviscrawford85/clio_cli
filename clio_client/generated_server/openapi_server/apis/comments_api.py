# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.comments_api_base import BaseCommentsApi
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
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.comment_create_request import CommentCreateRequest
from openapi_server.models.comment_list import CommentList
from openapi_server.models.comment_show import CommentShow
from openapi_server.models.comment_update_request import CommentUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/comments.json",
    responses={
        201: {"model": CommentShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Comments"],
    summary="Create a new Comment",
    response_model_by_alias=True,
)
async def comment_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    comment_create_request: Annotated[Optional[CommentCreateRequest], Field(description="Request Body for Comments")] = Body(None, description="Request Body for Comments"),
) -> CommentShow:
    """Outlines the parameters and data fields used when creating a new Comment"""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comment_create(x_api_version, fields, comment_create_request)


@router.delete(
    "/comments/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Comments"],
    summary="Delete a single Comment",
    response_model_by_alias=True,
)
async def comment_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Comment.")] = Path(..., description="The unique identifier for the Comment."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Comment"""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comment_destroy(id, x_api_version)


@router.get(
    "/comments.json",
    responses={
        200: {"model": CommentList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Comments"],
    summary="Return the data for all Comments",
    response_model_by_alias=True,
)
async def comment_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter Comment records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Comment records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    item_id: Annotated[Optional[StrictInt], Field(description="The ID of the Document or Folder this Comment belongs to")] = Query(None, description="The ID of the Document or Folder this Comment belongs to", alias="item_id"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Comment records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Comment records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Comment records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Comment records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> CommentList:
    """Outlines the parameters, optional and required, used when requesting the data for all Comments"""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comment_index(x_api_version, created_since, fields, item_id, limit, page_token, updated_since)


@router.get(
    "/comments/{id}.json",
    responses={
        200: {"model": CommentShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Comments"],
    summary="Return the data for a single Comment",
    response_model_by_alias=True,
)
async def comment_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Comment.")] = Path(..., description="The unique identifier for the Comment."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> CommentShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Comment"""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comment_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/comments/{id}.json",
    responses={
        200: {"model": CommentShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Comments"],
    summary="Update a single Comment",
    response_model_by_alias=True,
)
async def comment_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Comment.")] = Path(..., description="The unique identifier for the Comment."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    comment_update_request: Annotated[Optional[CommentUpdateRequest], Field(description="Request Body for Comments")] = Body(None, description="Request Body for Comments"),
) -> CommentShow:
    """Outlines the parameters and data fields used when updating a single Comment"""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comment_update(id, if_match, x_api_version, fields, comment_update_request)
