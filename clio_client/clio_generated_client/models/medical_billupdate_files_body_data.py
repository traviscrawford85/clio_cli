import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.medical_billupdate_files_body_data_payers_item import MedicalBillupdateFilesBodyDataPayersItem


T = TypeVar("T", bound="MedicalBillupdateFilesBodyData")


@_attrs_define
class MedicalBillupdateFilesBodyData:
    """
    Attributes:
        adjustment (Union[Unset, float]): Adjustment
        amount (Union[Unset, float]): Amount
        balance (Union[Unset, float]): Balance
        bill_date (Union[Unset, datetime.date]): Bill Date (Expects an ISO-8601 date).
        bill_received_date (Union[Unset, datetime.date]): Bill Received Date (Expects an ISO-8601 date).
        mark_balance_as_lien (Union[Unset, bool]): Mark balance as lien
        name (Union[Unset, str]): Name
        payers (Union[Unset, list['MedicalBillupdateFilesBodyDataPayersItem']]):
    """

    adjustment: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    balance: Union[Unset, float] = UNSET
    bill_date: Union[Unset, datetime.date] = UNSET
    bill_received_date: Union[Unset, datetime.date] = UNSET
    mark_balance_as_lien: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    payers: Union[Unset, list["MedicalBillupdateFilesBodyDataPayersItem"]] = UNSET
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

        mark_balance_as_lien = self.mark_balance_as_lien

        name = self.name

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
        if mark_balance_as_lien is not UNSET:
            field_dict["mark_balance_as_lien"] = mark_balance_as_lien
        if name is not UNSET:
            field_dict["name"] = name
        if payers is not UNSET:
            field_dict["payers"] = payers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medical_billupdate_files_body_data_payers_item import MedicalBillupdateFilesBodyDataPayersItem

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

        mark_balance_as_lien = d.pop("mark_balance_as_lien", UNSET)

        name = d.pop("name", UNSET)

        payers = []
        _payers = d.pop("payers", UNSET)
        for payers_item_data in _payers or []:
            payers_item = MedicalBillupdateFilesBodyDataPayersItem.from_dict(payers_item_data)

            payers.append(payers_item)

        medical_billupdate_files_body_data = cls(
            adjustment=adjustment,
            amount=amount,
            balance=balance,
            bill_date=bill_date,
            bill_received_date=bill_received_date,
            mark_balance_as_lien=mark_balance_as_lien,
            name=name,
            payers=payers,
        )

        medical_billupdate_files_body_data.additional_properties = d
        return medical_billupdate_files_body_data

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
