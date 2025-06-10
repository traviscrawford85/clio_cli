import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextSnippet")


@_attrs_define
class TextSnippet:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *TextSnippet*
        etag (Union[Unset, str]): ETag for the *TextSnippet*
        created_at (Union[Unset, datetime.datetime]): The time the *TextSnippet* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *TextSnippet* was last updated (as a ISO-8601
            timestamp)
        snippet (Union[Unset, str]): The abbreviation that should be expanded
        phrase (Union[Unset, str]): The phrase the abbreviation should be expanded to
        whole_word (Union[Unset, bool]): Whether the *TextSnippet* abbreviation requires a space after it has been
            entered to expand to a phrase
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    snippet: Union[Unset, str] = UNSET
    phrase: Union[Unset, str] = UNSET
    whole_word: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        snippet = self.snippet

        phrase = self.phrase

        whole_word = self.whole_word

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if phrase is not UNSET:
            field_dict["phrase"] = phrase
        if whole_word is not UNSET:
            field_dict["whole_word"] = whole_word

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

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

        snippet = d.pop("snippet", UNSET)

        phrase = d.pop("phrase", UNSET)

        whole_word = d.pop("whole_word", UNSET)

        text_snippet = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            snippet=snippet,
            phrase=phrase,
            whole_word=whole_word,
        )

        text_snippet.additional_properties = d
        return text_snippet

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
