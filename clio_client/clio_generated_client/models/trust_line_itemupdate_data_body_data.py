import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrustLineItemupdateDataBodyData")


@_attrs_define
class TrustLineItemupdateDataBodyData:
    """
    Attributes:
        date (Union[Unset, datetime.date]): Date for the TrustLineItem. (Expects an ISO-8601 date).
        note (Union[Unset, str]): Note for the TrustLineItem.
        total (Union[Unset, float]): Total amount the TrustLineItem is for.
    """

    date: Union[Unset, datetime.date] = UNSET
    note: Union[Unset, str] = UNSET
    total: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        note = self.note

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if note is not UNSET:
            field_dict["note"] = note
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        note = d.pop("note", UNSET)

        total = d.pop("total", UNSET)

        trust_line_itemupdate_data_body_data = cls(
            date=date,
            note=note,
            total=total,
        )

        trust_line_itemupdate_data_body_data.additional_properties = d
        return trust_line_itemupdate_data_body_data

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
