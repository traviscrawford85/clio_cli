import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bill_base import BillBase
    from ..models.contact_base import ContactBase
    from ..models.currency_base import CurrencyBase


T = TypeVar("T", bound="OutstandingClientBalance")


@_attrs_define
class OutstandingClientBalance:
    """
    Attributes:
        associated_matter_ids (Union[Unset, list[int]]): An array of Matter IDs associated with bills in the unpaid
            state
        etag (Union[Unset, str]): ETag for the *OutstandingClientBalance*
        id (Union[Unset, int]): Unique identifier for the *OutstandingClientBalance*
        last_payment_date (Union[Unset, datetime.date]): The date the most recent payment from the contact was received
        last_shared_date (Union[Unset, datetime.date]): The date of the most recently shared bills through the
            outstanding balance table
        newest_issued_bill_due_date (Union[Unset, datetime.date]): The due date of the contact's newest bill
        pending_payments_total (Union[Unset, float]): The sum of all online payments in a pending state on the
            outstanding bills
        reminders_enabled (Union[Unset, bool]): The status of automated reminders for this client
        total_outstanding_balance (Union[Unset, float]): The sum of all bills in the unpaid state
        created_at (Union[Unset, datetime.datetime]): The time the *OutstandingClientBalance* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *OutstandingClientBalance* was last updated (as a
            ISO-8601 timestamp)
        outstanding_bills (Union[Unset, list['BillBase']]): Bill
        contact (Union[Unset, ContactBase]):
        currency (Union[Unset, CurrencyBase]):
    """

    associated_matter_ids: Union[Unset, list[int]] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    last_payment_date: Union[Unset, datetime.date] = UNSET
    last_shared_date: Union[Unset, datetime.date] = UNSET
    newest_issued_bill_due_date: Union[Unset, datetime.date] = UNSET
    pending_payments_total: Union[Unset, float] = UNSET
    reminders_enabled: Union[Unset, bool] = UNSET
    total_outstanding_balance: Union[Unset, float] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    outstanding_bills: Union[Unset, list["BillBase"]] = UNSET
    contact: Union[Unset, "ContactBase"] = UNSET
    currency: Union[Unset, "CurrencyBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associated_matter_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.associated_matter_ids, Unset):
            associated_matter_ids = self.associated_matter_ids

        etag = self.etag

        id = self.id

        last_payment_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_payment_date, Unset):
            last_payment_date = self.last_payment_date.isoformat()

        last_shared_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_shared_date, Unset):
            last_shared_date = self.last_shared_date.isoformat()

        newest_issued_bill_due_date: Union[Unset, str] = UNSET
        if not isinstance(self.newest_issued_bill_due_date, Unset):
            newest_issued_bill_due_date = self.newest_issued_bill_due_date.isoformat()

        pending_payments_total = self.pending_payments_total

        reminders_enabled = self.reminders_enabled

        total_outstanding_balance = self.total_outstanding_balance

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        outstanding_bills: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.outstanding_bills, Unset):
            outstanding_bills = []
            for outstanding_bills_item_data in self.outstanding_bills:
                outstanding_bills_item = outstanding_bills_item_data.to_dict()
                outstanding_bills.append(outstanding_bills_item)

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_matter_ids is not UNSET:
            field_dict["associated_matter_ids"] = associated_matter_ids
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if last_payment_date is not UNSET:
            field_dict["last_payment_date"] = last_payment_date
        if last_shared_date is not UNSET:
            field_dict["last_shared_date"] = last_shared_date
        if newest_issued_bill_due_date is not UNSET:
            field_dict["newest_issued_bill_due_date"] = newest_issued_bill_due_date
        if pending_payments_total is not UNSET:
            field_dict["pending_payments_total"] = pending_payments_total
        if reminders_enabled is not UNSET:
            field_dict["reminders_enabled"] = reminders_enabled
        if total_outstanding_balance is not UNSET:
            field_dict["total_outstanding_balance"] = total_outstanding_balance
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if outstanding_bills is not UNSET:
            field_dict["outstanding_bills"] = outstanding_bills
        if contact is not UNSET:
            field_dict["contact"] = contact
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bill_base import BillBase
        from ..models.contact_base import ContactBase
        from ..models.currency_base import CurrencyBase

        d = dict(src_dict)
        associated_matter_ids = cast(list[int], d.pop("associated_matter_ids", UNSET))

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        _last_payment_date = d.pop("last_payment_date", UNSET)
        last_payment_date: Union[Unset, datetime.date]
        if isinstance(_last_payment_date, Unset):
            last_payment_date = UNSET
        else:
            last_payment_date = isoparse(_last_payment_date).date()

        _last_shared_date = d.pop("last_shared_date", UNSET)
        last_shared_date: Union[Unset, datetime.date]
        if isinstance(_last_shared_date, Unset):
            last_shared_date = UNSET
        else:
            last_shared_date = isoparse(_last_shared_date).date()

        _newest_issued_bill_due_date = d.pop("newest_issued_bill_due_date", UNSET)
        newest_issued_bill_due_date: Union[Unset, datetime.date]
        if isinstance(_newest_issued_bill_due_date, Unset):
            newest_issued_bill_due_date = UNSET
        else:
            newest_issued_bill_due_date = isoparse(_newest_issued_bill_due_date).date()

        pending_payments_total = d.pop("pending_payments_total", UNSET)

        reminders_enabled = d.pop("reminders_enabled", UNSET)

        total_outstanding_balance = d.pop("total_outstanding_balance", UNSET)

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

        outstanding_bills = []
        _outstanding_bills = d.pop("outstanding_bills", UNSET)
        for outstanding_bills_item_data in _outstanding_bills or []:
            outstanding_bills_item = BillBase.from_dict(outstanding_bills_item_data)

            outstanding_bills.append(outstanding_bills_item)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, ContactBase]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactBase.from_dict(_contact)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, CurrencyBase]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = CurrencyBase.from_dict(_currency)

        outstanding_client_balance = cls(
            associated_matter_ids=associated_matter_ids,
            etag=etag,
            id=id,
            last_payment_date=last_payment_date,
            last_shared_date=last_shared_date,
            newest_issued_bill_due_date=newest_issued_bill_due_date,
            pending_payments_total=pending_payments_total,
            reminders_enabled=reminders_enabled,
            total_outstanding_balance=total_outstanding_balance,
            created_at=created_at,
            updated_at=updated_at,
            outstanding_bills=outstanding_bills,
            contact=contact,
            currency=currency,
        )

        outstanding_client_balance.additional_properties = d
        return outstanding_client_balance

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
