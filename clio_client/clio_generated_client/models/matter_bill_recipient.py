import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_base import ContactBase


T = TypeVar("T", bound="MatterBillRecipient")


@_attrs_define
class MatterBillRecipient:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]): The time the *MatterBillRecipient* was created (as a ISO-8601
            timestamp)
        etag (Union[Unset, str]): ETag for the *MatterBillRecipient*
        id (Union[Unset, int]): Unique identifier for the *MatterBillRecipient*
        updated_at (Union[Unset, datetime.datetime]): The time the *MatterBillRecipient* was last updated (as a ISO-8601
            timestamp)
        recipient (Union[Unset, ContactBase]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    recipient: Union[Unset, "ContactBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        etag = self.etag

        id = self.id

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        recipient: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if recipient is not UNSET:
            field_dict["recipient"] = recipient

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_base import ContactBase

        d = dict(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _recipient = d.pop("recipient", UNSET)
        recipient: Union[Unset, ContactBase]
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = ContactBase.from_dict(_recipient)

        matter_bill_recipient = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            updated_at=updated_at,
            recipient=recipient,
        )

        matter_bill_recipient.additional_properties = d
        return matter_bill_recipient

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
