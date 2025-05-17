# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.log_entries_api_base import BaseLogEntriesApi
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
from openapi_server.models.log_entry_list import LogEntryList


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/log_entries.json",
    responses={
        200: {"model": LogEntryList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Log Entries"],
    summary="Return the data for all LogEntries",
    response_model_by_alias=True,
)
async def log_entry_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter LogEntry records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter LogEntry records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter LogEntry records to those having the specified unique identifiers.")] = Query(None, description="Filter LogEntry records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of LogEntry records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of LogEntry records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the LogEntry records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the LogEntry records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter LogEntry records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter LogEntry records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> LogEntryList:
    """Outlines the parameters, optional and required, used when requesting the data for all LogEntries"""
    if not BaseLogEntriesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLogEntriesApi.subclasses[0]().log_entry_index(x_api_version, created_since, fields, ids, limit, order, page_token, updated_since)
