# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.notes_api_base import BaseNotesApi
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
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.note_create_request import NoteCreateRequest
from openapi_server.models.note_list import NoteList
from openapi_server.models.note_show import NoteShow
from openapi_server.models.note_update_request import NoteUpdateRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/notes.json",
    responses={
        201: {"model": NoteShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Notes"],
    summary="Create a new Note",
    response_model_by_alias=True,
)
async def note_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    note_create_request: Annotated[Optional[NoteCreateRequest], Field(description="Request Body for Notes")] = Body(None, description="Request Body for Notes"),
) -> NoteShow:
    """Outlines the parameters and data fields used when creating a new Note"""
    if not BaseNotesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNotesApi.subclasses[0]().note_create(x_api_version, fields, note_create_request)


@router.delete(
    "/notes/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Notes"],
    summary="Delete a single Note",
    response_model_by_alias=True,
)
async def note_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Note.")] = Path(..., description="The unique identifier for the Note."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Note"""
    if not BaseNotesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNotesApi.subclasses[0]().note_destroy(id, x_api_version)


@router.get(
    "/notes.json",
    responses={
        200: {"model": NoteList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Notes"],
    summary="Return the data for all Notes",
    response_model_by_alias=True,
)
async def note_index(
    type: Annotated[StrictStr, Field(description="Filter Note records to those of the specified type.")] = Query(None, description="Filter Note records to those of the specified type.", alias="type"),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Note records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Note records with the matching property.", alias="contact_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter Note records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Note records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    has_time_entries: Annotated[Optional[StrictBool], Field(description="Filter Note records to those with or without associated time entries.")] = Query(None, description="Filter Note records to those with or without associated time entries.", alias="has_time_entries"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Note records to those having the specified unique identifiers.")] = Query(None, description="Filter Note records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Note records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Note records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the Note records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Note records with the matching property.", alias="matter_id"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Note records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Note records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search across note subject and detail.")] = Query(None, description="Wildcard search across note subject and detail.", alias="query"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Note records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Note records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> NoteList:
    """Outlines the parameters, optional and required, used when requesting the data for all Notes"""
    if not BaseNotesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNotesApi.subclasses[0]().note_index(type, x_api_version, contact_id, created_since, fields, has_time_entries, ids, limit, matter_id, order, page_token, query, updated_since)


@router.get(
    "/notes/{id}.json",
    responses={
        200: {"model": NoteShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Notes"],
    summary="Return the data for a single Note",
    response_model_by_alias=True,
)
async def note_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Note.")] = Path(..., description="The unique identifier for the Note."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> NoteShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Note"""
    if not BaseNotesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNotesApi.subclasses[0]().note_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/notes/{id}.json",
    responses={
        200: {"model": NoteShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Notes"],
    summary="Update a single Note",
    response_model_by_alias=True,
)
async def note_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Note.")] = Path(..., description="The unique identifier for the Note."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    note_update_request: Annotated[Optional[NoteUpdateRequest], Field(description="Request Body for Notes")] = Body(None, description="Request Body for Notes"),
) -> NoteShow:
    """Outlines the parameters and data fields used when updating a single Note"""
    if not BaseNotesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNotesApi.subclasses[0]().note_update(id, if_match, x_api_version, fields, note_update_request)
