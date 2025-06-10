import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MedicalBillBase")


@_attrs_define
class MedicalBillBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *MedicalBill*
        adjustment (Union[Unset, float]): Adjustment for Medical Bill
        amount (Union[Unset, float]): Amount for Medical Bill
        bill_date (Union[Unset, datetime.date]): Bill date for Medical Bill (as a ISO-8601 date)
        bill_received_date (Union[Unset, datetime.date]): Bill received date for Medical Bill (as a ISO-8601 date)
        damage_type (Union[Unset, str]): Damage Type
        document_id (Union[Unset, int]): The id of the document associated with the Medical Bill
        etag (Union[Unset, str]): ETag for the *MedicalBill*
        name (Union[Unset, str]): Name of the Medical Bill
        created_at (Union[Unset, datetime.datetime]): The time the *MedicalBill* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *MedicalBill* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    adjustment: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    bill_date: Union[Unset, datetime.date] = UNSET
    bill_received_date: Union[Unset, datetime.date] = UNSET
    damage_type: Union[Unset, str] = UNSET
    document_id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        adjustment = self.adjustment

        amount = self.amount

        bill_date: Union[Unset, str] = UNSET
        if not isinstance(self.bill_date, Unset):
            bill_date = self.bill_date.isoformat()

        bill_received_date: Union[Unset, str] = UNSET
        if not isinstance(self.bill_received_date, Unset):
            bill_received_date = self.bill_received_date.isoformat()

        damage_type = self.damage_type

        document_id = self.document_id

        etag = self.etag

        name = self.name

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
        if adjustment is not UNSET:
            field_dict["adjustment"] = adjustment
        if amount is not UNSET:
            field_dict["amount"] = amount
        if bill_date is not UNSET:
            field_dict["bill_date"] = bill_date
        if bill_received_date is not UNSET:
            field_dict["bill_received_date"] = bill_received_date
        if damage_type is not UNSET:
            field_dict["damage_type"] = damage_type
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        adjustment = d.pop("adjustment", UNSET)

        amount = d.pop("amount", UNSET)

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

        damage_type = d.pop("damage_type", UNSET)

        document_id = d.pop("document_id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

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

        medical_bill_base = cls(
            id=id,
            adjustment=adjustment,
            amount=amount,
            bill_date=bill_date,
            bill_received_date=bill_received_date,
            damage_type=damage_type,
            document_id=document_id,
            etag=etag,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
        )

        medical_bill_base.additional_properties = d
        return medical_bill_base

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
