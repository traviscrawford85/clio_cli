# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.damage_create_request import DamageCreateRequest
from openapi_server.models.damage_list import DamageList
from openapi_server.models.damage_show import DamageShow
from openapi_server.models.damage_update_request import DamageUpdateRequest
from openapi_server.models.error import Error


class BaseDamagesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDamagesApi.subclasses = BaseDamagesApi.subclasses + (cls,)
    async def damage_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        damage_create_request: Annotated[Optional[DamageCreateRequest], Field(description="Request Body for Damages")],
    ) -> DamageShow:
        """Outlines the parameters and data fields used when creating a new Damage"""
        ...


    async def damage_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Damage.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Damage"""
        ...


    async def damage_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Damage records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Damage records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Damage records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Damage records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> DamageList:
        """Outlines the parameters, optional and required, used when requesting the data for all Damages"""
        ...


    async def damage_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Damage.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> DamageShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Damage"""
        ...


    async def damage_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Damage.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        damage_update_request: Annotated[Optional[DamageUpdateRequest], Field(description="Request Body for Damages")],
    ) -> DamageShow:
        """Outlines the parameters and data fields used when updating a single Damage"""
        ...
