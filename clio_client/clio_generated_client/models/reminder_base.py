import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reminder_base_state import ReminderBaseState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReminderBase")


@_attrs_define
class ReminderBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Reminder*
        etag (Union[Unset, str]): ETag for the *Reminder*
        duration (Union[Unset, int]): Time in minutes to remind user before the subject
        next_delivery_at (Union[Unset, datetime.datetime]): The time the *Reminder* will be delivered (as a ISO-8601
            timestamp)
        state (Union[Unset, ReminderBaseState]): The current state of the *Reminder*
        created_at (Union[Unset, datetime.datetime]): The time the *Reminder* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Reminder* was last updated (as a ISO-8601 timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    next_delivery_at: Union[Unset, datetime.datetime] = UNSET
    state: Union[Unset, ReminderBaseState] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        duration = self.duration

        next_delivery_at: Union[Unset, str] = UNSET
        if not isinstance(self.next_delivery_at, Unset):
            next_delivery_at = self.next_delivery_at.isoformat()

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

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
        if etag is not UNSET:
            field_dict["etag"] = etag
        if duration is not UNSET:
            field_dict["duration"] = duration
        if next_delivery_at is not UNSET:
            field_dict["next_delivery_at"] = next_delivery_at
        if state is not UNSET:
            field_dict["state"] = state
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        duration = d.pop("duration", UNSET)

        _next_delivery_at = d.pop("next_delivery_at", UNSET)
        next_delivery_at: Union[Unset, datetime.datetime]
        if isinstance(_next_delivery_at, Unset):
            next_delivery_at = UNSET
        else:
            next_delivery_at = isoparse(_next_delivery_at)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ReminderBaseState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ReminderBaseState(_state)

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

        reminder_base = cls(
            id=id,
            etag=etag,
            duration=duration,
            next_delivery_at=next_delivery_at,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
        )

        reminder_base.additional_properties = d
        return reminder_base

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
