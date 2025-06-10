from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_descriptioncreate_json_body_data_rate_type import ActivityDescriptioncreateJsonBodyDataRateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityDescriptioncreateJsonBodyDataRate")


@_attrs_define
class ActivityDescriptioncreateJsonBodyDataRate:
    """
    Attributes:
        amount (Union[Unset, float]): The rate of the ActivityDescription. This is ignored for 'User' rates. Default:
            0.0.
        non_billable_amount (Union[Unset, float]): The non billable rate of the ActivityDescription. This is ignored for
            'User' rates. Default: 0.0.
        type_ (Union[Unset, ActivityDescriptioncreateJsonBodyDataRateType]): What kind of rate it will be.
    """

    amount: Union[Unset, float] = 0.0
    non_billable_amount: Union[Unset, float] = 0.0
    type_: Union[Unset, ActivityDescriptioncreateJsonBodyDataRateType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        non_billable_amount = self.non_billable_amount

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if non_billable_amount is not UNSET:
            field_dict["non_billable_amount"] = non_billable_amount
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        non_billable_amount = d.pop("non_billable_amount", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ActivityDescriptioncreateJsonBodyDataRateType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ActivityDescriptioncreateJsonBodyDataRateType(_type_)

        activity_descriptioncreate_json_body_data_rate = cls(
            amount=amount,
            non_billable_amount=non_billable_amount,
            type_=type_,
        )

        activity_descriptioncreate_json_body_data_rate.additional_properties = d
        return activity_descriptioncreate_json_body_data_rate

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
