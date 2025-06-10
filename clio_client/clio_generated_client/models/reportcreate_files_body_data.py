import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reportcreate_files_body_data_format import ReportcreateFilesBodyDataFormat
from ..models.reportcreate_files_body_data_kind import ReportcreateFilesBodyDataKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reportcreate_files_body_data_client import ReportcreateFilesBodyDataClient
    from ..models.reportcreate_files_body_data_matter import ReportcreateFilesBodyDataMatter
    from ..models.reportcreate_files_body_data_originating_attorney import ReportcreateFilesBodyDataOriginatingAttorney
    from ..models.reportcreate_files_body_data_practice_area import ReportcreateFilesBodyDataPracticeArea
    from ..models.reportcreate_files_body_data_responsible_attorney import ReportcreateFilesBodyDataResponsibleAttorney
    from ..models.reportcreate_files_body_data_user import ReportcreateFilesBodyDataUser


T = TypeVar("T", bound="ReportcreateFilesBodyData")


@_attrs_define
class ReportcreateFilesBodyData:
    """
    Attributes:
        format_ (ReportcreateFilesBodyDataFormat): What format the Report will be generated in.
        kind (ReportcreateFilesBodyDataKind): What kind of Report will be generated.
        client (Union[Unset, ReportcreateFilesBodyDataClient]):
        end_date (Union[Unset, datetime.date]): Filters Report data by date. (Expects an ISO-8601 date).
        matter (Union[Unset, ReportcreateFilesBodyDataMatter]):
        originating_attorney (Union[Unset, ReportcreateFilesBodyDataOriginatingAttorney]):
        practice_area (Union[Unset, ReportcreateFilesBodyDataPracticeArea]):
        responsible_attorney (Union[Unset, ReportcreateFilesBodyDataResponsibleAttorney]):
        start_date (Union[Unset, datetime.date]): Filters Report data by date. (Expects an ISO-8601 date).
        user (Union[Unset, ReportcreateFilesBodyDataUser]):
        year (Union[Unset, str]): Filters Report data by year. Sets start_date and end_date. (Expects a year).
    """

    format_: ReportcreateFilesBodyDataFormat
    kind: ReportcreateFilesBodyDataKind
    client: Union[Unset, "ReportcreateFilesBodyDataClient"] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    matter: Union[Unset, "ReportcreateFilesBodyDataMatter"] = UNSET
    originating_attorney: Union[Unset, "ReportcreateFilesBodyDataOriginatingAttorney"] = UNSET
    practice_area: Union[Unset, "ReportcreateFilesBodyDataPracticeArea"] = UNSET
    responsible_attorney: Union[Unset, "ReportcreateFilesBodyDataResponsibleAttorney"] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    user: Union[Unset, "ReportcreateFilesBodyDataUser"] = UNSET
    year: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_.value

        kind = self.kind.value

        client: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        originating_attorney: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.originating_attorney, Unset):
            originating_attorney = self.originating_attorney.to_dict()

        practice_area: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.practice_area, Unset):
            practice_area = self.practice_area.to_dict()

        responsible_attorney: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.responsible_attorney, Unset):
            responsible_attorney = self.responsible_attorney.to_dict()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "kind": kind,
            }
        )
        if client is not UNSET:
            field_dict["client"] = client
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if matter is not UNSET:
            field_dict["matter"] = matter
        if originating_attorney is not UNSET:
            field_dict["originating_attorney"] = originating_attorney
        if practice_area is not UNSET:
            field_dict["practice_area"] = practice_area
        if responsible_attorney is not UNSET:
            field_dict["responsible_attorney"] = responsible_attorney
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if user is not UNSET:
            field_dict["user"] = user
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reportcreate_files_body_data_client import ReportcreateFilesBodyDataClient
        from ..models.reportcreate_files_body_data_matter import ReportcreateFilesBodyDataMatter
        from ..models.reportcreate_files_body_data_originating_attorney import (
            ReportcreateFilesBodyDataOriginatingAttorney,
        )
        from ..models.reportcreate_files_body_data_practice_area import ReportcreateFilesBodyDataPracticeArea
        from ..models.reportcreate_files_body_data_responsible_attorney import (
            ReportcreateFilesBodyDataResponsibleAttorney,
        )
        from ..models.reportcreate_files_body_data_user import ReportcreateFilesBodyDataUser

        d = dict(src_dict)
        format_ = ReportcreateFilesBodyDataFormat(d.pop("format"))

        kind = ReportcreateFilesBodyDataKind(d.pop("kind"))

        _client = d.pop("client", UNSET)
        client: Union[Unset, ReportcreateFilesBodyDataClient]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = ReportcreateFilesBodyDataClient.from_dict(_client)

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, ReportcreateFilesBodyDataMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = ReportcreateFilesBodyDataMatter.from_dict(_matter)

        _originating_attorney = d.pop("originating_attorney", UNSET)
        originating_attorney: Union[Unset, ReportcreateFilesBodyDataOriginatingAttorney]
        if isinstance(_originating_attorney, Unset):
            originating_attorney = UNSET
        else:
            originating_attorney = ReportcreateFilesBodyDataOriginatingAttorney.from_dict(_originating_attorney)

        _practice_area = d.pop("practice_area", UNSET)
        practice_area: Union[Unset, ReportcreateFilesBodyDataPracticeArea]
        if isinstance(_practice_area, Unset):
            practice_area = UNSET
        else:
            practice_area = ReportcreateFilesBodyDataPracticeArea.from_dict(_practice_area)

        _responsible_attorney = d.pop("responsible_attorney", UNSET)
        responsible_attorney: Union[Unset, ReportcreateFilesBodyDataResponsibleAttorney]
        if isinstance(_responsible_attorney, Unset):
            responsible_attorney = UNSET
        else:
            responsible_attorney = ReportcreateFilesBodyDataResponsibleAttorney.from_dict(_responsible_attorney)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _user = d.pop("user", UNSET)
        user: Union[Unset, ReportcreateFilesBodyDataUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ReportcreateFilesBodyDataUser.from_dict(_user)

        year = d.pop("year", UNSET)

        reportcreate_files_body_data = cls(
            format_=format_,
            kind=kind,
            client=client,
            end_date=end_date,
            matter=matter,
            originating_attorney=originating_attorney,
            practice_area=practice_area,
            responsible_attorney=responsible_attorney,
            start_date=start_date,
            user=user,
            year=year,
        )

        reportcreate_files_body_data.additional_properties = d
        return reportcreate_files_body_data

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
