from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_messagecreate_json_body_data_receivers_item_type import (
    ConversationMessagecreateJsonBodyDataReceiversItemType,
)

T = TypeVar("T", bound="ConversationMessagecreateJsonBodyDataReceiversItem")


@_attrs_define
class ConversationMessagecreateJsonBodyDataReceiversItem:
    """
    Attributes:
        id (int): The unique identifier for a single receiver for this ConversationMessage.
        type_ (ConversationMessagecreateJsonBodyDataReceiversItemType): The type for a single receiver for this
            ConversationMessage, could be `Contact` or `User`.
    """

    id: int
    type_: ConversationMessagecreateJsonBodyDataReceiversItemType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = ConversationMessagecreateJsonBodyDataReceiversItemType(d.pop("type"))

        conversation_messagecreate_json_body_data_receivers_item = cls(
            id=id,
            type_=type_,
        )

        conversation_messagecreate_json_body_data_receivers_item.additional_properties = d
        return conversation_messagecreate_json_body_data_receivers_item

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
