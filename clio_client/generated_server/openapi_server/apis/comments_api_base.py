# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.comment_create_request import CommentCreateRequest
from openapi_server.models.comment_list import CommentList
from openapi_server.models.comment_show import CommentShow
from openapi_server.models.comment_update_request import CommentUpdateRequest
from openapi_server.models.error import Error


class BaseCommentsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCommentsApi.subclasses = BaseCommentsApi.subclasses + (cls,)
    async def comment_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        comment_create_request: Annotated[Optional[CommentCreateRequest], Field(description="Request Body for Comments")],
    ) -> CommentShow:
        """Outlines the parameters and data fields used when creating a new Comment"""
        ...


    async def comment_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Comment.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Comment"""
        ...


    async def comment_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Comment records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        item_id: Annotated[Optional[StrictInt], Field(description="The ID of the Document or Folder this Comment belongs to")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Comment records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Comment records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> CommentList:
        """Outlines the parameters, optional and required, used when requesting the data for all Comments"""
        ...


    async def comment_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Comment.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> CommentShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Comment"""
        ...


    async def comment_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Comment.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        comment_update_request: Annotated[Optional[CommentUpdateRequest], Field(description="Request Body for Comments")],
    ) -> CommentShow:
        """Outlines the parameters and data fields used when updating a single Comment"""
        ...
