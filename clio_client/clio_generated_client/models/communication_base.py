import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.communication_base_type import CommunicationBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommunicationBase")


@_attrs_define
class CommunicationBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Communication*
        etag (Union[Unset, str]): ETag for the *Communication*
        subject (Union[Unset, str]): The subject line of the *Communication*
        body (Union[Unset, str]): The main content of the *Communication*
        type_ (Union[Unset, CommunicationBaseType]): The type of the *Communication*
        date (Union[Unset, datetime.date]): The date of the *Communication* (as a ISO-8601 datestamp)
        time_entries_count (Union[Unset, int]): The number of time_entries associated with the *Communication*
        created_at (Union[Unset, datetime.datetime]): The time the *Communication* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Communication* was last updated (as a ISO-8601
            timestamp)
        received_at (Union[Unset, datetime.datetime]): The date-time of the *Communication* (in ISO-8601 format)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    type_: Union[Unset, CommunicationBaseType] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    time_entries_count: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    received_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        subject = self.subject

        body = self.body

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        time_entries_count = self.time_entries_count

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        received_at: Union[Unset, str] = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if type_ is not UNSET:
            field_dict["type"] = type_
        if date is not UNSET:
            field_dict["date"] = date
        if time_entries_count is not UNSET:
            field_dict["time_entries_count"] = time_entries_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if received_at is not UNSET:
            field_dict["received_at"] = received_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CommunicationBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CommunicationBaseType(_type_)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        time_entries_count = d.pop("time_entries_count", UNSET)

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

        _received_at = d.pop("received_at", UNSET)
        received_at: Union[Unset, datetime.datetime]
        if isinstance(_received_at, Unset):
            received_at = UNSET
        else:
            received_at = isoparse(_received_at)

        communication_base = cls(
            id=id,
            etag=etag,
            subject=subject,
            body=body,
            type_=type_,
            date=date,
            time_entries_count=time_entries_count,
            created_at=created_at,
            updated_at=updated_at,
            received_at=received_at,
        )

        communication_base.additional_properties = d
        return communication_base

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
