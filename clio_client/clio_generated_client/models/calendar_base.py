import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.calendar_base_color import CalendarBaseColor
from ..models.calendar_base_light_color import CalendarBaseLightColor
from ..models.calendar_base_permission import CalendarBasePermission
from ..models.calendar_base_source import CalendarBaseSource
from ..models.calendar_base_type import CalendarBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarBase")


@_attrs_define
class CalendarBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Calendar*
        etag (Union[Unset, str]): ETag for the *Calendar*
        color (Union[Unset, CalendarBaseColor]): Color
        light_color (Union[Unset, CalendarBaseLightColor]): Accent color to complement the main calendar color.
        court_rules_default_calendar (Union[Unset, bool]): Whether the calendar is default court rules calendar for
            current user
        name (Union[Unset, str]): The name of the *Calendar*
        permission (Union[Unset, CalendarBasePermission]): The user's permission to the *Calendar*
        type_ (Union[Unset, CalendarBaseType]): The type of the *Calendar*
        visible (Union[Unset, bool]): Whether the *Calendar* will be shown by default in the Clio Web UI (assuming no
            source is provided).
        created_at (Union[Unset, datetime.datetime]): The time the *Calendar* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Calendar* was last updated (as a ISO-8601 timestamp)
        source (Union[Unset, CalendarBaseSource]): The source that visible applies to, by default the Clio Web UI
            (Expects 'mobile' or 'web').
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    color: Union[Unset, CalendarBaseColor] = UNSET
    light_color: Union[Unset, CalendarBaseLightColor] = UNSET
    court_rules_default_calendar: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    permission: Union[Unset, CalendarBasePermission] = UNSET
    type_: Union[Unset, CalendarBaseType] = UNSET
    visible: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    source: Union[Unset, CalendarBaseSource] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        light_color: Union[Unset, str] = UNSET
        if not isinstance(self.light_color, Unset):
            light_color = self.light_color.value

        court_rules_default_calendar = self.court_rules_default_calendar

        name = self.name

        permission: Union[Unset, str] = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        visible = self.visible

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if color is not UNSET:
            field_dict["color"] = color
        if light_color is not UNSET:
            field_dict["light_color"] = light_color
        if court_rules_default_calendar is not UNSET:
            field_dict["court_rules_default_calendar"] = court_rules_default_calendar
        if name is not UNSET:
            field_dict["name"] = name
        if permission is not UNSET:
            field_dict["permission"] = permission
        if type_ is not UNSET:
            field_dict["type"] = type_
        if visible is not UNSET:
            field_dict["visible"] = visible
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _color = d.pop("color", UNSET)
        color: Union[Unset, CalendarBaseColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CalendarBaseColor(_color)

        _light_color = d.pop("light_color", UNSET)
        light_color: Union[Unset, CalendarBaseLightColor]
        if isinstance(_light_color, Unset):
            light_color = UNSET
        else:
            light_color = CalendarBaseLightColor(_light_color)

        court_rules_default_calendar = d.pop("court_rules_default_calendar", UNSET)

        name = d.pop("name", UNSET)

        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, CalendarBasePermission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = CalendarBasePermission(_permission)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CalendarBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CalendarBaseType(_type_)

        visible = d.pop("visible", UNSET)

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

        _source = d.pop("source", UNSET)
        source: Union[Unset, CalendarBaseSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = CalendarBaseSource(_source)

        calendar_base = cls(
            id=id,
            etag=etag,
            color=color,
            light_color=light_color,
            court_rules_default_calendar=court_rules_default_calendar,
            name=name,
            permission=permission,
            type_=type_,
            visible=visible,
            created_at=created_at,
            updated_at=updated_at,
            source=source,
        )

        calendar_base.additional_properties = d
        return calendar_base

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
