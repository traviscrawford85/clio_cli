from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MedicalBillupdateDataBodyDataPayersItem")


@_attrs_define
class MedicalBillupdateDataBodyDataPayersItem:
    """
    Attributes:
        amount (Union[Unset, float]): Lien amount.
        holder_id (Union[Unset, int]): Lien holder ID
        mark_as_lien (Union[Unset, bool]): Mark record as Lien.
    """

    amount: Union[Unset, float] = UNSET
    holder_id: Union[Unset, int] = UNSET
    mark_as_lien: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        holder_id = self.holder_id

        mark_as_lien = self.mark_as_lien

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if holder_id is not UNSET:
            field_dict["holder_id"] = holder_id
        if mark_as_lien is not UNSET:
            field_dict["mark_as_lien"] = mark_as_lien

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        holder_id = d.pop("holder_id", UNSET)

        mark_as_lien = d.pop("mark_as_lien", UNSET)

        medical_billupdate_data_body_data_payers_item = cls(
            amount=amount,
            holder_id=holder_id,
            mark_as_lien=mark_as_lien,
        )

        medical_billupdate_data_body_data_payers_item.additional_properties = d
        return medical_billupdate_data_body_data_payers_item

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
