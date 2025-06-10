from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactcreate_files_body_data_email_addresses_item_name import (
    ContactcreateFilesBodyDataEmailAddressesItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactcreateFilesBodyDataEmailAddressesItem")


@_attrs_define
class ContactcreateFilesBodyDataEmailAddressesItem:
    """
    Attributes:
        name (Union[Unset, ContactcreateFilesBodyDataEmailAddressesItemName]): Name of the EmailAddress. Default:
            ContactcreateFilesBodyDataEmailAddressesItemName.OTHER.
        address (Union[Unset, str]): Email address.
        default_email (Union[Unset, bool]): Whether or not the Contact should be the default email for the Contact.
    """

    name: Union[Unset, ContactcreateFilesBodyDataEmailAddressesItemName] = (
        ContactcreateFilesBodyDataEmailAddressesItemName.OTHER
    )
    address: Union[Unset, str] = UNSET
    default_email: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        address = self.address

        default_email = self.default_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if default_email is not UNSET:
            field_dict["default_email"] = default_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactcreateFilesBodyDataEmailAddressesItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactcreateFilesBodyDataEmailAddressesItemName(_name)

        address = d.pop("address", UNSET)

        default_email = d.pop("default_email", UNSET)

        contactcreate_files_body_data_email_addresses_item = cls(
            name=name,
            address=address,
            default_email=default_email,
        )

        contactcreate_files_body_data_email_addresses_item.additional_properties = d
        return contactcreate_files_body_data_email_addresses_item

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
