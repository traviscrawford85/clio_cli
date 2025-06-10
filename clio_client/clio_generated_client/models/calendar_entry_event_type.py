import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.calendar_entry_event_type_base_color import CalendarEntryEventTypeBaseColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarEntryEventType")


@_attrs_define
class CalendarEntryEventType:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *CalendarEntryEventType*
        etag (Union[Unset, str]): ETag for the *CalendarEntryEventType*
        created_at (Union[Unset, datetime.datetime]): The time the *CalendarEntryEventType* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *CalendarEntryEventType* was last updated (as a
            ISO-8601 timestamp)
        color (Union[Unset, CalendarEntryEventTypeBaseColor]): The color describing the *CalendarEntryEventType*
        name (Union[Unset, str]): The name for the *CalendarEntryEventType*
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    color: Union[Unset, CalendarEntryEventTypeBaseColor] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if color is not UNSET:
            field_dict["color"] = color
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

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

        _color = d.pop("color", UNSET)
        color: Union[Unset, CalendarEntryEventTypeBaseColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CalendarEntryEventTypeBaseColor(_color)

        name = d.pop("name", UNSET)

        calendar_entry_event_type = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            color=color,
            name=name,
        )

        calendar_entry_event_type.additional_properties = d
        return calendar_entry_event_type

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
