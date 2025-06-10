from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.taskcreate_data_body_data_assignee_type import TaskcreateDataBodyDataAssigneeType

T = TypeVar("T", bound="TaskcreateDataBodyDataAssignee")


@_attrs_define
class TaskcreateDataBodyDataAssignee:
    """
    Attributes:
        id (int): The unique identifier for a single User or Contact associated with the Task. The keyword `null` is not
            valid for this field.
        type_ (TaskcreateDataBodyDataAssigneeType): Model type of the assignee.
    """

    id: int
    type_: TaskcreateDataBodyDataAssigneeType
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

        type_ = TaskcreateDataBodyDataAssigneeType(d.pop("type"))

        taskcreate_data_body_data_assignee = cls(
            id=id,
            type_=type_,
        )

        taskcreate_data_body_data_assignee.additional_properties = d
        return taskcreate_data_body_data_assignee

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
