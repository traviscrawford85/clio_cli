# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.jurisdictions_to_triggers_api_base import BaseJurisdictionsToTriggersApi
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
from openapi_server.models.jurisdictions_to_trigger_list import JurisdictionsToTriggerList
from openapi_server.models.jurisdictions_to_trigger_show import JurisdictionsToTriggerShow


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/court_rules/jurisdictions/{jurisdiction_id}/triggers.json",
    responses={
        200: {"model": JurisdictionsToTriggerList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Jurisdictions To Triggers"],
    summary="Return the data for all triggers",
    response_model_by_alias=True,
)
async def jurisdictions_to_trigger_index(
    jurisdiction_id: Annotated[StrictInt, Field(description="The unique identifier for the Jurisdiction.")] = Path(..., description="The unique identifier for the Jurisdiction."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter JurisdictionsToTrigger records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter JurisdictionsToTrigger records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter JurisdictionsToTrigger records to those having the specified unique identifiers.")] = Query(None, description="Filter JurisdictionsToTrigger records to those having the specified unique identifiers.", alias="ids[]"),
    is_requirements_required: Annotated[Optional[StrictBool], Field(description="Filter JurisdictionsToTrigger records to those which require addition requirements to be checked (usually specifying trigger time).")] = Query(None, description="Filter JurisdictionsToTrigger records to those which require addition requirements to be checked (usually specifying trigger time).", alias="is_requirements_required"),
    is_served: Annotated[Optional[StrictBool], Field(description="Filter JurisdictionsToTrigger records to those which require a service type to be selected.")] = Query(None, description="Filter JurisdictionsToTrigger records to those which require a service type to be selected.", alias="is_served"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of JurisdictionsToTrigger records to be returned. Limit can range between 1 and 1000. Default: `1000`.")] = Query(None, description="A limit on the number of JurisdictionsToTrigger records to be returned. Limit can range between 1 and 1000. Default: &#x60;1000&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the JurisdictionsToTrigger records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the JurisdictionsToTrigger records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `description` matching a given string.")] = Query(None, description="Wildcard search for &#x60;description&#x60; matching a given string.", alias="query"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter JurisdictionsToTrigger records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter JurisdictionsToTrigger records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> JurisdictionsToTriggerList:
    """Outlines the parameters, optional and required, used when requesting the data for all JurisdictionsToTriggers"""
    if not BaseJurisdictionsToTriggersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseJurisdictionsToTriggersApi.subclasses[0]().jurisdictions_to_trigger_index(jurisdiction_id, x_api_version, created_since, fields, ids, is_requirements_required, is_served, limit, order, page_token, query, updated_since)


@router.get(
    "/court_rules/jurisdictions/{jurisdiction_id}/triggers/{id}.json",
    responses={
        200: {"model": JurisdictionsToTriggerShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Jurisdictions To Triggers"],
    summary="Return the data for the trigger",
    response_model_by_alias=True,
)
async def jurisdictions_to_trigger_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the JurisdictionsToTrigger.")] = Path(..., description="The unique identifier for the JurisdictionsToTrigger."),
    jurisdiction_id: Annotated[StrictInt, Field(description="The unique identifier for the Jurisdiction.")] = Path(..., description="The unique identifier for the Jurisdiction."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> JurisdictionsToTriggerShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single JurisdictionsToTrigger"""
    if not BaseJurisdictionsToTriggersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseJurisdictionsToTriggersApi.subclasses[0]().jurisdictions_to_trigger_show(id, jurisdiction_id, if_modified_since, if_none_match, x_api_version, fields)
