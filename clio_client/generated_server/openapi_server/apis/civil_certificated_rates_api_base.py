# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.lauk_civil_certificated_rate_list import LaukCivilCertificatedRateList


class BaseCivilCertificatedRatesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCivilCertificatedRatesApi.subclasses = BaseCivilCertificatedRatesApi.subclasses + (cls,)
    async def lauk_civil_certificated_rate_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        activity: Annotated[Optional[StrictStr], Field(description="Filter by activity.")],
        activity_sub_category: Annotated[Optional[StrictStr], Field(description="Filter by activity sub-category.")],
        attended_several_hearings_for_multiple_clients: Annotated[Optional[StrictBool], Field(description="Filter by whether multiple hearings were attended for multiple clients.")],
        category_of_law: Annotated[Optional[StrictStr], Field(description="Filter by category of law.")],
        change_of_solicitor: Annotated[Optional[StrictBool], Field(description="Filter by change of solicitor status.")],
        court: Annotated[Optional[StrictStr], Field(description="Filter by court.")],
        eligible_for_sqm: Annotated[Optional[StrictBool], Field(description="Filter by SQM eligibility.")],
        fee_scheme: Annotated[Optional[StrictStr], Field(description="Fee scheme")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        first_conducting_solicitor: Annotated[Optional[StrictBool], Field(description="Filter by first conducting solicitor status.")],
        key: Annotated[Optional[StrictStr], Field(description="Filter by key.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of LaukCivilCertificatedRate records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        number_of_clients: Annotated[Optional[StrictStr], Field(description="Filter by number of clients.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        party: Annotated[Optional[StrictStr], Field(description="Filter by party.")],
        post_transfer_clients_represented: Annotated[Optional[StrictStr], Field(description="Filter by post-transfer clients represented.")],
        rate_type: Annotated[Optional[StrictStr], Field(description="Filter by rate type.")],
        region: Annotated[Optional[StrictStr], Field(description="Filter by region.")],
        session_type: Annotated[Optional[StrictStr], Field(description="Filter by session type.")],
        user_type: Annotated[Optional[StrictStr], Field(description="Filter by user type.")],
    ) -> LaukCivilCertificatedRateList:
        """Outlines the parameters, optional and required, used when requesting the data for all LaukCivilCertificatedRates"""
        ...
