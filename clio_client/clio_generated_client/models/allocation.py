import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_account_base import BankAccountBase
    from ..models.bill_base import BillBase
    from ..models.contact_base import ContactBase
    from ..models.matter_base import MatterBase
    from ..models.polymorphic_object_base import PolymorphicObjectBase


T = TypeVar("T", bound="Allocation")


@_attrs_define
class Allocation:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Allocation*
        etag (Union[Unset, str]): ETag for the *Allocation*
        date (Union[Unset, datetime.date]): The date the allocation was applied (as a ISO-8601 date)
        amount (Union[Unset, float]): The total amount of money that the user has allocated
        interest (Union[Unset, bool]): Whether the allocation is applied to interest amount
        voided_at (Union[Unset, datetime.datetime]): Time the *Allocation* was voided (as a ISO-8601 timestamp)
        created_at (Union[Unset, datetime.datetime]): The time the *Allocation* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Allocation* was last updated (as a ISO-8601
            timestamp)
        description (Union[Unset, str]): The description from the associated Credit Memo (if applicable)
        has_online_payment (Union[Unset, bool]): Whether this allocation is associated with an online payment or not
        destroyable (Union[Unset, bool]): Whether the record can be deleted or not
        payment_type (Union[Unset, str]): A string indicating whether the payment is a card or an eCheck payment.
        bill (Union[Unset, BillBase]):
        source_bank_account (Union[Unset, BankAccountBase]):
        destination_bank_account (Union[Unset, BankAccountBase]):
        matter (Union[Unset, MatterBase]):
        contact (Union[Unset, ContactBase]):
        parent (Union[Unset, PolymorphicObjectBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    amount: Union[Unset, float] = UNSET
    interest: Union[Unset, bool] = UNSET
    voided_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    has_online_payment: Union[Unset, bool] = UNSET
    destroyable: Union[Unset, bool] = UNSET
    payment_type: Union[Unset, str] = UNSET
    bill: Union[Unset, "BillBase"] = UNSET
    source_bank_account: Union[Unset, "BankAccountBase"] = UNSET
    destination_bank_account: Union[Unset, "BankAccountBase"] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    contact: Union[Unset, "ContactBase"] = UNSET
    parent: Union[Unset, "PolymorphicObjectBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        amount = self.amount

        interest = self.interest

        voided_at: Union[Unset, str] = UNSET
        if not isinstance(self.voided_at, Unset):
            voided_at = self.voided_at.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        description = self.description

        has_online_payment = self.has_online_payment

        destroyable = self.destroyable

        payment_type = self.payment_type

        bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        source_bank_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source_bank_account, Unset):
            source_bank_account = self.source_bank_account.to_dict()

        destination_bank_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination_bank_account, Unset):
            destination_bank_account = self.destination_bank_account.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        parent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if date is not UNSET:
            field_dict["date"] = date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if interest is not UNSET:
            field_dict["interest"] = interest
        if voided_at is not UNSET:
            field_dict["voided_at"] = voided_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if description is not UNSET:
            field_dict["description"] = description
        if has_online_payment is not UNSET:
            field_dict["has_online_payment"] = has_online_payment
        if destroyable is not UNSET:
            field_dict["destroyable"] = destroyable
        if payment_type is not UNSET:
            field_dict["payment_type"] = payment_type
        if bill is not UNSET:
            field_dict["bill"] = bill
        if source_bank_account is not UNSET:
            field_dict["source_bank_account"] = source_bank_account
        if destination_bank_account is not UNSET:
            field_dict["destination_bank_account"] = destination_bank_account
        if matter is not UNSET:
            field_dict["matter"] = matter
        if contact is not UNSET:
            field_dict["contact"] = contact
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bank_account_base import BankAccountBase
        from ..models.bill_base import BillBase
        from ..models.contact_base import ContactBase
        from ..models.matter_base import MatterBase
        from ..models.polymorphic_object_base import PolymorphicObjectBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        amount = d.pop("amount", UNSET)

        interest = d.pop("interest", UNSET)

        _voided_at = d.pop("voided_at", UNSET)
        voided_at: Union[Unset, datetime.datetime]
        if isinstance(_voided_at, Unset):
            voided_at = UNSET
        else:
            voided_at = isoparse(_voided_at)

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

        description = d.pop("description", UNSET)

        has_online_payment = d.pop("has_online_payment", UNSET)

        destroyable = d.pop("destroyable", UNSET)

        payment_type = d.pop("payment_type", UNSET)

        _bill = d.pop("bill", UNSET)
        bill: Union[Unset, BillBase]
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = BillBase.from_dict(_bill)

        _source_bank_account = d.pop("source_bank_account", UNSET)
        source_bank_account: Union[Unset, BankAccountBase]
        if isinstance(_source_bank_account, Unset):
            source_bank_account = UNSET
        else:
            source_bank_account = BankAccountBase.from_dict(_source_bank_account)

        _destination_bank_account = d.pop("destination_bank_account", UNSET)
        destination_bank_account: Union[Unset, BankAccountBase]
        if isinstance(_destination_bank_account, Unset):
            destination_bank_account = UNSET
        else:
            destination_bank_account = BankAccountBase.from_dict(_destination_bank_account)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, ContactBase]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactBase.from_dict(_contact)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, PolymorphicObjectBase]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = PolymorphicObjectBase.from_dict(_parent)

        allocation = cls(
            id=id,
            etag=etag,
            date=date,
            amount=amount,
            interest=interest,
            voided_at=voided_at,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            has_online_payment=has_online_payment,
            destroyable=destroyable,
            payment_type=payment_type,
            bill=bill,
            source_bank_account=source_bank_account,
            destination_bank_account=destination_bank_account,
            matter=matter,
            contact=contact,
            parent=parent,
        )

        allocation.additional_properties = d
        return allocation

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
