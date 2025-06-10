import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_base import ActivityBase
    from ..models.attendee_base import AttendeeBase
    from ..models.calendar_base import CalendarBase
    from ..models.calendar_entry_base import CalendarEntryBase
    from ..models.calendar_entry_event_type_base import CalendarEntryEventTypeBase
    from ..models.conference_meeting_base import ConferenceMeetingBase
    from ..models.external_property_base import ExternalPropertyBase
    from ..models.matter_base import MatterBase
    from ..models.matter_docket_base import MatterDocketBase
    from ..models.reminder_base import ReminderBase


T = TypeVar("T", bound="CalendarEntry")


@_attrs_define
class CalendarEntry:
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
        time_entries (Union[Unset, list['ActivityBase']]): Activity
        conference_meeting (Union[Unset, ConferenceMeetingBase]):
        matter (Union[Unset, MatterBase]):
        matter_docket (Union[Unset, MatterDocketBase]):
        calendar_owner (Union[Unset, CalendarBase]):
        parent_calendar_entry (Union[Unset, CalendarEntryBase]):
        calendar_entry_event_type (Union[Unset, CalendarEntryEventTypeBase]):
        attendees (Union[Unset, list['AttendeeBase']]): Attendee
        calendars (Union[Unset, list['CalendarBase']]): Calendar
        reminders (Union[Unset, list['ReminderBase']]): Reminder
        external_properties (Union[Unset, list['ExternalPropertyBase']]): ExternalProperty
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
    time_entries: Union[Unset, list["ActivityBase"]] = UNSET
    conference_meeting: Union[Unset, "ConferenceMeetingBase"] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    matter_docket: Union[Unset, "MatterDocketBase"] = UNSET
    calendar_owner: Union[Unset, "CalendarBase"] = UNSET
    parent_calendar_entry: Union[Unset, "CalendarEntryBase"] = UNSET
    calendar_entry_event_type: Union[Unset, "CalendarEntryEventTypeBase"] = UNSET
    attendees: Union[Unset, list["AttendeeBase"]] = UNSET
    calendars: Union[Unset, list["CalendarBase"]] = UNSET
    reminders: Union[Unset, list["ReminderBase"]] = UNSET
    external_properties: Union[Unset, list["ExternalPropertyBase"]] = UNSET
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

        time_entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.time_entries, Unset):
            time_entries = []
            for time_entries_item_data in self.time_entries:
                time_entries_item = time_entries_item_data.to_dict()
                time_entries.append(time_entries_item)

        conference_meeting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conference_meeting, Unset):
            conference_meeting = self.conference_meeting.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        matter_docket: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter_docket, Unset):
            matter_docket = self.matter_docket.to_dict()

        calendar_owner: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.calendar_owner, Unset):
            calendar_owner = self.calendar_owner.to_dict()

        parent_calendar_entry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_calendar_entry, Unset):
            parent_calendar_entry = self.parent_calendar_entry.to_dict()

        calendar_entry_event_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.calendar_entry_event_type, Unset):
            calendar_entry_event_type = self.calendar_entry_event_type.to_dict()

        attendees: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = []
            for attendees_item_data in self.attendees:
                attendees_item = attendees_item_data.to_dict()
                attendees.append(attendees_item)

        calendars: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.calendars, Unset):
            calendars = []
            for calendars_item_data in self.calendars:
                calendars_item = calendars_item_data.to_dict()
                calendars.append(calendars_item)

        reminders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reminders, Unset):
            reminders = []
            for reminders_item_data in self.reminders:
                reminders_item = reminders_item_data.to_dict()
                reminders.append(reminders_item)

        external_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

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
        if time_entries is not UNSET:
            field_dict["time_entries"] = time_entries
        if conference_meeting is not UNSET:
            field_dict["conference_meeting"] = conference_meeting
        if matter is not UNSET:
            field_dict["matter"] = matter
        if matter_docket is not UNSET:
            field_dict["matter_docket"] = matter_docket
        if calendar_owner is not UNSET:
            field_dict["calendar_owner"] = calendar_owner
        if parent_calendar_entry is not UNSET:
            field_dict["parent_calendar_entry"] = parent_calendar_entry
        if calendar_entry_event_type is not UNSET:
            field_dict["calendar_entry_event_type"] = calendar_entry_event_type
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if calendars is not UNSET:
            field_dict["calendars"] = calendars
        if reminders is not UNSET:
            field_dict["reminders"] = reminders
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_base import ActivityBase
        from ..models.attendee_base import AttendeeBase
        from ..models.calendar_base import CalendarBase
        from ..models.calendar_entry_base import CalendarEntryBase
        from ..models.calendar_entry_event_type_base import CalendarEntryEventTypeBase
        from ..models.conference_meeting_base import ConferenceMeetingBase
        from ..models.external_property_base import ExternalPropertyBase
        from ..models.matter_base import MatterBase
        from ..models.matter_docket_base import MatterDocketBase
        from ..models.reminder_base import ReminderBase

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

        time_entries = []
        _time_entries = d.pop("time_entries", UNSET)
        for time_entries_item_data in _time_entries or []:
            time_entries_item = ActivityBase.from_dict(time_entries_item_data)

            time_entries.append(time_entries_item)

        _conference_meeting = d.pop("conference_meeting", UNSET)
        conference_meeting: Union[Unset, ConferenceMeetingBase]
        if isinstance(_conference_meeting, Unset):
            conference_meeting = UNSET
        else:
            conference_meeting = ConferenceMeetingBase.from_dict(_conference_meeting)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        _matter_docket = d.pop("matter_docket", UNSET)
        matter_docket: Union[Unset, MatterDocketBase]
        if isinstance(_matter_docket, Unset):
            matter_docket = UNSET
        else:
            matter_docket = MatterDocketBase.from_dict(_matter_docket)

        _calendar_owner = d.pop("calendar_owner", UNSET)
        calendar_owner: Union[Unset, CalendarBase]
        if isinstance(_calendar_owner, Unset):
            calendar_owner = UNSET
        else:
            calendar_owner = CalendarBase.from_dict(_calendar_owner)

        _parent_calendar_entry = d.pop("parent_calendar_entry", UNSET)
        parent_calendar_entry: Union[Unset, CalendarEntryBase]
        if isinstance(_parent_calendar_entry, Unset):
            parent_calendar_entry = UNSET
        else:
            parent_calendar_entry = CalendarEntryBase.from_dict(_parent_calendar_entry)

        _calendar_entry_event_type = d.pop("calendar_entry_event_type", UNSET)
        calendar_entry_event_type: Union[Unset, CalendarEntryEventTypeBase]
        if isinstance(_calendar_entry_event_type, Unset):
            calendar_entry_event_type = UNSET
        else:
            calendar_entry_event_type = CalendarEntryEventTypeBase.from_dict(_calendar_entry_event_type)

        attendees = []
        _attendees = d.pop("attendees", UNSET)
        for attendees_item_data in _attendees or []:
            attendees_item = AttendeeBase.from_dict(attendees_item_data)

            attendees.append(attendees_item)

        calendars = []
        _calendars = d.pop("calendars", UNSET)
        for calendars_item_data in _calendars or []:
            calendars_item = CalendarBase.from_dict(calendars_item_data)

            calendars.append(calendars_item)

        reminders = []
        _reminders = d.pop("reminders", UNSET)
        for reminders_item_data in _reminders or []:
            reminders_item = ReminderBase.from_dict(reminders_item_data)

            reminders.append(reminders_item)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = ExternalPropertyBase.from_dict(external_properties_item_data)

            external_properties.append(external_properties_item)

        calendar_entry = cls(
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
            time_entries=time_entries,
            conference_meeting=conference_meeting,
            matter=matter,
            matter_docket=matter_docket,
            calendar_owner=calendar_owner,
            parent_calendar_entry=parent_calendar_entry,
            calendar_entry_event_type=calendar_entry_event_type,
            attendees=attendees,
            calendars=calendars,
            reminders=reminders,
            external_properties=external_properties,
        )

        calendar_entry.additional_properties = d
        return calendar_entry

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
