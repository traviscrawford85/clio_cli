import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_membership import ConversationMembership
    from ..models.conversation_message_base import ConversationMessageBase
    from ..models.document_base import DocumentBase
    from ..models.matter_base import MatterBase


T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
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
        last_message (Union[Unset, ConversationMessageBase]):
        first_message (Union[Unset, ConversationMessageBase]):
        matter (Union[Unset, MatterBase]):
        messages (Union[Unset, list['ConversationMessageBase']]): ConversationMessage
        documents (Union[Unset, list['DocumentBase']]): Document
        memberships (Union[Unset, list['ConversationMembership']]): ConversationMembership
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
    last_message: Union[Unset, "ConversationMessageBase"] = UNSET
    first_message: Union[Unset, "ConversationMessageBase"] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    messages: Union[Unset, list["ConversationMessageBase"]] = UNSET
    documents: Union[Unset, list["DocumentBase"]] = UNSET
    memberships: Union[Unset, list["ConversationMembership"]] = UNSET
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

        last_message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_message, Unset):
            last_message = self.last_message.to_dict()

        first_message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first_message, Unset):
            first_message = self.first_message.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        memberships: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.memberships, Unset):
            memberships = []
            for memberships_item_data in self.memberships:
                memberships_item = memberships_item_data.to_dict()
                memberships.append(memberships_item)

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
        if last_message is not UNSET:
            field_dict["last_message"] = last_message
        if first_message is not UNSET:
            field_dict["first_message"] = first_message
        if matter is not UNSET:
            field_dict["matter"] = matter
        if messages is not UNSET:
            field_dict["messages"] = messages
        if documents is not UNSET:
            field_dict["documents"] = documents
        if memberships is not UNSET:
            field_dict["memberships"] = memberships

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_membership import ConversationMembership
        from ..models.conversation_message_base import ConversationMessageBase
        from ..models.document_base import DocumentBase
        from ..models.matter_base import MatterBase

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

        _last_message = d.pop("last_message", UNSET)
        last_message: Union[Unset, ConversationMessageBase]
        if isinstance(_last_message, Unset):
            last_message = UNSET
        else:
            last_message = ConversationMessageBase.from_dict(_last_message)

        _first_message = d.pop("first_message", UNSET)
        first_message: Union[Unset, ConversationMessageBase]
        if isinstance(_first_message, Unset):
            first_message = UNSET
        else:
            first_message = ConversationMessageBase.from_dict(_first_message)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = ConversationMessageBase.from_dict(messages_item_data)

            messages.append(messages_item)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = DocumentBase.from_dict(documents_item_data)

            documents.append(documents_item)

        memberships = []
        _memberships = d.pop("memberships", UNSET)
        for memberships_item_data in _memberships or []:
            memberships_item = ConversationMembership.from_dict(memberships_item_data)

            memberships.append(memberships_item)

        conversation = cls(
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
            last_message=last_message,
            first_message=first_message,
            matter=matter,
            messages=messages,
            documents=documents,
            memberships=memberships,
        )

        conversation.additional_properties = d
        return conversation

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
