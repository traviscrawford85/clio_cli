import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.payment_profile_base_interest_type import PaymentProfileBaseInterestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentProfileBase")


@_attrs_define
class PaymentProfileBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *PaymentProfile*
        etag (Union[Unset, str]): ETag for the *PaymentProfile*
        created_at (Union[Unset, datetime.datetime]): The time the *PaymentProfile* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *PaymentProfile* was last updated (as a ISO-8601
            timestamp)
        billing_setting_id (Union[Unset, int]): The unique identifier for the *PaymentProfile
        name (Union[Unset, str]): The name of the *PaymentProfile
        terms (Union[Unset, int]): The total grace period for the *PaymentProfile
        discount_rate (Union[Unset, float]): The early payment discount rate for the *PaymentProfile
        discount_period (Union[Unset, int]): The early payment discount period for the *PaymentProfile
        interest_rate (Union[Unset, float]): The interest rate for the *PaymentProfile
        interest_period (Union[Unset, int]): The interest period interval for the *PaymentProfile
        interest_type (Union[Unset, PaymentProfileBaseInterestType]): The type of interest to be calculated for the
            *PaymentProfile (Simple or Compound)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    billing_setting_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    terms: Union[Unset, int] = UNSET
    discount_rate: Union[Unset, float] = UNSET
    discount_period: Union[Unset, int] = UNSET
    interest_rate: Union[Unset, float] = UNSET
    interest_period: Union[Unset, int] = UNSET
    interest_type: Union[Unset, PaymentProfileBaseInterestType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        billing_setting_id = self.billing_setting_id

        name = self.name

        terms = self.terms

        discount_rate = self.discount_rate

        discount_period = self.discount_period

        interest_rate = self.interest_rate

        interest_period = self.interest_period

        interest_type: Union[Unset, str] = UNSET
        if not isinstance(self.interest_type, Unset):
            interest_type = self.interest_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if billing_setting_id is not UNSET:
            field_dict["billing_setting_id"] = billing_setting_id
        if name is not UNSET:
            field_dict["name"] = name
        if terms is not UNSET:
            field_dict["terms"] = terms
        if discount_rate is not UNSET:
            field_dict["discount_rate"] = discount_rate
        if discount_period is not UNSET:
            field_dict["discount_period"] = discount_period
        if interest_rate is not UNSET:
            field_dict["interest_rate"] = interest_rate
        if interest_period is not UNSET:
            field_dict["interest_period"] = interest_period
        if interest_type is not UNSET:
            field_dict["interest_type"] = interest_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        billing_setting_id = d.pop("billing_setting_id", UNSET)

        name = d.pop("name", UNSET)

        terms = d.pop("terms", UNSET)

        discount_rate = d.pop("discount_rate", UNSET)

        discount_period = d.pop("discount_period", UNSET)

        interest_rate = d.pop("interest_rate", UNSET)

        interest_period = d.pop("interest_period", UNSET)

        _interest_type = d.pop("interest_type", UNSET)
        interest_type: Union[Unset, PaymentProfileBaseInterestType]
        if isinstance(_interest_type, Unset):
            interest_type = UNSET
        else:
            interest_type = PaymentProfileBaseInterestType(_interest_type)

        payment_profile_base = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            billing_setting_id=billing_setting_id,
            name=name,
            terms=terms,
            discount_rate=discount_rate,
            discount_period=discount_period,
            interest_rate=interest_rate,
            interest_period=interest_period,
            interest_type=interest_type,
        )

        payment_profile_base.additional_properties = d
        return payment_profile_base

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
