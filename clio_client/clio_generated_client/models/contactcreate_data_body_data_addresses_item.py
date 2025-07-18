from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactcreate_data_body_data_addresses_item_name import ContactcreateDataBodyDataAddressesItemName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactcreateDataBodyDataAddressesItem")


@_attrs_define
class ContactcreateDataBodyDataAddressesItem:
    """
    Attributes:
        name (Union[Unset, ContactcreateDataBodyDataAddressesItemName]): Name of the Address. Default:
            ContactcreateDataBodyDataAddressesItemName.OTHER.
        street (Union[Unset, str]): Street.
        city (Union[Unset, str]): City.
        province (Union[Unset, str]): Province or state.
        postal_code (Union[Unset, str]): Postal code or zip code.
        country (Union[Unset, str]): Country
    """

    name: Union[Unset, ContactcreateDataBodyDataAddressesItemName] = ContactcreateDataBodyDataAddressesItemName.OTHER
    street: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    province: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        street = self.street

        city = self.city

        province = self.province

        postal_code = self.postal_code

        country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if street is not UNSET:
            field_dict["street"] = street
        if city is not UNSET:
            field_dict["city"] = city
        if province is not UNSET:
            field_dict["province"] = province
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactcreateDataBodyDataAddressesItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactcreateDataBodyDataAddressesItemName(_name)

        street = d.pop("street", UNSET)

        city = d.pop("city", UNSET)

        province = d.pop("province", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        country = d.pop("country", UNSET)

        contactcreate_data_body_data_addresses_item = cls(
            name=name,
            street=street,
            city=city,
            province=province,
            postal_code=postal_code,
            country=country,
        )

        contactcreate_data_body_data_addresses_item.additional_properties = d
        return contactcreate_data_body_data_addresses_item

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
