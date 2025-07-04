import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.medical_records_request_base_bills_status import MedicalRecordsRequestBaseBillsStatus
from ..models.medical_records_request_base_records_status import MedicalRecordsRequestBaseRecordsStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="MedicalRecordsRequestBase")


@_attrs_define
class MedicalRecordsRequestBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *MedicalRecordsRequest*
        etag (Union[Unset, str]): ETag for the *MedicalRecordsRequest*
        bills_follow_up_date (Union[Unset, datetime.datetime]): Follow up date for Medical Bills (as a ISO-8601 date)
        bills_request_date (Union[Unset, datetime.datetime]): Date for when the Medical Bills were requested (as a
            ISO-8601 date)
        bills_status (Union[Unset, MedicalRecordsRequestBaseBillsStatus]): Medical Bills status
        description (Union[Unset, str]): Description of the Medical Records Detail
        in_treatment (Union[Unset, bool]): Treatment status for Medical Records Detail
        records_follow_up_date (Union[Unset, datetime.datetime]): Follow up date for Medical Records (as a ISO-8601
            date)
        records_request_date (Union[Unset, datetime.datetime]): Date for when the Medical Records were requested (as a
            ISO-8601 date)
        records_status (Union[Unset, MedicalRecordsRequestBaseRecordsStatus]): Medical Records status
        treatment_end_date (Union[Unset, datetime.datetime]): Treatment end date for Medical Records Detail (as a
            ISO-8601 date)
        treatment_start_date (Union[Unset, datetime.datetime]): Treatment start date for Medical Records Detail (as a
            ISO-8601 date)
        created_at (Union[Unset, datetime.datetime]): The time the *MedicalRecordsRequest* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *MedicalRecordsRequest* was last updated (as a
            ISO-8601 timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    bills_follow_up_date: Union[Unset, datetime.datetime] = UNSET
    bills_request_date: Union[Unset, datetime.datetime] = UNSET
    bills_status: Union[Unset, MedicalRecordsRequestBaseBillsStatus] = UNSET
    description: Union[Unset, str] = UNSET
    in_treatment: Union[Unset, bool] = UNSET
    records_follow_up_date: Union[Unset, datetime.datetime] = UNSET
    records_request_date: Union[Unset, datetime.datetime] = UNSET
    records_status: Union[Unset, MedicalRecordsRequestBaseRecordsStatus] = UNSET
    treatment_end_date: Union[Unset, datetime.datetime] = UNSET
    treatment_start_date: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        bills_follow_up_date: Union[Unset, str] = UNSET
        if not isinstance(self.bills_follow_up_date, Unset):
            bills_follow_up_date = self.bills_follow_up_date.isoformat()

        bills_request_date: Union[Unset, str] = UNSET
        if not isinstance(self.bills_request_date, Unset):
            bills_request_date = self.bills_request_date.isoformat()

        bills_status: Union[Unset, str] = UNSET
        if not isinstance(self.bills_status, Unset):
            bills_status = self.bills_status.value

        description = self.description

        in_treatment = self.in_treatment

        records_follow_up_date: Union[Unset, str] = UNSET
        if not isinstance(self.records_follow_up_date, Unset):
            records_follow_up_date = self.records_follow_up_date.isoformat()

        records_request_date: Union[Unset, str] = UNSET
        if not isinstance(self.records_request_date, Unset):
            records_request_date = self.records_request_date.isoformat()

        records_status: Union[Unset, str] = UNSET
        if not isinstance(self.records_status, Unset):
            records_status = self.records_status.value

        treatment_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.treatment_end_date, Unset):
            treatment_end_date = self.treatment_end_date.isoformat()

        treatment_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.treatment_start_date, Unset):
            treatment_start_date = self.treatment_start_date.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if bills_follow_up_date is not UNSET:
            field_dict["bills_follow_up_date"] = bills_follow_up_date
        if bills_request_date is not UNSET:
            field_dict["bills_request_date"] = bills_request_date
        if bills_status is not UNSET:
            field_dict["bills_status"] = bills_status
        if description is not UNSET:
            field_dict["description"] = description
        if in_treatment is not UNSET:
            field_dict["in_treatment"] = in_treatment
        if records_follow_up_date is not UNSET:
            field_dict["records_follow_up_date"] = records_follow_up_date
        if records_request_date is not UNSET:
            field_dict["records_request_date"] = records_request_date
        if records_status is not UNSET:
            field_dict["records_status"] = records_status
        if treatment_end_date is not UNSET:
            field_dict["treatment_end_date"] = treatment_end_date
        if treatment_start_date is not UNSET:
            field_dict["treatment_start_date"] = treatment_start_date
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _bills_follow_up_date = d.pop("bills_follow_up_date", UNSET)
        bills_follow_up_date: Union[Unset, datetime.datetime]
        if isinstance(_bills_follow_up_date, Unset):
            bills_follow_up_date = UNSET
        else:
            bills_follow_up_date = isoparse(_bills_follow_up_date)

        _bills_request_date = d.pop("bills_request_date", UNSET)
        bills_request_date: Union[Unset, datetime.datetime]
        if isinstance(_bills_request_date, Unset):
            bills_request_date = UNSET
        else:
            bills_request_date = isoparse(_bills_request_date)

        _bills_status = d.pop("bills_status", UNSET)
        bills_status: Union[Unset, MedicalRecordsRequestBaseBillsStatus]
        if isinstance(_bills_status, Unset):
            bills_status = UNSET
        else:
            bills_status = MedicalRecordsRequestBaseBillsStatus(_bills_status)

        description = d.pop("description", UNSET)

        in_treatment = d.pop("in_treatment", UNSET)

        _records_follow_up_date = d.pop("records_follow_up_date", UNSET)
        records_follow_up_date: Union[Unset, datetime.datetime]
        if isinstance(_records_follow_up_date, Unset):
            records_follow_up_date = UNSET
        else:
            records_follow_up_date = isoparse(_records_follow_up_date)

        _records_request_date = d.pop("records_request_date", UNSET)
        records_request_date: Union[Unset, datetime.datetime]
        if isinstance(_records_request_date, Unset):
            records_request_date = UNSET
        else:
            records_request_date = isoparse(_records_request_date)

        _records_status = d.pop("records_status", UNSET)
        records_status: Union[Unset, MedicalRecordsRequestBaseRecordsStatus]
        if isinstance(_records_status, Unset):
            records_status = UNSET
        else:
            records_status = MedicalRecordsRequestBaseRecordsStatus(_records_status)

        _treatment_end_date = d.pop("treatment_end_date", UNSET)
        treatment_end_date: Union[Unset, datetime.datetime]
        if isinstance(_treatment_end_date, Unset):
            treatment_end_date = UNSET
        else:
            treatment_end_date = isoparse(_treatment_end_date)

        _treatment_start_date = d.pop("treatment_start_date", UNSET)
        treatment_start_date: Union[Unset, datetime.datetime]
        if isinstance(_treatment_start_date, Unset):
            treatment_start_date = UNSET
        else:
            treatment_start_date = isoparse(_treatment_start_date)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        medical_records_request_base = cls(
            id=id,
            etag=etag,
            bills_follow_up_date=bills_follow_up_date,
            bills_request_date=bills_request_date,
            bills_status=bills_status,
            description=description,
            in_treatment=in_treatment,
            records_follow_up_date=records_follow_up_date,
            records_request_date=records_request_date,
            records_status=records_status,
            treatment_end_date=treatment_end_date,
            treatment_start_date=treatment_start_date,
            created_at=created_at,
            updated_at=updated_at,
        )

        medical_records_request_base.additional_properties = d
        return medical_records_request_base

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
