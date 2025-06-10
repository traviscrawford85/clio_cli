import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.report_schedule_base_frequency import ReportScheduleBaseFrequency
from ..models.report_schedule_base_status import ReportScheduleBaseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportSchedule")


@_attrs_define
class ReportSchedule:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *ReportSchedule*
        etag (Union[Unset, str]): ETag for the *ReportSchedule*
        time_of_day (Union[Unset, datetime.datetime]): What time the Report Schedule is run
        frequency (Union[Unset, ReportScheduleBaseFrequency]): How often the Report Schedule is run
        days_of_week (Union[Unset, list[int]]): If the frequency is weekly, which days of the week the Report Schedule
            is run. Values are 0 to 6, representing Sunday to Saturday.
        day_of_month (Union[Unset, int]): If the frequency is monthly, which day of the month the Report Schedule is
            run. 32 is used to represent the last day of the month.
        status (Union[Unset, ReportScheduleBaseStatus]): The status of the Report Schedule
        status_updated_at (Union[Unset, datetime.datetime]): When the status of the Report Schedule was last updated
        next_scheduled_date (Union[Unset, datetime.datetime]): The next time the Report Schedule should run
        time_zone (Union[Unset, str]): Used in conjunction with `time_of_day` to determine when the Report Schedule
            should run
        report_preset_id (Union[Unset, int]): The unique identifier of the Report Preset to use when generating the
            scheduled report
        created_at (Union[Unset, datetime.datetime]): The time the *ReportSchedule* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *ReportSchedule* was last updated (as a ISO-8601
            timestamp)
        every_no_of_months (Union[Unset, int]): If the frequency is monthly, how many months between each run of the
            Report Schedule
        effective_from (Union[Unset, datetime.date]): The date the Report Schedule will become enabled (a ISO-8601 date)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    time_of_day: Union[Unset, datetime.datetime] = UNSET
    frequency: Union[Unset, ReportScheduleBaseFrequency] = UNSET
    days_of_week: Union[Unset, list[int]] = UNSET
    day_of_month: Union[Unset, int] = UNSET
    status: Union[Unset, ReportScheduleBaseStatus] = UNSET
    status_updated_at: Union[Unset, datetime.datetime] = UNSET
    next_scheduled_date: Union[Unset, datetime.datetime] = UNSET
    time_zone: Union[Unset, str] = UNSET
    report_preset_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    every_no_of_months: Union[Unset, int] = UNSET
    effective_from: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        time_of_day: Union[Unset, str] = UNSET
        if not isinstance(self.time_of_day, Unset):
            time_of_day = self.time_of_day.isoformat()

        frequency: Union[Unset, str] = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        days_of_week: Union[Unset, list[int]] = UNSET
        if not isinstance(self.days_of_week, Unset):
            days_of_week = self.days_of_week

        day_of_month = self.day_of_month

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.status_updated_at, Unset):
            status_updated_at = self.status_updated_at.isoformat()

        next_scheduled_date: Union[Unset, str] = UNSET
        if not isinstance(self.next_scheduled_date, Unset):
            next_scheduled_date = self.next_scheduled_date.isoformat()

        time_zone = self.time_zone

        report_preset_id = self.report_preset_id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        every_no_of_months = self.every_no_of_months

        effective_from: Union[Unset, str] = UNSET
        if not isinstance(self.effective_from, Unset):
            effective_from = self.effective_from.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if time_of_day is not UNSET:
            field_dict["time_of_day"] = time_of_day
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if days_of_week is not UNSET:
            field_dict["days_of_week"] = days_of_week
        if day_of_month is not UNSET:
            field_dict["day_of_month"] = day_of_month
        if status is not UNSET:
            field_dict["status"] = status
        if status_updated_at is not UNSET:
            field_dict["status_updated_at"] = status_updated_at
        if next_scheduled_date is not UNSET:
            field_dict["next_scheduled_date"] = next_scheduled_date
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if report_preset_id is not UNSET:
            field_dict["report_preset_id"] = report_preset_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if every_no_of_months is not UNSET:
            field_dict["every_no_of_months"] = every_no_of_months
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _time_of_day = d.pop("time_of_day", UNSET)
        time_of_day: Union[Unset, datetime.datetime]
        if isinstance(_time_of_day, Unset):
            time_of_day = UNSET
        else:
            time_of_day = isoparse(_time_of_day)

        _frequency = d.pop("frequency", UNSET)
        frequency: Union[Unset, ReportScheduleBaseFrequency]
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = ReportScheduleBaseFrequency(_frequency)

        days_of_week = cast(list[int], d.pop("days_of_week", UNSET))

        day_of_month = d.pop("day_of_month", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ReportScheduleBaseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ReportScheduleBaseStatus(_status)

        _status_updated_at = d.pop("status_updated_at", UNSET)
        status_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_status_updated_at, Unset):
            status_updated_at = UNSET
        else:
            status_updated_at = isoparse(_status_updated_at)

        _next_scheduled_date = d.pop("next_scheduled_date", UNSET)
        next_scheduled_date: Union[Unset, datetime.datetime]
        if isinstance(_next_scheduled_date, Unset):
            next_scheduled_date = UNSET
        else:
            next_scheduled_date = isoparse(_next_scheduled_date)

        time_zone = d.pop("time_zone", UNSET)

        report_preset_id = d.pop("report_preset_id", UNSET)

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

        every_no_of_months = d.pop("every_no_of_months", UNSET)

        _effective_from = d.pop("effective_from", UNSET)
        effective_from: Union[Unset, datetime.date]
        if isinstance(_effective_from, Unset):
            effective_from = UNSET
        else:
            effective_from = isoparse(_effective_from).date()

        report_schedule = cls(
            id=id,
            etag=etag,
            time_of_day=time_of_day,
            frequency=frequency,
            days_of_week=days_of_week,
            day_of_month=day_of_month,
            status=status,
            status_updated_at=status_updated_at,
            next_scheduled_date=next_scheduled_date,
            time_zone=time_zone,
            report_preset_id=report_preset_id,
            created_at=created_at,
            updated_at=updated_at,
            every_no_of_months=every_no_of_months,
            effective_from=effective_from,
        )

        report_schedule.additional_properties = d
        return report_schedule

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
