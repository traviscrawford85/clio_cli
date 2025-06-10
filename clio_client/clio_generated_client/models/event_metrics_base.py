from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventMetricsBase")


@_attrs_define
class EventMetricsBase:
    """
    Attributes:
        unread_mobile_events (Union[Unset, int]): The number of unread mobile event notifications for the current user
        unread_web_events (Union[Unset, int]): The number of unread web event notifications for the current user
        unread_secure_messages (Union[Unset, int]): The number of unread secure messages for the current user
        unread_client_portal_messages (Union[Unset, int]): The number of unread client portal messages for the current
            user
        unread_text_messages (Union[Unset, int]): The number of unread text messages for the current user
    """

    unread_mobile_events: Union[Unset, int] = UNSET
    unread_web_events: Union[Unset, int] = UNSET
    unread_secure_messages: Union[Unset, int] = UNSET
    unread_client_portal_messages: Union[Unset, int] = UNSET
    unread_text_messages: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unread_mobile_events = self.unread_mobile_events

        unread_web_events = self.unread_web_events

        unread_secure_messages = self.unread_secure_messages

        unread_client_portal_messages = self.unread_client_portal_messages

        unread_text_messages = self.unread_text_messages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unread_mobile_events is not UNSET:
            field_dict["unread_mobile_events"] = unread_mobile_events
        if unread_web_events is not UNSET:
            field_dict["unread_web_events"] = unread_web_events
        if unread_secure_messages is not UNSET:
            field_dict["unread_secure_messages"] = unread_secure_messages
        if unread_client_portal_messages is not UNSET:
            field_dict["unread_client_portal_messages"] = unread_client_portal_messages
        if unread_text_messages is not UNSET:
            field_dict["unread_text_messages"] = unread_text_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unread_mobile_events = d.pop("unread_mobile_events", UNSET)

        unread_web_events = d.pop("unread_web_events", UNSET)

        unread_secure_messages = d.pop("unread_secure_messages", UNSET)

        unread_client_portal_messages = d.pop("unread_client_portal_messages", UNSET)

        unread_text_messages = d.pop("unread_text_messages", UNSET)

        event_metrics_base = cls(
            unread_mobile_events=unread_mobile_events,
            unread_web_events=unread_web_events,
            unread_secure_messages=unread_secure_messages,
            unread_client_portal_messages=unread_client_portal_messages,
            unread_text_messages=unread_text_messages,
        )

        event_metrics_base.additional_properties = d
        return event_metrics_base

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
