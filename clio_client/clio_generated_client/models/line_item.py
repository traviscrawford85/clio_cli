import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.line_item_base_kind import LineItemBaseKind
from ..models.line_item_base_type import LineItemBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_base import ActivityBase
    from ..models.bill_base import BillBase
    from ..models.discount_base import DiscountBase
    from ..models.line_item_totals_base import LineItemTotalsBase
    from ..models.matter_base import MatterBase
    from ..models.user_base import UserBase


T = TypeVar("T", bound="LineItem")


@_attrs_define
class LineItem:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *LineItem*
        etag (Union[Unset, str]): ETag for the *LineItem*
        type_ (Union[Unset, LineItemBaseType]): The type of the *LineItem*
        description (Union[Unset, str]): The description for the *LineItem*
        date (Union[Unset, datetime.date]): The *LineItem* date (as a ISO-8601 date)
        price (Union[Unset, float]): The price of the *LineItem*
        taxable (Union[Unset, bool]): Whether the *LineItem* is taxable
        kind (Union[Unset, LineItemBaseKind]): The kind of *LineItem*
        note (Union[Unset, str]): The note attached to the *LineItem*
        secondary_taxable (Union[Unset, bool]): Whether the *LineItem* is secondary taxable
        total (Union[Unset, float]): The total amount for the *LineItem*
        tax (Union[Unset, float]): The tax amount for the *LineItem*
        secondary_tax (Union[Unset, float]): The secondary tax amount for the *LineItem*
        sub_total (Union[Unset, float]): The subtotal amount for the *LineItem*
        quantity (Union[Unset, float]): The amount of hours for the *LineItem*
        group_ordering (Union[Unset, int]): The value to specify the ordering of the *LineItem* on a bill
        created_at (Union[Unset, datetime.datetime]): The time the *LineItem* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *LineItem* was last updated (as a ISO-8601 timestamp)
        bill (Union[Unset, BillBase]):
        activity (Union[Unset, ActivityBase]):
        matter (Union[Unset, MatterBase]):
        user (Union[Unset, UserBase]):
        discount (Union[Unset, DiscountBase]):
        included_line_item_totals (Union[Unset, LineItemTotalsBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    type_: Union[Unset, LineItemBaseType] = UNSET
    description: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    price: Union[Unset, float] = UNSET
    taxable: Union[Unset, bool] = UNSET
    kind: Union[Unset, LineItemBaseKind] = UNSET
    note: Union[Unset, str] = UNSET
    secondary_taxable: Union[Unset, bool] = UNSET
    total: Union[Unset, float] = UNSET
    tax: Union[Unset, float] = UNSET
    secondary_tax: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    group_ordering: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    bill: Union[Unset, "BillBase"] = UNSET
    activity: Union[Unset, "ActivityBase"] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    user: Union[Unset, "UserBase"] = UNSET
    discount: Union[Unset, "DiscountBase"] = UNSET
    included_line_item_totals: Union[Unset, "LineItemTotalsBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        description = self.description

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        price = self.price

        taxable = self.taxable

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        note = self.note

        secondary_taxable = self.secondary_taxable

        total = self.total

        tax = self.tax

        secondary_tax = self.secondary_tax

        sub_total = self.sub_total

        quantity = self.quantity

        group_ordering = self.group_ordering

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        activity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        discount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        included_line_item_totals: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.included_line_item_totals, Unset):
            included_line_item_totals = self.included_line_item_totals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if date is not UNSET:
            field_dict["date"] = date
        if price is not UNSET:
            field_dict["price"] = price
        if taxable is not UNSET:
            field_dict["taxable"] = taxable
        if kind is not UNSET:
            field_dict["kind"] = kind
        if note is not UNSET:
            field_dict["note"] = note
        if secondary_taxable is not UNSET:
            field_dict["secondary_taxable"] = secondary_taxable
        if total is not UNSET:
            field_dict["total"] = total
        if tax is not UNSET:
            field_dict["tax"] = tax
        if secondary_tax is not UNSET:
            field_dict["secondary_tax"] = secondary_tax
        if sub_total is not UNSET:
            field_dict["sub_total"] = sub_total
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if group_ordering is not UNSET:
            field_dict["group_ordering"] = group_ordering
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if bill is not UNSET:
            field_dict["bill"] = bill
        if activity is not UNSET:
            field_dict["activity"] = activity
        if matter is not UNSET:
            field_dict["matter"] = matter
        if user is not UNSET:
            field_dict["user"] = user
        if discount is not UNSET:
            field_dict["discount"] = discount
        if included_line_item_totals is not UNSET:
            field_dict["included_line_item_totals"] = included_line_item_totals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_base import ActivityBase
        from ..models.bill_base import BillBase
        from ..models.discount_base import DiscountBase
        from ..models.line_item_totals_base import LineItemTotalsBase
        from ..models.matter_base import MatterBase
        from ..models.user_base import UserBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, LineItemBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LineItemBaseType(_type_)

        description = d.pop("description", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        price = d.pop("price", UNSET)

        taxable = d.pop("taxable", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, LineItemBaseKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = LineItemBaseKind(_kind)

        note = d.pop("note", UNSET)

        secondary_taxable = d.pop("secondary_taxable", UNSET)

        total = d.pop("total", UNSET)

        tax = d.pop("tax", UNSET)

        secondary_tax = d.pop("secondary_tax", UNSET)

        sub_total = d.pop("sub_total", UNSET)

        quantity = d.pop("quantity", UNSET)

        group_ordering = d.pop("group_ordering", UNSET)

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

        _activity = d.pop("activity", UNSET)
        activity: Union[Unset, ActivityBase]
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = ActivityBase.from_dict(_activity)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserBase]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserBase.from_dict(_user)

        _discount = d.pop("discount", UNSET)
        discount: Union[Unset, DiscountBase]
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = DiscountBase.from_dict(_discount)

        _included_line_item_totals = d.pop("included_line_item_totals", UNSET)
        included_line_item_totals: Union[Unset, LineItemTotalsBase]
        if isinstance(_included_line_item_totals, Unset):
            included_line_item_totals = UNSET
        else:
            included_line_item_totals = LineItemTotalsBase.from_dict(_included_line_item_totals)

        line_item = cls(
            id=id,
            etag=etag,
            type_=type_,
            description=description,
            date=date,
            price=price,
            taxable=taxable,
            kind=kind,
            note=note,
            secondary_taxable=secondary_taxable,
            total=total,
            tax=tax,
            secondary_tax=secondary_tax,
            sub_total=sub_total,
            quantity=quantity,
            group_ordering=group_ordering,
            created_at=created_at,
            updated_at=updated_at,
            bill=bill,
            activity=activity,
            matter=matter,
            user=user,
            discount=discount,
            included_line_item_totals=included_line_item_totals,
        )

        line_item.additional_properties = d
        return line_item

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
