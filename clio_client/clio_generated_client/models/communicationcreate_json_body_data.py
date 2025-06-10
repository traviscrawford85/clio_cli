from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.communicationcreate_json_body_data_type import CommunicationcreateJsonBodyDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.communicationcreate_json_body_data_external_properties_item import (
        CommunicationcreateJsonBodyDataExternalPropertiesItem,
    )
    from ..models.communicationcreate_json_body_data_matter import CommunicationcreateJsonBodyDataMatter
    from ..models.communicationcreate_json_body_data_notification_event_subscribers_item import (
        CommunicationcreateJsonBodyDataNotificationEventSubscribersItem,
    )
    from ..models.communicationcreate_json_body_data_receivers_item import CommunicationcreateJsonBodyDataReceiversItem
    from ..models.communicationcreate_json_body_data_senders_item import CommunicationcreateJsonBodyDataSendersItem


T = TypeVar("T", bound="CommunicationcreateJsonBodyData")


@_attrs_define
class CommunicationcreateJsonBodyData:
    """
    Attributes:
        body (str): The body value.
        subject (str): The subject value.
        type_ (CommunicationcreateJsonBodyDataType): Type of the Communication.
        date (Union[Unset, str]): The date for the Communication. (Expects an ISO-8601 date.)
        external_properties (Union[Unset, list['CommunicationcreateJsonBodyDataExternalPropertiesItem']]):
        matter (Union[Unset, CommunicationcreateJsonBodyDataMatter]):
        notification_event_subscribers (Union[Unset,
            list['CommunicationcreateJsonBodyDataNotificationEventSubscribersItem']]):
        received_at (Union[Unset, str]): The date-time for the Communication. (Expects an ISO-8601 date-time.)
        receivers (Union[Unset, list['CommunicationcreateJsonBodyDataReceiversItem']]):
        senders (Union[Unset, list['CommunicationcreateJsonBodyDataSendersItem']]):
    """

    body: str
    subject: str
    type_: CommunicationcreateJsonBodyDataType
    date: Union[Unset, str] = UNSET
    external_properties: Union[Unset, list["CommunicationcreateJsonBodyDataExternalPropertiesItem"]] = UNSET
    matter: Union[Unset, "CommunicationcreateJsonBodyDataMatter"] = UNSET
    notification_event_subscribers: Union[
        Unset, list["CommunicationcreateJsonBodyDataNotificationEventSubscribersItem"]
    ] = UNSET
    received_at: Union[Unset, str] = UNSET
    receivers: Union[Unset, list["CommunicationcreateJsonBodyDataReceiversItem"]] = UNSET
    senders: Union[Unset, list["CommunicationcreateJsonBodyDataSendersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        subject = self.subject

        type_ = self.type_.value

        date = self.date

        external_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        notification_event_subscribers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_event_subscribers, Unset):
            notification_event_subscribers = []
            for notification_event_subscribers_item_data in self.notification_event_subscribers:
                notification_event_subscribers_item = notification_event_subscribers_item_data.to_dict()
                notification_event_subscribers.append(notification_event_subscribers_item)

        received_at = self.received_at

        receivers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.receivers, Unset):
            receivers = []
            for receivers_item_data in self.receivers:
                receivers_item = receivers_item_data.to_dict()
                receivers.append(receivers_item)

        senders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.senders, Unset):
            senders = []
            for senders_item_data in self.senders:
                senders_item = senders_item_data.to_dict()
                senders.append(senders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "subject": subject,
                "type": type_,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if matter is not UNSET:
            field_dict["matter"] = matter
        if notification_event_subscribers is not UNSET:
            field_dict["notification_event_subscribers"] = notification_event_subscribers
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if receivers is not UNSET:
            field_dict["receivers"] = receivers
        if senders is not UNSET:
            field_dict["senders"] = senders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicationcreate_json_body_data_external_properties_item import (
            CommunicationcreateJsonBodyDataExternalPropertiesItem,
        )
        from ..models.communicationcreate_json_body_data_matter import CommunicationcreateJsonBodyDataMatter
        from ..models.communicationcreate_json_body_data_notification_event_subscribers_item import (
            CommunicationcreateJsonBodyDataNotificationEventSubscribersItem,
        )
        from ..models.communicationcreate_json_body_data_receivers_item import (
            CommunicationcreateJsonBodyDataReceiversItem,
        )
        from ..models.communicationcreate_json_body_data_senders_item import CommunicationcreateJsonBodyDataSendersItem

        d = dict(src_dict)
        body = d.pop("body")

        subject = d.pop("subject")

        type_ = CommunicationcreateJsonBodyDataType(d.pop("type"))

        date = d.pop("date", UNSET)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = CommunicationcreateJsonBodyDataExternalPropertiesItem.from_dict(
                external_properties_item_data
            )

            external_properties.append(external_properties_item)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, CommunicationcreateJsonBodyDataMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = CommunicationcreateJsonBodyDataMatter.from_dict(_matter)

        notification_event_subscribers = []
        _notification_event_subscribers = d.pop("notification_event_subscribers", UNSET)
        for notification_event_subscribers_item_data in _notification_event_subscribers or []:
            notification_event_subscribers_item = (
                CommunicationcreateJsonBodyDataNotificationEventSubscribersItem.from_dict(
                    notification_event_subscribers_item_data
                )
            )

            notification_event_subscribers.append(notification_event_subscribers_item)

        received_at = d.pop("received_at", UNSET)

        receivers = []
        _receivers = d.pop("receivers", UNSET)
        for receivers_item_data in _receivers or []:
            receivers_item = CommunicationcreateJsonBodyDataReceiversItem.from_dict(receivers_item_data)

            receivers.append(receivers_item)

        senders = []
        _senders = d.pop("senders", UNSET)
        for senders_item_data in _senders or []:
            senders_item = CommunicationcreateJsonBodyDataSendersItem.from_dict(senders_item_data)

            senders.append(senders_item)

        communicationcreate_json_body_data = cls(
            body=body,
            subject=subject,
            type_=type_,
            date=date,
            external_properties=external_properties,
            matter=matter,
            notification_event_subscribers=notification_event_subscribers,
            received_at=received_at,
            receivers=receivers,
            senders=senders,
        )

        communicationcreate_json_body_data.additional_properties = d
        return communicationcreate_json_body_data

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
