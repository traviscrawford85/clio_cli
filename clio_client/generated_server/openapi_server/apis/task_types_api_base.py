# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.task_type_create_request import TaskTypeCreateRequest
from openapi_server.models.task_type_list import TaskTypeList
from openapi_server.models.task_type_show import TaskTypeShow
from openapi_server.models.task_type_update_request import TaskTypeUpdateRequest


class BaseTaskTypesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTaskTypesApi.subclasses = BaseTaskTypesApi.subclasses + (cls,)
    async def task_type_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        task_type_create_request: Annotated[Optional[TaskTypeCreateRequest], Field(description="Request Body for Task Types")],
    ) -> TaskTypeShow:
        """Outlines the parameters and data fields used when creating a new TaskType"""
        ...


    async def task_type_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter TaskType records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        enabled: Annotated[Optional[StrictBool], Field(description="Filter TaskType records to those that are enabled or disabled.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter TaskType records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of TaskType records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        name: Annotated[Optional[StrictStr], Field(description="Filter TaskType records to those with the given name.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the TaskType records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching a given string.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter TaskType records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> TaskTypeList:
        """Outlines the parameters, optional and required, used when requesting the data for all TaskTypes"""
        ...


    async def task_type_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the TaskType.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> TaskTypeShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single TaskType"""
        ...


    async def task_type_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the TaskType.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        task_type_update_request: Annotated[Optional[TaskTypeUpdateRequest], Field(description="Request Body for Task Types")],
    ) -> TaskTypeShow:
        """Outlines the parameters and data fields used when updating a single TaskType"""
        ...
