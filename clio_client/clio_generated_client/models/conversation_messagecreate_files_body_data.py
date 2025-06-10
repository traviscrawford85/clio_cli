from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_messagecreate_files_body_data_attachment import (
        ConversationMessagecreateFilesBodyDataAttachment,
    )
    from ..models.conversation_messagecreate_files_body_data_conversation import (
        ConversationMessagecreateFilesBodyDataConversation,
    )
    from ..models.conversation_messagecreate_files_body_data_matter import ConversationMessagecreateFilesBodyDataMatter
    from ..models.conversation_messagecreate_files_body_data_receivers_item import (
        ConversationMessagecreateFilesBodyDataReceiversItem,
    )


T = TypeVar("T", bound="ConversationMessagecreateFilesBodyData")


@_attrs_define
class ConversationMessagecreateFilesBodyData:
    """
    Attributes:
        body (str): The body value.
        receivers (list['ConversationMessagecreateFilesBodyDataReceiversItem']):
        subject (str): The subject value.
        attachment (Union[Unset, ConversationMessagecreateFilesBodyDataAttachment]):
        conversation (Union[Unset, ConversationMessagecreateFilesBodyDataConversation]):
        matter (Union[Unset, ConversationMessagecreateFilesBodyDataMatter]):
    """

    body: str
    receivers: list["ConversationMessagecreateFilesBodyDataReceiversItem"]
    subject: str
    attachment: Union[Unset, "ConversationMessagecreateFilesBodyDataAttachment"] = UNSET
    conversation: Union[Unset, "ConversationMessagecreateFilesBodyDataConversation"] = UNSET
    matter: Union[Unset, "ConversationMessagecreateFilesBodyDataMatter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        receivers = []
        for receivers_item_data in self.receivers:
            receivers_item = receivers_item_data.to_dict()
            receivers.append(receivers_item)

        subject = self.subject

        attachment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = self.attachment.to_dict()

        conversation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conversation, Unset):
            conversation = self.conversation.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "receivers": receivers,
                "subject": subject,
            }
        )
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if conversation is not UNSET:
            field_dict["conversation"] = conversation
        if matter is not UNSET:
            field_dict["matter"] = matter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_messagecreate_files_body_data_attachment import (
            ConversationMessagecreateFilesBodyDataAttachment,
        )
        from ..models.conversation_messagecreate_files_body_data_conversation import (
            ConversationMessagecreateFilesBodyDataConversation,
        )
        from ..models.conversation_messagecreate_files_body_data_matter import (
            ConversationMessagecreateFilesBodyDataMatter,
        )
        from ..models.conversation_messagecreate_files_body_data_receivers_item import (
            ConversationMessagecreateFilesBodyDataReceiversItem,
        )

        d = dict(src_dict)
        body = d.pop("body")

        receivers = []
        _receivers = d.pop("receivers")
        for receivers_item_data in _receivers:
            receivers_item = ConversationMessagecreateFilesBodyDataReceiversItem.from_dict(receivers_item_data)

            receivers.append(receivers_item)

        subject = d.pop("subject")

        _attachment = d.pop("attachment", UNSET)
        attachment: Union[Unset, ConversationMessagecreateFilesBodyDataAttachment]
        if isinstance(_attachment, Unset):
            attachment = UNSET
        else:
            attachment = ConversationMessagecreateFilesBodyDataAttachment.from_dict(_attachment)

        _conversation = d.pop("conversation", UNSET)
        conversation: Union[Unset, ConversationMessagecreateFilesBodyDataConversation]
        if isinstance(_conversation, Unset):
            conversation = UNSET
        else:
            conversation = ConversationMessagecreateFilesBodyDataConversation.from_dict(_conversation)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, ConversationMessagecreateFilesBodyDataMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = ConversationMessagecreateFilesBodyDataMatter.from_dict(_matter)

        conversation_messagecreate_files_body_data = cls(
            body=body,
            receivers=receivers,
            subject=subject,
            attachment=attachment,
            conversation=conversation,
            matter=matter,
        )

        conversation_messagecreate_files_body_data.additional_properties = d
        return conversation_messagecreate_files_body_data

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
