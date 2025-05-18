# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList


class BaseCriminalControlledRatesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCriminalControlledRatesApi.subclasses = BaseCriminalControlledRatesApi.subclasses + (cls,)
    async def lauk_criminal_controlled_rate_index(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        activityquery: Annotated[Optional[StrictStr], Field(description="Filter by activity.")],
        category_of_lawquery: Annotated[Optional[StrictStr], Field(description="Filter by category of law.")],
        counselquery: Annotated[Optional[StrictStr], Field(description="Filter by counsel.")],
        courtquery: Annotated[Optional[StrictStr], Field(description="Filter by court.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        keyquery: Annotated[Optional[StrictStr], Field(description="Filter by key.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        rate_typequery: Annotated[Optional[StrictStr], Field(description="Filter by rate type.")],
        regionquery: Annotated[Optional[StrictStr], Field(description="Filter by region.")],
        solicitor_typequery: Annotated[Optional[StrictStr], Field(description="Filter by solicitor type.")],
        standard_fee_categoryquery: Annotated[Optional[StrictStr], Field(description="Filter by standard fee category.")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all LaukCriminalControlledRates"""
        ...
