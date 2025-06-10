from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_templateupdate_data_body_data_reminder_templates_item_notification_type import (
    TaskTemplateupdateDataBodyDataReminderTemplatesItemNotificationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskTemplateupdateDataBodyDataReminderTemplatesItem")


@_attrs_define
class TaskTemplateupdateDataBodyDataReminderTemplatesItem:
    """
    Attributes:
        duration_value (Union[Unset, int]): Time measured in `duration_unit` to remind user before the subject.
        duration_unit (Union[Unset, str]): Unit to measure the duration value in.
        notification_type (Union[Unset, TaskTemplateupdateDataBodyDataReminderTemplatesItemNotificationType]):
            Notification method.
        id (Union[Unset, int]): The unique identifier for a single ReminderTemplate associated with the TaskTemplate.
            The keyword `null` is not valid for this field.
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated ReminderTemplate is present, the ReminderTemplate is deleted from the TaskTemplate.
    """

    duration_value: Union[Unset, int] = UNSET
    duration_unit: Union[Unset, str] = UNSET
    notification_type: Union[Unset, TaskTemplateupdateDataBodyDataReminderTemplatesItemNotificationType] = UNSET
    id: Union[Unset, int] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_value = self.duration_value

        duration_unit = self.duration_unit

        notification_type: Union[Unset, str] = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type.value

        id = self.id

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration_value is not UNSET:
            field_dict["duration_value"] = duration_value
        if duration_unit is not UNSET:
            field_dict["duration_unit"] = duration_unit
        if notification_type is not UNSET:
            field_dict["notification_type"] = notification_type
        if id is not UNSET:
            field_dict["id"] = id
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration_value = d.pop("duration_value", UNSET)

        duration_unit = d.pop("duration_unit", UNSET)

        _notification_type = d.pop("notification_type", UNSET)
        notification_type: Union[Unset, TaskTemplateupdateDataBodyDataReminderTemplatesItemNotificationType]
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = TaskTemplateupdateDataBodyDataReminderTemplatesItemNotificationType(_notification_type)

        id = d.pop("id", UNSET)

        field_destroy = d.pop("_destroy", UNSET)

        task_templateupdate_data_body_data_reminder_templates_item = cls(
            duration_value=duration_value,
            duration_unit=duration_unit,
            notification_type=notification_type,
            id=id,
            field_destroy=field_destroy,
        )

        task_templateupdate_data_body_data_reminder_templates_item.additional_properties = d
        return task_templateupdate_data_body_data_reminder_templates_item

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
