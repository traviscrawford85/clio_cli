import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.medical_records_requestupdate_files_body_data_medical_bills_item_payers_item import (
        MedicalRecordsRequestupdateFilesBodyDataMedicalBillsItemPayersItem,
    )


T = TypeVar("T", bound="MedicalRecordsRequestupdateFilesBodyDataMedicalBillsItem")


@_attrs_define
class MedicalRecordsRequestupdateFilesBodyDataMedicalBillsItem:
    """
    Attributes:
        adjustment (Union[Unset, float]): Adjustment for Medical Bill.
        amount (Union[Unset, float]): Amount for Medical Bill.
        balance (Union[Unset, float]): Balance for Medical Bill.
        bill_date (Union[Unset, datetime.date]): Bill date for Medical Bill. (Expects an ISO-8601 date).
        bill_received_date (Union[Unset, datetime.date]): Bill received date for Medical Bill. (Expects an ISO-8601
            date).
        document_id (Union[Unset, int]): The unique identifier for a single Damage associated with the
            MedicalRecordsRequest. The keyword `null` is not valid for this field.
        name (Union[Unset, str]): Name for Medical Bill.
        mark_balance_as_lien (Union[Unset, bool]): Setting the balance of the Medical Bill as a lien.
        payers (Union[Unset, list['MedicalRecordsRequestupdateFilesBodyDataMedicalBillsItemPayersItem']]):
    """

    adjustment: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    balance: Union[Unset, float] = UNSET
    bill_date: Union[Unset, datetime.date] = UNSET
    bill_received_date: Union[Unset, datetime.date] = UNSET
    document_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    mark_balance_as_lien: Union[Unset, bool] = UNSET
    payers: Union[Unset, list["MedicalRecordsRequestupdateFilesBodyDataMedicalBillsItemPayersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adjustment = self.adjustment

        amount = self.amount

        balance = self.balance

        bill_date: Union[Unset, str] = UNSET
        if not isinstance(self.bill_date, Unset):
            bill_date = self.bill_date.isoformat()

        bill_received_date: Union[Unset, str] = UNSET
        if not isinstance(self.bill_received_date, Unset):
            bill_received_date = self.bill_received_date.isoformat()

        document_id = self.document_id

        name = self.name

        mark_balance_as_lien = self.mark_balance_as_lien

        payers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.payers, Unset):
            payers = []
            for payers_item_data in self.payers:
                payers_item = payers_item_data.to_dict()
                payers.append(payers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adjustment is not UNSET:
            field_dict["adjustment"] = adjustment
        if amount is not UNSET:
            field_dict["amount"] = amount
        if balance is not UNSET:
            field_dict["balance"] = balance
        if bill_date is not UNSET:
            field_dict["bill_date"] = bill_date
        if bill_received_date is not UNSET:
            field_dict["bill_received_date"] = bill_received_date
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if name is not UNSET:
            field_dict["name"] = name
        if mark_balance_as_lien is not UNSET:
            field_dict["mark_balance_as_lien"] = mark_balance_as_lien
        if payers is not UNSET:
            field_dict["payers"] = payers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medical_records_requestupdate_files_body_data_medical_bills_item_payers_item import (
            MedicalRecordsRequestupdateFilesBodyDataMedicalBillsItemPayersItem,
        )

        d = dict(src_dict)
        adjustment = d.pop("adjustment", UNSET)

        amount = d.pop("amount", UNSET)

        balance = d.pop("balance", UNSET)

        _bill_date = d.pop("bill_date", UNSET)
        bill_date: Union[Unset, datetime.date]
        if isinstance(_bill_date, Unset):
            bill_date = UNSET
        else:
            bill_date = isoparse(_bill_date).date()

        _bill_received_date = d.pop("bill_received_date", UNSET)
        bill_received_date: Union[Unset, datetime.date]
        if isinstance(_bill_received_date, Unset):
            bill_received_date = UNSET
        else:
            bill_received_date = isoparse(_bill_received_date).date()

        document_id = d.pop("document_id", UNSET)

        name = d.pop("name", UNSET)

        mark_balance_as_lien = d.pop("mark_balance_as_lien", UNSET)

        payers = []
        _payers = d.pop("payers", UNSET)
        for payers_item_data in _payers or []:
            payers_item = MedicalRecordsRequestupdateFilesBodyDataMedicalBillsItemPayersItem.from_dict(payers_item_data)

            payers.append(payers_item)

        medical_records_requestupdate_files_body_data_medical_bills_item = cls(
            adjustment=adjustment,
            amount=amount,
            balance=balance,
            bill_date=bill_date,
            bill_received_date=bill_received_date,
            document_id=document_id,
            name=name,
            mark_balance_as_lien=mark_balance_as_lien,
            payers=payers,
        )

        medical_records_requestupdate_files_body_data_medical_bills_item.additional_properties = d
        return medical_records_requestupdate_files_body_data_medical_bills_item

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
