import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConferenceMeetingBase")


@_attrs_define
class ConferenceMeetingBase:
    """
    Attributes:
        conference_id (Union[Unset, int]): Third-party provider unique meeting ID
        conference_password (Union[Unset, str]): Third-party provider meeting password
        created_at (Union[Unset, datetime.datetime]): The time the *ConferenceMeeting* was created (as a ISO-8601
            timestamp)
        etag (Union[Unset, str]): ETag for the *ConferenceMeeting*
        id (Union[Unset, int]): Unique identifier for the *ConferenceMeeting*
        join_url (Union[Unset, str]): URL for participants to join the video conference
        type_ (Union[Unset, str]): The type of video conference
        source_id (Union[Unset, int]): The external ID of the video conference meeting
        updated_at (Union[Unset, datetime.datetime]): The time the *ConferenceMeeting* was last updated (as a ISO-8601
            timestamp)
    """

    conference_id: Union[Unset, int] = UNSET
    conference_password: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    join_url: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    source_id: Union[Unset, int] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conference_id = self.conference_id

        conference_password = self.conference_password

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        etag = self.etag

        id = self.id

        join_url = self.join_url

        type_ = self.type_

        source_id = self.source_id

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conference_id is not UNSET:
            field_dict["conference_id"] = conference_id
        if conference_password is not UNSET:
            field_dict["conference_password"] = conference_password
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if join_url is not UNSET:
            field_dict["join_url"] = join_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conference_id = d.pop("conference_id", UNSET)

        conference_password = d.pop("conference_password", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        join_url = d.pop("join_url", UNSET)

        type_ = d.pop("type", UNSET)

        source_id = d.pop("source_id", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        conference_meeting_base = cls(
            conference_id=conference_id,
            conference_password=conference_password,
            created_at=created_at,
            etag=etag,
            id=id,
            join_url=join_url,
            type_=type_,
            source_id=source_id,
            updated_at=updated_at,
        )

        conference_meeting_base.additional_properties = d
        return conference_meeting_base

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
