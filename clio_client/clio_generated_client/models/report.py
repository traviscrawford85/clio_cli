import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.report_base_category import ReportBaseCategory
from ..models.report_base_format import ReportBaseFormat
from ..models.report_base_kind import ReportBaseKind
from ..models.report_base_source import ReportBaseSource
from ..models.report_base_state import ReportBaseState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Report")


@_attrs_define
class Report:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Report*
        etag (Union[Unset, str]): ETag for the *Report*
        name (Union[Unset, str]): A specified name for the report
        state (Union[Unset, ReportBaseState]): The current state of the report
        kind (Union[Unset, ReportBaseKind]): The kind of report to generate
        format_ (Union[Unset, ReportBaseFormat]): The requested format of the report
        progress (Union[Unset, int]): The integer percentage of how complete the report is.
        created_at (Union[Unset, datetime.datetime]): The time the *Report* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Report* was last updated (as a ISO-8601 timestamp)
        category (Union[Unset, ReportBaseCategory]): The category of the report
        source (Union[Unset, ReportBaseSource]): The source of the report
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    state: Union[Unset, ReportBaseState] = UNSET
    kind: Union[Unset, ReportBaseKind] = UNSET
    format_: Union[Unset, ReportBaseFormat] = UNSET
    progress: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    category: Union[Unset, ReportBaseCategory] = UNSET
    source: Union[Unset, ReportBaseSource] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        progress = self.progress

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

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
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if kind is not UNSET:
            field_dict["kind"] = kind
        if format_ is not UNSET:
            field_dict["format"] = format_
        if progress is not UNSET:
            field_dict["progress"] = progress
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if category is not UNSET:
            field_dict["category"] = category
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ReportBaseState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ReportBaseState(_state)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, ReportBaseKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ReportBaseKind(_kind)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, ReportBaseFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = ReportBaseFormat(_format_)

        progress = d.pop("progress", UNSET)

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
        category: Union[Unset, ReportBaseCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ReportBaseCategory(_category)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ReportBaseSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ReportBaseSource(_source)

        report = cls(
            id=id,
            etag=etag,
            name=name,
            state=state,
            kind=kind,
            format_=format_,
            progress=progress,
            created_at=created_at,
            updated_at=updated_at,
            category=category,
            source=source,
        )

        report.additional_properties = d
        return report

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
