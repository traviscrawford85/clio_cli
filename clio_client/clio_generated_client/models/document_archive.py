import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.document_archive_base_state import DocumentArchiveBaseState
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentArchive")


@_attrs_define
class DocumentArchive:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *DocumentArchive*
        etag (Union[Unset, str]): ETag for the *DocumentArchive*
        created_at (Union[Unset, datetime.datetime]): The time the *DocumentArchive* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *DocumentArchive* was last updated (as a ISO-8601
            timestamp)
        size (Union[Unset, int]): The size of the DocumentArchive in bytes.
        progress (Union[Unset, float]): The percent completion of the DocumentArchive.
        state (Union[Unset, DocumentArchiveBaseState]): The current state of the DocumentArchive.
        message (Union[Unset, str]): A message to indicate why the DocumentArchive didn't complete.
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    size: Union[Unset, int] = UNSET
    progress: Union[Unset, float] = UNSET
    state: Union[Unset, DocumentArchiveBaseState] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        size = self.size

        progress = self.progress

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if size is not UNSET:
            field_dict["size"] = size
        if progress is not UNSET:
            field_dict["progress"] = progress
        if state is not UNSET:
            field_dict["state"] = state
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

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

        size = d.pop("size", UNSET)

        progress = d.pop("progress", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, DocumentArchiveBaseState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DocumentArchiveBaseState(_state)

        message = d.pop("message", UNSET)

        document_archive = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            size=size,
            progress=progress,
            state=state,
            message=message,
        )

        document_archive.additional_properties = d
        return document_archive

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
