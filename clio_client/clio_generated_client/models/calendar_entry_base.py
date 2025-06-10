import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarEntryBase")


@_attrs_define
class CalendarEntryBase:
    """
    Attributes:
        id (Union[Unset, str]): Unique identifier for the *CalendarEntry*
        etag (Union[Unset, str]): ETag for the *CalendarEntry*
        summary (Union[Unset, str]): A short summary of the *CalendarEntry*
        description (Union[Unset, str]): A detailed description of the *CalendarEntry*
        location (Union[Unset, str]): The geographic location of the *CalendarEntry*
        start_at (Union[Unset, datetime.datetime]): The time the *CalendarEntry* starts (as an ISO-8601 timestamp)
        end_at (Union[Unset, datetime.datetime]): The time the *CalendarEntry* ends (as an ISO-8601 timestamp)
        all_day (Union[Unset, bool]): Whether the event is all day
        recurrence_rule (Union[Unset, str]): Recurrence rule for expanding
        parent_calendar_entry_id (Union[Unset, int]): Identifier for the parent *CalendarEntry*
        court_rule (Union[Unset, bool]): Whether this event is associated with a Court Rule
        created_at (Union[Unset, datetime.datetime]): The time the *CalendarEntry* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *CalendarEntry* was last updated (as a ISO-8601
            timestamp)
        permission (Union[Unset, str]): The view permission for the current user, will return 'viewer' when permission
            is 'limited_viewer' and the user is an attendee.
        calendar_owner_id (Union[Unset, int]): The id of the calendar owner.
        start_at_time_zone (Union[Unset, str]): Original start at time zone of the event.
        time_entries_count (Union[Unset, int]): The number of `TimeEntry` activities associated with the *CalendarEntry*
    """

    id: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    start_at: Union[Unset, datetime.datetime] = UNSET
    end_at: Union[Unset, datetime.datetime] = UNSET
    all_day: Union[Unset, bool] = UNSET
    recurrence_rule: Union[Unset, str] = UNSET
    parent_calendar_entry_id: Union[Unset, int] = UNSET
    court_rule: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    permission: Union[Unset, str] = UNSET
    calendar_owner_id: Union[Unset, int] = UNSET
    start_at_time_zone: Union[Unset, str] = UNSET
    time_entries_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        summary = self.summary

        description = self.description

        location = self.location

        start_at: Union[Unset, str] = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        end_at: Union[Unset, str] = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        all_day = self.all_day

        recurrence_rule = self.recurrence_rule

        parent_calendar_entry_id = self.parent_calendar_entry_id

        court_rule = self.court_rule

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        permission = self.permission

        calendar_owner_id = self.calendar_owner_id

        start_at_time_zone = self.start_at_time_zone

        time_entries_count = self.time_entries_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if all_day is not UNSET:
            field_dict["all_day"] = all_day
        if recurrence_rule is not UNSET:
            field_dict["recurrence_rule"] = recurrence_rule
        if parent_calendar_entry_id is not UNSET:
            field_dict["parent_calendar_entry_id"] = parent_calendar_entry_id
        if court_rule is not UNSET:
            field_dict["court_rule"] = court_rule
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if permission is not UNSET:
            field_dict["permission"] = permission
        if calendar_owner_id is not UNSET:
            field_dict["calendar_owner_id"] = calendar_owner_id
        if start_at_time_zone is not UNSET:
            field_dict["start_at_time_zone"] = start_at_time_zone
        if time_entries_count is not UNSET:
            field_dict["time_entries_count"] = time_entries_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        summary = d.pop("summary", UNSET)

        description = d.pop("description", UNSET)

        location = d.pop("location", UNSET)

        _start_at = d.pop("start_at", UNSET)
        start_at: Union[Unset, datetime.datetime]
        if isinstance(_start_at, Unset):
            start_at = UNSET
        else:
            start_at = isoparse(_start_at)

        _end_at = d.pop("end_at", UNSET)
        end_at: Union[Unset, datetime.datetime]
        if isinstance(_end_at, Unset):
            end_at = UNSET
        else:
            end_at = isoparse(_end_at)

        all_day = d.pop("all_day", UNSET)

        recurrence_rule = d.pop("recurrence_rule", UNSET)

        parent_calendar_entry_id = d.pop("parent_calendar_entry_id", UNSET)

        court_rule = d.pop("court_rule", UNSET)

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

        permission = d.pop("permission", UNSET)

        calendar_owner_id = d.pop("calendar_owner_id", UNSET)

        start_at_time_zone = d.pop("start_at_time_zone", UNSET)

        time_entries_count = d.pop("time_entries_count", UNSET)

        calendar_entry_base = cls(
            id=id,
            etag=etag,
            summary=summary,
            description=description,
            location=location,
            start_at=start_at,
            end_at=end_at,
            all_day=all_day,
            recurrence_rule=recurrence_rule,
            parent_calendar_entry_id=parent_calendar_entry_id,
            court_rule=court_rule,
            created_at=created_at,
            updated_at=updated_at,
            permission=permission,
            calendar_owner_id=calendar_owner_id,
            start_at_time_zone=start_at_time_zone,
            time_entries_count=time_entries_count,
        )

        calendar_entry_base.additional_properties = d
        return calendar_entry_base

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
