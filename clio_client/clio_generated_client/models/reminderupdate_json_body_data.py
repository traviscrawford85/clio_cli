from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reminderupdate_json_body_data_duration_unit import ReminderupdateJsonBodyDataDurationUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reminderupdate_json_body_data_notification_method import ReminderupdateJsonBodyDataNotificationMethod


T = TypeVar("T", bound="ReminderupdateJsonBodyData")


@_attrs_define
class ReminderupdateJsonBodyData:
    """
    Attributes:
        duration_unit (Union[Unset, ReminderupdateJsonBodyDataDurationUnit]): Unit to measure the duration value in.
        duration_value (Union[Unset, int]): Time measured in `duration_unit` to remind user before the subject.
        notification_method (Union[Unset, ReminderupdateJsonBodyDataNotificationMethod]):
    """

    duration_unit: Union[Unset, ReminderupdateJsonBodyDataDurationUnit] = UNSET
    duration_value: Union[Unset, int] = UNSET
    notification_method: Union[Unset, "ReminderupdateJsonBodyDataNotificationMethod"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_unit: Union[Unset, str] = UNSET
        if not isinstance(self.duration_unit, Unset):
            duration_unit = self.duration_unit.value

        duration_value = self.duration_value

        notification_method: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notification_method, Unset):
            notification_method = self.notification_method.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration_unit is not UNSET:
            field_dict["duration_unit"] = duration_unit
        if duration_value is not UNSET:
            field_dict["duration_value"] = duration_value
        if notification_method is not UNSET:
            field_dict["notification_method"] = notification_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reminderupdate_json_body_data_notification_method import (
            ReminderupdateJsonBodyDataNotificationMethod,
        )

        d = dict(src_dict)
        _duration_unit = d.pop("duration_unit", UNSET)
        duration_unit: Union[Unset, ReminderupdateJsonBodyDataDurationUnit]
        if isinstance(_duration_unit, Unset):
            duration_unit = UNSET
        else:
            duration_unit = ReminderupdateJsonBodyDataDurationUnit(_duration_unit)

        duration_value = d.pop("duration_value", UNSET)

        _notification_method = d.pop("notification_method", UNSET)
        notification_method: Union[Unset, ReminderupdateJsonBodyDataNotificationMethod]
        if isinstance(_notification_method, Unset):
            notification_method = UNSET
        else:
            notification_method = ReminderupdateJsonBodyDataNotificationMethod.from_dict(_notification_method)

        reminderupdate_json_body_data = cls(
            duration_unit=duration_unit,
            duration_value=duration_value,
            notification_method=notification_method,
        )

        reminderupdate_json_body_data.additional_properties = d
        return reminderupdate_json_body_data

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
