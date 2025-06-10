from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactcreate_files_body_data_phone_numbers_item_name import (
    ContactcreateFilesBodyDataPhoneNumbersItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactcreateFilesBodyDataPhoneNumbersItem")


@_attrs_define
class ContactcreateFilesBodyDataPhoneNumbersItem:
    """
    Attributes:
        name (Union[Unset, ContactcreateFilesBodyDataPhoneNumbersItemName]): Name of the PhoneNumber. Default:
            ContactcreateFilesBodyDataPhoneNumbersItemName.OTHER.
        number (Union[Unset, str]): Phone number.
        default_number (Union[Unset, bool]): Whether or not the PhoneNumber should be the default number for the
            Contact.
    """

    name: Union[Unset, ContactcreateFilesBodyDataPhoneNumbersItemName] = (
        ContactcreateFilesBodyDataPhoneNumbersItemName.OTHER
    )
    number: Union[Unset, str] = UNSET
    default_number: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        number = self.number

        default_number = self.default_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if default_number is not UNSET:
            field_dict["default_number"] = default_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactcreateFilesBodyDataPhoneNumbersItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactcreateFilesBodyDataPhoneNumbersItemName(_name)

        number = d.pop("number", UNSET)

        default_number = d.pop("default_number", UNSET)

        contactcreate_files_body_data_phone_numbers_item = cls(
            name=name,
            number=number,
            default_number=default_number,
        )

        contactcreate_files_body_data_phone_numbers_item.additional_properties = d
        return contactcreate_files_body_data_phone_numbers_item

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
