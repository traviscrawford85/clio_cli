# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.custom_field_set_create_request import CustomFieldSetCreateRequest
from openapi_server.models.custom_field_set_list import CustomFieldSetList
from openapi_server.models.custom_field_set_show import CustomFieldSetShow
from openapi_server.models.custom_field_set_update_request import CustomFieldSetUpdateRequest
from openapi_server.models.error import Error


class BaseCustomFieldSetsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCustomFieldSetsApi.subclasses = BaseCustomFieldSetsApi.subclasses + (cls,)
    async def custom_field_set_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        custom_field_set_create_request: Annotated[Optional[CustomFieldSetCreateRequest], Field(description="Request Body for Custom Field Sets")],
    ) -> CustomFieldSetShow:
        """Outlines the parameters and data fields used when creating a new CustomFieldSet"""
        ...


    async def custom_field_set_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the CustomFieldSet.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single CustomFieldSet"""
        ...


    async def custom_field_set_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter CustomFieldSet records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        displayed: Annotated[Optional[StrictBool], Field(description="Filter CustomFieldSet records to those that should be displayed by default.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter CustomFieldSet records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of CustomFieldSet records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the CustomFieldSet records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        parent_type: Annotated[Optional[StrictStr], Field(description="Filter CustomFieldSet records to those that have the specified `parent_type`.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching a given string.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter CustomFieldSet records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> CustomFieldSetList:
        """Outlines the parameters, optional and required, used when requesting the data for all CustomFieldSets"""
        ...


    async def custom_field_set_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the CustomFieldSet.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> CustomFieldSetShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single CustomFieldSet"""
        ...


    async def custom_field_set_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the CustomFieldSet.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        custom_field_set_update_request: Annotated[Optional[CustomFieldSetUpdateRequest], Field(description="Request Body for Custom Field Sets")],
    ) -> CustomFieldSetShow:
        """Outlines the parameters and data fields used when updating a single CustomFieldSet"""
        ...
