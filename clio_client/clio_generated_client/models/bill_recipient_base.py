import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillRecipientBase")


@_attrs_define
class BillRecipientBase:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]): The time the *BillRecipient* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *BillRecipient*
        id (Union[Unset, int]): Unique identifier for the *BillRecipient*
        on_all_matters (Union[Unset, bool]): If the associated contact is a recipient for all of the bill's matters
        updated_at (Union[Unset, datetime.datetime]): The time the *BillRecipient* was updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    on_all_matters: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        etag = self.etag

        id = self.id

        on_all_matters = self.on_all_matters

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if on_all_matters is not UNSET:
            field_dict["on_all_matters"] = on_all_matters
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        on_all_matters = d.pop("on_all_matters", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        bill_recipient_base = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            on_all_matters=on_all_matters,
            updated_at=updated_at,
        )

        bill_recipient_base.additional_properties = d
        return bill_recipient_base

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
