import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LaukCriminalControlledRate")


@_attrs_define
class LaukCriminalControlledRate:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *LaukCriminalControlledRate*
        activity (Union[Unset, str]): Activity of the *LaukCriminalControlledRate*
        activity_type (Union[Unset, str]): Activity type
        category_of_law (Union[Unset, str]): Category of law
        counsel (Union[Unset, str]): Associated counsel
        court (Union[Unset, str]): Court associated
        created_at (Union[Unset, datetime.datetime]): The time the *LaukCriminalControlledRate* was created (as a
            ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *LaukCriminalControlledRate*
        exceptional (Union[Unset, float]): Fee applied for high activity count
        fee (Union[Unset, float]): Fee amount
        fee_scheme (Union[Unset, str]): Fee scheme
        post_nov_24_exceptional (Union[Unset, float]): Post-Nov 24 exceptional fee
        post_nov_24_fee (Union[Unset, float]): Post-Nov 24 fee amount
        post_sept_22_exceptional (Union[Unset, float]): Post-Sept 22 exceptional fee
        post_sept_22_fee (Union[Unset, float]): Post-Sept 22 fee amount
        key (Union[Unset, str]): Unique key
        rate_type (Union[Unset, str]): Rate type
        region (Union[Unset, str]): Region
        solicitor_type (Union[Unset, str]): Solicitor type
        updated_at (Union[Unset, datetime.datetime]): The time the *LaukCriminalControlledRate* was last updated (as a
            ISO-8601 timestamp)
    """

    id: Union[Unset, int] = UNSET
    activity: Union[Unset, str] = UNSET
    activity_type: Union[Unset, str] = UNSET
    category_of_law: Union[Unset, str] = UNSET
    counsel: Union[Unset, str] = UNSET
    court: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    etag: Union[Unset, str] = UNSET
    exceptional: Union[Unset, float] = UNSET
    fee: Union[Unset, float] = UNSET
    fee_scheme: Union[Unset, str] = UNSET
    post_nov_24_exceptional: Union[Unset, float] = UNSET
    post_nov_24_fee: Union[Unset, float] = UNSET
    post_sept_22_exceptional: Union[Unset, float] = UNSET
    post_sept_22_fee: Union[Unset, float] = UNSET
    key: Union[Unset, str] = UNSET
    rate_type: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    solicitor_type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        activity = self.activity

        activity_type = self.activity_type

        category_of_law = self.category_of_law

        counsel = self.counsel

        court = self.court

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        etag = self.etag

        exceptional = self.exceptional

        fee = self.fee

        fee_scheme = self.fee_scheme

        post_nov_24_exceptional = self.post_nov_24_exceptional

        post_nov_24_fee = self.post_nov_24_fee

        post_sept_22_exceptional = self.post_sept_22_exceptional

        post_sept_22_fee = self.post_sept_22_fee

        key = self.key

        rate_type = self.rate_type

        region = self.region

        solicitor_type = self.solicitor_type

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if activity is not UNSET:
            field_dict["activity"] = activity
        if activity_type is not UNSET:
            field_dict["activity_type"] = activity_type
        if category_of_law is not UNSET:
            field_dict["category_of_law"] = category_of_law
        if counsel is not UNSET:
            field_dict["counsel"] = counsel
        if court is not UNSET:
            field_dict["court"] = court
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if exceptional is not UNSET:
            field_dict["exceptional"] = exceptional
        if fee is not UNSET:
            field_dict["fee"] = fee
        if fee_scheme is not UNSET:
            field_dict["fee_scheme"] = fee_scheme
        if post_nov_24_exceptional is not UNSET:
            field_dict["post_nov_24_exceptional"] = post_nov_24_exceptional
        if post_nov_24_fee is not UNSET:
            field_dict["post_nov_24_fee"] = post_nov_24_fee
        if post_sept_22_exceptional is not UNSET:
            field_dict["post_sept_22_exceptional"] = post_sept_22_exceptional
        if post_sept_22_fee is not UNSET:
            field_dict["post_sept_22_fee"] = post_sept_22_fee
        if key is not UNSET:
            field_dict["key"] = key
        if rate_type is not UNSET:
            field_dict["rate_type"] = rate_type
        if region is not UNSET:
            field_dict["region"] = region
        if solicitor_type is not UNSET:
            field_dict["solicitor_type"] = solicitor_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        activity = d.pop("activity", UNSET)

        activity_type = d.pop("activity_type", UNSET)

        category_of_law = d.pop("category_of_law", UNSET)

        counsel = d.pop("counsel", UNSET)

        court = d.pop("court", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        etag = d.pop("etag", UNSET)

        exceptional = d.pop("exceptional", UNSET)

        fee = d.pop("fee", UNSET)

        fee_scheme = d.pop("fee_scheme", UNSET)

        post_nov_24_exceptional = d.pop("post_nov_24_exceptional", UNSET)

        post_nov_24_fee = d.pop("post_nov_24_fee", UNSET)

        post_sept_22_exceptional = d.pop("post_sept_22_exceptional", UNSET)

        post_sept_22_fee = d.pop("post_sept_22_fee", UNSET)

        key = d.pop("key", UNSET)

        rate_type = d.pop("rate_type", UNSET)

        region = d.pop("region", UNSET)

        solicitor_type = d.pop("solicitor_type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        lauk_criminal_controlled_rate = cls(
            id=id,
            activity=activity,
            activity_type=activity_type,
            category_of_law=category_of_law,
            counsel=counsel,
            court=court,
            created_at=created_at,
            etag=etag,
            exceptional=exceptional,
            fee=fee,
            fee_scheme=fee_scheme,
            post_nov_24_exceptional=post_nov_24_exceptional,
            post_nov_24_fee=post_nov_24_fee,
            post_sept_22_exceptional=post_sept_22_exceptional,
            post_sept_22_fee=post_sept_22_fee,
            key=key,
            rate_type=rate_type,
            region=region,
            solicitor_type=solicitor_type,
            updated_at=updated_at,
        )

        lauk_criminal_controlled_rate.additional_properties = d
        return lauk_criminal_controlled_rate

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
