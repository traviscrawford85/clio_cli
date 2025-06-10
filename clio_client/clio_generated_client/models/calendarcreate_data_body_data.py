from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendarcreate_data_body_data_color import CalendarcreateDataBodyDataColor
from ..models.calendarcreate_data_body_data_source import CalendarcreateDataBodyDataSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarcreateDataBodyData")


@_attrs_define
class CalendarcreateDataBodyData:
    """
    Attributes:
        name (str): Calendar name.
        color (Union[Unset, CalendarcreateDataBodyDataColor]): Calendar color as seen in the Clio Web UI.
        source (Union[Unset, CalendarcreateDataBodyDataSource]): The source that visible applies to, by default the Clio
            Web UI (Expects 'mobile' or 'web').
        visible (Union[Unset, bool]): Whether or not the Calendar should be visible by default in the Clio Web UI
            (assuming no source is provided).
    """

    name: str
    color: Union[Unset, CalendarcreateDataBodyDataColor] = UNSET
    source: Union[Unset, CalendarcreateDataBodyDataSource] = UNSET
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
        color: Union[Unset, CalendarcreateDataBodyDataColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CalendarcreateDataBodyDataColor(_color)

        _source = d.pop("source", UNSET)
        source: Union[Unset, CalendarcreateDataBodyDataSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = CalendarcreateDataBodyDataSource(_source)

        visible = d.pop("visible", UNSET)

        calendarcreate_data_body_data = cls(
            name=name,
            color=color,
            source=source,
            visible=visible,
        )

        calendarcreate_data_body_data.additional_properties = d
        return calendarcreate_data_body_data

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
