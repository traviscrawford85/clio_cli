from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendarupdate_data_body_data_color import CalendarupdateDataBodyDataColor
from ..models.calendarupdate_data_body_data_source import CalendarupdateDataBodyDataSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarupdateDataBodyData")


@_attrs_define
class CalendarupdateDataBodyData:
    """
    Attributes:
        color (Union[Unset, CalendarupdateDataBodyDataColor]): Calendar color as seen in the Clio Web UI.
        name (Union[Unset, str]): Calendar name.
        source (Union[Unset, CalendarupdateDataBodyDataSource]): The source that visible applies to, by default the Clio
            Web UI (Expects 'mobile' or 'web').
        visible (Union[Unset, bool]): Whether or not the Calendar should be visible by default in the Clio Web UI
            (assuming no source is provided).
    """

    color: Union[Unset, CalendarupdateDataBodyDataColor] = UNSET
    name: Union[Unset, str] = UNSET
    source: Union[Unset, CalendarupdateDataBodyDataSource] = UNSET
    visible: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        name = self.name

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: Union[Unset, CalendarupdateDataBodyDataColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CalendarupdateDataBodyDataColor(_color)

        name = d.pop("name", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, CalendarupdateDataBodyDataSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = CalendarupdateDataBodyDataSource(_source)

        visible = d.pop("visible", UNSET)

        calendarupdate_data_body_data = cls(
            color=color,
            name=name,
            source=source,
            visible=visible,
        )

        calendarupdate_data_body_data.additional_properties = d
        return calendarupdate_data_body_data

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
