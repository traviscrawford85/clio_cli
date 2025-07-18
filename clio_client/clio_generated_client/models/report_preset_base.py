import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.report_preset_base_category import ReportPresetBaseCategory
from ..models.report_preset_base_format import ReportPresetBaseFormat
from ..models.report_preset_base_kind import ReportPresetBaseKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportPresetBase")


@_attrs_define
class ReportPresetBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *ReportPreset*
        etag (Union[Unset, str]): ETag for the *ReportPreset*
        name (Union[Unset, str]): A specified name for the report preset
        kind (Union[Unset, ReportPresetBaseKind]): The kind of report the preset generates
        format_ (Union[Unset, ReportPresetBaseFormat]): The format of the report the preset generates
        last_generated_at (Union[Unset, datetime.datetime]): The time of the last generated report from this preset (as
            a ISO-8601 timestamp)
        created_at (Union[Unset, datetime.datetime]): The time the *ReportPreset* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *ReportPreset* was last updated (as a ISO-8601
            timestamp)
        category (Union[Unset, ReportPresetBaseCategory]): The category of the report the preset generates
        options (Union[Unset, str]): The report options parameters
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    kind: Union[Unset, ReportPresetBaseKind] = UNSET
    format_: Union[Unset, ReportPresetBaseFormat] = UNSET
    last_generated_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    category: Union[Unset, ReportPresetBaseCategory] = UNSET
    options: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        last_generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_generated_at, Unset):
            last_generated_at = self.last_generated_at.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if format_ is not UNSET:
            field_dict["format"] = format_
        if last_generated_at is not UNSET:
            field_dict["last_generated_at"] = last_generated_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if category is not UNSET:
            field_dict["category"] = category
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, ReportPresetBaseKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ReportPresetBaseKind(_kind)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, ReportPresetBaseFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = ReportPresetBaseFormat(_format_)

        _last_generated_at = d.pop("last_generated_at", UNSET)
        last_generated_at: Union[Unset, datetime.datetime]
        if isinstance(_last_generated_at, Unset):
            last_generated_at = UNSET
        else:
            last_generated_at = isoparse(_last_generated_at)

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

        _category = d.pop("category", UNSET)
        category: Union[Unset, ReportPresetBaseCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ReportPresetBaseCategory(_category)

        options = d.pop("options", UNSET)

        report_preset_base = cls(
            id=id,
            etag=etag,
            name=name,
            kind=kind,
            format_=format_,
            last_generated_at=last_generated_at,
            created_at=created_at,
            updated_at=updated_at,
            category=category,
            options=options,
        )

        report_preset_base.additional_properties = d
        return report_preset_base

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
