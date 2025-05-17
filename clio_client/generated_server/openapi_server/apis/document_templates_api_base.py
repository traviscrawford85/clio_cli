# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.document_template_create_request import DocumentTemplateCreateRequest
from openapi_server.models.document_template_list import DocumentTemplateList
from openapi_server.models.document_template_show import DocumentTemplateShow
from openapi_server.models.document_template_update_request import DocumentTemplateUpdateRequest
from openapi_server.models.error import Error


class BaseDocumentTemplatesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDocumentTemplatesApi.subclasses = BaseDocumentTemplatesApi.subclasses + (cls,)
    async def document_template_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        document_template_create_request: Annotated[Optional[DocumentTemplateCreateRequest], Field(description="Request Body for Document Templates")],
    ) -> DocumentTemplateShow:
        """Outlines the parameters and data fields used when creating a new DocumentTemplate"""
        ...


    async def document_template_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the DocumentTemplate.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single DocumentTemplate"""
        ...


    async def document_template_download(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the DocumentTemplate.")],
    ) -> None:
        """Get the contents of the DocumentTemplate"""
        ...


    async def document_template_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter DocumentTemplate records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter DocumentTemplate records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of DocumentTemplate records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the DocumentTemplate records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter DocumentTemplate records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> DocumentTemplateList:
        """Outlines the parameters, optional and required, used when requesting the data for all DocumentTemplates"""
        ...


    async def document_template_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the DocumentTemplate.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> DocumentTemplateShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single DocumentTemplate"""
        ...


    async def document_template_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the DocumentTemplate.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        document_template_update_request: Annotated[Optional[DocumentTemplateUpdateRequest], Field(description="Request Body for Document Templates")],
    ) -> DocumentTemplateShow:
        """Outlines the parameters and data fields used when updating a single DocumentTemplate"""
        ...
