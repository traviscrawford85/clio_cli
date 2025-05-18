# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.medical_records_details_api_base import BaseMedicalRecordsDetailsApi
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
from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.error import Error
from clio_mock.models.medical_records_request_create_request import MedicalRecordsRequestCreateRequest
from clio_mock.models.medical_records_request_update_request import MedicalRecordsRequestUpdateRequest


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/medical_records_details.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Medical Records Details"],
    summary="Creating a Medical Records Detail, Medical Records and Medical Bills",
    response_model_by_alias=True,
)
async def medical_records_request_create(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    medical_records_request_create_request: Annotated[Optional[MedicalRecordsRequestCreateRequest], Field(description="Request Body for Medical Records Details")] = Body(None, description="Request Body for Medical Records Details"),
) -> ActivityShow:
    """This endpoint allows a creation of a Medical Records Detail, multiple Medical Records and Medical Bills. Medical Liens can also be created as a property under Medical Bills.  Reference the payload to see how the records are being passed in. """
    if not BaseMedicalRecordsDetailsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMedicalRecordsDetailsApi.subclasses[0]().medical_records_request_create(x_api_versio_nheader, fieldsquery, medical_records_request_create_request)


@router.delete(
    "/medical_records_details/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Medical Records Details"],
    summary="Destroying a Medical Records Detail",
    response_model_by_alias=True,
)
async def medical_records_request_destroy(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """When a Medical Records Detail is destroyed, the child records, such as Medical Records, Medical Bills and Liens will also be destroyed in the same transaction. """
    if not BaseMedicalRecordsDetailsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMedicalRecordsDetailsApi.subclasses[0]().medical_records_request_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/medical_records_details.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Medical Records Details"],
    summary="Return the data for all Medical Records Details",
    response_model_by_alias=True,
)
async def medical_records_request_index(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    treatment_end_datequery: Annotated[Optional[datetime], Field(description="Filters Medical Records data by treatment end date.")] = Query(None, description="Filters Medical Records data by treatment end date.", alias="treatment_end_datequery"),
    treatment_start_datequery: Annotated[Optional[datetime], Field(description="Filters Medical Records data by treatment start date.")] = Query(None, description="Filters Medical Records data by treatment start date.", alias="treatment_start_datequery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all Medical Records Details """
    if not BaseMedicalRecordsDetailsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMedicalRecordsDetailsApi.subclasses[0]().medical_records_request_index(x_api_versio_nheader, created_sincequery, fieldsquery, idsquery, limitquery, page_tokenquery, treatment_end_datequery, treatment_start_datequery, updated_sincequery)


@router.get(
    "/medical_records_details/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Medical Records Details"],
    summary="Return the data for a single Medical Records Detail",
    response_model_by_alias=True,
)
async def medical_records_request_show(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single Medical Records Details """
    if not BaseMedicalRecordsDetailsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMedicalRecordsDetailsApi.subclasses[0]().medical_records_request_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, fieldsquery)


@router.patch(
    "/medical_records_details/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Medical Records Details"],
    summary="Updating a Medical Records Detail",
    response_model_by_alias=True,
)
async def medical_records_request_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    medical_records_request_update_request: Annotated[Optional[MedicalRecordsRequestUpdateRequest], Field(description="Request Body for Medical Records Details")] = Body(None, description="Request Body for Medical Records Details"),
) -> ActivityList:
    """If there are records being passed into the Medical Records or Medical Bills parameter they will be treated as new records and new Medical Records / Medical Bills will be created. """
    if not BaseMedicalRecordsDetailsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMedicalRecordsDetailsApi.subclasses[0]().medical_records_request_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, medical_records_request_update_request)
