# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.task_create_request import TaskCreateRequest
from openapi_server.models.task_list import TaskList
from openapi_server.models.task_show import TaskShow
from openapi_server.models.task_update_request import TaskUpdateRequest


class BaseTasksApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTasksApi.subclasses = BaseTasksApi.subclasses + (cls,)
    async def task_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        task_create_request: Annotated[Optional[TaskCreateRequest], Field(description="Request Body for Tasks")],
    ) -> TaskShow:
        """Outlines the parameters and data fields used when creating a new Task"""
        ...


    async def task_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Task.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Task"""
        ...


    async def task_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        assignee_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User or Contact. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")],
        assignee_type: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with a specific assignee. Must be passed if filtering by assignee.")],
        assigner_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")],
        cascading_source_id: Annotated[Optional[StrictInt], Field(description="Filter Task records to those with a parent task that has the specified ID.")],
        client_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")],
        complete: Annotated[Optional[StrictBool], Field(description="Filter Task records to those which are complete or not.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Task records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        due_at_from: Annotated[Optional[date], Field(description="Start of date range when querying by due_at in a range. (Expects an ISO-8601 date).")],
        due_at_present: Annotated[Optional[StrictBool], Field(description="Filter Task records to those that have a due date specified, or not.")],
        due_at_to: Annotated[Optional[date], Field(description="End of date range when querying by due_at in a range. (Expects an ISO-8601 date).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Task records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Task records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Task records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        permission: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given permission. Returns all tasks by default.")],
        priority: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given priority.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` or `description` matching a given string.")],
        responsible_attorney_id: Annotated[Optional[StrictInt], Field(description="Filter Task records to those that have an associated matter with a responsible attorney ID.")],
        status: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given status. Users without advanced tasks enabled may only specify 'complete' or 'pending'.")],
        statuses: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given statuses. Users without advanced tasks enabled may only specify 'complete' or 'pending'.")],
        statute_of_limitations: Annotated[Optional[StrictBool], Field(description="Filter Task records to those which are a statute of limitations or not.")],
        task_type_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single TaskType. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")],
        time_entries_present: Annotated[Optional[StrictBool], Field(description="Filter Task records to those that have associated time entries, or not.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Task records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> TaskList:
        """Outlines the parameters, optional and required, used when requesting the data for all Tasks"""
        ...


    async def task_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Task.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> TaskShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Task"""
        ...


    async def task_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Task.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        task_update_request: Annotated[Optional[TaskUpdateRequest], Field(description="Request Body for Tasks")],
    ) -> TaskShow:
        """Outlines the parameters and data fields used when updating a single Task"""
        ...
