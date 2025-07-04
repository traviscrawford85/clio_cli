import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.address_base_name import AddressBaseName
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressBase")


@_attrs_define
class AddressBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Address*
        etag (Union[Unset, str]): ETag for the *Address*
        street (Union[Unset, str]): Street of the *Address*
        city (Union[Unset, str]): City of the *Address*
        province (Union[Unset, str]): Province or state of the *Address*
        postal_code (Union[Unset, str]): Postal code of the *Address*
        country (Union[Unset, str]): Country of the *Address*
        name (Union[Unset, AddressBaseName]): The name of the *Address*
        created_at (Union[Unset, datetime.datetime]): The time the *Address* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Address* was last updated (as a ISO-8601 timestamp)
        primary (Union[Unset, bool]): Whether it is the default for this contact
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    province: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    name: Union[Unset, AddressBaseName] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    primary: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        street = self.street

        city = self.city

        province = self.province

        postal_code = self.postal_code

        country = self.country

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
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
        if name is not UNSET:
            field_dict["name"] = name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        street = d.pop("street", UNSET)

        city = d.pop("city", UNSET)

        province = d.pop("province", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        country = d.pop("country", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, AddressBaseName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = AddressBaseName(_name)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        primary = d.pop("primary", UNSET)

        address_base = cls(
            id=id,
            etag=etag,
            street=street,
            city=city,
            province=province,
            postal_code=postal_code,
            country=country,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            primary=primary,
        )

        address_base.additional_properties = d
        return address_base

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
