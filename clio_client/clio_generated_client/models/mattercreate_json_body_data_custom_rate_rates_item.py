import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mattercreate_json_body_data_custom_rate_rates_item_activity_description import (
        MattercreateJsonBodyDataCustomRateRatesItemActivityDescription,
    )
    from ..models.mattercreate_json_body_data_custom_rate_rates_item_group import (
        MattercreateJsonBodyDataCustomRateRatesItemGroup,
    )
    from ..models.mattercreate_json_body_data_custom_rate_rates_item_user import (
        MattercreateJsonBodyDataCustomRateRatesItemUser,
    )


T = TypeVar("T", bound="MattercreateJsonBodyDataCustomRateRatesItem")


@_attrs_define
class MattercreateJsonBodyDataCustomRateRatesItem:
    """
    Attributes:
        user (MattercreateJsonBodyDataCustomRateRatesItemUser):
        rate (float): If `type` is `HourlyRate`, it is the dollar amount of the custom rate of the User or Group for the
            Matter.

            If `type` is `FlatRate`, it is the dollar amount of the custom flat rate for the Matter.

            If `type` is `ContingencyFee`, it is the percentage of the contingency fee awarded to the user for the Matter.
        award (Union[Unset, float]): The full amount of the award given. Only valid for ContingencyFee. If given as an
            empty string, it will reset the ContingencyFee into the unawarded state.
        note (Union[Unset, str]): Detailed description of the rate. Only valid for ContingencyFee.
        date (Union[Unset, datetime.date]): The date the rate is for. Only valid for ContingencyFee. (Expects an
            ISO-8601 date).
        activity_description (Union[Unset, MattercreateJsonBodyDataCustomRateRatesItemActivityDescription]):
        group (Union[Unset, MattercreateJsonBodyDataCustomRateRatesItemGroup]):
    """

    user: "MattercreateJsonBodyDataCustomRateRatesItemUser"
    rate: float
    award: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    activity_description: Union[Unset, "MattercreateJsonBodyDataCustomRateRatesItemActivityDescription"] = UNSET
    group: Union[Unset, "MattercreateJsonBodyDataCustomRateRatesItemGroup"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        rate = self.rate

        award = self.award

        note = self.note

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        activity_description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.activity_description, Unset):
            activity_description = self.activity_description.to_dict()

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "rate": rate,
            }
        )
        if award is not UNSET:
            field_dict["award"] = award
        if note is not UNSET:
            field_dict["note"] = note
        if date is not UNSET:
            field_dict["date"] = date
        if activity_description is not UNSET:
            field_dict["activity_description"] = activity_description
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mattercreate_json_body_data_custom_rate_rates_item_activity_description import (
            MattercreateJsonBodyDataCustomRateRatesItemActivityDescription,
        )
        from ..models.mattercreate_json_body_data_custom_rate_rates_item_group import (
            MattercreateJsonBodyDataCustomRateRatesItemGroup,
        )
        from ..models.mattercreate_json_body_data_custom_rate_rates_item_user import (
            MattercreateJsonBodyDataCustomRateRatesItemUser,
        )

        d = dict(src_dict)
        user = MattercreateJsonBodyDataCustomRateRatesItemUser.from_dict(d.pop("user"))

        rate = d.pop("rate")

        award = d.pop("award", UNSET)

        note = d.pop("note", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        _activity_description = d.pop("activity_description", UNSET)
        activity_description: Union[Unset, MattercreateJsonBodyDataCustomRateRatesItemActivityDescription]
        if isinstance(_activity_description, Unset):
            activity_description = UNSET
        else:
            activity_description = MattercreateJsonBodyDataCustomRateRatesItemActivityDescription.from_dict(
                _activity_description
            )

        _group = d.pop("group", UNSET)
        group: Union[Unset, MattercreateJsonBodyDataCustomRateRatesItemGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = MattercreateJsonBodyDataCustomRateRatesItemGroup.from_dict(_group)

        mattercreate_json_body_data_custom_rate_rates_item = cls(
            user=user,
            rate=rate,
            award=award,
            note=note,
            date=date,
            activity_description=activity_description,
            group=group,
        )

        mattercreate_json_body_data_custom_rate_rates_item.additional_properties = d
        return mattercreate_json_body_data_custom_rate_rates_item

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
