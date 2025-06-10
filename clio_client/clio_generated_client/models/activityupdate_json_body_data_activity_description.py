from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityupdateJsonBodyDataActivityDescription")


@_attrs_define
class ActivityupdateJsonBodyDataActivityDescription:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier for a single ActivityDescription associated with the Activity. The
            keyword `null` is not valid for this field.
        utbms_task_id (Union[Unset, int]): The unique identifier for a single UtbmsTask associated with the Activity.
            The keyword `null` is not valid for this field.
        utbms_activity_id (Union[Unset, int]): The unique identifier for a single UtbmsActivity associated with the
            Activity. The keyword `null` is not valid for this field.
    """

    id: Union[Unset, int] = UNSET
    utbms_task_id: Union[Unset, int] = UNSET
    utbms_activity_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        utbms_task_id = self.utbms_task_id

        utbms_activity_id = self.utbms_activity_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if utbms_task_id is not UNSET:
            field_dict["utbms_task_id"] = utbms_task_id
        if utbms_activity_id is not UNSET:
            field_dict["utbms_activity_id"] = utbms_activity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        utbms_task_id = d.pop("utbms_task_id", UNSET)

        utbms_activity_id = d.pop("utbms_activity_id", UNSET)

        activityupdate_json_body_data_activity_description = cls(
            id=id,
            utbms_task_id=utbms_task_id,
            utbms_activity_id=utbms_activity_id,
        )

        activityupdate_json_body_data_activity_description.additional_properties = d
        return activityupdate_json_body_data_activity_description

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
