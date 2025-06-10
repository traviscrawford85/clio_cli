import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.attendee_base_type import AttendeeBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttendeeBase")


@_attrs_define
class AttendeeBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Attendee*
        etag (Union[Unset, str]): ETag for the *Attendee*
        type_ (Union[Unset, AttendeeBaseType]): The class name of the *Attendee*
        name (Union[Unset, str]): The name of the *Attendee*
        enabled (Union[Unset, bool]): If the Attendee is a user, represents whether the user is enabled or disabled.
            Returns null if attendee is a Contact.
        email (Union[Unset, str]): If the Attendee is a User, this is the User's email. If the Attendee is a contact,
            this is the Contact's primary email address.
        created_at (Union[Unset, datetime.datetime]): The time the *Attendee* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Attendee* was last updated (as a ISO-8601 timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    type_: Union[Unset, AttendeeBaseType] = UNSET
    name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        name = self.name

        enabled = self.enabled

        email = self.email

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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if email is not UNSET:
            field_dict["email"] = email
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

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AttendeeBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AttendeeBaseType(_type_)

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        email = d.pop("email", UNSET)

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

        attendee_base = cls(
            id=id,
            etag=etag,
            type_=type_,
            name=name,
            enabled=enabled,
            email=email,
            created_at=created_at,
            updated_at=updated_at,
        )

        attendee_base.additional_properties = d
        return attendee_base

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
