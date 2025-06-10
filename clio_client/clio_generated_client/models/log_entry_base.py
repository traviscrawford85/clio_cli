import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.log_entry_base_type import LogEntryBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LogEntryBase")


@_attrs_define
class LogEntryBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *LogEntry*
        etag (Union[Unset, str]): ETag for the *LogEntry*
        type_ (Union[Unset, LogEntryBaseType]): The type of the *LogEntry*
        accessed_at (Union[Unset, datetime.datetime]): The time the item was last accessed (as a ISO-8601 timestamp)
        created_at (Union[Unset, datetime.datetime]): The time the *LogEntry* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *LogEntry* was last updated (as a ISO-8601 timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    type_: Union[Unset, LogEntryBaseType] = UNSET
    accessed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        accessed_at: Union[Unset, str] = UNSET
        if not isinstance(self.accessed_at, Unset):
            accessed_at = self.accessed_at.isoformat()

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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if accessed_at is not UNSET:
            field_dict["accessed_at"] = accessed_at
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

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, LogEntryBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LogEntryBaseType(_type_)

        _accessed_at = d.pop("accessed_at", UNSET)
        accessed_at: Union[Unset, datetime.datetime]
        if isinstance(_accessed_at, Unset):
            accessed_at = UNSET
        else:
            accessed_at = isoparse(_accessed_at)

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

        log_entry_base = cls(
            id=id,
            etag=etag,
            type_=type_,
            accessed_at=accessed_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        log_entry_base.additional_properties = d
        return log_entry_base

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
