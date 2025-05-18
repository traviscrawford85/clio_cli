# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.task_create_request import TaskCreateRequest
from clio_mock.models.task_update_request import TaskUpdateRequest


class BaseTasksApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTasksApi.subclasses = BaseTasksApi.subclasses + (cls,)
    async def task_create(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        task_create_request: Annotated[Optional[TaskCreateRequest], Field(description="Request Body for Tasks")],
    ) -> ActivityShow:
        """Outlines the parameters and data fields used when creating a new Task"""
        ...


    async def task_destroy(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Task"""
        ...


    async def task_index(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        assignee_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User or Contact. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")],
        assignee_typequery: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with a specific assignee. Must be passed if filtering by assignee.")],
        assigner_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")],
        cascading_source_idquery: Annotated[Optional[StrictInt], Field(description="Filter Task records to those with a parent task that has the specified ID.")],
        client_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.")],
        completequery: Annotated[Optional[StrictBool], Field(description="Filter Task records to those which are complete or not.")],
        created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        due_at_fromquery: Annotated[Optional[date], Field(description="Start of date range when querying by due_at in a range. (Expects an ISO-8601 date).")],
        due_at_presentquery: Annotated[Optional[StrictBool], Field(description="Filter Task records to those that have a due date specified, or not.")],
        due_at_toquery: Annotated[Optional[date], Field(description="End of date range when querying by due_at in a range. (Expects an ISO-8601 date).")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        permissionquery: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given permission. Returns all tasks by default.")],
        priorityquery: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given priority.")],
        queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")],
        responsible_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")],
        statusquery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those that are draft, billed, unbilled or non-billable.")],
        statusesquery: Annotated[Optional[StrictStr], Field(description="Filter Task records to those with the given statuses. Users without advanced tasks enabled may only specify 'complete' or 'pending'.")],
        statute_of_limitationsquery: Annotated[Optional[StrictBool], Field(description="Filter Task records to those which are a statute of limitations or not.")],
        task_type_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single TaskType. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property.")],
        time_entries_presentquery: Annotated[Optional[StrictBool], Field(description="Filter Task records to those that have associated time entries, or not.")],
        updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all Tasks"""
        ...


    async def task_show(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for a single Task"""
        ...


    async def task_update(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        task_update_request: Annotated[Optional[TaskUpdateRequest], Field(description="Request Body for Tasks")],
    ) -> ActivityList:
        """Outlines the parameters and data fields used when updating a single Task"""
        ...
