# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.document_versions_api_base import BaseDocumentVersionsApi
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
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.document_version_list import DocumentVersionList
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/documents/{id}/versions.json",
    responses={
        200: {"model": DocumentVersionList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Document Versions"],
    summary="Return the data for all DocumentVersions",
    response_model_by_alias=True,
)
async def document_version_index(
    document_version_id: Annotated[StrictInt, Query( description="The unique identifier for the DocumentVersion.", alias="id")] = None],
    document_id: Annotated[StrictInt, Path(..., description="ID of the Document")],
    x_api_version: Annotated[Optional[StrictStr], Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    fields: Annotated[Optional[StrictStr], Query( description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields)] = None.", alias="fields")],
    fully_uploaded: Annotated[Optional[StrictBool], Query( description="Filter DocumentVersion records to those with the given `fully_uploaded` status.", alias="fully_uploaded")] = None],
    limit: Annotated[Optional[StrictInt], Query( description="A limit on the number of DocumentVersion records to be returned. Limit can range between 1 and 200. Default: `200`.", alias="limit")] = None],
    page_token: Annotated[Optional[StrictStr], Query( description="A token specifying which page to return.", alias="page_token")] = None],
) -> DocumentVersionList:
    """Outlines the parameters, optional and required, used when requesting the data for all DocumentVersions"""
    if not BaseDocumentVersionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentVersionsApi.subclasses[0]().document_version_index(
        document_version_id, document_id, x_api_version, fields, fully_uploaded, limit, page_token
    )

