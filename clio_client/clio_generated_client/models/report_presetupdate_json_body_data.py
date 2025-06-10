from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_presetupdate_json_body_data_format import ReportPresetupdateJsonBodyDataFormat
from ..models.report_presetupdate_json_body_data_kind import ReportPresetupdateJsonBodyDataKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportPresetupdateJsonBodyData")


@_attrs_define
class ReportPresetupdateJsonBodyData:
    """
    Attributes:
        format_ (Union[Unset, ReportPresetupdateJsonBodyDataFormat]): What format the report will be generated in.
        kind (Union[Unset, ReportPresetupdateJsonBodyDataKind]): What kind of report will be generated.
        name (Union[Unset, str]): Name of the ReportPreset.
        options (Union[Unset, str]): What the report generation parameters are. See [Creating a Report
            Preset](#section/Creating-a-Report-Preset) for a sample request.
    """

    format_: Union[Unset, ReportPresetupdateJsonBodyDataFormat] = UNSET
    kind: Union[Unset, ReportPresetupdateJsonBodyDataKind] = UNSET
    name: Union[Unset, str] = UNSET
    options: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        name = self.name

        options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, ReportPresetupdateJsonBodyDataFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = ReportPresetupdateJsonBodyDataFormat(_format_)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, ReportPresetupdateJsonBodyDataKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ReportPresetupdateJsonBodyDataKind(_kind)

        name = d.pop("name", UNSET)

        options = d.pop("options", UNSET)

        report_presetupdate_json_body_data = cls(
            format_=format_,
            kind=kind,
            name=name,
            options=options,
        )

        report_presetupdate_json_body_data.additional_properties = d
        return report_presetupdate_json_body_data

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
