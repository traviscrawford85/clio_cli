from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remindercreate_data_body_data_subject_type import RemindercreateDataBodyDataSubjectType

T = TypeVar("T", bound="RemindercreateDataBodyDataSubject")


@_attrs_define
class RemindercreateDataBodyDataSubject:
    """
    Attributes:
        id (int): The unique identifier for a single CalendarEntry and Task associated with the Reminder. The keyword
            `null` is not valid for this field.
        type_ (RemindercreateDataBodyDataSubjectType): Model type of the Subject.
    """

    id: int
    type_: RemindercreateDataBodyDataSubjectType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = RemindercreateDataBodyDataSubjectType(d.pop("type"))

        remindercreate_data_body_data_subject = cls(
            id=id,
            type_=type_,
        )

        remindercreate_data_body_data_subject.additional_properties = d
        return remindercreate_data_body_data_subject

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
