import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventBase")


@_attrs_define
class EventBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Event*
        etag (Union[Unset, str]): ETag for the *Event*
        message (Union[Unset, str]): Concise headline message describing the event
        icon (Union[Unset, str]): Font Awesome icon to display (without the fa- prefix)
        title (Union[Unset, str]): The title or subject of the event (e.g. Matter Number, Document Title)
        title_url (Union[Unset, str]): Target URL that will be opened if the user clicks on the event title
        description (Union[Unset, str]): Description or additional information about the event (e.g. Matter Description)
        description_url (Union[Unset, str]): Target URL that will be opened if the user clicks on the event description
        primary_detail (Union[Unset, str]): Optional additional information about the event (e.g. Matter Client,
            Document Author)
        primary_detail_url (Union[Unset, str]): Target URL that will be opened if the user clicks on the primary detail
        secondary_detail (Union[Unset, str]): Optional additional information about the event (e.g. Matter Status,
            Document Size)
        secondary_detail_url (Union[Unset, str]): Target URL that will be opened if the user clicks on the secondary
            detail
        occurred_at (Union[Unset, datetime.datetime]): When the event occurred
        mobile_icon (Union[Unset, str]): Icon to be displayed in the mobile app
        subject_type (Union[Unset, str]): The type of subject that triggered the notification (e.g. Matter, Document)
        subject_id (Union[Unset, int]): Id of the subject that triggered the notification
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    title_url: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    description_url: Union[Unset, str] = UNSET
    primary_detail: Union[Unset, str] = UNSET
    primary_detail_url: Union[Unset, str] = UNSET
    secondary_detail: Union[Unset, str] = UNSET
    secondary_detail_url: Union[Unset, str] = UNSET
    occurred_at: Union[Unset, datetime.datetime] = UNSET
    mobile_icon: Union[Unset, str] = UNSET
    subject_type: Union[Unset, str] = UNSET
    subject_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        message = self.message

        icon = self.icon

        title = self.title

        title_url = self.title_url

        description = self.description

        description_url = self.description_url

        primary_detail = self.primary_detail

        primary_detail_url = self.primary_detail_url

        secondary_detail = self.secondary_detail

        secondary_detail_url = self.secondary_detail_url

        occurred_at: Union[Unset, str] = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        mobile_icon = self.mobile_icon

        subject_type = self.subject_type

        subject_id = self.subject_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if message is not UNSET:
            field_dict["message"] = message
        if icon is not UNSET:
            field_dict["icon"] = icon
        if title is not UNSET:
            field_dict["title"] = title
        if title_url is not UNSET:
            field_dict["title_url"] = title_url
        if description is not UNSET:
            field_dict["description"] = description
        if description_url is not UNSET:
            field_dict["description_url"] = description_url
        if primary_detail is not UNSET:
            field_dict["primary_detail"] = primary_detail
        if primary_detail_url is not UNSET:
            field_dict["primary_detail_url"] = primary_detail_url
        if secondary_detail is not UNSET:
            field_dict["secondary_detail"] = secondary_detail
        if secondary_detail_url is not UNSET:
            field_dict["secondary_detail_url"] = secondary_detail_url
        if occurred_at is not UNSET:
            field_dict["occurred_at"] = occurred_at
        if mobile_icon is not UNSET:
            field_dict["mobile_icon"] = mobile_icon
        if subject_type is not UNSET:
            field_dict["subject_type"] = subject_type
        if subject_id is not UNSET:
            field_dict["subject_id"] = subject_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        message = d.pop("message", UNSET)

        icon = d.pop("icon", UNSET)

        title = d.pop("title", UNSET)

        title_url = d.pop("title_url", UNSET)

        description = d.pop("description", UNSET)

        description_url = d.pop("description_url", UNSET)

        primary_detail = d.pop("primary_detail", UNSET)

        primary_detail_url = d.pop("primary_detail_url", UNSET)

        secondary_detail = d.pop("secondary_detail", UNSET)

        secondary_detail_url = d.pop("secondary_detail_url", UNSET)

        _occurred_at = d.pop("occurred_at", UNSET)
        occurred_at: Union[Unset, datetime.datetime]
        if isinstance(_occurred_at, Unset):
            occurred_at = UNSET
        else:
            occurred_at = isoparse(_occurred_at)

        mobile_icon = d.pop("mobile_icon", UNSET)

        subject_type = d.pop("subject_type", UNSET)

        subject_id = d.pop("subject_id", UNSET)

        event_base = cls(
            id=id,
            etag=etag,
            message=message,
            icon=icon,
            title=title,
            title_url=title_url,
            description=description,
            description_url=description_url,
            primary_detail=primary_detail,
            primary_detail_url=primary_detail_url,
            secondary_detail=secondary_detail,
            secondary_detail_url=secondary_detail_url,
            occurred_at=occurred_at,
            mobile_icon=mobile_icon,
            subject_type=subject_type,
            subject_id=subject_id,
        )

        event_base.additional_properties = d
        return event_base

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
