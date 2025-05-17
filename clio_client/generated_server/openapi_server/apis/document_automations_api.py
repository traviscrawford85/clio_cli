# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.document_automations_api_base import BaseDocumentAutomationsApi
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
from openapi_server.models.document_automation_create_request import DocumentAutomationCreateRequest
from openapi_server.models.document_automation_list import DocumentAutomationList
from openapi_server.models.document_automation_show import DocumentAutomationShow
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/document_automations.json",
    responses={
        201: {"model": DocumentAutomationShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Document Automations"],
    summary="Create a new DocumentAutomation",
    response_model_by_alias=True,
)
async def document_automation_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    document_automation_create_request: Annotated[Optional[DocumentAutomationCreateRequest], Field(description="Request Body for Document Automations")] = Body(None, description="Request Body for Document Automations"),
) -> DocumentAutomationShow:
    """Outlines the parameters and data fields used when creating a new DocumentAutomation"""
    if not BaseDocumentAutomationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentAutomationsApi.subclasses[0]().document_automation_create(x_api_version, fields, document_automation_create_request)


@router.get(
    "/document_automations.json",
    responses={
        200: {"model": DocumentAutomationList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Document Automations"],
    summary="Return the data for all DocumentAutomations",
    response_model_by_alias=True,
)
async def document_automation_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter DocumentAutomation records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter DocumentAutomation records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter DocumentAutomation records to those having the specified unique identifiers.")] = Query(None, description="Filter DocumentAutomation records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of DocumentAutomation records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of DocumentAutomation records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the DocumentAutomation records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the DocumentAutomation records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter DocumentAutomation records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter DocumentAutomation records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> DocumentAutomationList:
    """Outlines the parameters, optional and required, used when requesting the data for all DocumentAutomations"""
    if not BaseDocumentAutomationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentAutomationsApi.subclasses[0]().document_automation_index(x_api_version, created_since, fields, ids, limit, order, page_token, updated_since)


@router.get(
    "/document_automations/{id}.json",
    responses={
        200: {"model": DocumentAutomationShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Document Automations"],
    summary="Return the data for a single DocumentAutomation",
    response_model_by_alias=True,
)
async def document_automation_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the DocumentAutomation.")] = Path(..., description="The unique identifier for the DocumentAutomation."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> DocumentAutomationShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single DocumentAutomation"""
    if not BaseDocumentAutomationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentAutomationsApi.subclasses[0]().document_automation_show(id, if_modified_since, if_none_match, x_api_version, fields)
