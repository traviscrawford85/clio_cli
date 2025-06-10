import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activity_base_tax_setting import ActivityBaseTaxSetting
from ..models.activity_base_type import ActivityBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_base_currency import ActivityBaseCurrency


T = TypeVar("T", bound="ActivityBase")


@_attrs_define
class ActivityBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Activity*
        etag (Union[Unset, str]): ETag for the *Activity*
        type_ (Union[Unset, ActivityBaseType]): The type of the *Activity*
        date (Union[Unset, datetime.date]): The date the *Activity* was performed (as a ISO-8601 date)
        quantity_in_hours (Union[Unset, float]): The number of hours the TimeEntry took.
        rounded_quantity_in_hours (Union[Unset, float]): The number of hours rounded accordingly to the billing
            settings.
            The rounded value is used to calculate the total.
        quantity (Union[Unset, float]): The field is applicable to TimeEntry, ExpenseEntry, and SoftCostEntry.

            **Version <= 4.0.3:**
            The number of hours the TimeEntry took.

            **Latest version:**
            The number of seconds the TimeEntry took.
        rounded_quantity (Union[Unset, float]): The field is applicable to time entries only.

            **Version <= 4.0.3:**
            The number of hours rounded accordingly to the billing settings.
            The rounded value is used to calculate the total.

            **Latest version:**
            The number of seconds rounded accordingly to the billing settings.
            The rounded value is used to calculate the total.
        quantity_redacted (Union[Unset, bool]): Is `true` if any of the following fields are redacted:
            `quantity`, `rounded_quantity`, `rounded_quantity_in_hours`, `quantity_in_hours`, `total`, `non_billable_total`
        price (Union[Unset, float]): The hourly or flat rate of the *Activity*
        note (Union[Unset, str]): The details about the *Activity*
        flat_rate (Union[Unset, bool]): Whether the *Activity* is a flat rate
        billed (Union[Unset, bool]): Whether the *Activity* has been added to an active bill that is in the state of
            `awaiting_payment` or `paid`
        on_bill (Union[Unset, bool]): Whether the *Activity* has been added to an active bill that is in the state of
            `draft`, `awaiting_approval`, `awaiting_payment` or `paid`
        total (Union[Unset, float]): The total cost of draft, billable and billed items in the *Activity*
        contingency_fee (Union[Unset, bool]): Whether or not the *Activity* is a contingency fee
        created_at (Union[Unset, datetime.datetime]): The time the *Activity* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Activity* was last updated (as a ISO-8601 timestamp)
        reference (Union[Unset, str]): A check reference for a HardCostEntry.
        non_billable (Union[Unset, bool]): Whether the *Activity* is non-billable
        non_billable_total (Union[Unset, float]): The total cost of non-billable items in the *Activity*
        no_charge (Union[Unset, bool]): Whether the non-billable *Activity* is shown on the bill.
        tax_setting (Union[Unset, ActivityBaseTaxSetting]): The option denoting whether primary tax, secondary tax, or
            both is applied to an expense entry.
        currency (Union[Unset, ActivityBaseCurrency]): The currency of the *Activity*
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    type_: Union[Unset, ActivityBaseType] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    quantity_in_hours: Union[Unset, float] = UNSET
    rounded_quantity_in_hours: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    rounded_quantity: Union[Unset, float] = UNSET
    quantity_redacted: Union[Unset, bool] = UNSET
    price: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    flat_rate: Union[Unset, bool] = UNSET
    billed: Union[Unset, bool] = UNSET
    on_bill: Union[Unset, bool] = UNSET
    total: Union[Unset, float] = UNSET
    contingency_fee: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    reference: Union[Unset, str] = UNSET
    non_billable: Union[Unset, bool] = UNSET
    non_billable_total: Union[Unset, float] = UNSET
    no_charge: Union[Unset, bool] = UNSET
    tax_setting: Union[Unset, ActivityBaseTaxSetting] = UNSET
    currency: Union[Unset, "ActivityBaseCurrency"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        quantity_in_hours = self.quantity_in_hours

        rounded_quantity_in_hours = self.rounded_quantity_in_hours

        quantity = self.quantity

        rounded_quantity = self.rounded_quantity

        quantity_redacted = self.quantity_redacted

        price = self.price

        note = self.note

        flat_rate = self.flat_rate

        billed = self.billed

        on_bill = self.on_bill

        total = self.total

        contingency_fee = self.contingency_fee

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        reference = self.reference

        non_billable = self.non_billable

        non_billable_total = self.non_billable_total

        no_charge = self.no_charge

        tax_setting: Union[Unset, str] = UNSET
        if not isinstance(self.tax_setting, Unset):
            tax_setting = self.tax_setting.value

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if type_ is not UNSET:
            field_dict["type"] = type_
        if date is not UNSET:
            field_dict["date"] = date
        if quantity_in_hours is not UNSET:
            field_dict["quantity_in_hours"] = quantity_in_hours
        if rounded_quantity_in_hours is not UNSET:
            field_dict["rounded_quantity_in_hours"] = rounded_quantity_in_hours
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if rounded_quantity is not UNSET:
            field_dict["rounded_quantity"] = rounded_quantity
        if quantity_redacted is not UNSET:
            field_dict["quantity_redacted"] = quantity_redacted
        if price is not UNSET:
            field_dict["price"] = price
        if note is not UNSET:
            field_dict["note"] = note
        if flat_rate is not UNSET:
            field_dict["flat_rate"] = flat_rate
        if billed is not UNSET:
            field_dict["billed"] = billed
        if on_bill is not UNSET:
            field_dict["on_bill"] = on_bill
        if total is not UNSET:
            field_dict["total"] = total
        if contingency_fee is not UNSET:
            field_dict["contingency_fee"] = contingency_fee
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if reference is not UNSET:
            field_dict["reference"] = reference
        if non_billable is not UNSET:
            field_dict["non_billable"] = non_billable
        if non_billable_total is not UNSET:
            field_dict["non_billable_total"] = non_billable_total
        if no_charge is not UNSET:
            field_dict["no_charge"] = no_charge
        if tax_setting is not UNSET:
            field_dict["tax_setting"] = tax_setting
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_base_currency import ActivityBaseCurrency

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ActivityBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ActivityBaseType(_type_)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        quantity_in_hours = d.pop("quantity_in_hours", UNSET)

        rounded_quantity_in_hours = d.pop("rounded_quantity_in_hours", UNSET)

        quantity = d.pop("quantity", UNSET)

        rounded_quantity = d.pop("rounded_quantity", UNSET)

        quantity_redacted = d.pop("quantity_redacted", UNSET)

        price = d.pop("price", UNSET)

        note = d.pop("note", UNSET)

        flat_rate = d.pop("flat_rate", UNSET)

        billed = d.pop("billed", UNSET)

        on_bill = d.pop("on_bill", UNSET)

        total = d.pop("total", UNSET)

        contingency_fee = d.pop("contingency_fee", UNSET)

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

        reference = d.pop("reference", UNSET)

        non_billable = d.pop("non_billable", UNSET)

        non_billable_total = d.pop("non_billable_total", UNSET)

        no_charge = d.pop("no_charge", UNSET)

        _tax_setting = d.pop("tax_setting", UNSET)
        tax_setting: Union[Unset, ActivityBaseTaxSetting]
        if isinstance(_tax_setting, Unset):
            tax_setting = UNSET
        else:
            tax_setting = ActivityBaseTaxSetting(_tax_setting)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, ActivityBaseCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = ActivityBaseCurrency.from_dict(_currency)

        activity_base = cls(
            id=id,
            etag=etag,
            type_=type_,
            date=date,
            quantity_in_hours=quantity_in_hours,
            rounded_quantity_in_hours=rounded_quantity_in_hours,
            quantity=quantity,
            rounded_quantity=rounded_quantity,
            quantity_redacted=quantity_redacted,
            price=price,
            note=note,
            flat_rate=flat_rate,
            billed=billed,
            on_bill=on_bill,
            total=total,
            contingency_fee=contingency_fee,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            non_billable=non_billable,
            non_billable_total=non_billable_total,
            no_charge=no_charge,
            tax_setting=tax_setting,
            currency=currency,
        )

        activity_base.additional_properties = d
        return activity_base

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
