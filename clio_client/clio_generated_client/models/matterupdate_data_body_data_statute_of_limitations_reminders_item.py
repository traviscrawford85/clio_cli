from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matterupdate_data_body_data_statute_of_limitations_reminders_item_notification_method import (
        MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod,
    )


T = TypeVar("T", bound="MatterupdateDataBodyDataStatuteOfLimitationsRemindersItem")


@_attrs_define
class MatterupdateDataBodyDataStatuteOfLimitationsRemindersItem:
    """
    Attributes:
        duration_value (Union[Unset, int]): Time measured in `duration_unit` to remind user before the subject.
        duration_unit (Union[Unset, str]): Unit to measure the duration value in.
        notification_method (Union[Unset, MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod]):
        id (Union[Unset, int]): The unique identifier for a single Reminder associated with the Matter. The keyword
            `null` is not valid for this field.
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated Reminder is present, the Reminder is deleted from the Matter.
    """

    duration_value: Union[Unset, int] = UNSET
    duration_unit: Union[Unset, str] = UNSET
    notification_method: Union[Unset, "MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod"] = (
        UNSET
    )
    id: Union[Unset, int] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_value = self.duration_value

        duration_unit = self.duration_unit

        notification_method: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notification_method, Unset):
            notification_method = self.notification_method.to_dict()

        id = self.id

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration_value is not UNSET:
            field_dict["duration_value"] = duration_value
        if duration_unit is not UNSET:
            field_dict["duration_unit"] = duration_unit
        if notification_method is not UNSET:
            field_dict["notification_method"] = notification_method
        if id is not UNSET:
            field_dict["id"] = id
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matterupdate_data_body_data_statute_of_limitations_reminders_item_notification_method import (
            MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod,
        )

        d = dict(src_dict)
        duration_value = d.pop("duration_value", UNSET)

        duration_unit = d.pop("duration_unit", UNSET)

        _notification_method = d.pop("notification_method", UNSET)
        notification_method: Union[Unset, MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod]
        if isinstance(_notification_method, Unset):
            notification_method = UNSET
        else:
            notification_method = MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod.from_dict(
                _notification_method
            )

        id = d.pop("id", UNSET)

        field_destroy = d.pop("_destroy", UNSET)

        matterupdate_data_body_data_statute_of_limitations_reminders_item = cls(
            duration_value=duration_value,
            duration_unit=duration_unit,
            notification_method=notification_method,
            id=id,
            field_destroy=field_destroy,
        )

        matterupdate_data_body_data_statute_of_limitations_reminders_item.additional_properties = d
        return matterupdate_data_body_data_statute_of_limitations_reminders_item

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
