# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.report_preset_create_request import ReportPresetCreateRequest
from openapi_server.models.report_preset_list import ReportPresetList
from openapi_server.models.report_preset_show import ReportPresetShow
from openapi_server.models.report_preset_update_request import ReportPresetUpdateRequest
from openapi_server.models.report_show import ReportShow


class BaseReportPresetsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseReportPresetsApi.subclasses = BaseReportPresetsApi.subclasses + (cls,)
    async def report_preset_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        report_preset_create_request: Annotated[Optional[ReportPresetCreateRequest], Field(description="Request Body for Report Presets")],
    ) -> ReportPresetShow:
        """Outlines the parameters and data fields used when creating a new ReportPreset"""
        ...


    async def report_preset_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ReportPreset.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single ReportPreset"""
        ...


    async def report_preset_generate_report(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ReportPreset.")],
    ) -> ReportShow:
        """Generate a new report for a given preset"""
        ...


    async def report_preset_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        category: Annotated[Optional[StrictStr], Field(description="Filters ReportPreset data by category.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter ReportPreset records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        has_schedule: Annotated[Optional[StrictBool], Field(description="Filters ReportPreset records to those that have or do not have a Report Schedule.")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter ReportPreset records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ReportPreset records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the ReportPreset records by the given field. Default: `id(asc)`.")],
        output_format: Annotated[Optional[StrictStr], Field(description="Filters ReportPreset data by format.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for ReportPreset name.")],
        schedule_frequency: Annotated[Optional[StrictStr], Field(description="Filters ReportPreset records to those that have a Report Schedule of the specified frequency.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter ReportPreset records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ReportPresetList:
        """Outlines the parameters, optional and required, used when requesting the data for all ReportPresets"""
        ...


    async def report_preset_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ReportPreset.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ReportPresetShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single ReportPreset"""
        ...


    async def report_preset_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ReportPreset.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        report_preset_update_request: Annotated[Optional[ReportPresetUpdateRequest], Field(description="Request Body for Report Presets")],
    ) -> ReportPresetShow:
        """Outlines the parameters and data fields used when updating a single ReportPreset"""
        ...
