import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.notecreate_data_body_data_type import NotecreateDataBodyDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notecreate_data_body_data_contact import NotecreateDataBodyDataContact
    from ..models.notecreate_data_body_data_matter import NotecreateDataBodyDataMatter
    from ..models.notecreate_data_body_data_notification_event_subscribers_item import (
        NotecreateDataBodyDataNotificationEventSubscribersItem,
    )


T = TypeVar("T", bound="NotecreateDataBodyData")


@_attrs_define
class NotecreateDataBodyData:
    """
    Attributes:
        contact (NotecreateDataBodyDataContact):
        matter (NotecreateDataBodyDataMatter):
        type_ (NotecreateDataBodyDataType): Note type.
        date (Union[Unset, datetime.date]): Date for the Note. (Expects an ISO-8601 date).
        detail (Union[Unset, str]): Note body in text. This Note supports rich text when setting the `detail_text_type`
            field to `rich_text`. With supported tags such as `<a>`, `<b>`, `<br>`, `<div>`, `<em>`, `<i>` `<li>`, `<ol>`,
            `<p>`, `<s>`, `<strong>`, `<u>` and `<ul>`. This Note also supports attributes such as `href`, `rel`, `type`,
            and `target`.
        detail_text_type (Union[Unset, str]): The type of text in the detail field. Default: 'plain_text'.
        notification_event_subscribers (Union[Unset, list['NotecreateDataBodyDataNotificationEventSubscribersItem']]):
        subject (Union[Unset, str]): Note subject.
    """

    contact: "NotecreateDataBodyDataContact"
    matter: "NotecreateDataBodyDataMatter"
    type_: NotecreateDataBodyDataType
    date: Union[Unset, datetime.date] = UNSET
    detail: Union[Unset, str] = UNSET
    detail_text_type: Union[Unset, str] = "plain_text"
    notification_event_subscribers: Union[Unset, list["NotecreateDataBodyDataNotificationEventSubscribersItem"]] = UNSET
    subject: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact = self.contact.to_dict()

        matter = self.matter.to_dict()

        type_ = self.type_.value

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        detail = self.detail

        detail_text_type = self.detail_text_type

        notification_event_subscribers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_event_subscribers, Unset):
            notification_event_subscribers = []
            for notification_event_subscribers_item_data in self.notification_event_subscribers:
                notification_event_subscribers_item = notification_event_subscribers_item_data.to_dict()
                notification_event_subscribers.append(notification_event_subscribers_item)

        subject = self.subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact": contact,
                "matter": matter,
                "type": type_,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if detail is not UNSET:
            field_dict["detail"] = detail
        if detail_text_type is not UNSET:
            field_dict["detail_text_type"] = detail_text_type
        if notification_event_subscribers is not UNSET:
            field_dict["notification_event_subscribers"] = notification_event_subscribers
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notecreate_data_body_data_contact import NotecreateDataBodyDataContact
        from ..models.notecreate_data_body_data_matter import NotecreateDataBodyDataMatter
        from ..models.notecreate_data_body_data_notification_event_subscribers_item import (
            NotecreateDataBodyDataNotificationEventSubscribersItem,
        )

        d = dict(src_dict)
        contact = NotecreateDataBodyDataContact.from_dict(d.pop("contact"))

        matter = NotecreateDataBodyDataMatter.from_dict(d.pop("matter"))

        type_ = NotecreateDataBodyDataType(d.pop("type"))

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        detail = d.pop("detail", UNSET)

        detail_text_type = d.pop("detail_text_type", UNSET)

        notification_event_subscribers = []
        _notification_event_subscribers = d.pop("notification_event_subscribers", UNSET)
        for notification_event_subscribers_item_data in _notification_event_subscribers or []:
            notification_event_subscribers_item = NotecreateDataBodyDataNotificationEventSubscribersItem.from_dict(
                notification_event_subscribers_item_data
            )

            notification_event_subscribers.append(notification_event_subscribers_item)

        subject = d.pop("subject", UNSET)

        notecreate_data_body_data = cls(
            contact=contact,
            matter=matter,
            type_=type_,
            date=date,
            detail=detail,
            detail_text_type=detail_text_type,
            notification_event_subscribers=notification_event_subscribers,
            subject=subject,
        )

        notecreate_data_body_data.additional_properties = d
        return notecreate_data_body_data

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
