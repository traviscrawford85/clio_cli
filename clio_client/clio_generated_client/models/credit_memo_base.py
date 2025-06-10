import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditMemoBase")


@_attrs_define
class CreditMemoBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *CreditMemo*
        etag (Union[Unset, str]): ETag for the *CreditMemo*
        date (Union[Unset, datetime.date]): Date the *CreditMemo* was recorded (as a ISO-8601 date)
        amount (Union[Unset, float]): Total amount credited
        description (Union[Unset, str]): A detailed description for the *CreditMemo*
        discount (Union[Unset, bool]): Whether the *CreditMemo* is applied as discount
        voided_at (Union[Unset, datetime.datetime]): Time the *CreditMemo* was voided (as a ISO-8601 timestamp)
        created_at (Union[Unset, datetime.datetime]): The time the *CreditMemo* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *CreditMemo* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    amount: Union[Unset, float] = UNSET
    description: Union[Unset, str] = UNSET
    discount: Union[Unset, bool] = UNSET
    voided_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        amount = self.amount

        description = self.description

        discount = self.discount

        voided_at: Union[Unset, str] = UNSET
        if not isinstance(self.voided_at, Unset):
            voided_at = self.voided_at.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if date is not UNSET:
            field_dict["date"] = date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if description is not UNSET:
            field_dict["description"] = description
        if discount is not UNSET:
            field_dict["discount"] = discount
        if voided_at is not UNSET:
            field_dict["voided_at"] = voided_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        amount = d.pop("amount", UNSET)

        description = d.pop("description", UNSET)

        discount = d.pop("discount", UNSET)

        _voided_at = d.pop("voided_at", UNSET)
        voided_at: Union[Unset, datetime.datetime]
        if isinstance(_voided_at, Unset):
            voided_at = UNSET
        else:
            voided_at = isoparse(_voided_at)

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

        credit_memo_base = cls(
            id=id,
            etag=etag,
            date=date,
            amount=amount,
            description=description,
            discount=discount,
            voided_at=voided_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        credit_memo_base.additional_properties = d
        return credit_memo_base

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
