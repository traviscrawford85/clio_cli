from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendarcreate_json_body_data_color import CalendarcreateJsonBodyDataColor
from ..models.calendarcreate_json_body_data_source import CalendarcreateJsonBodyDataSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarcreateJsonBodyData")


@_attrs_define
class CalendarcreateJsonBodyData:
    """
    Attributes:
        name (str): Calendar name.
        color (Union[Unset, CalendarcreateJsonBodyDataColor]): Calendar color as seen in the Clio Web UI.
        source (Union[Unset, CalendarcreateJsonBodyDataSource]): The source that visible applies to, by default the Clio
            Web UI (Expects 'mobile' or 'web').
        visible (Union[Unset, bool]): Whether or not the Calendar should be visible by default in the Clio Web UI
            (assuming no source is provided).
    """

    name: str
    color: Union[Unset, CalendarcreateJsonBodyDataColor] = UNSET
    source: Union[Unset, CalendarcreateJsonBodyDataSource] = UNSET
    visible: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if source is not UNSET:
            field_dict["source"] = source
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _color = d.pop("color", UNSET)
        color: Union[Unset, CalendarcreateJsonBodyDataColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CalendarcreateJsonBodyDataColor(_color)

        _source = d.pop("source", UNSET)
        source: Union[Unset, CalendarcreateJsonBodyDataSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = CalendarcreateJsonBodyDataSource(_source)

        visible = d.pop("visible", UNSET)

        calendarcreate_json_body_data = cls(
            name=name,
            color=color,
            source=source,
            visible=visible,
        )

        calendarcreate_json_body_data.additional_properties = d
        return calendarcreate_json_body_data

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
