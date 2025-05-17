# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.group_create_request import GroupCreateRequest
from openapi_server.models.group_list import GroupList
from openapi_server.models.group_show import GroupShow


class BaseGroupsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseGroupsApi.subclasses = BaseGroupsApi.subclasses + (cls,)
    async def group_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        group_create_request: Annotated[Optional[GroupCreateRequest], Field(description="Request Body for Groups")],
    ) -> GroupShow:
        """Outlines the parameters and data fields used when creating a new Group"""
        ...


    async def group_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Group.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Group"""
        ...


    async def group_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        archived: Annotated[Optional[StrictBool], Field(description="Filter archived Group records.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Group records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Group records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Group records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        name: Annotated[Optional[StrictStr], Field(description="Filter Group records to those that match the given name.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Group records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching a given string.")],
        type: Annotated[Optional[StrictStr], Field(description="Filter Group records to those that match the given type.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Group records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        user_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. The keyword `null` is not valid for this field. The list will be filtered to include only the Group records with the matching property.")],
    ) -> GroupList:
        """Outlines the parameters, optional and required, used when requesting the data for all Groups"""
        ...


    async def group_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Group.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> GroupShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Group"""
        ...


    async def group_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Group.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        group_create_request: Annotated[Optional[GroupCreateRequest], Field(description="Request Body for Groups")],
    ) -> GroupShow:
        """Outlines the parameters and data fields used when updating a single Group"""
        ...
