from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MyEventupdateDataBodyData")


@_attrs_define
class MyEventupdateDataBodyData:
    """
    Attributes:
        marked_as_read (Union[Unset, bool]): Indicates whether the event notification should be marked as read by the
            current user. If `false` the event status is reset to unread.
    """

    marked_as_read: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        marked_as_read = self.marked_as_read

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if marked_as_read is not UNSET:
            field_dict["marked_as_read"] = marked_as_read

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        marked_as_read = d.pop("marked_as_read", UNSET)

        my_eventupdate_data_body_data = cls(
            marked_as_read=marked_as_read,
        )

        my_eventupdate_data_body_data.additional_properties = d
        return my_eventupdate_data_body_data

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
