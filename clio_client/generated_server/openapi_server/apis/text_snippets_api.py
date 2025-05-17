# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.text_snippets_api_base import BaseTextSnippetsApi
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
from openapi_server.models.text_snippet_create_request import TextSnippetCreateRequest
from openapi_server.models.text_snippet_list import TextSnippetList
from openapi_server.models.text_snippet_show import TextSnippetShow
from openapi_server.models.text_snippet_update_request import TextSnippetUpdateRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/settings/text_snippets.json",
    responses={
        201: {"model": TextSnippetShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Text Snippets"],
    summary="Create a text snippet",
    response_model_by_alias=True,
)
async def text_snippet_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    text_snippet_create_request: Annotated[Optional[TextSnippetCreateRequest], Field(description="Request Body for Text Snippets")] = Body(None, description="Request Body for Text Snippets"),
) -> TextSnippetShow:
    """Outlines the parameters and data fields used when creating a new TextSnippet"""
    if not BaseTextSnippetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTextSnippetsApi.subclasses[0]().text_snippet_create(x_api_version, fields, text_snippet_create_request)


@router.delete(
    "/settings/text_snippets/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Text Snippets"],
    summary="Destroy a text snippet",
    response_model_by_alias=True,
)
async def text_snippet_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the TextSnippet.")] = Path(..., description="The unique identifier for the TextSnippet."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single TextSnippet"""
    if not BaseTextSnippetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTextSnippetsApi.subclasses[0]().text_snippet_destroy(id, x_api_version)


@router.get(
    "/settings/text_snippets.json",
    responses={
        200: {"model": TextSnippetList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Text Snippets"],
    summary="Return all text snippets",
    response_model_by_alias=True,
)
async def text_snippet_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter TextSnippet records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter TextSnippet records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter TextSnippet records to those having the specified unique identifiers.")] = Query(None, description="Filter TextSnippet records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of TextSnippet records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of TextSnippet records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the TextSnippet records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the TextSnippet records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `snippet` or `phrase` matching a given string.")] = Query(None, description="Wildcard search for &#x60;snippet&#x60; or &#x60;phrase&#x60; matching a given string.", alias="query"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter TextSnippet records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter TextSnippet records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> TextSnippetList:
    """Outlines the parameters, optional and required, used when requesting the data for all TextSnippets"""
    if not BaseTextSnippetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTextSnippetsApi.subclasses[0]().text_snippet_index(x_api_version, created_since, fields, ids, limit, order, page_token, query, updated_since)


@router.get(
    "/settings/text_snippets/{id}.json",
    responses={
        200: {"model": TextSnippetShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Text Snippets"],
    summary="Return the data for the text snippet",
    response_model_by_alias=True,
)
async def text_snippet_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the TextSnippet.")] = Path(..., description="The unique identifier for the TextSnippet."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> TextSnippetShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single TextSnippet"""
    if not BaseTextSnippetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTextSnippetsApi.subclasses[0]().text_snippet_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/settings/text_snippets/{id}.json",
    responses={
        200: {"model": TextSnippetShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Text Snippets"],
    summary="Update a text snippet",
    response_model_by_alias=True,
)
async def text_snippet_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the TextSnippet.")] = Path(..., description="The unique identifier for the TextSnippet."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    text_snippet_update_request: Annotated[Optional[TextSnippetUpdateRequest], Field(description="Request Body for Text Snippets")] = Body(None, description="Request Body for Text Snippets"),
) -> TextSnippetShow:
    """Outlines the parameters and data fields used when updating a single TextSnippet"""
    if not BaseTextSnippetsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTextSnippetsApi.subclasses[0]().text_snippet_update(id, if_match, x_api_version, fields, text_snippet_update_request)
