# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.document_archives_api_base import BaseDocumentArchivesApi
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
from datetime import date
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.document_archive_create_request import DocumentArchiveCreateRequest
from openapi_server.models.document_archive_show import DocumentArchiveShow
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/document_archives.json",
    responses={
        201: {"model": DocumentArchiveShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Document Archives"],
    summary="Create a new DocumentArchive",
    response_model_by_alias=True,
)
async def document_archive_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    document_archive_create_request: Annotated[Optional[DocumentArchiveCreateRequest], Field(description="Request Body for Document Archives")] = Body(None, description="Request Body for Document Archives"),
) -> DocumentArchiveShow:
    """Outlines the parameters and data fields used when creating a new DocumentArchive"""
    if not BaseDocumentArchivesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentArchivesApi.subclasses[0]().document_archive_create(x_api_version, fields, document_archive_create_request)


@router.get(
    "/document_archives/{id}/download.json",
    responses={
        303: {"description": "See Other"},
        404: {"description": "Not Found"},
    },
    tags=["Document Archives"],
    summary="Download the DocumentArchive",
    response_model_by_alias=True,
)
async def document_archive_download(
    id: Annotated[StrictInt, Field(description="The unique identifier for the DocumentArchive.")] = Path(..., description="The unique identifier for the DocumentArchive."),
) -> None:
    """Download the DocumentArchive"""
    if not BaseDocumentArchivesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentArchivesApi.subclasses[0]().document_archive_download(id)


@router.get(
    "/document_archives/{id}.json",
    responses={
        200: {"model": DocumentArchiveShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Document Archives"],
    summary="Return the data for a single DocumentArchive",
    response_model_by_alias=True,
)
async def document_archive_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the DocumentArchive.")] = Path(..., description="The unique identifier for the DocumentArchive."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> DocumentArchiveShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single DocumentArchive"""
    if not BaseDocumentArchivesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentArchivesApi.subclasses[0]().document_archive_show(id, if_modified_since, if_none_match, x_api_version, fields)
