# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.folders_api_base import BaseFoldersApi
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
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.error import Error
from clio_mock.models.folder_create_request import FolderCreateRequest
from clio_mock.models.folder_update_request import FolderUpdateRequest


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/folders.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Folders"],
    summary="Create a new Folder",
    response_model_by_alias=True,
)
async def folder_create(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    folder_create_request: Annotated[Optional[FolderCreateRequest], Field(description="Request Body for Folders")] = Body(None, description="Request Body for Folders"),
) -> ActivityShow:
    """Create a Folder to an existing folder. """
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_create(x_api_versio_nheader, fieldsquery, folder_create_request)


@router.delete(
    "/folders/{id}.json",
    responses={
        204: {"description": "No Content"},
        400: {"model": Error, "description": "Bad Request"},
        409: {"model": Error, "description": "Conflict"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Folders"],
    summary="Delete a single Folder",
    response_model_by_alias=True,
)
async def folder_destroy(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Deleting a Folder using this method will move it to the trash instead of permanently deleting it. Trashed Folders are permanently deleted after 30 days. The following errors may be returned:  - &#x60;400 Bad Request&#x60;: The Folder cannot be trashed. The &#x60;type&#x60; of the error will be &#x60;DeleteFailed&#x60; and the &#x60;message&#x60; of the error will be one of the following:   - &#x60;Delete failed: This folder contains more than 100,000 items and cannot be trashed. Please trash some of the items inside it before trying again.&#x60;   - &#x60;Delete failed: This item contains locked items and cannot be deleted.&#x60;   - &#x60;Delete failed: The root folder cannot be trashed&#x60; - &#x60;409 Conflict&#x60;: The Folder (or one of its descendants) is currently being modified by another request, and cannot be trashed. """
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/folders.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Folders"],
    summary="Return the data for all Folders",
    response_model_by_alias=True,
)
async def folder_index(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    contact_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.", alias="contact_idquery"),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    document_category_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")] = Query(None, description="The unique identifier for a single DocumentCategory. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property.", alias="document_category_idquery"),
    external_property_namequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")] = Query(None, description="Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; ", alias="external_property_namequery"),
    external_property_valuequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")] = Query(None, description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; ", alias="external_property_valuequery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    include_deletedquery: Annotated[Optional[StrictBool], Field(description="Allow trashed Document record to be included.")] = Query(None, description="Allow trashed Document record to be included.", alias="include_deletedquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="matter_idquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    parent_idquery: Annotated[Optional[StrictInt], Field(description="ID of parent (either a Payment or CreditMemo) this allocation belongs to")] = Query(None, description="ID of parent (either a Payment or CreditMemo) this allocation belongs to", alias="parent_idquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    scopequery: Annotated[Optional[StrictStr], Field(description="Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`.")] = Query(None, description="Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is &#x60;children&#x60;.", alias="scopequery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all Folders"""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_index(x_api_versio_nheader, contact_idquery, created_sincequery, document_category_idquery, external_property_namequery, external_property_valuequery, fieldsquery, idsquery, include_deletedquery, limitquery, matter_idquery, orderquery, page_tokenquery, parent_idquery, queryquery, scopequery, updated_sincequery)


@router.get(
    "/folders/list.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Folders"],
    summary="Return the data of the contents of a Folder",
    response_model_by_alias=True,
)
async def folder_list(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    contact_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.", alias="contact_idquery"),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    document_category_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")] = Query(None, description="The unique identifier for a single DocumentCategory. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property.", alias="document_category_idquery"),
    external_property_namequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")] = Query(None, description="Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; ", alias="external_property_namequery"),
    external_property_valuequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")] = Query(None, description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; ", alias="external_property_valuequery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    include_deletedquery: Annotated[Optional[StrictBool], Field(description="Allow trashed Document record to be included.")] = Query(None, description="Allow trashed Document record to be included.", alias="include_deletedquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="matter_idquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    parent_idquery: Annotated[Optional[StrictInt], Field(description="ID of parent (either a Payment or CreditMemo) this allocation belongs to")] = Query(None, description="ID of parent (either a Payment or CreditMemo) this allocation belongs to", alias="parent_idquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    scopequery: Annotated[Optional[StrictStr], Field(description="Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`.")] = Query(None, description="Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is &#x60;children&#x60;.", alias="scopequery"),
    show_uncompletedquery: Annotated[Optional[StrictBool], Field(description="Allow Document record being uploaded to be included.")] = Query(None, description="Allow Document record being uploaded to be included.", alias="show_uncompletedquery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Return the data of the contents of a Folder. """
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_list(x_api_versio_nheader, contact_idquery, created_sincequery, document_category_idquery, external_property_namequery, external_property_valuequery, fieldsquery, idsquery, include_deletedquery, limitquery, matter_idquery, orderquery, page_tokenquery, parent_idquery, queryquery, scopequery, show_uncompletedquery, updated_sincequery)


@router.get(
    "/folders/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Folders"],
    summary="Return the data for a single Folder",
    response_model_by_alias=True,
)
async def folder_show(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single Folder"""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, fieldsquery)


@router.patch(
    "/folders/{id}.json",
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
    tags=["Folders"],
    summary="Update a single Folder",
    response_model_by_alias=True,
)
async def folder_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    folder_update_request: Annotated[Optional[FolderUpdateRequest], Field(description="Request Body for Folders")] = Body(None, description="Request Body for Folders"),
) -> ActivityList:
    """Update Folder, move Folder to another Folder, and/or restore a trashed Folder. """
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, folder_update_request)
