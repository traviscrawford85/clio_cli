# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.folders_api_base import BaseFoldersApi
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
from openapi_server.models.folder_create_request import FolderCreateRequest
from openapi_server.models.folder_list import FolderList
from openapi_server.models.folder_show import FolderShow
from openapi_server.models.folder_update_request import FolderUpdateRequest
from openapi_server.models.item_list import ItemList


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/folders.json",
    responses={
        201: {"model": FolderShow, "description": "Created"},
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
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    folder_create_request: Annotated[Optional[FolderCreateRequest], Field(description="Request Body for Folders")] = Body(None, description="Request Body for Folders"),
) -> FolderShow:
    """Create a Folder to an existing folder. """
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_create(x_api_version, fields, folder_create_request)


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
    id: Annotated[StrictInt, Field(description="The unique identifier for the Folder.")] = Path(..., description="The unique identifier for the Folder."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Deleting a Folder using this method will move it to the trash instead of permanently deleting it. Trashed Folders are permanently deleted after 30 days. The following errors may be returned:  - &#x60;400 Bad Request&#x60;: The Folder cannot be trashed. The &#x60;type&#x60; of the error will be &#x60;DeleteFailed&#x60; and the &#x60;message&#x60; of the error will be one of the following:   - &#x60;Delete failed: This folder contains more than 100,000 items and cannot be trashed. Please trash some of the items inside it before trying again.&#x60;   - &#x60;Delete failed: This item contains locked items and cannot be deleted.&#x60;   - &#x60;Delete failed: The root folder cannot be trashed&#x60; - &#x60;409 Conflict&#x60;: The Folder (or one of its descendants) is currently being modified by another request, and cannot be trashed. """
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_destroy(id, x_api_version)


@router.get(
    "/folders.json",
    responses={
        200: {"model": FolderList, "description": "Ok"},
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
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.", alias="contact_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter Folder records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Folder records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    document_category_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")] = Query(None, description="The unique identifier for a single DocumentCategory. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.", alias="document_category_id"),
    external_property_name: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")] = Query(None, description="Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; ", alias="external_property_name"),
    external_property_value: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")] = Query(None, description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; ", alias="external_property_value"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Folder records to those having the specified unique identifiers.")] = Query(None, description="Filter Folder records to those having the specified unique identifiers.", alias="ids[]"),
    include_deleted: Annotated[Optional[StrictBool], Field(description="Allow trashed Folder record to be included.")] = Query(None, description="Allow trashed Folder record to be included.", alias="include_deleted"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.", alias="matter_id"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Folder records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Folder records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    parent_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword `null` is not valid for this field. If no Folder is provided, it will default to the account's root Folder.  When returning the data for all Folders, use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. ")] = Query(None, description="The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword &#x60;null&#x60; is not valid for this field. If no Folder is provided, it will default to the account&#39;s root Folder.  When returning the data for all Folders, use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. ", alias="parent_id"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching the given string.")] = Query(None, description="Wildcard search for &#x60;name&#x60; matching the given string.", alias="query"),
    scope: Annotated[Optional[StrictStr], Field(description="Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`.")] = Query(None, description="Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is &#x60;children&#x60;.", alias="scope"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Folder records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Folder records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> FolderList:
    """Outlines the parameters, optional and required, used when requesting the data for all Folders"""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_index(x_api_version, contact_id, created_since, document_category_id, external_property_name, external_property_value, fields, ids, include_deleted, limit, matter_id, order, page_token, parent_id, query, scope, updated_since)


@router.get(
    "/folders/list.json",
    responses={
        200: {"model": ItemList, "description": "Ok"},
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
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.", alias="contact_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter Folder records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Folder records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    document_category_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")] = Query(None, description="The unique identifier for a single DocumentCategory. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.", alias="document_category_id"),
    external_property_name: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")] = Query(None, description="Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; ", alias="external_property_name"),
    external_property_value: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")] = Query(None, description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; ", alias="external_property_value"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Folder records to those having the specified unique identifiers.")] = Query(None, description="Filter Folder records to those having the specified unique identifiers.", alias="ids[]"),
    include_deleted: Annotated[Optional[StrictBool], Field(description="Allow trashed Folder record to be included.")] = Query(None, description="Allow trashed Folder record to be included.", alias="include_deleted"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.", alias="matter_id"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Folder records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Folder records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    parent_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword `null` is not valid for this field. If no Folder is provided, it will default to the account's root Folder.  When returning the data for all Folders, use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. ")] = Query(None, description="The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword &#x60;null&#x60; is not valid for this field. If no Folder is provided, it will default to the account&#39;s root Folder.  When returning the data for all Folders, use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. ", alias="parent_id"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching the given string.")] = Query(None, description="Wildcard search for &#x60;name&#x60; matching the given string.", alias="query"),
    scope: Annotated[Optional[StrictStr], Field(description="Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`.")] = Query(None, description="Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is &#x60;children&#x60;.", alias="scope"),
    show_uncompleted: Annotated[Optional[StrictBool], Field(description="Allow Folder record being uploaded to be included.")] = Query(None, description="Allow Folder record being uploaded to be included.", alias="show_uncompleted"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Folder records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Folder records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> ItemList:
    """Return the data of the contents of a Folder. """
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_list(x_api_version, contact_id, created_since, document_category_id, external_property_name, external_property_value, fields, ids, include_deleted, limit, matter_id, order, page_token, parent_id, query, scope, show_uncompleted, updated_since)


@router.get(
    "/folders/{id}.json",
    responses={
        200: {"model": FolderShow, "description": "Ok"},
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
    id: Annotated[StrictInt, Field(description="The unique identifier for the Folder.")] = Path(..., description="The unique identifier for the Folder."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> FolderShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Folder"""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/folders/{id}.json",
    responses={
        200: {"model": FolderShow, "description": "Ok"},
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
    id: Annotated[StrictInt, Field(description="The unique identifier for the Folder.")] = Path(..., description="The unique identifier for the Folder."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    folder_update_request: Annotated[Optional[FolderUpdateRequest], Field(description="Request Body for Folders")] = Body(None, description="Request Body for Folders"),
) -> FolderShow:
    """Update Folder, move Folder to another Folder, and/or restore a trashed Folder. """
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folder_update(id, if_match, x_api_version, fields, folder_update_request)
