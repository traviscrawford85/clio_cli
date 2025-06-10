from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_presetcreate_json_body_data_format import ReportPresetcreateJsonBodyDataFormat
from ..models.report_presetcreate_json_body_data_kind import ReportPresetcreateJsonBodyDataKind

T = TypeVar("T", bound="ReportPresetcreateJsonBodyData")


@_attrs_define
class ReportPresetcreateJsonBodyData:
    """
    Attributes:
        format_ (ReportPresetcreateJsonBodyDataFormat): What format the report will be generated in.
        kind (ReportPresetcreateJsonBodyDataKind): What kind of report will be generated.
        name (str): Name of the ReportPreset.
        options (str): What the report generation parameters are. See [Creating a Report Preset](#section/Creating-a-
            Report-Preset) for a sample request.
    """

    format_: ReportPresetcreateJsonBodyDataFormat
    kind: ReportPresetcreateJsonBodyDataKind
    name: str
    options: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_.value

        kind = self.kind.value

        name = self.name

        options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "kind": kind,
                "name": name,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        format_ = ReportPresetcreateJsonBodyDataFormat(d.pop("format"))

        kind = ReportPresetcreateJsonBodyDataKind(d.pop("kind"))

        name = d.pop("name")

        options = d.pop("options")

        report_presetcreate_json_body_data = cls(
            format_=format_,
            kind=kind,
            name=name,
            options=options,
        )

        report_presetcreate_json_body_data.additional_properties = d
        return report_presetcreate_json_body_data

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
