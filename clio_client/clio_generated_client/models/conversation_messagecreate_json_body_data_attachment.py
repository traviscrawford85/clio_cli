from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationMessagecreateJsonBodyDataAttachment")


@_attrs_define
class ConversationMessagecreateJsonBodyDataAttachment:
    """
    Attributes:
        document_id (Union[Unset, int]): The document id of the attached document.
        document_version_id (Union[Unset, int]): The document version id of the attached document.
    """

    document_id: Union[Unset, int] = UNSET
    document_version_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        document_version_id = self.document_version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if document_version_id is not UNSET:
            field_dict["document_version_id"] = document_version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("document_id", UNSET)

        document_version_id = d.pop("document_version_id", UNSET)

        conversation_messagecreate_json_body_data_attachment = cls(
            document_id=document_id,
            document_version_id=document_version_id,
        )

        conversation_messagecreate_json_body_data_attachment.additional_properties = d
        return conversation_messagecreate_json_body_data_attachment

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
