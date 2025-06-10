from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.timercreate_json_body_data import TimercreateJsonBodyData


T = TypeVar("T", bound="TimercreateJsonBody")


@_attrs_define
class TimercreateJsonBody:
    """
    Attributes:
        data (TimercreateJsonBodyData):
    """

    data: "TimercreateJsonBodyData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timercreate_json_body_data import TimercreateJsonBodyData

        d = dict(src_dict)
        data = TimercreateJsonBodyData.from_dict(d.pop("data"))

        timercreate_json_body = cls(
            data=data,
        )

        timercreate_json_body.additional_properties = d
        return timercreate_json_body

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
