from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityCalendarEntryBase")


@_attrs_define
class ActivityCalendarEntryBase:
    """
    Attributes:
        id (Union[Unset, str]): Unique identifier for the *CalendarEntry*
        etag (Union[Unset, str]): ETag for the *CalendarEntry*
        calendar_owner_id (Union[Unset, int]): The id of the calendar owner.
    """

    id: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    calendar_owner_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        calendar_owner_id = self.calendar_owner_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if calendar_owner_id is not UNSET:
            field_dict["calendar_owner_id"] = calendar_owner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        calendar_owner_id = d.pop("calendar_owner_id", UNSET)

        activity_calendar_entry_base = cls(
            id=id,
            etag=etag,
            calendar_owner_id=calendar_owner_id,
        )

        activity_calendar_entry_base.additional_properties = d
        return activity_calendar_entry_base

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
