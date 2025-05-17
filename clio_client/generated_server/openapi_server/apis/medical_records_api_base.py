# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.medical_record_show import MedicalRecordShow
from openapi_server.models.medical_record_update_request import MedicalRecordUpdateRequest


class BaseMedicalRecordsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMedicalRecordsApi.subclasses = BaseMedicalRecordsApi.subclasses + (cls,)
    async def medical_record_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the MedicalRecord.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single MedicalRecord"""
        ...


    async def medical_record_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the MedicalRecord.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        medical_record_update_request: Annotated[Optional[MedicalRecordUpdateRequest], Field(description="Request Body for Medical Records")],
    ) -> MedicalRecordShow:
        """Outlines the parameters and data fields used when updating a single MedicalRecord"""
        ...
