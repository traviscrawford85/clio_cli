import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.calendar_visibility_base_color import CalendarVisibilityBaseColor
from ..models.calendar_visibility_base_light_color import CalendarVisibilityBaseLightColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarVisibilityBase")


@_attrs_define
class CalendarVisibilityBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *CalendarVisibility*
        etag (Union[Unset, str]): ETag for the *CalendarVisibility*
        color (Union[Unset, CalendarVisibilityBaseColor]): Calendar color
        light_color (Union[Unset, CalendarVisibilityBaseLightColor]): Accent color to complement the main calendar
            color.
        visible (Union[Unset, bool]): Whether the *CalendarVisibility* will be shown by default in the Clio Web UI.
        name (Union[Unset, str]): Calendar name
        created_at (Union[Unset, datetime.datetime]): The time the *CalendarVisibility* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *CalendarVisibility* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    color: Union[Unset, CalendarVisibilityBaseColor] = UNSET
    light_color: Union[Unset, CalendarVisibilityBaseLightColor] = UNSET
    visible: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
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

        visible = self.visible

        name = self.name

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
        if color is not UNSET:
            field_dict["color"] = color
        if light_color is not UNSET:
            field_dict["light_color"] = light_color
        if visible is not UNSET:
            field_dict["visible"] = visible
        if name is not UNSET:
            field_dict["name"] = name
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

        _color = d.pop("color", UNSET)
        color: Union[Unset, CalendarVisibilityBaseColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CalendarVisibilityBaseColor(_color)

        _light_color = d.pop("light_color", UNSET)
        light_color: Union[Unset, CalendarVisibilityBaseLightColor]
        if isinstance(_light_color, Unset):
            light_color = UNSET
        else:
            light_color = CalendarVisibilityBaseLightColor(_light_color)

        visible = d.pop("visible", UNSET)

        name = d.pop("name", UNSET)

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

        calendar_visibility_base = cls(
            id=id,
            etag=etag,
            color=color,
            light_color=light_color,
            visible=visible,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
        )

        calendar_visibility_base.additional_properties = d
        return calendar_visibility_base

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
