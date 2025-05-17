# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.task_template_list_copy_request import TaskTemplateListCopyRequest
from openapi_server.models.task_template_list_create_request import TaskTemplateListCreateRequest
from openapi_server.models.task_template_list_list import TaskTemplateListList
from openapi_server.models.task_template_list_show import TaskTemplateListShow
from openapi_server.models.task_template_list_update_request import TaskTemplateListUpdateRequest


class BaseTaskTemplateListsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTaskTemplateListsApi.subclasses = BaseTaskTemplateListsApi.subclasses + (cls,)
    async def task_template_list_copy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the TaskTemplateList.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        task_template_list_copy_request: Annotated[Optional[TaskTemplateListCopyRequest], Field(description="Request Body for Task Template Lists")],
    ) -> TaskTemplateListShow:
        """Creates a copy of the TaskTemplateList identified by the &#x60;id&#x60; path parameter. """
        ...


    async def task_template_list_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        task_template_list_create_request: Annotated[Optional[TaskTemplateListCreateRequest], Field(description="Request Body for Task Template Lists")],
    ) -> TaskTemplateListShow:
        """Outlines the parameters and data fields used when creating a new TaskTemplateList"""
        ...


    async def task_template_list_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the TaskTemplateList.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single TaskTemplateList"""
        ...


    async def task_template_list_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter TaskTemplateList records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        empty: Annotated[Optional[StrictBool], Field(description="Filter TaskTemplateList records to those that either contain at least one task template or contain none.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter TaskTemplateList records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of TaskTemplateList records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the TaskTemplateList records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        practice_area_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single PracticeArea. Use the keyword `null` to match those without a TaskTemplateList. The list will be filtered to include only the TaskTemplateList records with the matching property.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching a given string.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter TaskTemplateList records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> TaskTemplateListList:
        """Outlines the parameters, optional and required, used when requesting the data for all TaskTemplateLists"""
        ...


    async def task_template_list_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the TaskTemplateList.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> TaskTemplateListShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single TaskTemplateList"""
        ...


    async def task_template_list_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the TaskTemplateList.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        task_template_list_update_request: Annotated[Optional[TaskTemplateListUpdateRequest], Field(description="Request Body for Task Template Lists")],
    ) -> TaskTemplateListShow:
        """Outlines the parameters and data fields used when updating a single TaskTemplateList"""
        ...
