import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expense_category_base_currency import ExpenseCategoryBaseCurrency
    from ..models.group_base import GroupBase
    from ..models.utbms_code_base import UtbmsCodeBase


T = TypeVar("T", bound="ExpenseCategory")


@_attrs_define
class ExpenseCategory:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *ExpenseCategory*
        etag (Union[Unset, str]): ETag for the *ExpenseCategory*
        name (Union[Unset, str]): The name of the expense category
        rate (Union[Unset, int]): The price charged per unit cost
        entry_type (Union[Unset, str]): The type of expense entry the category is associated to. Can be either
            "hard_cost", "soft_cost" or "unassociated"
        created_at (Union[Unset, datetime.datetime]): The time the *ExpenseCategory* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *ExpenseCategory* was last updated (as a ISO-8601
            timestamp)
        xero_expense_code (Union[Unset, str]): Custom Xero expense code for an expense category
        accessible_to_user (Union[Unset, bool]): Determines if expense category is accessible to user
        tax_setting (Union[Unset, str]): The type of tax rate applied to the expense category.
        currency (Union[Unset, ExpenseCategoryBaseCurrency]): The currency details for the expense category
        groups (Union[Unset, list['GroupBase']]): Group
        utbms_code (Union[Unset, UtbmsCodeBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    rate: Union[Unset, int] = UNSET
    entry_type: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    xero_expense_code: Union[Unset, str] = UNSET
    accessible_to_user: Union[Unset, bool] = UNSET
    tax_setting: Union[Unset, str] = UNSET
    currency: Union[Unset, "ExpenseCategoryBaseCurrency"] = UNSET
    groups: Union[Unset, list["GroupBase"]] = UNSET
    utbms_code: Union[Unset, "UtbmsCodeBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        rate = self.rate

        entry_type = self.entry_type

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        xero_expense_code = self.xero_expense_code

        accessible_to_user = self.accessible_to_user

        tax_setting = self.tax_setting

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        utbms_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.utbms_code, Unset):
            utbms_code = self.utbms_code.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if rate is not UNSET:
            field_dict["rate"] = rate
        if entry_type is not UNSET:
            field_dict["entry_type"] = entry_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if xero_expense_code is not UNSET:
            field_dict["xero_expense_code"] = xero_expense_code
        if accessible_to_user is not UNSET:
            field_dict["accessible_to_user"] = accessible_to_user
        if tax_setting is not UNSET:
            field_dict["tax_setting"] = tax_setting
        if currency is not UNSET:
            field_dict["currency"] = currency
        if groups is not UNSET:
            field_dict["groups"] = groups
        if utbms_code is not UNSET:
            field_dict["utbms_code"] = utbms_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expense_category_base_currency import ExpenseCategoryBaseCurrency
        from ..models.group_base import GroupBase
        from ..models.utbms_code_base import UtbmsCodeBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        rate = d.pop("rate", UNSET)

        entry_type = d.pop("entry_type", UNSET)

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

        xero_expense_code = d.pop("xero_expense_code", UNSET)

        accessible_to_user = d.pop("accessible_to_user", UNSET)

        tax_setting = d.pop("tax_setting", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, ExpenseCategoryBaseCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = ExpenseCategoryBaseCurrency.from_dict(_currency)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GroupBase.from_dict(groups_item_data)

            groups.append(groups_item)

        _utbms_code = d.pop("utbms_code", UNSET)
        utbms_code: Union[Unset, UtbmsCodeBase]
        if isinstance(_utbms_code, Unset):
            utbms_code = UNSET
        else:
            utbms_code = UtbmsCodeBase.from_dict(_utbms_code)

        expense_category = cls(
            id=id,
            etag=etag,
            name=name,
            rate=rate,
            entry_type=entry_type,
            created_at=created_at,
            updated_at=updated_at,
            xero_expense_code=xero_expense_code,
            accessible_to_user=accessible_to_user,
            tax_setting=tax_setting,
            currency=currency,
            groups=groups,
            utbms_code=utbms_code,
        )

        expense_category.additional_properties = d
        return expense_category

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
