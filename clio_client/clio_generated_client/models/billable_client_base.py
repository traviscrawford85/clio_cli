from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillableClientBase")


@_attrs_define
class BillableClientBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *BillableClient*
        unbilled_hours (Union[Unset, float]): The unbilled hours of  the client
        unbilled_amount (Union[Unset, float]): The unbilled amount of the client
        amount_in_trust (Union[Unset, float]): The trust amount available for the client
        name (Union[Unset, str]): The name of the Client
        billable_matters_count (Union[Unset, int]): The total number of billable matters the client has
    """

    id: Union[Unset, int] = UNSET
    unbilled_hours: Union[Unset, float] = UNSET
    unbilled_amount: Union[Unset, float] = UNSET
    amount_in_trust: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    billable_matters_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        unbilled_hours = self.unbilled_hours

        unbilled_amount = self.unbilled_amount

        amount_in_trust = self.amount_in_trust

        name = self.name

        billable_matters_count = self.billable_matters_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if unbilled_hours is not UNSET:
            field_dict["unbilled_hours"] = unbilled_hours
        if unbilled_amount is not UNSET:
            field_dict["unbilled_amount"] = unbilled_amount
        if amount_in_trust is not UNSET:
            field_dict["amount_in_trust"] = amount_in_trust
        if name is not UNSET:
            field_dict["name"] = name
        if billable_matters_count is not UNSET:
            field_dict["billable_matters_count"] = billable_matters_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        unbilled_hours = d.pop("unbilled_hours", UNSET)

        unbilled_amount = d.pop("unbilled_amount", UNSET)

        amount_in_trust = d.pop("amount_in_trust", UNSET)

        name = d.pop("name", UNSET)

        billable_matters_count = d.pop("billable_matters_count", UNSET)

        billable_client_base = cls(
            id=id,
            unbilled_hours=unbilled_hours,
            unbilled_amount=unbilled_amount,
            amount_in_trust=amount_in_trust,
            name=name,
            billable_matters_count=billable_matters_count,
        )

        billable_client_base.additional_properties = d
        return billable_client_base

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
