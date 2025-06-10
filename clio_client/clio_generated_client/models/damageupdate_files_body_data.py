from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.damageupdate_files_body_data_damage_type import DamageupdateFilesBodyDataDamageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DamageupdateFilesBodyData")


@_attrs_define
class DamageupdateFilesBodyData:
    """
    Attributes:
        amount (Union[Unset, float]): Amount
        damage_type (Union[Unset, DamageupdateFilesBodyDataDamageType]): Damage type
        description (Union[Unset, str]): Description
    """

    amount: Union[Unset, float] = UNSET
    damage_type: Union[Unset, DamageupdateFilesBodyDataDamageType] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        damage_type: Union[Unset, str] = UNSET
        if not isinstance(self.damage_type, Unset):
            damage_type = self.damage_type.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if damage_type is not UNSET:
            field_dict["damage_type"] = damage_type
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _damage_type = d.pop("damage_type", UNSET)
        damage_type: Union[Unset, DamageupdateFilesBodyDataDamageType]
        if isinstance(_damage_type, Unset):
            damage_type = UNSET
        else:
            damage_type = DamageupdateFilesBodyDataDamageType(_damage_type)

        description = d.pop("description", UNSET)

        damageupdate_files_body_data = cls(
            amount=amount,
            damage_type=damage_type,
            description=description,
        )

        damageupdate_files_body_data.additional_properties = d
        return damageupdate_files_body_data

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
