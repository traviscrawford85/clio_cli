import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reminder_template_base_notification_type import ReminderTemplateBaseNotificationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReminderTemplateBase")


@_attrs_define
class ReminderTemplateBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *ReminderTemplate*
        etag (Union[Unset, str]): ETag for the *ReminderTemplate*
        duration (Union[Unset, int]): The time in minutes to remind user before the subject.
        notification_type (Union[Unset, ReminderTemplateBaseNotificationType]): The type of method to be notified by
        created_at (Union[Unset, datetime.datetime]): The time the *ReminderTemplate* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *ReminderTemplate* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    notification_type: Union[Unset, ReminderTemplateBaseNotificationType] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        duration = self.duration

        notification_type: Union[Unset, str] = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type.value

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
        if duration is not UNSET:
            field_dict["duration"] = duration
        if notification_type is not UNSET:
            field_dict["notification_type"] = notification_type
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

        duration = d.pop("duration", UNSET)

        _notification_type = d.pop("notification_type", UNSET)
        notification_type: Union[Unset, ReminderTemplateBaseNotificationType]
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = ReminderTemplateBaseNotificationType(_notification_type)

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

        reminder_template_base = cls(
            id=id,
            etag=etag,
            duration=duration,
            notification_type=notification_type,
            created_at=created_at,
            updated_at=updated_at,
        )

        reminder_template_base.additional_properties = d
        return reminder_template_base

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
