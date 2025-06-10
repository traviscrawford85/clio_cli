from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendar_entry_event_typeupdate_json_body_data_color import CalendarEntryEventTypeupdateJsonBodyDataColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarEntryEventTypeupdateJsonBodyData")


@_attrs_define
class CalendarEntryEventTypeupdateJsonBodyData:
    """
    Attributes:
        color (Union[Unset, CalendarEntryEventTypeupdateJsonBodyDataColor]): The color assigned to the
            CalendarEntryEventType
        name (Union[Unset, str]): The name of the CalendarEntryEventType
    """

    color: Union[Unset, CalendarEntryEventTypeupdateJsonBodyDataColor] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: Union[Unset, CalendarEntryEventTypeupdateJsonBodyDataColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CalendarEntryEventTypeupdateJsonBodyDataColor(_color)

        name = d.pop("name", UNSET)

        calendar_entry_event_typeupdate_json_body_data = cls(
            color=color,
            name=name,
        )

        calendar_entry_event_typeupdate_json_body_data.additional_properties = d
        return calendar_entry_event_typeupdate_json_body_data

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
