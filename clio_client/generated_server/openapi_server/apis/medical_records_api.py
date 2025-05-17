# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.medical_records_api_base import BaseMedicalRecordsApi
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
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.medical_record_show import MedicalRecordShow
from openapi_server.models.medical_record_update_request import MedicalRecordUpdateRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/medical_records/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Medical Records"],
    summary="Destroying a Medical Record",
    response_model_by_alias=True,
)
async def medical_record_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the MedicalRecord.")] = Path(..., description="The unique identifier for the MedicalRecord."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single MedicalRecord"""
    if not BaseMedicalRecordsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMedicalRecordsApi.subclasses[0]().medical_record_destroy(id, x_api_version)


@router.patch(
    "/medical_records/{id}.json",
    responses={
        200: {"model": MedicalRecordShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Medical Records"],
    summary="Updating a Medical Record",
    response_model_by_alias=True,
)
async def medical_record_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the MedicalRecord.")] = Path(..., description="The unique identifier for the MedicalRecord."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    medical_record_update_request: Annotated[Optional[MedicalRecordUpdateRequest], Field(description="Request Body for Medical Records")] = Body(None, description="Request Body for Medical Records"),
) -> MedicalRecordShow:
    """Outlines the parameters and data fields used when updating a single MedicalRecord"""
    if not BaseMedicalRecordsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMedicalRecordsApi.subclasses[0]().medical_record_update(id, if_match, x_api_version, fields, medical_record_update_request)
