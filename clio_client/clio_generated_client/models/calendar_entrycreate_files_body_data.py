import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.calendar_entrycreate_files_body_data_deleted import CalendarEntrycreateFilesBodyDataDeleted
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calendar_entrycreate_files_body_data_attendees_item import (
        CalendarEntrycreateFilesBodyDataAttendeesItem,
    )
    from ..models.calendar_entrycreate_files_body_data_calendar_entry_event_type import (
        CalendarEntrycreateFilesBodyDataCalendarEntryEventType,
    )
    from ..models.calendar_entrycreate_files_body_data_calendar_owner import (
        CalendarEntrycreateFilesBodyDataCalendarOwner,
    )
    from ..models.calendar_entrycreate_files_body_data_conference_meeting import (
        CalendarEntrycreateFilesBodyDataConferenceMeeting,
    )
    from ..models.calendar_entrycreate_files_body_data_external_properties_item import (
        CalendarEntrycreateFilesBodyDataExternalPropertiesItem,
    )
    from ..models.calendar_entrycreate_files_body_data_matter import CalendarEntrycreateFilesBodyDataMatter


T = TypeVar("T", bound="CalendarEntrycreateFilesBodyData")


@_attrs_define
class CalendarEntrycreateFilesBodyData:
    """
    Attributes:
        calendar_owner (CalendarEntrycreateFilesBodyDataCalendarOwner):
        end_at (datetime.datetime): The time the CalendarEntry ends (Expects an ISO-8601 timestamp).
        start_at (datetime.datetime): The time the CalendarEntry starts (Expects an ISO-8601 timestamp).
        summary (str): A short summary of the CalendarEntry.
        field_deleted (Union[Unset, CalendarEntrycreateFilesBodyDataDeleted]): Flag to delete a specific instance of a
            recurring event.
        all_day (Union[Unset, bool]): Whether or not the CalendarEntry is for all day.
        attendees (Union[Unset, list['CalendarEntrycreateFilesBodyDataAttendeesItem']]):
        calendar_entry_event_type (Union[Unset, CalendarEntrycreateFilesBodyDataCalendarEntryEventType]):
        conference_meeting (Union[Unset, CalendarEntrycreateFilesBodyDataConferenceMeeting]):
        description (Union[Unset, str]): A detailed description of the CalendarEntry.
        external_properties (Union[Unset, list['CalendarEntrycreateFilesBodyDataExternalPropertiesItem']]):
        location (Union[Unset, str]): The geographic location of the CalendarEntry.
        matter (Union[Unset, CalendarEntrycreateFilesBodyDataMatter]):
        recurrence_rule (Union[Unset, str]): Recurrence rule for expanding recurring CalendarEntry. To convert an
            existing recurring event to a non-recurring event, `''` or `null` are valid values.
        send_email_notification (Union[Unset, bool]): Whether the calendar Entry should send email notifications to
            attendees
    """

    calendar_owner: "CalendarEntrycreateFilesBodyDataCalendarOwner"
    end_at: datetime.datetime
    start_at: datetime.datetime
    summary: str
    field_deleted: Union[Unset, CalendarEntrycreateFilesBodyDataDeleted] = UNSET
    all_day: Union[Unset, bool] = UNSET
    attendees: Union[Unset, list["CalendarEntrycreateFilesBodyDataAttendeesItem"]] = UNSET
    calendar_entry_event_type: Union[Unset, "CalendarEntrycreateFilesBodyDataCalendarEntryEventType"] = UNSET
    conference_meeting: Union[Unset, "CalendarEntrycreateFilesBodyDataConferenceMeeting"] = UNSET
    description: Union[Unset, str] = UNSET
    external_properties: Union[Unset, list["CalendarEntrycreateFilesBodyDataExternalPropertiesItem"]] = UNSET
    location: Union[Unset, str] = UNSET
    matter: Union[Unset, "CalendarEntrycreateFilesBodyDataMatter"] = UNSET
    recurrence_rule: Union[Unset, str] = UNSET
    send_email_notification: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calendar_owner = self.calendar_owner.to_dict()

        end_at = self.end_at.isoformat()

        start_at = self.start_at.isoformat()

        summary = self.summary

        field_deleted: Union[Unset, str] = UNSET
        if not isinstance(self.field_deleted, Unset):
            field_deleted = self.field_deleted.value

        all_day = self.all_day

        attendees: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = []
            for attendees_item_data in self.attendees:
                attendees_item = attendees_item_data.to_dict()
                attendees.append(attendees_item)

        calendar_entry_event_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.calendar_entry_event_type, Unset):
            calendar_entry_event_type = self.calendar_entry_event_type.to_dict()

        conference_meeting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conference_meeting, Unset):
            conference_meeting = self.conference_meeting.to_dict()

        description = self.description

        external_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        location = self.location

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        recurrence_rule = self.recurrence_rule

        send_email_notification = self.send_email_notification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calendar_owner": calendar_owner,
                "end_at": end_at,
                "start_at": start_at,
                "summary": summary,
            }
        )
        if field_deleted is not UNSET:
            field_dict["_deleted"] = field_deleted
        if all_day is not UNSET:
            field_dict["all_day"] = all_day
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if calendar_entry_event_type is not UNSET:
            field_dict["calendar_entry_event_type"] = calendar_entry_event_type
        if conference_meeting is not UNSET:
            field_dict["conference_meeting"] = conference_meeting
        if description is not UNSET:
            field_dict["description"] = description
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if location is not UNSET:
            field_dict["location"] = location
        if matter is not UNSET:
            field_dict["matter"] = matter
        if recurrence_rule is not UNSET:
            field_dict["recurrence_rule"] = recurrence_rule
        if send_email_notification is not UNSET:
            field_dict["send_email_notification"] = send_email_notification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calendar_entrycreate_files_body_data_attendees_item import (
            CalendarEntrycreateFilesBodyDataAttendeesItem,
        )
        from ..models.calendar_entrycreate_files_body_data_calendar_entry_event_type import (
            CalendarEntrycreateFilesBodyDataCalendarEntryEventType,
        )
        from ..models.calendar_entrycreate_files_body_data_calendar_owner import (
            CalendarEntrycreateFilesBodyDataCalendarOwner,
        )
        from ..models.calendar_entrycreate_files_body_data_conference_meeting import (
            CalendarEntrycreateFilesBodyDataConferenceMeeting,
        )
        from ..models.calendar_entrycreate_files_body_data_external_properties_item import (
            CalendarEntrycreateFilesBodyDataExternalPropertiesItem,
        )
        from ..models.calendar_entrycreate_files_body_data_matter import CalendarEntrycreateFilesBodyDataMatter

        d = dict(src_dict)
        calendar_owner = CalendarEntrycreateFilesBodyDataCalendarOwner.from_dict(d.pop("calendar_owner"))

        end_at = isoparse(d.pop("end_at"))

        start_at = isoparse(d.pop("start_at"))

        summary = d.pop("summary")

        _field_deleted = d.pop("_deleted", UNSET)
        field_deleted: Union[Unset, CalendarEntrycreateFilesBodyDataDeleted]
        if isinstance(_field_deleted, Unset):
            field_deleted = UNSET
        else:
            field_deleted = CalendarEntrycreateFilesBodyDataDeleted(_field_deleted)

        all_day = d.pop("all_day", UNSET)

        attendees = []
        _attendees = d.pop("attendees", UNSET)
        for attendees_item_data in _attendees or []:
            attendees_item = CalendarEntrycreateFilesBodyDataAttendeesItem.from_dict(attendees_item_data)

            attendees.append(attendees_item)

        _calendar_entry_event_type = d.pop("calendar_entry_event_type", UNSET)
        calendar_entry_event_type: Union[Unset, CalendarEntrycreateFilesBodyDataCalendarEntryEventType]
        if isinstance(_calendar_entry_event_type, Unset):
            calendar_entry_event_type = UNSET
        else:
            calendar_entry_event_type = CalendarEntrycreateFilesBodyDataCalendarEntryEventType.from_dict(
                _calendar_entry_event_type
            )

        _conference_meeting = d.pop("conference_meeting", UNSET)
        conference_meeting: Union[Unset, CalendarEntrycreateFilesBodyDataConferenceMeeting]
        if isinstance(_conference_meeting, Unset):
            conference_meeting = UNSET
        else:
            conference_meeting = CalendarEntrycreateFilesBodyDataConferenceMeeting.from_dict(_conference_meeting)

        description = d.pop("description", UNSET)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = CalendarEntrycreateFilesBodyDataExternalPropertiesItem.from_dict(
                external_properties_item_data
            )

            external_properties.append(external_properties_item)

        location = d.pop("location", UNSET)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, CalendarEntrycreateFilesBodyDataMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = CalendarEntrycreateFilesBodyDataMatter.from_dict(_matter)

        recurrence_rule = d.pop("recurrence_rule", UNSET)

        send_email_notification = d.pop("send_email_notification", UNSET)

        calendar_entrycreate_files_body_data = cls(
            calendar_owner=calendar_owner,
            end_at=end_at,
            start_at=start_at,
            summary=summary,
            field_deleted=field_deleted,
            all_day=all_day,
            attendees=attendees,
            calendar_entry_event_type=calendar_entry_event_type,
            conference_meeting=conference_meeting,
            description=description,
            external_properties=external_properties,
            location=location,
            matter=matter,
            recurrence_rule=recurrence_rule,
            send_email_notification=send_email_notification,
        )

        calendar_entrycreate_files_body_data.additional_properties = d
        return calendar_entrycreate_files_body_data

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
