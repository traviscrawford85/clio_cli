from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billable_matter_base import BillableMatterBase


T = TypeVar("T", bound="BillableClient")


@_attrs_define
class BillableClient:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *BillableClient*
        unbilled_hours (Union[Unset, float]): The unbilled hours of  the client
        unbilled_amount (Union[Unset, float]): The unbilled amount of the client
        amount_in_trust (Union[Unset, float]): The trust amount available for the client
        name (Union[Unset, str]): The name of the Client
        billable_matters_count (Union[Unset, int]): The total number of billable matters the client has
        billable_matters (Union[Unset, list['BillableMatterBase']]): BillableMatter
    """

    id: Union[Unset, int] = UNSET
    unbilled_hours: Union[Unset, float] = UNSET
    unbilled_amount: Union[Unset, float] = UNSET
    amount_in_trust: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    billable_matters_count: Union[Unset, int] = UNSET
    billable_matters: Union[Unset, list["BillableMatterBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        unbilled_hours = self.unbilled_hours

        unbilled_amount = self.unbilled_amount

        amount_in_trust = self.amount_in_trust

        name = self.name

        billable_matters_count = self.billable_matters_count

        billable_matters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billable_matters, Unset):
            billable_matters = []
            for billable_matters_item_data in self.billable_matters:
                billable_matters_item = billable_matters_item_data.to_dict()
                billable_matters.append(billable_matters_item)

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
        if billable_matters is not UNSET:
            field_dict["billable_matters"] = billable_matters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billable_matter_base import BillableMatterBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        unbilled_hours = d.pop("unbilled_hours", UNSET)

        unbilled_amount = d.pop("unbilled_amount", UNSET)

        amount_in_trust = d.pop("amount_in_trust", UNSET)

        name = d.pop("name", UNSET)

        billable_matters_count = d.pop("billable_matters_count", UNSET)

        billable_matters = []
        _billable_matters = d.pop("billable_matters", UNSET)
        for billable_matters_item_data in _billable_matters or []:
            billable_matters_item = BillableMatterBase.from_dict(billable_matters_item_data)

            billable_matters.append(billable_matters_item)

        billable_client = cls(
            id=id,
            unbilled_hours=unbilled_hours,
            unbilled_amount=unbilled_amount,
            amount_in_trust=amount_in_trust,
            name=name,
            billable_matters_count=billable_matters_count,
            billable_matters=billable_matters,
        )

        billable_client.additional_properties = d
        return billable_client

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
