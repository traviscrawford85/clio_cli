from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextSnippetupdateFilesBodyData")


@_attrs_define
class TextSnippetupdateFilesBodyData:
    """
    Attributes:
        phrase (Union[Unset, str]): The phrase expanded to from a TextSnippet.
        snippet (Union[Unset, str]): The abbreviation that expands to a phrase.
        whole_word (Union[Unset, bool]): Whether or not the TextSnippet requires a space after to trigger the expansion.
    """

    phrase: Union[Unset, str] = UNSET
    snippet: Union[Unset, str] = UNSET
    whole_word: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phrase = self.phrase

        snippet = self.snippet

        whole_word = self.whole_word

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phrase is not UNSET:
            field_dict["phrase"] = phrase
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if whole_word is not UNSET:
            field_dict["whole_word"] = whole_word

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phrase = d.pop("phrase", UNSET)

        snippet = d.pop("snippet", UNSET)

        whole_word = d.pop("whole_word", UNSET)

        text_snippetupdate_files_body_data = cls(
            phrase=phrase,
            snippet=snippet,
            whole_word=whole_word,
        )

        text_snippetupdate_files_body_data.additional_properties = d
        return text_snippetupdate_files_body_data

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
