from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_descriptionupdate_data_body_data_currency import (
        ActivityDescriptionupdateDataBodyDataCurrency,
    )
    from ..models.activity_descriptionupdate_data_body_data_groups_item import (
        ActivityDescriptionupdateDataBodyDataGroupsItem,
    )
    from ..models.activity_descriptionupdate_data_body_data_rate import ActivityDescriptionupdateDataBodyDataRate


T = TypeVar("T", bound="ActivityDescriptionupdateDataBodyData")


@_attrs_define
class ActivityDescriptionupdateDataBodyData:
    """
    Attributes:
        currency (Union[Unset, ActivityDescriptionupdateDataBodyDataCurrency]): Currency of the ActivityDescription.
        default (Union[Unset, bool]): Whether or not this should be the API User's default ActivityDescription.
        groups (Union[Unset, list['ActivityDescriptionupdateDataBodyDataGroupsItem']]):
        name (Union[Unset, str]): A detailed description of the ActivityDescription.
        rate (Union[Unset, ActivityDescriptionupdateDataBodyDataRate]):
        visible_to_co_counsel (Union[Unset, bool]): Whether or not co counsels on the account can see this
            ActivityDescription.
    """

    currency: Union[Unset, "ActivityDescriptionupdateDataBodyDataCurrency"] = UNSET
    default: Union[Unset, bool] = UNSET
    groups: Union[Unset, list["ActivityDescriptionupdateDataBodyDataGroupsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    rate: Union[Unset, "ActivityDescriptionupdateDataBodyDataRate"] = UNSET
    visible_to_co_counsel: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        default = self.default

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        name = self.name

        rate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rate, Unset):
            rate = self.rate.to_dict()

        visible_to_co_counsel = self.visible_to_co_counsel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if default is not UNSET:
            field_dict["default"] = default
        if groups is not UNSET:
            field_dict["groups"] = groups
        if name is not UNSET:
            field_dict["name"] = name
        if rate is not UNSET:
            field_dict["rate"] = rate
        if visible_to_co_counsel is not UNSET:
            field_dict["visible_to_co_counsel"] = visible_to_co_counsel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_descriptionupdate_data_body_data_currency import (
            ActivityDescriptionupdateDataBodyDataCurrency,
        )
        from ..models.activity_descriptionupdate_data_body_data_groups_item import (
            ActivityDescriptionupdateDataBodyDataGroupsItem,
        )
        from ..models.activity_descriptionupdate_data_body_data_rate import ActivityDescriptionupdateDataBodyDataRate

        d = dict(src_dict)
        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, ActivityDescriptionupdateDataBodyDataCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = ActivityDescriptionupdateDataBodyDataCurrency.from_dict(_currency)

        default = d.pop("default", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = ActivityDescriptionupdateDataBodyDataGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        name = d.pop("name", UNSET)

        _rate = d.pop("rate", UNSET)
        rate: Union[Unset, ActivityDescriptionupdateDataBodyDataRate]
        if isinstance(_rate, Unset):
            rate = UNSET
        else:
            rate = ActivityDescriptionupdateDataBodyDataRate.from_dict(_rate)

        visible_to_co_counsel = d.pop("visible_to_co_counsel", UNSET)

        activity_descriptionupdate_data_body_data = cls(
            currency=currency,
            default=default,
            groups=groups,
            name=name,
            rate=rate,
            visible_to_co_counsel=visible_to_co_counsel,
        )

        activity_descriptionupdate_data_body_data.additional_properties = d
        return activity_descriptionupdate_data_body_data

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
