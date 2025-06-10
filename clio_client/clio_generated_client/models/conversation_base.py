import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationBase")


@_attrs_define
class ConversationBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Conversation*
        etag (Union[Unset, str]): ETag for the *Conversation*
        archived (Union[Unset, bool]): Whether the conversation has been archived
        read_only (Union[Unset, bool]): Whether the conversation is read only
        current_user_is_member (Union[Unset, bool]): Whether the current user is a member of this conversation
        subject (Union[Unset, str]): The subject of the *Conversation*
        message_count (Union[Unset, int]): The number of messages in this conversation
        time_entries_count (Union[Unset, int]): The number of time entries applied to this conversation
        read (Union[Unset, bool]): Whether any messages in this conversation have been viewed
        created_at (Union[Unset, datetime.datetime]): The time the *Conversation* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Conversation* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    read_only: Union[Unset, bool] = UNSET
    current_user_is_member: Union[Unset, bool] = UNSET
    subject: Union[Unset, str] = UNSET
    message_count: Union[Unset, int] = UNSET
    time_entries_count: Union[Unset, int] = UNSET
    read: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        archived = self.archived

        read_only = self.read_only

        current_user_is_member = self.current_user_is_member

        subject = self.subject

        message_count = self.message_count

        time_entries_count = self.time_entries_count

        read = self.read

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
        if archived is not UNSET:
            field_dict["archived"] = archived
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if current_user_is_member is not UNSET:
            field_dict["current_user_is_member"] = current_user_is_member
        if subject is not UNSET:
            field_dict["subject"] = subject
        if message_count is not UNSET:
            field_dict["message_count"] = message_count
        if time_entries_count is not UNSET:
            field_dict["time_entries_count"] = time_entries_count
        if read is not UNSET:
            field_dict["read"] = read
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

        archived = d.pop("archived", UNSET)

        read_only = d.pop("read_only", UNSET)

        current_user_is_member = d.pop("current_user_is_member", UNSET)

        subject = d.pop("subject", UNSET)

        message_count = d.pop("message_count", UNSET)

        time_entries_count = d.pop("time_entries_count", UNSET)

        read = d.pop("read", UNSET)

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

        conversation_base = cls(
            id=id,
            etag=etag,
            archived=archived,
            read_only=read_only,
            current_user_is_member=current_user_is_member,
            subject=subject,
            message_count=message_count,
            time_entries_count=time_entries_count,
            read=read,
            created_at=created_at,
            updated_at=updated_at,
        )

        conversation_base.additional_properties = d
        return conversation_base

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
