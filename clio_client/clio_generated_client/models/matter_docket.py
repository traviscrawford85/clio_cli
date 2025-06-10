import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calendar_entry_base import CalendarEntryBase
    from ..models.jurisdiction_base import JurisdictionBase
    from ..models.jurisdictions_to_trigger_base import JurisdictionsToTriggerBase
    from ..models.matter_base import MatterBase
    from ..models.service_type_base import ServiceTypeBase


T = TypeVar("T", bound="MatterDocket")


@_attrs_define
class MatterDocket:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *MatterDocket*
        etag (Union[Unset, str]): ETag for the *MatterDocket*
        name (Union[Unset, str]): The name of the *MatterDocket*
        start_date (Union[Unset, datetime.date]): The date the *MatterDocket* will start (as a ISO-8601 date)
        start_time (Union[Unset, datetime.datetime]): The time the *MatterDocket* will start, required for specific
            triggers (as a ISO-8601 timestamp)
        status (Union[Unset, str]): The status of the *MatterDocket* creation
        created_at (Union[Unset, datetime.datetime]): The time the *MatterDocket* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *MatterDocket* was last updated (as a ISO-8601
            timestamp)
        deleted_at (Union[Unset, datetime.datetime]): The time the *MatterDocket* was deleted (as a ISO-8601 timestamp)
        matter (Union[Unset, MatterBase]):
        jurisdiction (Union[Unset, JurisdictionBase]):
        trigger (Union[Unset, JurisdictionsToTriggerBase]):
        service_type (Union[Unset, ServiceTypeBase]):
        calendar_entries (Union[Unset, list['CalendarEntryBase']]): CalendarEntry
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    jurisdiction: Union[Unset, "JurisdictionBase"] = UNSET
    trigger: Union[Unset, "JurisdictionsToTriggerBase"] = UNSET
    service_type: Union[Unset, "ServiceTypeBase"] = UNSET
    calendar_entries: Union[Unset, list["CalendarEntryBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        status = self.status

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        deleted_at: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        jurisdiction: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.jurisdiction, Unset):
            jurisdiction = self.jurisdiction.to_dict()

        trigger: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.to_dict()

        service_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.service_type, Unset):
            service_type = self.service_type.to_dict()

        calendar_entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.calendar_entries, Unset):
            calendar_entries = []
            for calendar_entries_item_data in self.calendar_entries:
                calendar_entries_item = calendar_entries_item_data.to_dict()
                calendar_entries.append(calendar_entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if matter is not UNSET:
            field_dict["matter"] = matter
        if jurisdiction is not UNSET:
            field_dict["jurisdiction"] = jurisdiction
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if service_type is not UNSET:
            field_dict["service_type"] = service_type
        if calendar_entries is not UNSET:
            field_dict["calendar_entries"] = calendar_entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calendar_entry_base import CalendarEntryBase
        from ..models.jurisdiction_base import JurisdictionBase
        from ..models.jurisdictions_to_trigger_base import JurisdictionsToTriggerBase
        from ..models.matter_base import MatterBase
        from ..models.service_type_base import ServiceTypeBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _start_time = d.pop("start_time", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        status = d.pop("status", UNSET)

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

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: Union[Unset, datetime.datetime]
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        _jurisdiction = d.pop("jurisdiction", UNSET)
        jurisdiction: Union[Unset, JurisdictionBase]
        if isinstance(_jurisdiction, Unset):
            jurisdiction = UNSET
        else:
            jurisdiction = JurisdictionBase.from_dict(_jurisdiction)

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, JurisdictionsToTriggerBase]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = JurisdictionsToTriggerBase.from_dict(_trigger)

        _service_type = d.pop("service_type", UNSET)
        service_type: Union[Unset, ServiceTypeBase]
        if isinstance(_service_type, Unset):
            service_type = UNSET
        else:
            service_type = ServiceTypeBase.from_dict(_service_type)

        calendar_entries = []
        _calendar_entries = d.pop("calendar_entries", UNSET)
        for calendar_entries_item_data in _calendar_entries or []:
            calendar_entries_item = CalendarEntryBase.from_dict(calendar_entries_item_data)

            calendar_entries.append(calendar_entries_item)

        matter_docket = cls(
            id=id,
            etag=etag,
            name=name,
            start_date=start_date,
            start_time=start_time,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            matter=matter,
            jurisdiction=jurisdiction,
            trigger=trigger,
            service_type=service_type,
            calendar_entries=calendar_entries,
        )

        matter_docket.additional_properties = d
        return matter_docket

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
