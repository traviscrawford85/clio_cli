import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.balance_base import BalanceBase
    from ..models.bill_base import BillBase
    from ..models.matter_base import MatterBase


T = TypeVar("T", bound="InterestCharge")


@_attrs_define
class InterestCharge:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *InterestCharge*
        etag (Union[Unset, str]): ETag for the *InterestCharge*
        date (Union[Unset, datetime.date]): The *InterestCharge* date (as a ISO-8601 date)
        description (Union[Unset, str]): The description for the *InterestCharge*
        total (Union[Unset, float]): The total amount for the *InterestCharge*
        created_at (Union[Unset, datetime.datetime]): The time the *InterestCharge* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *InterestCharge* was last updated (as a ISO-8601
            timestamp)
        bill (Union[Unset, BillBase]):
        balances (Union[Unset, list['BalanceBase']]): Balance
        matters (Union[Unset, list['MatterBase']]): Matter
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    description: Union[Unset, str] = UNSET
    total: Union[Unset, float] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    bill: Union[Unset, "BillBase"] = UNSET
    balances: Union[Unset, list["BalanceBase"]] = UNSET
    matters: Union[Unset, list["MatterBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        description = self.description

        total = self.total

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        balances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.balances, Unset):
            balances = []
            for balances_item_data in self.balances:
                balances_item = balances_item_data.to_dict()
                balances.append(balances_item)

        matters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matters, Unset):
            matters = []
            for matters_item_data in self.matters:
                matters_item = matters_item_data.to_dict()
                matters.append(matters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if total is not UNSET:
            field_dict["total"] = total
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if bill is not UNSET:
            field_dict["bill"] = bill
        if balances is not UNSET:
            field_dict["balances"] = balances
        if matters is not UNSET:
            field_dict["matters"] = matters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.balance_base import BalanceBase
        from ..models.bill_base import BillBase
        from ..models.matter_base import MatterBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        description = d.pop("description", UNSET)

        total = d.pop("total", UNSET)

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

        _bill = d.pop("bill", UNSET)
        bill: Union[Unset, BillBase]
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = BillBase.from_dict(_bill)

        balances = []
        _balances = d.pop("balances", UNSET)
        for balances_item_data in _balances or []:
            balances_item = BalanceBase.from_dict(balances_item_data)

            balances.append(balances_item)

        matters = []
        _matters = d.pop("matters", UNSET)
        for matters_item_data in _matters or []:
            matters_item = MatterBase.from_dict(matters_item_data)

            matters.append(matters_item)

        interest_charge = cls(
            id=id,
            etag=etag,
            date=date,
            description=description,
            total=total,
            created_at=created_at,
            updated_at=updated_at,
            bill=bill,
            balances=balances,
            matters=matters,
        )

        interest_charge.additional_properties = d
        return interest_charge

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
