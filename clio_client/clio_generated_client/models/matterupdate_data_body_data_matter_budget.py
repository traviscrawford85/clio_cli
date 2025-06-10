from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatterupdateDataBodyDataMatterBudget")


@_attrs_define
class MatterupdateDataBodyDataMatterBudget:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): Determines whether the matter budget associated with the matter should be
            destroyed. Only users with matter budget destroy capabilities can destroy matter budgets.
        budget (Union[Unset, float]): The amount allocated for the matter.
        include_expenses (Union[Unset, bool]): Determines whether the budget includes expenses in the calculation.
        notification_threshold (Union[Unset, int]): Percentage of the budget when it starts notifying users.
        notify_users (Union[Unset, bool]): Determine whether to notify users when the matter reaches the notification
            threshold. Default: False.
    """

    field_destroy: Union[Unset, bool] = UNSET
    budget: Union[Unset, float] = UNSET
    include_expenses: Union[Unset, bool] = UNSET
    notification_threshold: Union[Unset, int] = UNSET
    notify_users: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        budget = self.budget

        include_expenses = self.include_expenses

        notification_threshold = self.notification_threshold

        notify_users = self.notify_users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if budget is not UNSET:
            field_dict["budget"] = budget
        if include_expenses is not UNSET:
            field_dict["include_expenses"] = include_expenses
        if notification_threshold is not UNSET:
            field_dict["notification_threshold"] = notification_threshold
        if notify_users is not UNSET:
            field_dict["notify_users"] = notify_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_destroy = d.pop("_destroy", UNSET)

        budget = d.pop("budget", UNSET)

        include_expenses = d.pop("include_expenses", UNSET)

        notification_threshold = d.pop("notification_threshold", UNSET)

        notify_users = d.pop("notify_users", UNSET)

        matterupdate_data_body_data_matter_budget = cls(
            field_destroy=field_destroy,
            budget=budget,
            include_expenses=include_expenses,
            notification_threshold=notification_threshold,
            notify_users=notify_users,
        )

        matterupdate_data_body_data_matter_budget.additional_properties = d
        return matterupdate_data_body_data_matter_budget

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
