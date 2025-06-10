from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mattercreate_data_body_data_statute_of_limitations_reminders_item_notification_method import (
        MattercreateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod,
    )


T = TypeVar("T", bound="MattercreateDataBodyDataStatuteOfLimitationsRemindersItem")


@_attrs_define
class MattercreateDataBodyDataStatuteOfLimitationsRemindersItem:
    """
    Attributes:
        duration_value (int): Time measured in `duration_unit` to remind user before the subject.
        duration_unit (str): Unit to measure the duration value in.
        notification_method (MattercreateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod):
    """

    duration_value: int
    duration_unit: str
    notification_method: "MattercreateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_value = self.duration_value

        duration_unit = self.duration_unit

        notification_method = self.notification_method.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration_value": duration_value,
                "duration_unit": duration_unit,
                "notification_method": notification_method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mattercreate_data_body_data_statute_of_limitations_reminders_item_notification_method import (
            MattercreateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod,
        )

        d = dict(src_dict)
        duration_value = d.pop("duration_value")

        duration_unit = d.pop("duration_unit")

        notification_method = MattercreateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod.from_dict(
            d.pop("notification_method")
        )

        mattercreate_data_body_data_statute_of_limitations_reminders_item = cls(
            duration_value=duration_value,
            duration_unit=duration_unit,
            notification_method=notification_method,
        )

        mattercreate_data_body_data_statute_of_limitations_reminders_item.additional_properties = d
        return mattercreate_data_body_data_statute_of_limitations_reminders_item

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
