from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactupdate_data_body_data_email_addresses_item_name import (
    ContactupdateDataBodyDataEmailAddressesItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactupdateDataBodyDataEmailAddressesItem")


@_attrs_define
class ContactupdateDataBodyDataEmailAddressesItem:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier for a single EmailAddress associated with the Contact. The keyword
            `null` is not valid for this field.
        name (Union[Unset, ContactupdateDataBodyDataEmailAddressesItemName]): Name of the EmailAddress. Default:
            ContactupdateDataBodyDataEmailAddressesItemName.OTHER.
        address (Union[Unset, str]): Email address.
        default_email (Union[Unset, bool]): Whether or not the Contact should be the default email for the Contact.
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated EmailAddress is present, the EmailAddress is deleted from the Contact.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, ContactupdateDataBodyDataEmailAddressesItemName] = (
        ContactupdateDataBodyDataEmailAddressesItemName.OTHER
    )
    address: Union[Unset, str] = UNSET
    default_email: Union[Unset, bool] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        address = self.address

        default_email = self.default_email

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if default_email is not UNSET:
            field_dict["default_email"] = default_email
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactupdateDataBodyDataEmailAddressesItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactupdateDataBodyDataEmailAddressesItemName(_name)

        address = d.pop("address", UNSET)

        default_email = d.pop("default_email", UNSET)

        field_destroy = d.pop("_destroy", UNSET)

        contactupdate_data_body_data_email_addresses_item = cls(
            id=id,
            name=name,
            address=address,
            default_email=default_email,
            field_destroy=field_destroy,
        )

        contactupdate_data_body_data_email_addresses_item.additional_properties = d
        return contactupdate_data_body_data_email_addresses_item

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
