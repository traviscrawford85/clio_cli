from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.taskupdate_json_body_data_assignee_type import TaskupdateJsonBodyDataAssigneeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskupdateJsonBodyDataAssignee")


@_attrs_define
class TaskupdateJsonBodyDataAssignee:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier for a single User or Contact associated with the Task. The keyword
            `null` is not valid for this field.
        type_ (Union[Unset, TaskupdateJsonBodyDataAssigneeType]): Model type of the assignee.
    """

    id: Union[Unset, int] = UNSET
    type_: Union[Unset, TaskupdateJsonBodyDataAssigneeType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, TaskupdateJsonBodyDataAssigneeType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TaskupdateJsonBodyDataAssigneeType(_type_)

        taskupdate_json_body_data_assignee = cls(
            id=id,
            type_=type_,
        )

        taskupdate_json_body_data_assignee.additional_properties = d
        return taskupdate_json_body_data_assignee

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
