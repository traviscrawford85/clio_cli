import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polymorphic_custom_rate_activity_description_base import PolymorphicCustomRateActivityDescriptionBase
    from ..models.polymorphic_custom_rate_group_base import PolymorphicCustomRateGroupBase
    from ..models.polymorphic_custom_rate_user_base import PolymorphicCustomRateUserBase


T = TypeVar("T", bound="PolymorphicCustomRate")


@_attrs_define
class PolymorphicCustomRate:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier for the custom rate
        etag (Union[Unset, str]): ETag for the *PolymorphicCustomRate*
        created_at (Union[Unset, datetime.datetime]): The time the *PolymorphicCustomRate* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *PolymorphicCustomRate* was last updated (as a
            ISO-8601 timestamp)
        rate (Union[Unset, float]): If `custom_rate.type` is `HourlyRate`, it is the dollar amount of the custom rate of
            the User or Group for the Matter.

            If `custom_rate.type` is `FlatRate`, it is the dollar amount of the custom flat rate for the Matter.

            If `custom_rate.type` is `ContingencyFee`, it is the percentage of the contingency fee awarded to the user for
            the Matter. The value may also be expressed as string that represents a rational number such as `1/3`.

            If the user does not have sufficient rate visibility, the rates are hidden.
        award (Union[Unset, float]): The value of the ContingencyFee award.
        note (Union[Unset, str]): Details about the ContingencyFee award.
        date (Union[Unset, datetime.date]): The date of the ContingencyFee award.
        user (Union[Unset, PolymorphicCustomRateUserBase]):
        group (Union[Unset, PolymorphicCustomRateGroupBase]):
        activity_description (Union[Unset, PolymorphicCustomRateActivityDescriptionBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    rate: Union[Unset, float] = UNSET
    award: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    user: Union[Unset, "PolymorphicCustomRateUserBase"] = UNSET
    group: Union[Unset, "PolymorphicCustomRateGroupBase"] = UNSET
    activity_description: Union[Unset, "PolymorphicCustomRateActivityDescriptionBase"] = UNSET
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

        rate = self.rate

        award = self.award

        note = self.note

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        activity_description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.activity_description, Unset):
            activity_description = self.activity_description.to_dict()

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
        if rate is not UNSET:
            field_dict["rate"] = rate
        if award is not UNSET:
            field_dict["award"] = award
        if note is not UNSET:
            field_dict["note"] = note
        if date is not UNSET:
            field_dict["date"] = date
        if user is not UNSET:
            field_dict["user"] = user
        if group is not UNSET:
            field_dict["group"] = group
        if activity_description is not UNSET:
            field_dict["activity_description"] = activity_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polymorphic_custom_rate_activity_description_base import (
            PolymorphicCustomRateActivityDescriptionBase,
        )
        from ..models.polymorphic_custom_rate_group_base import PolymorphicCustomRateGroupBase
        from ..models.polymorphic_custom_rate_user_base import PolymorphicCustomRateUserBase

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

        rate = d.pop("rate", UNSET)

        award = d.pop("award", UNSET)

        note = d.pop("note", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        _user = d.pop("user", UNSET)
        user: Union[Unset, PolymorphicCustomRateUserBase]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PolymorphicCustomRateUserBase.from_dict(_user)

        _group = d.pop("group", UNSET)
        group: Union[Unset, PolymorphicCustomRateGroupBase]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = PolymorphicCustomRateGroupBase.from_dict(_group)

        _activity_description = d.pop("activity_description", UNSET)
        activity_description: Union[Unset, PolymorphicCustomRateActivityDescriptionBase]
        if isinstance(_activity_description, Unset):
            activity_description = UNSET
        else:
            activity_description = PolymorphicCustomRateActivityDescriptionBase.from_dict(_activity_description)

        polymorphic_custom_rate = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            rate=rate,
            award=award,
            note=note,
            date=date,
            user=user,
            group=group,
            activity_description=activity_description,
        )

        polymorphic_custom_rate.additional_properties = d
        return polymorphic_custom_rate

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
