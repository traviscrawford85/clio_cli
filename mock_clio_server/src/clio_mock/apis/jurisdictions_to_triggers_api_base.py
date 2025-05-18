# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList


class BaseJurisdictionsToTriggersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseJurisdictionsToTriggersApi.subclasses = BaseJurisdictionsToTriggersApi.subclasses + (cls,)
    async def jurisdictions_to_trigger_index(
        self,
        jurisdiction_idpath: Annotated[StrictInt, Field(description="The unique identifier for the Jurisdiction.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")],
        is_requirements_requiredquery: Annotated[Optional[StrictBool], Field(description="Filter JurisdictionsToTrigger records to those which require addition requirements to be checked (usually specifying trigger time).")],
        is_servedquery: Annotated[Optional[StrictBool], Field(description="Filter JurisdictionsToTrigger records to those which require a service type to be selected.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")],
        updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all JurisdictionsToTriggers"""
        ...


    async def jurisdictions_to_trigger_show(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        jurisdiction_idpath: Annotated[StrictInt, Field(description="The unique identifier for the Jurisdiction.")],
        if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for a single JurisdictionsToTrigger"""
        ...
