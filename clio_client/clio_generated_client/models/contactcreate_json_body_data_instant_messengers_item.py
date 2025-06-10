from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactcreate_json_body_data_instant_messengers_item_name import (
    ContactcreateJsonBodyDataInstantMessengersItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactcreateJsonBodyDataInstantMessengersItem")


@_attrs_define
class ContactcreateJsonBodyDataInstantMessengersItem:
    """
    Attributes:
        name (Union[Unset, ContactcreateJsonBodyDataInstantMessengersItemName]): Name of the InstantMessenger. Default:
            ContactcreateJsonBodyDataInstantMessengersItemName.OTHER.
        address (Union[Unset, str]): Address of the InstantMessenger.
    """

    name: Union[Unset, ContactcreateJsonBodyDataInstantMessengersItemName] = (
        ContactcreateJsonBodyDataInstantMessengersItemName.OTHER
    )
    address: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactcreateJsonBodyDataInstantMessengersItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactcreateJsonBodyDataInstantMessengersItemName(_name)

        address = d.pop("address", UNSET)

        contactcreate_json_body_data_instant_messengers_item = cls(
            name=name,
            address=address,
        )

        contactcreate_json_body_data_instant_messengers_item.additional_properties = d
        return contactcreate_json_body_data_instant_messengers_item

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
