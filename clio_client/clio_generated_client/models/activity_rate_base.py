import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityRateBase")


@_attrs_define
class ActivityRateBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *ActivityRate*
        etag (Union[Unset, str]): ETag for the *ActivityRate*
        rate (Union[Unset, float]): Monetary value of this rate. Either hourly value or flat rate value
        flat_rate (Union[Unset, bool]): Whether this is a flat rate
        created_at (Union[Unset, datetime.datetime]): The time the *ActivityRate* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *ActivityRate* was last updated (as a ISO-8601
            timestamp)
        contact_id (Union[Unset, int]): Filter ActivityRate records for the contact.
        co_counsel_contact_id (Union[Unset, int]): Filter ActivityRate records for the co-counsel.
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    flat_rate: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    contact_id: Union[Unset, int] = UNSET
    co_counsel_contact_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        rate = self.rate

        flat_rate = self.flat_rate

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        contact_id = self.contact_id

        co_counsel_contact_id = self.co_counsel_contact_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if rate is not UNSET:
            field_dict["rate"] = rate
        if flat_rate is not UNSET:
            field_dict["flat_rate"] = flat_rate
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if co_counsel_contact_id is not UNSET:
            field_dict["co_counsel_contact_id"] = co_counsel_contact_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        rate = d.pop("rate", UNSET)

        flat_rate = d.pop("flat_rate", UNSET)

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

        contact_id = d.pop("contact_id", UNSET)

        co_counsel_contact_id = d.pop("co_counsel_contact_id", UNSET)

        activity_rate_base = cls(
            id=id,
            etag=etag,
            rate=rate,
            flat_rate=flat_rate,
            created_at=created_at,
            updated_at=updated_at,
            contact_id=contact_id,
            co_counsel_contact_id=co_counsel_contact_id,
        )

        activity_rate_base.additional_properties = d
        return activity_rate_base

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
