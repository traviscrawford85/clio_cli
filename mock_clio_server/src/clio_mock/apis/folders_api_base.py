# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.folder_create_request import FolderCreateRequest
from clio_mock.models.folder_update_request import FolderUpdateRequest


class BaseFoldersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseFoldersApi.subclasses = BaseFoldersApi.subclasses + (cls,)
    async def folder_create(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        folder_create_request: Annotated[Optional[FolderCreateRequest], Field(description="Request Body for Folders")],
    ) -> ActivityShow:
        """Create a Folder to an existing folder. """
        ...


    async def folder_destroy(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Deleting a Folder using this method will move it to the trash instead of permanently deleting it. Trashed Folders are permanently deleted after 30 days. The following errors may be returned:  - &#x60;400 Bad Request&#x60;: The Folder cannot be trashed. The &#x60;type&#x60; of the error will be &#x60;DeleteFailed&#x60; and the &#x60;message&#x60; of the error will be one of the following:   - &#x60;Delete failed: This folder contains more than 100,000 items and cannot be trashed. Please trash some of the items inside it before trying again.&#x60;   - &#x60;Delete failed: This item contains locked items and cannot be deleted.&#x60;   - &#x60;Delete failed: The root folder cannot be trashed&#x60; - &#x60;409 Conflict&#x60;: The Folder (or one of its descendants) is currently being modified by another request, and cannot be trashed. """
        ...


    async def folder_index(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        contact_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.")],
        created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        document_category_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")],
        external_property_namequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")],
        external_property_valuequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")],
        include_deletedquery: Annotated[Optional[StrictBool], Field(description="Allow trashed Document record to be included.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        parent_idquery: Annotated[Optional[StrictInt], Field(description="ID of parent (either a Payment or CreditMemo) this allocation belongs to")],
        queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")],
        scopequery: Annotated[Optional[StrictStr], Field(description="Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`.")],
        updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all Folders"""
        ...


    async def folder_list(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        contact_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.")],
        created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        document_category_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")],
        external_property_namequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")],
        external_property_valuequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")],
        include_deletedquery: Annotated[Optional[StrictBool], Field(description="Allow trashed Document record to be included.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        parent_idquery: Annotated[Optional[StrictInt], Field(description="ID of parent (either a Payment or CreditMemo) this allocation belongs to")],
        queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")],
        scopequery: Annotated[Optional[StrictStr], Field(description="Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`.")],
        show_uncompletedquery: Annotated[Optional[StrictBool], Field(description="Allow Document record being uploaded to be included.")],
        updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ActivityList:
        """Return the data of the contents of a Folder. """
        ...


    async def folder_show(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for a single Folder"""
        ...


    async def folder_update(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        folder_update_request: Annotated[Optional[FolderUpdateRequest], Field(description="Request Body for Folders")],
    ) -> ActivityList:
        """Update Folder, move Folder to another Folder, and/or restore a trashed Folder. """
        ...
