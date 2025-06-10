from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.timercreate_data_body_data_activity import TimercreateDataBodyDataActivity


T = TypeVar("T", bound="TimercreateDataBodyData")


@_attrs_define
class TimercreateDataBodyData:
    """
    Attributes:
        activity (TimercreateDataBodyDataActivity):
    """

    activity: "TimercreateDataBodyDataActivity"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity = self.activity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activity": activity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timercreate_data_body_data_activity import TimercreateDataBodyDataActivity

        d = dict(src_dict)
        activity = TimercreateDataBodyDataActivity.from_dict(d.pop("activity"))

        timercreate_data_body_data = cls(
            activity=activity,
        )

        timercreate_data_body_data.additional_properties = d
        return timercreate_data_body_data

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
