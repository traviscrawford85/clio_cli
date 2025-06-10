import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matterupdate_files_body_data_task_template_list_instances_item_task_template_list import (
        MatterupdateFilesBodyDataTaskTemplateListInstancesItemTaskTemplateList,
    )


T = TypeVar("T", bound="MatterupdateFilesBodyDataTaskTemplateListInstancesItem")


@_attrs_define
class MatterupdateFilesBodyDataTaskTemplateListInstancesItem:
    """
    Attributes:
        task_template_list (Union[Unset, MatterupdateFilesBodyDataTaskTemplateListInstancesItemTaskTemplateList]):
        assignee_id (Union[Unset, int]): The id of the user to assign the task template list to.
        notify_assignees (Union[Unset, bool]): Whether or not task list assignees should be notified when the task list
            is assigned to a matter.
        due_at (Union[Unset, datetime.date]): Due date of the tasks. (Expects an ISO-8601 date).
    """

    task_template_list: Union[Unset, "MatterupdateFilesBodyDataTaskTemplateListInstancesItemTaskTemplateList"] = UNSET
    assignee_id: Union[Unset, int] = UNSET
    notify_assignees: Union[Unset, bool] = UNSET
    due_at: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_template_list: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.task_template_list, Unset):
            task_template_list = self.task_template_list.to_dict()

        assignee_id = self.assignee_id

        notify_assignees = self.notify_assignees

        due_at: Union[Unset, str] = UNSET
        if not isinstance(self.due_at, Unset):
            due_at = self.due_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_template_list is not UNSET:
            field_dict["task_template_list"] = task_template_list
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id
        if notify_assignees is not UNSET:
            field_dict["notify_assignees"] = notify_assignees
        if due_at is not UNSET:
            field_dict["due_at"] = due_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matterupdate_files_body_data_task_template_list_instances_item_task_template_list import (
            MatterupdateFilesBodyDataTaskTemplateListInstancesItemTaskTemplateList,
        )

        d = dict(src_dict)
        _task_template_list = d.pop("task_template_list", UNSET)
        task_template_list: Union[Unset, MatterupdateFilesBodyDataTaskTemplateListInstancesItemTaskTemplateList]
        if isinstance(_task_template_list, Unset):
            task_template_list = UNSET
        else:
            task_template_list = MatterupdateFilesBodyDataTaskTemplateListInstancesItemTaskTemplateList.from_dict(
                _task_template_list
            )

        assignee_id = d.pop("assignee_id", UNSET)

        notify_assignees = d.pop("notify_assignees", UNSET)

        _due_at = d.pop("due_at", UNSET)
        due_at: Union[Unset, datetime.date]
        if isinstance(_due_at, Unset):
            due_at = UNSET
        else:
            due_at = isoparse(_due_at).date()

        matterupdate_files_body_data_task_template_list_instances_item = cls(
            task_template_list=task_template_list,
            assignee_id=assignee_id,
            notify_assignees=notify_assignees,
            due_at=due_at,
        )

        matterupdate_files_body_data_task_template_list_instances_item.additional_properties = d
        return matterupdate_files_body_data_task_template_list_instances_item

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
