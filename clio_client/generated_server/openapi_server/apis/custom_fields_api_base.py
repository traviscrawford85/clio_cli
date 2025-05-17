# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.custom_field_create_request import CustomFieldCreateRequest
from openapi_server.models.custom_field_list import CustomFieldList
from openapi_server.models.custom_field_show import CustomFieldShow
from openapi_server.models.custom_field_update_request import CustomFieldUpdateRequest
from openapi_server.models.error import Error


class BaseCustomFieldsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCustomFieldsApi.subclasses = BaseCustomFieldsApi.subclasses + (cls,)
    async def custom_field_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        custom_field_create_request: Annotated[Optional[CustomFieldCreateRequest], Field(description="Request Body for Custom Fields")],
    ) -> CustomFieldShow:
        """Outlines the parameters and data fields used when creating a new CustomField"""
        ...


    async def custom_field_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the CustomField.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single CustomField"""
        ...


    async def custom_field_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter CustomField records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        deleted: Annotated[Optional[StrictBool], Field(description="Filter CustomField records to those that have been deleted for future use.")],
        field_type: Annotated[Optional[StrictStr], Field(description="Field type of this custom field")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter CustomField records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of CustomField records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the CustomField records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        parent_type: Annotated[Optional[StrictStr], Field(description="Filter CustomField records to those that have the specified `parent_type`.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching a given string.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter CustomField records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        visible_and_required: Annotated[Optional[StrictBool], Field(description="Filter CustomField records to those that are visible and required.")],
    ) -> CustomFieldList:
        """Outlines the parameters, optional and required, used when requesting the data for all CustomFields"""
        ...


    async def custom_field_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the CustomField.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> CustomFieldShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single CustomField"""
        ...


    async def custom_field_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the CustomField.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        custom_field_update_request: Annotated[Optional[CustomFieldUpdateRequest], Field(description="Request Body for Custom Fields")],
    ) -> CustomFieldShow:
        """Outlines the parameters and data fields used when updating a single CustomField"""
        ...
