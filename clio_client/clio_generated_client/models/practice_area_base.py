import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.practice_area_base_category import PracticeAreaBaseCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="PracticeAreaBase")


@_attrs_define
class PracticeAreaBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *PracticeArea*
        etag (Union[Unset, str]): ETag for the *PracticeArea*
        created_at (Union[Unset, datetime.datetime]): The time the *PracticeArea* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *PracticeArea* was last updated (as a ISO-8601
            timestamp)
        name (Union[Unset, str]): The name of the *PracticeArea*
        category (Union[Unset, PracticeAreaBaseCategory]): The practice area category associated with the *PracticeArea*
        code (Union[Unset, str]): The code of the *PracticeArea*
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    category: Union[Unset, PracticeAreaBaseCategory] = UNSET
    code: Union[Unset, str] = UNSET
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

        name = self.name

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        code = self.code

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
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if code is not UNSET:
            field_dict["code"] = code

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

        name = d.pop("name", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, PracticeAreaBaseCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = PracticeAreaBaseCategory(_category)

        code = d.pop("code", UNSET)

        practice_area_base = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            category=category,
            code=code,
        )

        practice_area_base.additional_properties = d
        return practice_area_base

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
