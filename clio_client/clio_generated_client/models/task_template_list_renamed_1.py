import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.practice_area_base import PracticeAreaBase
    from ..models.user_base import UserBase


T = TypeVar("T", bound="TaskTemplateListRenamed1")


@_attrs_define
class TaskTemplateListRenamed1:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]): The time the *TaskTemplateList* was created (as a ISO-8601
            timestamp)
        description (Union[Unset, str]): A detailed description of the *TaskTemplateList*
        id (Union[Unset, int]): Unique identifier for the *TaskTemplateList*
        etag (Union[Unset, str]): ETag for the *TaskTemplateList*
        name (Union[Unset, str]): The name of the *TaskTemplateList*
        templates_count (Union[Unset, int]): How many task templates exist as an association to the *TaskTemplateList*
        updated_at (Union[Unset, datetime.datetime]): The time the *TaskTemplateList* was last updated (as a ISO-8601
            timestamp)
        practice_area (Union[Unset, PracticeAreaBase]):
        creator (Union[Unset, UserBase]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    templates_count: Union[Unset, int] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    practice_area: Union[Unset, "PracticeAreaBase"] = UNSET
    creator: Union[Unset, "UserBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description

        id = self.id

        etag = self.etag

        name = self.name

        templates_count = self.templates_count

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        practice_area: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.practice_area, Unset):
            practice_area = self.practice_area.to_dict()

        creator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if templates_count is not UNSET:
            field_dict["templates_count"] = templates_count
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if practice_area is not UNSET:
            field_dict["practice_area"] = practice_area
        if creator is not UNSET:
            field_dict["creator"] = creator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.practice_area_base import PracticeAreaBase
        from ..models.user_base import UserBase

        d = dict(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        templates_count = d.pop("templates_count", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _practice_area = d.pop("practice_area", UNSET)
        practice_area: Union[Unset, PracticeAreaBase]
        if isinstance(_practice_area, Unset):
            practice_area = UNSET
        else:
            practice_area = PracticeAreaBase.from_dict(_practice_area)

        _creator = d.pop("creator", UNSET)
        creator: Union[Unset, UserBase]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = UserBase.from_dict(_creator)

        task_template_list_renamed_1 = cls(
            created_at=created_at,
            description=description,
            id=id,
            etag=etag,
            name=name,
            templates_count=templates_count,
            updated_at=updated_at,
            practice_area=practice_area,
            creator=creator,
        )

        task_template_list_renamed_1.additional_properties = d
        return task_template_list_renamed_1

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
