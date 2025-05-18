# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_create_request import ActivityCreateRequest
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.activity_update_request import ActivityUpdateRequest


class BaseActivitiesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseActivitiesApi.subclasses = BaseActivitiesApi.subclasses + (cls,)
    async def activity_create(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        activity_create_request: Annotated[Optional[ActivityCreateRequest], Field(description="Request Body for Activities")],
    ) -> ActivityShow:
        """Outlines the parameters and data fields used when creating a new Activity"""
        ...


    async def activity_destroy(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Activity"""
        ...


    async def activity_index(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        activity_description_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single ActivityDescription. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        calendar_entry_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single CalendarEntry. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        communication_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Communication. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        contact_note_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Note. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        end_datequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those whose `date` is on or before the date provided (Expects an ISO-8601 date).")],
        expense_category_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single ExpenseCategory. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        flat_ratequery: Annotated[Optional[StrictBool], Field(description="Filter Activity TimeEntry records to those that have a flat rate, or not.")],
        grant_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Grant. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        matter_note_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Note. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        only_unaccounted_forquery: Annotated[Optional[StrictBool], Field(description="Only unaccounted for activities.")],
        orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")],
        start_datequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those whose `date` is on or after the date provided (Expects an ISO-8601 date).")],
        statusquery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those that are draft, billed, unbilled or non-billable.")],
        task_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Task. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        typequery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those of a specific type.")],
        updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        user_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all Activities"""
        ...


    async def activity_show(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for a single Activity"""
        ...


    async def activity_update(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        activity_update_request: Annotated[Optional[ActivityUpdateRequest], Field(description="Request Body for Activities")],
    ) -> ActivityList:
        """Outlines the parameters and data fields used when updating a single Activity"""
        ...
