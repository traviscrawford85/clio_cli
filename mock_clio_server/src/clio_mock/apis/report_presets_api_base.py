# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.report_preset_create_request import ReportPresetCreateRequest
from clio_mock.models.report_preset_update_request import ReportPresetUpdateRequest


class BaseReportPresetsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseReportPresetsApi.subclasses = BaseReportPresetsApi.subclasses + (cls,)
    async def report_preset_create(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        report_preset_create_request: Annotated[Optional[ReportPresetCreateRequest], Field(description="Request Body for Report Presets")],
    ) -> ActivityShow:
        """Outlines the parameters and data fields used when creating a new ReportPreset"""
        ...


    async def report_preset_destroy(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single ReportPreset"""
        ...


    async def report_preset_generate_report(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
    ) -> ActivityShow:
        """Generate a new report for a given preset"""
        ...


    async def report_preset_index(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        categoryquery: Annotated[Optional[StrictStr], Field(description="Filters Report data by category.")],
        created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        has_schedulequery: Annotated[Optional[StrictBool], Field(description="Filters ReportPreset records to those that have or do not have a Report Schedule.")],
        idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")],
        output_formatquery: Annotated[Optional[StrictStr], Field(description="Filters Report data by format.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")],
        schedule_frequencyquery: Annotated[Optional[StrictStr], Field(description="Filters ReportPreset records to those that have a Report Schedule of the specified frequency.")],
        updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all ReportPresets"""
        ...


    async def report_preset_show(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for a single ReportPreset"""
        ...


    async def report_preset_update(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        report_preset_update_request: Annotated[Optional[ReportPresetUpdateRequest], Field(description="Request Body for Report Presets")],
    ) -> ActivityList:
        """Outlines the parameters and data fields used when updating a single ReportPreset"""
        ...
