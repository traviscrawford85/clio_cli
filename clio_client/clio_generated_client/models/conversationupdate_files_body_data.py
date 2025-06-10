from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversationupdate_files_body_data_matter import ConversationupdateFilesBodyDataMatter


T = TypeVar("T", bound="ConversationupdateFilesBodyData")


@_attrs_define
class ConversationupdateFilesBodyData:
    """
    Attributes:
        archived (Union[Unset, bool]): Whether or not the Conversation has been archived.
        matter (Union[Unset, ConversationupdateFilesBodyDataMatter]):
        read (Union[Unset, bool]): Whether or not the Conversation has been read.
    """

    archived: Union[Unset, bool] = UNSET
    matter: Union[Unset, "ConversationupdateFilesBodyDataMatter"] = UNSET
    read: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived = self.archived

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        read = self.read

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived is not UNSET:
            field_dict["archived"] = archived
        if matter is not UNSET:
            field_dict["matter"] = matter
        if read is not UNSET:
            field_dict["read"] = read

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversationupdate_files_body_data_matter import ConversationupdateFilesBodyDataMatter

        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, ConversationupdateFilesBodyDataMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = ConversationupdateFilesBodyDataMatter.from_dict(_matter)

        read = d.pop("read", UNSET)

        conversationupdate_files_body_data = cls(
            archived=archived,
            matter=matter,
            read=read,
        )

        conversationupdate_files_body_data.additional_properties = d
        return conversationupdate_files_body_data

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
