# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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


class BaseDocumentsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDocumentsApi.subclasses = BaseDocumentsApi.subclasses + (cls,)
    async def document_copy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Document.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        document_copy_request: Annotated[Optional[DocumentCopyRequest], Field(description="Request Body for Documents")],
    ) -> DocumentShow:
        """Copies the latest document version of a Document into a new Document. The parameters &#x60;filename&#x60; and &#x60;name&#x60; will be copied from the source Document if none are provided. """
        ...


    async def document_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        document_create_request: Annotated[Optional[DocumentCreateRequest], Field(description="Request Body for Documents")],
    ) -> DocumentShow:
        """Create a Document, or Create Document Version to an existing Document. """
        ...


    async def document_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Document.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Deleting a Document using this method will move it to the trash instead of permanently deleting it. Trashed Documents are permanently deleted after 30 days. The following errors may be returned:  - &#x60;409 Conflict&#x60;: The Document (or one of its ancestor folders) is currently being modified by another request, and cannot be trashed. """
        ...


    async def document_download(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Document.")],
        document_version_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a DocumentVersion to be downloaded. Defaults to the latest.")],
    ) -> None:
        """Download the Document"""
        ...


    async def document_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Document records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        document_category_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")],
        external_property_name: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")],
        external_property_value: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Document records to those having the specified unique identifiers.")],
        include_deleted: Annotated[Optional[StrictBool], Field(description="Allow trashed Document record to be included.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Document records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Document records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        parent_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Folder. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching the given string.")],
        scope: Annotated[Optional[StrictStr], Field(description="Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`.")],
        show_uncompleted: Annotated[Optional[StrictBool], Field(description="Allow Document record being uploaded to be included.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Document records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> DocumentList:
        """Outlines the parameters, optional and required, used when requesting the data for all Documents"""
        ...


    async def document_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Document.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> DocumentShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Document"""
        ...


    async def document_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Document.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        document_update_request: Annotated[Optional[DocumentUpdateRequest], Field(description="Request Body for Documents")],
    ) -> DocumentShow:
        """Update Document, move Document to another Folder, and/or restore a trashed Document. """
        ...
