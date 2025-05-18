# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList


class BaseCivilCertificatedRatesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCivilCertificatedRatesApi.subclasses = BaseCivilCertificatedRatesApi.subclasses + (cls,)
    async def lauk_civil_certificated_rate_index(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        activityquery: Annotated[Optional[StrictStr], Field(description="Filter by activity.")],
        activity_sub_categoryquery: Annotated[Optional[StrictStr], Field(description="Filter by activity sub-category.")],
        attended_several_hearings_for_multiple_clientsquery: Annotated[Optional[StrictBool], Field(description="Filter by whether multiple hearings were attended for multiple clients.")],
        category_of_lawquery: Annotated[Optional[StrictStr], Field(description="Filter by category of law.")],
        change_of_solicitorquery: Annotated[Optional[StrictBool], Field(description="Filter by change of solicitor status.")],
        courtquery: Annotated[Optional[StrictStr], Field(description="Filter by court.")],
        eligible_for_sqmquery: Annotated[Optional[StrictBool], Field(description="Filter by SQM eligibility.")],
        fee_schemequery: Annotated[Optional[StrictStr], Field(description="Fee scheme")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        first_conducting_solicitorquery: Annotated[Optional[StrictBool], Field(description="Filter by first conducting solicitor status.")],
        keyquery: Annotated[Optional[StrictStr], Field(description="Filter by key.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        number_of_clientsquery: Annotated[Optional[StrictStr], Field(description="Filter by number of clients.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        partyquery: Annotated[Optional[StrictStr], Field(description="Filter by party.")],
        post_transfer_clients_representedquery: Annotated[Optional[StrictStr], Field(description="Filter by post-transfer clients represented.")],
        rate_typequery: Annotated[Optional[StrictStr], Field(description="Filter by rate type.")],
        regionquery: Annotated[Optional[StrictStr], Field(description="Filter by region.")],
        session_typequery: Annotated[Optional[StrictStr], Field(description="Filter by session type.")],
        user_typequery: Annotated[Optional[StrictStr], Field(description="Filter by user type.")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all LaukCivilCertificatedRates"""
        ...
