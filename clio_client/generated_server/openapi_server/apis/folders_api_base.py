# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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


class BaseFoldersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseFoldersApi.subclasses = BaseFoldersApi.subclasses + (cls,)
    async def folder_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        folder_create_request: Annotated[Optional[FolderCreateRequest], Field(description="Request Body for Folders")],
    ) -> FolderShow:
        """Create a Folder to an existing folder. """
        ...


    async def folder_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Folder.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Deleting a Folder using this method will move it to the trash instead of permanently deleting it. Trashed Folders are permanently deleted after 30 days. The following errors may be returned:  - &#x60;400 Bad Request&#x60;: The Folder cannot be trashed. The &#x60;type&#x60; of the error will be &#x60;DeleteFailed&#x60; and the &#x60;message&#x60; of the error will be one of the following:   - &#x60;Delete failed: This folder contains more than 100,000 items and cannot be trashed. Please trash some of the items inside it before trying again.&#x60;   - &#x60;Delete failed: This item contains locked items and cannot be deleted.&#x60;   - &#x60;Delete failed: The root folder cannot be trashed&#x60; - &#x60;409 Conflict&#x60;: The Folder (or one of its descendants) is currently being modified by another request, and cannot be trashed. """
        ...


    async def folder_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Folder records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        document_category_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")],
        external_property_name: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")],
        external_property_value: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Folder records to those having the specified unique identifiers.")],
        include_deleted: Annotated[Optional[StrictBool], Field(description="Allow trashed Folder record to be included.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Folder records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        parent_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword `null` is not valid for this field. If no Folder is provided, it will default to the account's root Folder.  When returning the data for all Folders, use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. ")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching the given string.")],
        scope: Annotated[Optional[StrictStr], Field(description="Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Folder records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> FolderList:
        """Outlines the parameters, optional and required, used when requesting the data for all Folders"""
        ...


    async def folder_list(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Folder records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        document_category_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")],
        external_property_name: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")],
        external_property_value: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Folder records to those having the specified unique identifiers.")],
        include_deleted: Annotated[Optional[StrictBool], Field(description="Allow trashed Folder record to be included.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Folder records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        parent_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword `null` is not valid for this field. If no Folder is provided, it will default to the account's root Folder.  When returning the data for all Folders, use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. ")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching the given string.")],
        scope: Annotated[Optional[StrictStr], Field(description="Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`.")],
        show_uncompleted: Annotated[Optional[StrictBool], Field(description="Allow Folder record being uploaded to be included.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Folder records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ItemList:
        """Return the data of the contents of a Folder. """
        ...


    async def folder_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Folder.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> FolderShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Folder"""
        ...


    async def folder_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Folder.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        folder_update_request: Annotated[Optional[FolderUpdateRequest], Field(description="Request Body for Folders")],
    ) -> FolderShow:
        """Update Folder, move Folder to another Folder, and/or restore a trashed Folder. """
        ...
