# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.user_list import UserList
from openapi_server.models.user_show import UserShow


class BaseUsersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUsersApi.subclasses = BaseUsersApi.subclasses + (cls,)
    async def user_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter User records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        enabled: Annotated[Optional[StrictBool], Field(description="Filter User records to those that are enabled or disabled.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter User records to those having the specified unique identifiers.")],
        include_co_counsel: Annotated[Optional[StrictBool], Field(description="Filter User to include co-counsel users")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of User records to be returned. Limit can range between 1 and 2000. Default: `2000`.")],
        name: Annotated[Optional[StrictStr], Field(description="Filter User records to those with the given name.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the User records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        pending_setup: Annotated[Optional[StrictBool], Field(description="Filter User records based on whether or not they are still being setup.")],
        role: Annotated[Optional[StrictStr], Field(description="Filter User records to those with a specific role.")],
        subscription_type: Annotated[Optional[StrictStr], Field(description="Filter User records to those with a specific subscription type.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter User records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> UserList:
        """Outlines the parameters, optional and required, used when requesting the data for all Users"""
        ...


    async def user_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the User.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> UserShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single User"""
        ...


    async def user_who_am_i(
        self,
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> UserShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single User"""
        ...
