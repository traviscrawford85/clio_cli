from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityRatecreateDataBodyData")


@_attrs_define
class ActivityRatecreateDataBodyData:
    """
    Attributes:
        co_counsel_contact_id (Union[Unset, int]): The unique identifier for a single Contact associated with the
            ActivityRate. The keyword `null` is not valid for this field.
        contact_id (Union[Unset, int]): The unique identifier for a single Contact associated with the ActivityRate. The
            keyword `null` is not valid for this field.
        flat_rate (Union[Unset, bool]): Whether this is a flat rate
        rate (Union[Unset, float]): Monetary value of this rate. Either hourly value or flat rate value
    """

    co_counsel_contact_id: Union[Unset, int] = UNSET
    contact_id: Union[Unset, int] = UNSET
    flat_rate: Union[Unset, bool] = UNSET
    rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        co_counsel_contact_id = self.co_counsel_contact_id

        contact_id = self.contact_id

        flat_rate = self.flat_rate

        rate = self.rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co_counsel_contact_id is not UNSET:
            field_dict["co_counsel_contact_id"] = co_counsel_contact_id
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if flat_rate is not UNSET:
            field_dict["flat_rate"] = flat_rate
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        co_counsel_contact_id = d.pop("co_counsel_contact_id", UNSET)

        contact_id = d.pop("contact_id", UNSET)

        flat_rate = d.pop("flat_rate", UNSET)

        rate = d.pop("rate", UNSET)

        activity_ratecreate_data_body_data = cls(
            co_counsel_contact_id=co_counsel_contact_id,
            contact_id=contact_id,
            flat_rate=flat_rate,
            rate=rate,
        )

        activity_ratecreate_data_body_data.additional_properties = d
        return activity_ratecreate_data_body_data

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
