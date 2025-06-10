from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_description_rate_base_hierarchy import ActivityDescriptionRateBaseHierarchy
from ..models.activity_description_rate_base_type import ActivityDescriptionRateBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityDescriptionRateBase")


@_attrs_define
class ActivityDescriptionRateBase:
    """
    Attributes:
        amount (Union[Unset, float]): Monetary value of this rate. Either hourly value or flat rate value
        non_billable_amount (Union[Unset, float]): Monetary value of this rate for non billable activities. Either
            hourly value or flat rate value
        type_ (Union[Unset, ActivityDescriptionRateBaseType]): What kind of rate it is.
        hierarchy (Union[Unset, ActivityDescriptionRateBaseHierarchy]): What rate hierarchy the rate belongs to.
    """

    amount: Union[Unset, float] = UNSET
    non_billable_amount: Union[Unset, float] = UNSET
    type_: Union[Unset, ActivityDescriptionRateBaseType] = UNSET
    hierarchy: Union[Unset, ActivityDescriptionRateBaseHierarchy] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        non_billable_amount = self.non_billable_amount

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        hierarchy: Union[Unset, str] = UNSET
        if not isinstance(self.hierarchy, Unset):
            hierarchy = self.hierarchy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if non_billable_amount is not UNSET:
            field_dict["non_billable_amount"] = non_billable_amount
        if type_ is not UNSET:
            field_dict["type"] = type_
        if hierarchy is not UNSET:
            field_dict["hierarchy"] = hierarchy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        non_billable_amount = d.pop("non_billable_amount", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ActivityDescriptionRateBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ActivityDescriptionRateBaseType(_type_)

        _hierarchy = d.pop("hierarchy", UNSET)
        hierarchy: Union[Unset, ActivityDescriptionRateBaseHierarchy]
        if isinstance(_hierarchy, Unset):
            hierarchy = UNSET
        else:
            hierarchy = ActivityDescriptionRateBaseHierarchy(_hierarchy)

        activity_description_rate_base = cls(
            amount=amount,
            non_billable_amount=non_billable_amount,
            type_=type_,
            hierarchy=hierarchy,
        )

        activity_description_rate_base.additional_properties = d
        return activity_description_rate_base

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
