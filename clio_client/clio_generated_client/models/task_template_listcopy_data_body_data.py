from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_template_listcopy_data_body_data_practice_area import (
        TaskTemplateListcopyDataBodyDataPracticeArea,
    )


T = TypeVar("T", bound="TaskTemplateListcopyDataBodyData")


@_attrs_define
class TaskTemplateListcopyDataBodyData:
    """
    Attributes:
        description (Union[Unset, str]): The description of the TaskTemplateList copy.
        name (Union[Unset, str]): The name of the TaskTemplateList copy.
        practice_area (Union[Unset, TaskTemplateListcopyDataBodyDataPracticeArea]):
    """

    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    practice_area: Union[Unset, "TaskTemplateListcopyDataBodyDataPracticeArea"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        practice_area: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.practice_area, Unset):
            practice_area = self.practice_area.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if practice_area is not UNSET:
            field_dict["practice_area"] = practice_area

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_template_listcopy_data_body_data_practice_area import (
            TaskTemplateListcopyDataBodyDataPracticeArea,
        )

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        _practice_area = d.pop("practice_area", UNSET)
        practice_area: Union[Unset, TaskTemplateListcopyDataBodyDataPracticeArea]
        if isinstance(_practice_area, Unset):
            practice_area = UNSET
        else:
            practice_area = TaskTemplateListcopyDataBodyDataPracticeArea.from_dict(_practice_area)

        task_template_listcopy_data_body_data = cls(
            description=description,
            name=name,
            practice_area=practice_area,
        )

        task_template_listcopy_data_body_data.additional_properties = d
        return task_template_listcopy_data_body_data

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
