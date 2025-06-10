from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_templatecreate_json_body_data_reminder_templates_item_notification_type import (
    TaskTemplatecreateJsonBodyDataReminderTemplatesItemNotificationType,
)

T = TypeVar("T", bound="TaskTemplatecreateJsonBodyDataReminderTemplatesItem")


@_attrs_define
class TaskTemplatecreateJsonBodyDataReminderTemplatesItem:
    """
    Attributes:
        duration_value (int): Time measured in `duration_unit` to remind user before the subject.
        duration_unit (str): Unit to measure the duration value in.
        notification_type (TaskTemplatecreateJsonBodyDataReminderTemplatesItemNotificationType): Notification method.
    """

    duration_value: int
    duration_unit: str
    notification_type: TaskTemplatecreateJsonBodyDataReminderTemplatesItemNotificationType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_value = self.duration_value

        duration_unit = self.duration_unit

        notification_type = self.notification_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration_value": duration_value,
                "duration_unit": duration_unit,
                "notification_type": notification_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration_value = d.pop("duration_value")

        duration_unit = d.pop("duration_unit")

        notification_type = TaskTemplatecreateJsonBodyDataReminderTemplatesItemNotificationType(
            d.pop("notification_type")
        )

        task_templatecreate_json_body_data_reminder_templates_item = cls(
            duration_value=duration_value,
            duration_unit=duration_unit,
            notification_type=notification_type,
        )

        task_templatecreate_json_body_data_reminder_templates_item.additional_properties = d
        return task_templatecreate_json_body_data_reminder_templates_item

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
