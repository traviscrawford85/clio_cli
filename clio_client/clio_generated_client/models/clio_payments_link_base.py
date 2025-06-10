import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClioPaymentsLinkBase")


@_attrs_define
class ClioPaymentsLinkBase:
    """
    Attributes:
        active (Union[Unset, bool]): Whether or not the payment link is active.
        amount (Union[Unset, float]): The defined amount of the payment link, if set.
        created_at (Union[Unset, datetime.datetime]): The time the *ClioPaymentsLink* was created (as a ISO-8601
            timestamp)
        currency (Union[Unset, str]): The currency the payment link will collect.
        description (Union[Unset, str]): The defined description of the payment link, if set.
        email_address (Union[Unset, str]): The email address to pre-fill the field on the the payment link, if set.
        etag (Union[Unset, str]): ETag for the *ClioPaymentsLink*
        expires_at (Union[Unset, datetime.datetime]): The ISO 8601 date and time the payment link will expire.
        id (Union[Unset, int]): Unique identifier for the *ClioPaymentsLink*
        is_allocated_as_revenue (Union[Unset, bool]): Whether the payment link is allocated as revenue.
        redirect_url (Union[Unset, str]): The URL to redirect the client to after the payment has been made.
        url (Union[Unset, str]): The URL of the payment link.
    """

    active: Union[Unset, bool] = UNSET
    amount: Union[Unset, float] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    expires_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    is_allocated_as_revenue: Union[Unset, bool] = UNSET
    redirect_url: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        amount = self.amount

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        currency = self.currency

        description = self.description

        email_address = self.email_address

        etag = self.etag

        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        id = self.id

        is_allocated_as_revenue = self.is_allocated_as_revenue

        redirect_url = self.redirect_url

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if description is not UNSET:
            field_dict["description"] = description
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if etag is not UNSET:
            field_dict["etag"] = etag
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if is_allocated_as_revenue is not UNSET:
            field_dict["is_allocated_as_revenue"] = is_allocated_as_revenue
        if redirect_url is not UNSET:
            field_dict["redirect_url"] = redirect_url
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        amount = d.pop("amount", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        currency = d.pop("currency", UNSET)

        description = d.pop("description", UNSET)

        email_address = d.pop("email_address", UNSET)

        etag = d.pop("etag", UNSET)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        id = d.pop("id", UNSET)

        is_allocated_as_revenue = d.pop("is_allocated_as_revenue", UNSET)

        redirect_url = d.pop("redirect_url", UNSET)

        url = d.pop("url", UNSET)

        clio_payments_link_base = cls(
            active=active,
            amount=amount,
            created_at=created_at,
            currency=currency,
            description=description,
            email_address=email_address,
            etag=etag,
            expires_at=expires_at,
            id=id,
            is_allocated_as_revenue=is_allocated_as_revenue,
            redirect_url=redirect_url,
            url=url,
        )

        clio_payments_link_base.additional_properties = d
        return clio_payments_link_base

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
