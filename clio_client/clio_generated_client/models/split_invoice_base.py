import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SplitInvoiceBase")


@_attrs_define
class SplitInvoiceBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *SplitInvoice*
        bill_id (Union[Unset, int]): The ID of the bill that was split.
        linked_invoices_display_numbers (Union[Unset, list[str]]): Display numbers of all invoices split with this one.
        linked_invoices_ids (Union[Unset, list[int]]): IDs of all invoices split with this one.
        split_connection_id (Union[Unset, str]): UUID to determine which invoices are split together.
        split_portion (Union[Unset, float]): The percentage of the bill that the payer is responsible for.
        etag (Union[Unset, str]): ETag for the *SplitInvoice*
        created_at (Union[Unset, datetime.datetime]): The time the *SplitInvoice* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *SplitInvoice* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    bill_id: Union[Unset, int] = UNSET
    linked_invoices_display_numbers: Union[Unset, list[str]] = UNSET
    linked_invoices_ids: Union[Unset, list[int]] = UNSET
    split_connection_id: Union[Unset, str] = UNSET
    split_portion: Union[Unset, float] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        bill_id = self.bill_id

        linked_invoices_display_numbers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.linked_invoices_display_numbers, Unset):
            linked_invoices_display_numbers = self.linked_invoices_display_numbers

        linked_invoices_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.linked_invoices_ids, Unset):
            linked_invoices_ids = self.linked_invoices_ids

        split_connection_id = self.split_connection_id

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
        if bill_id is not UNSET:
            field_dict["bill_id"] = bill_id
        if linked_invoices_display_numbers is not UNSET:
            field_dict["linked_invoices_display_numbers"] = linked_invoices_display_numbers
        if linked_invoices_ids is not UNSET:
            field_dict["linked_invoices_ids"] = linked_invoices_ids
        if split_connection_id is not UNSET:
            field_dict["split_connection_id"] = split_connection_id
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

        bill_id = d.pop("bill_id", UNSET)

        linked_invoices_display_numbers = cast(list[str], d.pop("linked_invoices_display_numbers", UNSET))

        linked_invoices_ids = cast(list[int], d.pop("linked_invoices_ids", UNSET))

        split_connection_id = d.pop("split_connection_id", UNSET)

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

        split_invoice_base = cls(
            id=id,
            bill_id=bill_id,
            linked_invoices_display_numbers=linked_invoices_display_numbers,
            linked_invoices_ids=linked_invoices_ids,
            split_connection_id=split_connection_id,
            split_portion=split_portion,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
        )

        split_invoice_base.additional_properties = d
        return split_invoice_base

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
