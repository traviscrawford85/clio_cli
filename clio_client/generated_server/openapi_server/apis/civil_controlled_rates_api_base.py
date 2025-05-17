# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.lauk_civil_controlled_rate_list import LaukCivilControlledRateList


class BaseCivilControlledRatesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCivilControlledRatesApi.subclasses = BaseCivilControlledRatesApi.subclasses + (cls,)
    async def lauk_civil_controlled_rate_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        activity: Annotated[Optional[StrictStr], Field(description="Filter by activity.")],
        category_of_law: Annotated[Optional[StrictStr], Field(description="Filter by category of law.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        key: Annotated[Optional[StrictStr], Field(description="Filter by key.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of LaukCivilControlledRate records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_type_1: Annotated[Optional[StrictInt], Field(description="Filter by matter type 1.")],
        matter_type_2: Annotated[Optional[StrictInt], Field(description="Filter by matter type 2.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        rate_type: Annotated[Optional[StrictStr], Field(description="Filter by rate type.")],
        region: Annotated[Optional[StrictStr], Field(description="Filter by region.")],
    ) -> LaukCivilControlledRateList:
        """Outlines the parameters, optional and required, used when requesting the data for all LaukCivilControlledRates"""
        ...
