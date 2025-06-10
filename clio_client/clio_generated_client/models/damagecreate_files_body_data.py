from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.damagecreate_files_body_data_damage_type import DamagecreateFilesBodyDataDamageType

T = TypeVar("T", bound="DamagecreateFilesBodyData")


@_attrs_define
class DamagecreateFilesBodyData:
    """
    Attributes:
        amount (float): Amount
        damage_type (DamagecreateFilesBodyDataDamageType): Damage type
        description (str): Description
        matter_id (int): The unique identifier of the Matter to which the Damage is associated.
    """

    amount: float
    damage_type: DamagecreateFilesBodyDataDamageType
    description: str
    matter_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        damage_type = self.damage_type.value

        description = self.description

        matter_id = self.matter_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "damage_type": damage_type,
                "description": description,
                "matter_id": matter_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        damage_type = DamagecreateFilesBodyDataDamageType(d.pop("damage_type"))

        description = d.pop("description")

        matter_id = d.pop("matter_id")

        damagecreate_files_body_data = cls(
            amount=amount,
            damage_type=damage_type,
            description=description,
            matter_id=matter_id,
        )

        damagecreate_files_body_data.additional_properties = d
        return damagecreate_files_body_data

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
