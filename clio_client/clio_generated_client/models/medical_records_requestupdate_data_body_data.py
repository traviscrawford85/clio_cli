import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.medical_records_requestupdate_data_body_data_bills_status import (
    MedicalRecordsRequestupdateDataBodyDataBillsStatus,
)
from ..models.medical_records_requestupdate_data_body_data_records_status import (
    MedicalRecordsRequestupdateDataBodyDataRecordsStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.medical_records_requestupdate_data_body_data_medical_bills_item import (
        MedicalRecordsRequestupdateDataBodyDataMedicalBillsItem,
    )
    from ..models.medical_records_requestupdate_data_body_data_medical_records_item import (
        MedicalRecordsRequestupdateDataBodyDataMedicalRecordsItem,
    )


T = TypeVar("T", bound="MedicalRecordsRequestupdateDataBodyData")


@_attrs_define
class MedicalRecordsRequestupdateDataBodyData:
    """
    Attributes:
        bills_follow_up_date (Union[Unset, datetime.datetime]): Follow up date for Medical Bills. (Expects an ISO-8601
            date).
        bills_request_date (Union[Unset, datetime.datetime]): Requested date for Medical Bills. (Expects an ISO-8601
            date).
        bills_status (Union[Unset, MedicalRecordsRequestupdateDataBodyDataBillsStatus]): Current status for the Medical
            Bills.
        description (Union[Unset, str]): Detailed description of the Medical Records Detail.
        in_treatment (Union[Unset, bool]): True or false value to record if the treatment has been completed.
        medical_bills (Union[Unset, list['MedicalRecordsRequestupdateDataBodyDataMedicalBillsItem']]):
        medical_provider_id (Union[Unset, int]): The unique identifier for a single Medical Provider associated with
            this Medical Records Detail.
        medical_records (Union[Unset, list['MedicalRecordsRequestupdateDataBodyDataMedicalRecordsItem']]):
        records_follow_up_date (Union[Unset, datetime.datetime]): Follow up date for Medical Records. (Expects an
            ISO-8601 date).
        records_request_date (Union[Unset, datetime.datetime]): Requested date for Medical Records. (Expects an ISO-8601
            date).
        records_status (Union[Unset, MedicalRecordsRequestupdateDataBodyDataRecordsStatus]): Current status for the
            Medical Records.
        treatment_end_date (Union[Unset, datetime.datetime]): End date for the treatment. (Expects an ISO-8601 date).
        treatment_start_date (Union[Unset, datetime.datetime]): Start date for the treatment. (Expects an ISO-8601
            date).
    """

    bills_follow_up_date: Union[Unset, datetime.datetime] = UNSET
    bills_request_date: Union[Unset, datetime.datetime] = UNSET
    bills_status: Union[Unset, MedicalRecordsRequestupdateDataBodyDataBillsStatus] = UNSET
    description: Union[Unset, str] = UNSET
    in_treatment: Union[Unset, bool] = UNSET
    medical_bills: Union[Unset, list["MedicalRecordsRequestupdateDataBodyDataMedicalBillsItem"]] = UNSET
    medical_provider_id: Union[Unset, int] = UNSET
    medical_records: Union[Unset, list["MedicalRecordsRequestupdateDataBodyDataMedicalRecordsItem"]] = UNSET
    records_follow_up_date: Union[Unset, datetime.datetime] = UNSET
    records_request_date: Union[Unset, datetime.datetime] = UNSET
    records_status: Union[Unset, MedicalRecordsRequestupdateDataBodyDataRecordsStatus] = UNSET
    treatment_end_date: Union[Unset, datetime.datetime] = UNSET
    treatment_start_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        medical_bills: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.medical_bills, Unset):
            medical_bills = []
            for medical_bills_item_data in self.medical_bills:
                medical_bills_item = medical_bills_item_data.to_dict()
                medical_bills.append(medical_bills_item)

        medical_provider_id = self.medical_provider_id

        medical_records: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.medical_records, Unset):
            medical_records = []
            for medical_records_item_data in self.medical_records:
                medical_records_item = medical_records_item_data.to_dict()
                medical_records.append(medical_records_item)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if medical_bills is not UNSET:
            field_dict["medical_bills"] = medical_bills
        if medical_provider_id is not UNSET:
            field_dict["medical_provider_id"] = medical_provider_id
        if medical_records is not UNSET:
            field_dict["medical_records"] = medical_records
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medical_records_requestupdate_data_body_data_medical_bills_item import (
            MedicalRecordsRequestupdateDataBodyDataMedicalBillsItem,
        )
        from ..models.medical_records_requestupdate_data_body_data_medical_records_item import (
            MedicalRecordsRequestupdateDataBodyDataMedicalRecordsItem,
        )

        d = dict(src_dict)
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
        bills_status: Union[Unset, MedicalRecordsRequestupdateDataBodyDataBillsStatus]
        if isinstance(_bills_status, Unset):
            bills_status = UNSET
        else:
            bills_status = MedicalRecordsRequestupdateDataBodyDataBillsStatus(_bills_status)

        description = d.pop("description", UNSET)

        in_treatment = d.pop("in_treatment", UNSET)

        medical_bills = []
        _medical_bills = d.pop("medical_bills", UNSET)
        for medical_bills_item_data in _medical_bills or []:
            medical_bills_item = MedicalRecordsRequestupdateDataBodyDataMedicalBillsItem.from_dict(
                medical_bills_item_data
            )

            medical_bills.append(medical_bills_item)

        medical_provider_id = d.pop("medical_provider_id", UNSET)

        medical_records = []
        _medical_records = d.pop("medical_records", UNSET)
        for medical_records_item_data in _medical_records or []:
            medical_records_item = MedicalRecordsRequestupdateDataBodyDataMedicalRecordsItem.from_dict(
                medical_records_item_data
            )

            medical_records.append(medical_records_item)

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
        records_status: Union[Unset, MedicalRecordsRequestupdateDataBodyDataRecordsStatus]
        if isinstance(_records_status, Unset):
            records_status = UNSET
        else:
            records_status = MedicalRecordsRequestupdateDataBodyDataRecordsStatus(_records_status)

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

        medical_records_requestupdate_data_body_data = cls(
            bills_follow_up_date=bills_follow_up_date,
            bills_request_date=bills_request_date,
            bills_status=bills_status,
            description=description,
            in_treatment=in_treatment,
            medical_bills=medical_bills,
            medical_provider_id=medical_provider_id,
            medical_records=medical_records,
            records_follow_up_date=records_follow_up_date,
            records_request_date=records_request_date,
            records_status=records_status,
            treatment_end_date=treatment_end_date,
            treatment_start_date=treatment_start_date,
        )

        medical_records_requestupdate_data_body_data.additional_properties = d
        return medical_records_requestupdate_data_body_data

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
