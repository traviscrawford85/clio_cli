# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.documents_api_base import BaseDocumentsApi
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
from openapi_server.models.document_copy_request import DocumentCopyRequest
from openapi_server.models.document_create_request import DocumentCreateRequest
from openapi_server.models.document_list import DocumentList
from openapi_server.models.document_show import DocumentShow
from openapi_server.models.document_update_request import DocumentUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/documents/{id}/copy.json",
    responses={
        404: {"model": Error, "description": "Not Found"},
        400: {"model": Error, "description": "Bad Request"},
        201: {"model": DocumentShow, "description": "Created"},
    },
    tags=["Documents"],
    summary="Copy a Document",
    response_model_by_alias=True,
)
async def document_copy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Document.")] = Path(..., description="The unique identifier for the Document."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    document_copy_request: Annotated[Optional[DocumentCopyRequest], Field(description="Request Body for Documents")] = Body(None, description="Request Body for Documents"),
) -> DocumentShow:
    """Copies the latest document version of a Document into a new Document. The parameters &#x60;filename&#x60; and &#x60;name&#x60; will be copied from the source Document if none are provided. """
    if not BaseDocumentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentsApi.subclasses[0]().document_copy(id, fields, document_copy_request)


@router.post(
    "/documents.json",
    responses={
        201: {"model": DocumentShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Documents"],
    summary="Create a new Document",
    response_model_by_alias=True,
)
async def document_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    document_create_request: Annotated[Optional[DocumentCreateRequest], Field(description="Request Body for Documents")] = Body(None, description="Request Body for Documents"),
) -> DocumentShow:
    """Create a Document, or Create Document Version to an existing Document. """
    if not BaseDocumentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentsApi.subclasses[0]().document_create(x_api_version, fields, document_create_request)


@router.delete(
    "/documents/{id}.json",
    responses={
        204: {"description": "No Content"},
        409: {"model": Error, "description": "Conflict"},
    },
    tags=["Documents"],
    summary="Delete a single Document",
    response_model_by_alias=True,
)
async def document_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Document.")] = Path(..., description="The unique identifier for the Document."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Deleting a Document using this method will move it to the trash instead of permanently deleting it. Trashed Documents are permanently deleted after 30 days. The following errors may be returned:  - &#x60;409 Conflict&#x60;: The Document (or one of its ancestor folders) is currently being modified by another request, and cannot be trashed. """
    if not BaseDocumentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentsApi.subclasses[0]().document_destroy(id, x_api_version)


@router.get(
    "/documents/{id}/download.json",
    responses={
        303: {"description": "See Other"},
        404: {"description": "Not Found"},
        400: {"description": "Bad Request"},
    },
    tags=["Documents"],
    summary="Download the Document",
    response_model_by_alias=True,
)
async def document_download(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Document.")] = Path(..., description="The unique identifier for the Document."),
    document_version_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a DocumentVersion to be downloaded. Defaults to the latest.")] = Query(None, description="The unique identifier for a DocumentVersion to be downloaded. Defaults to the latest.", alias="document_version_id"),
) -> None:
    """Download the Document"""
    if not BaseDocumentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentsApi.subclasses[0]().document_download(id, document_version_id)


@router.get(
    "/documents.json",
    responses={
        200: {"model": DocumentList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Documents"],
    summary="Return the data for all Documents",
    response_model_by_alias=True,
)
async def document_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property.", alias="contact_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter Document records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Document records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    document_category_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")] = Query(None, description="The unique identifier for a single DocumentCategory. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property.", alias="document_category_id"),
    external_property_name: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")] = Query(None, description="Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; ", alias="external_property_name"),
    external_property_value: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")] = Query(None, description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; ", alias="external_property_value"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Document records to those having the specified unique identifiers.")] = Query(None, description="Filter Document records to those having the specified unique identifiers.", alias="ids[]"),
    include_deleted: Annotated[Optional[StrictBool], Field(description="Allow trashed Document record to be included.")] = Query(None, description="Allow trashed Document record to be included.", alias="include_deleted"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Document records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Document records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property.", alias="matter_id"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Document records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Document records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    parent_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Folder. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")] = Query(None, description="The unique identifier for a single Folder. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property.", alias="parent_id"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching the given string.")] = Query(None, description="Wildcard search for &#x60;name&#x60; matching the given string.", alias="query"),
    scope: Annotated[Optional[StrictStr], Field(description="Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`.")] = Query(None, description="Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is &#x60;children&#x60;.", alias="scope"),
    show_uncompleted: Annotated[Optional[StrictBool], Field(description="Allow Document record being uploaded to be included.")] = Query(None, description="Allow Document record being uploaded to be included.", alias="show_uncompleted"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Document records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Document records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> DocumentList:
    """Outlines the parameters, optional and required, used when requesting the data for all Documents"""
    if not BaseDocumentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentsApi.subclasses[0]().document_index(x_api_version, contact_id, created_since, document_category_id, external_property_name, external_property_value, fields, ids, include_deleted, limit, matter_id, order, page_token, parent_id, query, scope, show_uncompleted, updated_since)


@router.get(
    "/documents/{id}.json",
    responses={
        200: {"model": DocumentShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Documents"],
    summary="Return the data for a single Document",
    response_model_by_alias=True,
)
async def document_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Document.")] = Path(..., description="The unique identifier for the Document."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> DocumentShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Document"""
    if not BaseDocumentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentsApi.subclasses[0]().document_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/documents/{id}.json",
    responses={
        200: {"model": DocumentShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Documents"],
    summary="Update a single Document",
    response_model_by_alias=True,
)
async def document_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Document.")] = Path(..., description="The unique identifier for the Document."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    document_update_request: Annotated[Optional[DocumentUpdateRequest], Field(description="Request Body for Documents")] = Body(None, description="Request Body for Documents"),
) -> DocumentShow:
    """Update Document, move Document to another Folder, and/or restore a trashed Document. """
    if not BaseDocumentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentsApi.subclasses[0]().document_update(id, if_match, x_api_version, fields, document_update_request)
