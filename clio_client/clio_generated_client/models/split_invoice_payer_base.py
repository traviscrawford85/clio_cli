import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SplitInvoicePayerBase")


@_attrs_define
class SplitInvoicePayerBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *SplitInvoicePayer*
        contact_id (Union[Unset, int]): The ID of the payer for the split invoice.
        matter_id (Union[Unset, int]): The ID of the Matter that has split invoicing enabled.
        send_to_bill_recipients (Union[Unset, bool]): Boolean to indicate if the sent bills should include bill
            recipients by default.
        split_portion (Union[Unset, float]): The percentage of the bill that the payer is responsible for.
        etag (Union[Unset, str]): ETag for the *SplitInvoicePayer*
        created_at (Union[Unset, datetime.datetime]): The time the *SplitInvoicePayer* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *SplitInvoicePayer* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    contact_id: Union[Unset, int] = UNSET
    matter_id: Union[Unset, int] = UNSET
    send_to_bill_recipients: Union[Unset, bool] = UNSET
    split_portion: Union[Unset, float] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        contact_id = self.contact_id

        matter_id = self.matter_id

        send_to_bill_recipients = self.send_to_bill_recipients

        split_portion = self.split_portion

        etag = self.etag

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if matter_id is not UNSET:
            field_dict["matter_id"] = matter_id
        if send_to_bill_recipients is not UNSET:
            field_dict["send_to_bill_recipients"] = send_to_bill_recipients
        if split_portion is not UNSET:
            field_dict["split_portion"] = split_portion
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        contact_id = d.pop("contact_id", UNSET)

        matter_id = d.pop("matter_id", UNSET)

        send_to_bill_recipients = d.pop("send_to_bill_recipients", UNSET)

        split_portion = d.pop("split_portion", UNSET)

        etag = d.pop("etag", UNSET)

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

        split_invoice_payer_base = cls(
            id=id,
            contact_id=contact_id,
            matter_id=matter_id,
            send_to_bill_recipients=send_to_bill_recipients,
            split_portion=split_portion,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
        )

        split_invoice_payer_base.additional_properties = d
        return split_invoice_payer_base

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
