import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unredacted_participant_base import UnredactedParticipantBase


T = TypeVar("T", bound="ConversationMembership")


@_attrs_define
class ConversationMembership:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *ConversationMembership*
        etag (Union[Unset, str]): ETag for the *ConversationMembership*
        read (Union[Unset, bool]): Whether or not the ConversationMembership has been read by the member
        archived (Union[Unset, bool]): Whether or not the ConversationMembership has been archived by the member
        created_at (Union[Unset, datetime.datetime]): The time the *ConversationMembership* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *ConversationMembership* was last updated (as a
            ISO-8601 timestamp)
        member (Union[Unset, UnredactedParticipantBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    read: Union[Unset, bool] = UNSET
    archived: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    member: Union[Unset, "UnredactedParticipantBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        read = self.read

        archived = self.archived

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        member: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.member, Unset):
            member = self.member.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if read is not UNSET:
            field_dict["read"] = read
        if archived is not UNSET:
            field_dict["archived"] = archived
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if member is not UNSET:
            field_dict["member"] = member

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unredacted_participant_base import UnredactedParticipantBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        read = d.pop("read", UNSET)

        archived = d.pop("archived", UNSET)

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

        _member = d.pop("member", UNSET)
        member: Union[Unset, UnredactedParticipantBase]
        if isinstance(_member, Unset):
            member = UNSET
        else:
            member = UnredactedParticipantBase.from_dict(_member)

        conversation_membership = cls(
            id=id,
            etag=etag,
            read=read,
            archived=archived,
            created_at=created_at,
            updated_at=updated_at,
            member=member,
        )

        conversation_membership.additional_properties = d
        return conversation_membership

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
