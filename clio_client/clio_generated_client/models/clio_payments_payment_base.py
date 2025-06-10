import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.clio_payments_payment_base_state import ClioPaymentsPaymentBaseState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClioPaymentsPaymentBase")


@_attrs_define
class ClioPaymentsPaymentBase:
    """
    Attributes:
        amount (Union[Unset, float]): The amount of the payment.
        confirmation_number (Union[Unset, str]): The confirmation number of the payment.
        created_at (Union[Unset, datetime.datetime]): The time the *ClioPaymentsPayment* was created (as a ISO-8601
            timestamp)
        currency (Union[Unset, str]): The currency the payment was processed in.
        deposit_as_revenue (Union[Unset, bool]): Whether the payment was deposited as revenue.
        description (Union[Unset, str]): The description of the payment.
        email_address (Union[Unset, str]): The email address of the client.
        id (Union[Unset, int]): Unique identifier for the *ClioPaymentsPayment*
        state (Union[Unset, ClioPaymentsPaymentBaseState]): The state of the payment (authorized, completed, failed,
            etc).
        updated_at (Union[Unset, datetime.datetime]): The time the *ClioPaymentsPayment* was last updated (as a ISO-8601
            timestamp)
    """

    amount: Union[Unset, float] = UNSET
    confirmation_number: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    deposit_as_revenue: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    state: Union[Unset, ClioPaymentsPaymentBaseState] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        confirmation_number = self.confirmation_number

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        currency = self.currency

        deposit_as_revenue = self.deposit_as_revenue

        description = self.description

        email_address = self.email_address

        id = self.id

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if confirmation_number is not UNSET:
            field_dict["confirmation_number"] = confirmation_number
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if deposit_as_revenue is not UNSET:
            field_dict["deposit_as_revenue"] = deposit_as_revenue
        if description is not UNSET:
            field_dict["description"] = description
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        confirmation_number = d.pop("confirmation_number", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        currency = d.pop("currency", UNSET)

        deposit_as_revenue = d.pop("deposit_as_revenue", UNSET)

        description = d.pop("description", UNSET)

        email_address = d.pop("email_address", UNSET)

        id = d.pop("id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ClioPaymentsPaymentBaseState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ClioPaymentsPaymentBaseState(_state)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        clio_payments_payment_base = cls(
            amount=amount,
            confirmation_number=confirmation_number,
            created_at=created_at,
            currency=currency,
            deposit_as_revenue=deposit_as_revenue,
            description=description,
            email_address=email_address,
            id=id,
            state=state,
            updated_at=updated_at,
        )

        clio_payments_payment_base.additional_properties = d
        return clio_payments_payment_base

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
