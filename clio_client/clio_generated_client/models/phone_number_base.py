import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.phone_number_base_name import PhoneNumberBaseName
from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneNumberBase")


@_attrs_define
class PhoneNumberBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *PhoneNumber*
        etag (Union[Unset, str]): ETag for the *PhoneNumber*
        number (Union[Unset, str]): Contact's Phone Number
        name (Union[Unset, PhoneNumberBaseName]): The type of *PhoneNumber* it is
        primary (Union[Unset, bool]): Whether it is default for this contact
        created_at (Union[Unset, datetime.datetime]): The time the *PhoneNumber* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *PhoneNumber* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    name: Union[Unset, PhoneNumberBaseName] = UNSET
    primary: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        number = self.number

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        primary = self.primary

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if number is not UNSET:
            field_dict["number"] = number
        if name is not UNSET:
            field_dict["name"] = name
        if primary is not UNSET:
            field_dict["primary"] = primary
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        number = d.pop("number", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, PhoneNumberBaseName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PhoneNumberBaseName(_name)

        primary = d.pop("primary", UNSET)

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

        phone_number_base = cls(
            id=id,
            etag=etag,
            number=number,
            name=name,
            primary=primary,
            created_at=created_at,
            updated_at=updated_at,
        )

        phone_number_base.additional_properties = d
        return phone_number_base

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
