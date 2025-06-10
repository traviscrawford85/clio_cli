from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactupdate_data_body_data_phone_numbers_item_name import ContactupdateDataBodyDataPhoneNumbersItemName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactupdateDataBodyDataPhoneNumbersItem")


@_attrs_define
class ContactupdateDataBodyDataPhoneNumbersItem:
    """
    Attributes:
        name (Union[Unset, ContactupdateDataBodyDataPhoneNumbersItemName]): Name of the PhoneNumber. Default:
            ContactupdateDataBodyDataPhoneNumbersItemName.OTHER.
        number (Union[Unset, str]): Phone number.
        default_number (Union[Unset, bool]): Whether or not the PhoneNumber should be the default number for the
            Contact.
        id (Union[Unset, int]): The unique identifier for a single PhoneNumber associated with the Contact. The keyword
            `null` is not valid for this field.
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated PhoneNumber is present, the PhoneNumber is deleted from the Contact.
    """

    name: Union[Unset, ContactupdateDataBodyDataPhoneNumbersItemName] = (
        ContactupdateDataBodyDataPhoneNumbersItemName.OTHER
    )
    number: Union[Unset, str] = UNSET
    default_number: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        number = self.number

        default_number = self.default_number

        id = self.id

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if default_number is not UNSET:
            field_dict["default_number"] = default_number
        if id is not UNSET:
            field_dict["id"] = id
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactupdateDataBodyDataPhoneNumbersItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactupdateDataBodyDataPhoneNumbersItemName(_name)

        number = d.pop("number", UNSET)

        default_number = d.pop("default_number", UNSET)

        id = d.pop("id", UNSET)

        field_destroy = d.pop("_destroy", UNSET)

        contactupdate_data_body_data_phone_numbers_item = cls(
            name=name,
            number=number,
            default_number=default_number,
            id=id,
            field_destroy=field_destroy,
        )

        contactupdate_data_body_data_phone_numbers_item.additional_properties = d
        return contactupdate_data_body_data_phone_numbers_item

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
