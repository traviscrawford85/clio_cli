import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.billupdate_files_body_data_state import BillupdateFilesBodyDataState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billupdate_files_body_data_bill_theme import BillupdateFilesBodyDataBillTheme
    from ..models.billupdate_files_body_data_discount import BillupdateFilesBodyDataDiscount
    from ..models.billupdate_files_body_data_interest import BillupdateFilesBodyDataInterest


T = TypeVar("T", bound="BillupdateFilesBodyData")


@_attrs_define
class BillupdateFilesBodyData:
    """
    Attributes:
        bill_theme (Union[Unset, BillupdateFilesBodyDataBillTheme]):
        currency_id (Union[Unset, int]): ID of the currency applied to the Bill.
        discount (Union[Unset, BillupdateFilesBodyDataDiscount]):
        due_at (Union[Unset, datetime.date]): Date the Bill is due. If `use_grace_period` is true, this field is
            ignored.
        interest (Union[Unset, BillupdateFilesBodyDataInterest]):
        issued_at (Union[Unset, datetime.date]): Date the Bill was issued.
        memo (Union[Unset, str]): Memo for the Bill.
        number (Union[Unset, str]): Bill's number.
        purchase_order (Union[Unset, str]): Purchase order information for the Bill.
        secondary_tax_rate (Union[Unset, float]): Secondary tax rate as percentage for the Bill.
        state (Union[Unset, BillupdateFilesBodyDataState]): Bill's state.
        subject (Union[Unset, str]): Subject details for the Bill.
        tax_rate (Union[Unset, float]): Tax rate as percentage for the Bill
        use_grace_period (Union[Unset, bool]): When true, sets the bill's due date based on the client's grace period.
            This setting overrides the `due_at` parameter.
    """

    bill_theme: Union[Unset, "BillupdateFilesBodyDataBillTheme"] = UNSET
    currency_id: Union[Unset, int] = UNSET
    discount: Union[Unset, "BillupdateFilesBodyDataDiscount"] = UNSET
    due_at: Union[Unset, datetime.date] = UNSET
    interest: Union[Unset, "BillupdateFilesBodyDataInterest"] = UNSET
    issued_at: Union[Unset, datetime.date] = UNSET
    memo: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    purchase_order: Union[Unset, str] = UNSET
    secondary_tax_rate: Union[Unset, float] = UNSET
    state: Union[Unset, BillupdateFilesBodyDataState] = UNSET
    subject: Union[Unset, str] = UNSET
    tax_rate: Union[Unset, float] = UNSET
    use_grace_period: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bill_theme: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill_theme, Unset):
            bill_theme = self.bill_theme.to_dict()

        currency_id = self.currency_id

        discount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        due_at: Union[Unset, str] = UNSET
        if not isinstance(self.due_at, Unset):
            due_at = self.due_at.isoformat()

        interest: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.interest, Unset):
            interest = self.interest.to_dict()

        issued_at: Union[Unset, str] = UNSET
        if not isinstance(self.issued_at, Unset):
            issued_at = self.issued_at.isoformat()

        memo = self.memo

        number = self.number

        purchase_order = self.purchase_order

        secondary_tax_rate = self.secondary_tax_rate

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        subject = self.subject

        tax_rate = self.tax_rate

        use_grace_period = self.use_grace_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bill_theme is not UNSET:
            field_dict["bill_theme"] = bill_theme
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id
        if discount is not UNSET:
            field_dict["discount"] = discount
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if interest is not UNSET:
            field_dict["interest"] = interest
        if issued_at is not UNSET:
            field_dict["issued_at"] = issued_at
        if memo is not UNSET:
            field_dict["memo"] = memo
        if number is not UNSET:
            field_dict["number"] = number
        if purchase_order is not UNSET:
            field_dict["purchase_order"] = purchase_order
        if secondary_tax_rate is not UNSET:
            field_dict["secondary_tax_rate"] = secondary_tax_rate
        if state is not UNSET:
            field_dict["state"] = state
        if subject is not UNSET:
            field_dict["subject"] = subject
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if use_grace_period is not UNSET:
            field_dict["use_grace_period"] = use_grace_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billupdate_files_body_data_bill_theme import BillupdateFilesBodyDataBillTheme
        from ..models.billupdate_files_body_data_discount import BillupdateFilesBodyDataDiscount
        from ..models.billupdate_files_body_data_interest import BillupdateFilesBodyDataInterest

        d = dict(src_dict)
        _bill_theme = d.pop("bill_theme", UNSET)
        bill_theme: Union[Unset, BillupdateFilesBodyDataBillTheme]
        if isinstance(_bill_theme, Unset):
            bill_theme = UNSET
        else:
            bill_theme = BillupdateFilesBodyDataBillTheme.from_dict(_bill_theme)

        currency_id = d.pop("currency_id", UNSET)

        _discount = d.pop("discount", UNSET)
        discount: Union[Unset, BillupdateFilesBodyDataDiscount]
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = BillupdateFilesBodyDataDiscount.from_dict(_discount)

        _due_at = d.pop("due_at", UNSET)
        due_at: Union[Unset, datetime.date]
        if isinstance(_due_at, Unset):
            due_at = UNSET
        else:
            due_at = isoparse(_due_at).date()

        _interest = d.pop("interest", UNSET)
        interest: Union[Unset, BillupdateFilesBodyDataInterest]
        if isinstance(_interest, Unset):
            interest = UNSET
        else:
            interest = BillupdateFilesBodyDataInterest.from_dict(_interest)

        _issued_at = d.pop("issued_at", UNSET)
        issued_at: Union[Unset, datetime.date]
        if isinstance(_issued_at, Unset):
            issued_at = UNSET
        else:
            issued_at = isoparse(_issued_at).date()

        memo = d.pop("memo", UNSET)

        number = d.pop("number", UNSET)

        purchase_order = d.pop("purchase_order", UNSET)

        secondary_tax_rate = d.pop("secondary_tax_rate", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, BillupdateFilesBodyDataState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BillupdateFilesBodyDataState(_state)

        subject = d.pop("subject", UNSET)

        tax_rate = d.pop("tax_rate", UNSET)

        use_grace_period = d.pop("use_grace_period", UNSET)

        billupdate_files_body_data = cls(
            bill_theme=bill_theme,
            currency_id=currency_id,
            discount=discount,
            due_at=due_at,
            interest=interest,
            issued_at=issued_at,
            memo=memo,
            number=number,
            purchase_order=purchase_order,
            secondary_tax_rate=secondary_tax_rate,
            state=state,
            subject=subject,
            tax_rate=tax_rate,
            use_grace_period=use_grace_period,
        )

        billupdate_files_body_data.additional_properties = d
        return billupdate_files_body_data

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
