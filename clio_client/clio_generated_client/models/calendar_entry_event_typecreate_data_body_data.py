from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendar_entry_event_typecreate_data_body_data_color import CalendarEntryEventTypecreateDataBodyDataColor

T = TypeVar("T", bound="CalendarEntryEventTypecreateDataBodyData")


@_attrs_define
class CalendarEntryEventTypecreateDataBodyData:
    """
    Attributes:
        color (CalendarEntryEventTypecreateDataBodyDataColor): The color assigned to the CalendarEntryEventType
        name (str): The name of the CalendarEntryEventType
    """

    color: CalendarEntryEventTypecreateDataBodyDataColor
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = CalendarEntryEventTypecreateDataBodyDataColor(d.pop("color"))

        name = d.pop("name")

        calendar_entry_event_typecreate_data_body_data = cls(
            color=color,
            name=name,
        )

        calendar_entry_event_typecreate_data_body_data.additional_properties = d
        return calendar_entry_event_typecreate_data_body_data

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
