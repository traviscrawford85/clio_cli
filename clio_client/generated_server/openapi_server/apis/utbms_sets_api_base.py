# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.utbms_set_list import UtbmsSetList


class BaseUtbmsSetsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUtbmsSetsApi.subclasses = BaseUtbmsSetsApi.subclasses + (cls,)
    async def utbms_set_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter UtbmsSet records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter UtbmsSet records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of UtbmsSet records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the UtbmsSet records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter UtbmsSet records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> UtbmsSetList:
        """Outlines the parameters, optional and required, used when requesting the data for all UtbmsSets"""
        ...
