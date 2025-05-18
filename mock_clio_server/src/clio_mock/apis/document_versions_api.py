# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.document_versions_api_base import BaseDocumentVersionsApi
import clio_mock.impl

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

from clio_mock.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.error import Error


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/documents/{id}/versions.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    idquery: Annotated[StrictInt, Field(description="The unique identifier for the DocumentVersion.")] = Query(None, description="The unique identifier for the DocumentVersion.", alias="idquery"),
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    fully_uploadedquery: Annotated[Optional[StrictBool], Field(description="Filter DocumentVersion records to those with the given `fully_uploaded` status.")] = Query(None, description="Filter DocumentVersion records to those with the given &#x60;fully_uploaded&#x60; status.", alias="fully_uploadedquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all DocumentVersions"""
    if not BaseDocumentVersionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentVersionsApi.subclasses[0]().document_version_index(idquery, idpath, x_api_versio_nheader, fieldsquery, fully_uploadedquery, limitquery, page_tokenquery)
