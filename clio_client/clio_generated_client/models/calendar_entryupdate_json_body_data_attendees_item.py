from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarEntryupdateJsonBodyDataAttendeesItem")


@_attrs_define
class CalendarEntryupdateJsonBodyDataAttendeesItem:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier for a single Attendee associated with the CalendarEntry. The
            keyword `null` is not valid for this field. Not required for creating new Attendee, but required for updating or
            deleting existing ones.
        type_ (Union[Unset, str]): The type of attendee (Calendar, Contact)
        field_destroy (Union[Unset, bool]): Flag to delete a specific attendee.
    """

    id: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        field_destroy = d.pop("_destroy", UNSET)

        calendar_entryupdate_json_body_data_attendees_item = cls(
            id=id,
            type_=type_,
            field_destroy=field_destroy,
        )

        calendar_entryupdate_json_body_data_attendees_item.additional_properties = d
        return calendar_entryupdate_json_body_data_attendees_item

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
