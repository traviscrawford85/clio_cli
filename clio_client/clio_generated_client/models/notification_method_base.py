import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.notification_method_base_type import NotificationMethodBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationMethodBase")


@_attrs_define
class NotificationMethodBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *NotificationMethod*
        etag (Union[Unset, str]): ETag for the *NotificationMethod*
        type_ (Union[Unset, NotificationMethodBaseType]): Human readable description of the type of notification
        email_address (Union[Unset, str]): Email address to send the notification to (only for email type)
        is_default_email_address (Union[Unset, bool]): A boolean that is returned only on notification method objects
            that are relevant e.g. Email notification or Alternative Email
        created_at (Union[Unset, datetime.datetime]): The time the *NotificationMethod* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *NotificationMethod* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    type_: Union[Unset, NotificationMethodBaseType] = UNSET
    email_address: Union[Unset, str] = UNSET
    is_default_email_address: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        email_address = self.email_address

        is_default_email_address = self.is_default_email_address

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
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if is_default_email_address is not UNSET:
            field_dict["is_default_email_address"] = is_default_email_address
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
        type_: Union[Unset, NotificationMethodBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = NotificationMethodBaseType(_type_)

        email_address = d.pop("email_address", UNSET)

        is_default_email_address = d.pop("is_default_email_address", UNSET)

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

        notification_method_base = cls(
            id=id,
            etag=etag,
            type_=type_,
            email_address=email_address,
            is_default_email_address=is_default_email_address,
            created_at=created_at,
            updated_at=updated_at,
        )

        notification_method_base.additional_properties = d
        return notification_method_base

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
