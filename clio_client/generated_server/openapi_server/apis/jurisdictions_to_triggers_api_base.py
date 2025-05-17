# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.jurisdictions_to_trigger_list import JurisdictionsToTriggerList
from openapi_server.models.jurisdictions_to_trigger_show import JurisdictionsToTriggerShow


class BaseJurisdictionsToTriggersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseJurisdictionsToTriggersApi.subclasses = BaseJurisdictionsToTriggersApi.subclasses + (cls,)
    async def jurisdictions_to_trigger_index(
        self,
        jurisdiction_id: Annotated[StrictInt, Field(description="The unique identifier for the Jurisdiction.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter JurisdictionsToTrigger records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter JurisdictionsToTrigger records to those having the specified unique identifiers.")],
        is_requirements_required: Annotated[Optional[StrictBool], Field(description="Filter JurisdictionsToTrigger records to those which require addition requirements to be checked (usually specifying trigger time).")],
        is_served: Annotated[Optional[StrictBool], Field(description="Filter JurisdictionsToTrigger records to those which require a service type to be selected.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of JurisdictionsToTrigger records to be returned. Limit can range between 1 and 1000. Default: `1000`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the JurisdictionsToTrigger records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `description` matching a given string.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter JurisdictionsToTrigger records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> JurisdictionsToTriggerList:
        """Outlines the parameters, optional and required, used when requesting the data for all JurisdictionsToTriggers"""
        ...


    async def jurisdictions_to_trigger_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the JurisdictionsToTrigger.")],
        jurisdiction_id: Annotated[StrictInt, Field(description="The unique identifier for the Jurisdiction.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> JurisdictionsToTriggerShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single JurisdictionsToTrigger"""
        ...
