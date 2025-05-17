# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.medical_records_request_create_request import MedicalRecordsRequestCreateRequest
from openapi_server.models.medical_records_request_list import MedicalRecordsRequestList
from openapi_server.models.medical_records_request_show import MedicalRecordsRequestShow
from openapi_server.models.medical_records_request_update_request import MedicalRecordsRequestUpdateRequest


class BaseMedicalRecordsDetailsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMedicalRecordsDetailsApi.subclasses = BaseMedicalRecordsDetailsApi.subclasses + (cls,)
    async def medical_records_request_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        medical_records_request_create_request: Annotated[Optional[MedicalRecordsRequestCreateRequest], Field(description="Request Body for Medical Records Details")],
    ) -> MedicalRecordsRequestShow:
        """This endpoint allows a creation of a Medical Records Detail, multiple Medical Records and Medical Bills. Medical Liens can also be created as a property under Medical Bills.  Reference the payload to see how the records are being passed in. """
        ...


    async def medical_records_request_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Medical Records Detail.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """When a Medical Records Detail is destroyed, the child records, such as Medical Records, Medical Bills and Liens will also be destroyed in the same transaction. """
        ...


    async def medical_records_request_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter MedicalRecordsRequest records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter MedicalRecordsRequest records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Medical Records Detail records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        treatment_end_date: Annotated[Optional[datetime], Field(description="Filters Medical Records data by treatment end date.")],
        treatment_start_date: Annotated[Optional[datetime], Field(description="Filters Medical Records data by treatment start date.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter MedicalRecordsRequest records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> MedicalRecordsRequestList:
        """Outlines the parameters, optional and required, used when requesting the data for all Medical Records Details """
        ...


    async def medical_records_request_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Medical Records Detail.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> MedicalRecordsRequestShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Medical Records Details """
        ...


    async def medical_records_request_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Medical Records Detail.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        medical_records_request_update_request: Annotated[Optional[MedicalRecordsRequestUpdateRequest], Field(description="Request Body for Medical Records Details")],
    ) -> MedicalRecordsRequestShow:
        """If there are records being passed into the Medical Records or Medical Bills parameter they will be treated as new records and new Medical Records / Medical Bills will be created. """
        ...
