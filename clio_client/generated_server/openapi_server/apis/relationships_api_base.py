# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.relationship_create_request import RelationshipCreateRequest
from openapi_server.models.relationship_list import RelationshipList
from openapi_server.models.relationship_show import RelationshipShow


class BaseRelationshipsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseRelationshipsApi.subclasses = BaseRelationshipsApi.subclasses + (cls,)
    async def relationship_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        relationship_create_request: Annotated[Optional[RelationshipCreateRequest], Field(description="Request Body for Relationships")],
    ) -> RelationshipShow:
        """Outlines the parameters and data fields used when creating a new Relationship"""
        ...


    async def relationship_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Relationship.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Relationship"""
        ...


    async def relationship_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Relationship records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Relationship records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Relationship records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Relationship records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the Relationship records with the matching property.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Relationship records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> RelationshipList:
        """Outlines the parameters, optional and required, used when requesting the data for all Relationships"""
        ...


    async def relationship_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Relationship.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> RelationshipShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Relationship"""
        ...


    async def relationship_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Relationship.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        relationship_create_request: Annotated[Optional[RelationshipCreateRequest], Field(description="Request Body for Relationships")],
    ) -> RelationshipShow:
        """Outlines the parameters and data fields used when updating a single Relationship"""
        ...
