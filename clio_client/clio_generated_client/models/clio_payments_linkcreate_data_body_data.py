from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clio_payments_linkcreate_data_body_data_destination_account import (
        ClioPaymentsLinkcreateDataBodyDataDestinationAccount,
    )
    from ..models.clio_payments_linkcreate_data_body_data_destination_contact import (
        ClioPaymentsLinkcreateDataBodyDataDestinationContact,
    )
    from ..models.clio_payments_linkcreate_data_body_data_subject import ClioPaymentsLinkcreateDataBodyDataSubject


T = TypeVar("T", bound="ClioPaymentsLinkcreateDataBodyData")


@_attrs_define
class ClioPaymentsLinkcreateDataBodyData:
    """
    Attributes:
        currency (str): The currency the payment will be processed in. The supported currency depends on the account's
            location ('USD' for a US account). The currency must be a valid ISO 4217 currency code.
        description (str): Only applicable for a direct payment. A short description of the purpose of the payment. Max
            255 characters.
        destination_account (ClioPaymentsLinkcreateDataBodyDataDestinationAccount):
        duration (int): The amount of time, in seconds, that the payment link will be active for. The maximum allowed
            value is '7776000' (90 days in seconds).
        subject (ClioPaymentsLinkcreateDataBodyDataSubject):
        amount (Union[Unset, float]): The amount to be paid. If not provided, the client will be able to specify an
            amount.
        destination_contact (Union[Unset, ClioPaymentsLinkcreateDataBodyDataDestinationContact]):
        email_address (Union[Unset, str]): Pre-fills the relevant field for the client when filling out their details in
            the payment link.
        is_allocated_as_revenue (Union[Unset, bool]): Only applicable for a direct payment. If true, the payment will be
            allocated as revenue. If false, the payment will be collected as an unallocated balance. Payments into trust can
            not be allocated as revenue. Defaults to false.
    """

    currency: str
    description: str
    destination_account: "ClioPaymentsLinkcreateDataBodyDataDestinationAccount"
    duration: int
    subject: "ClioPaymentsLinkcreateDataBodyDataSubject"
    amount: Union[Unset, float] = UNSET
    destination_contact: Union[Unset, "ClioPaymentsLinkcreateDataBodyDataDestinationContact"] = UNSET
    email_address: Union[Unset, str] = UNSET
    is_allocated_as_revenue: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        description = self.description

        destination_account = self.destination_account.to_dict()

        duration = self.duration

        subject = self.subject.to_dict()

        amount = self.amount

        destination_contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination_contact, Unset):
            destination_contact = self.destination_contact.to_dict()

        email_address = self.email_address

        is_allocated_as_revenue = self.is_allocated_as_revenue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "description": description,
                "destination_account": destination_account,
                "duration": duration,
                "subject": subject,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if destination_contact is not UNSET:
            field_dict["destination_contact"] = destination_contact
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if is_allocated_as_revenue is not UNSET:
            field_dict["is_allocated_as_revenue"] = is_allocated_as_revenue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clio_payments_linkcreate_data_body_data_destination_account import (
            ClioPaymentsLinkcreateDataBodyDataDestinationAccount,
        )
        from ..models.clio_payments_linkcreate_data_body_data_destination_contact import (
            ClioPaymentsLinkcreateDataBodyDataDestinationContact,
        )
        from ..models.clio_payments_linkcreate_data_body_data_subject import ClioPaymentsLinkcreateDataBodyDataSubject

        d = dict(src_dict)
        currency = d.pop("currency")

        description = d.pop("description")

        destination_account = ClioPaymentsLinkcreateDataBodyDataDestinationAccount.from_dict(
            d.pop("destination_account")
        )

        duration = d.pop("duration")

        subject = ClioPaymentsLinkcreateDataBodyDataSubject.from_dict(d.pop("subject"))

        amount = d.pop("amount", UNSET)

        _destination_contact = d.pop("destination_contact", UNSET)
        destination_contact: Union[Unset, ClioPaymentsLinkcreateDataBodyDataDestinationContact]
        if isinstance(_destination_contact, Unset):
            destination_contact = UNSET
        else:
            destination_contact = ClioPaymentsLinkcreateDataBodyDataDestinationContact.from_dict(_destination_contact)

        email_address = d.pop("email_address", UNSET)

        is_allocated_as_revenue = d.pop("is_allocated_as_revenue", UNSET)

        clio_payments_linkcreate_data_body_data = cls(
            currency=currency,
            description=description,
            destination_account=destination_account,
            duration=duration,
            subject=subject,
            amount=amount,
            destination_contact=destination_contact,
            email_address=email_address,
            is_allocated_as_revenue=is_allocated_as_revenue,
        )

        clio_payments_linkcreate_data_body_data.additional_properties = d
        return clio_payments_linkcreate_data_body_data

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
