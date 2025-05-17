# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.text_snippet_create_request import TextSnippetCreateRequest
from openapi_server.models.text_snippet_list import TextSnippetList
from openapi_server.models.text_snippet_show import TextSnippetShow
from openapi_server.models.text_snippet_update_request import TextSnippetUpdateRequest


class BaseTextSnippetsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTextSnippetsApi.subclasses = BaseTextSnippetsApi.subclasses + (cls,)
    async def text_snippet_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        text_snippet_create_request: Annotated[Optional[TextSnippetCreateRequest], Field(description="Request Body for Text Snippets")],
    ) -> TextSnippetShow:
        """Outlines the parameters and data fields used when creating a new TextSnippet"""
        ...


    async def text_snippet_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the TextSnippet.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single TextSnippet"""
        ...


    async def text_snippet_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter TextSnippet records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter TextSnippet records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of TextSnippet records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the TextSnippet records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `snippet` or `phrase` matching a given string.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter TextSnippet records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> TextSnippetList:
        """Outlines the parameters, optional and required, used when requesting the data for all TextSnippets"""
        ...


    async def text_snippet_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the TextSnippet.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> TextSnippetShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single TextSnippet"""
        ...


    async def text_snippet_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the TextSnippet.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        text_snippet_update_request: Annotated[Optional[TextSnippetUpdateRequest], Field(description="Request Body for Text Snippets")],
    ) -> TextSnippetShow:
        """Outlines the parameters and data fields used when updating a single TextSnippet"""
        ...
