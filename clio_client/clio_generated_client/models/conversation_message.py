import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_base import ConversationBase
    from ..models.document_base import DocumentBase
    from ..models.unredacted_participant_base import UnredactedParticipantBase


T = TypeVar("T", bound="ConversationMessage")


@_attrs_define
class ConversationMessage:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *ConversationMessage*
        etag (Union[Unset, str]): ETag for the *ConversationMessage*
        date (Union[Unset, str]): The creation date of the message in the current user's time zone
        body (Union[Unset, str]): The main content of the *ConversationMessage*
        created_at (Union[Unset, datetime.datetime]): The time the *ConversationMessage* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *ConversationMessage* was last updated (as a ISO-8601
            timestamp)
        sender (Union[Unset, UnredactedParticipantBase]):
        document (Union[Unset, DocumentBase]):
        conversation (Union[Unset, ConversationBase]):
        receivers (Union[Unset, list['UnredactedParticipantBase']]): UnredactedParticipant
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    sender: Union[Unset, "UnredactedParticipantBase"] = UNSET
    document: Union[Unset, "DocumentBase"] = UNSET
    conversation: Union[Unset, "ConversationBase"] = UNSET
    receivers: Union[Unset, list["UnredactedParticipantBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        date = self.date

        body = self.body

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        sender: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        document: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        conversation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conversation, Unset):
            conversation = self.conversation.to_dict()

        receivers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.receivers, Unset):
            receivers = []
            for receivers_item_data in self.receivers:
                receivers_item = receivers_item_data.to_dict()
                receivers.append(receivers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if date is not UNSET:
            field_dict["date"] = date
        if body is not UNSET:
            field_dict["body"] = body
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if sender is not UNSET:
            field_dict["sender"] = sender
        if document is not UNSET:
            field_dict["document"] = document
        if conversation is not UNSET:
            field_dict["conversation"] = conversation
        if receivers is not UNSET:
            field_dict["receivers"] = receivers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_base import ConversationBase
        from ..models.document_base import DocumentBase
        from ..models.unredacted_participant_base import UnredactedParticipantBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        date = d.pop("date", UNSET)

        body = d.pop("body", UNSET)

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

        _sender = d.pop("sender", UNSET)
        sender: Union[Unset, UnredactedParticipantBase]
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = UnredactedParticipantBase.from_dict(_sender)

        _document = d.pop("document", UNSET)
        document: Union[Unset, DocumentBase]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = DocumentBase.from_dict(_document)

        _conversation = d.pop("conversation", UNSET)
        conversation: Union[Unset, ConversationBase]
        if isinstance(_conversation, Unset):
            conversation = UNSET
        else:
            conversation = ConversationBase.from_dict(_conversation)

        receivers = []
        _receivers = d.pop("receivers", UNSET)
        for receivers_item_data in _receivers or []:
            receivers_item = UnredactedParticipantBase.from_dict(receivers_item_data)

            receivers.append(receivers_item)

        conversation_message = cls(
            id=id,
            etag=etag,
            date=date,
            body=body,
            created_at=created_at,
            updated_at=updated_at,
            sender=sender,
            document=document,
            conversation=conversation,
            receivers=receivers,
        )

        conversation_message.additional_properties = d
        return conversation_message

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
