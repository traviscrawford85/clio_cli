from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.damagecreate_json_body_data import DamagecreateJsonBodyData


T = TypeVar("T", bound="DamagecreateJsonBody")


@_attrs_define
class DamagecreateJsonBody:
    """
    Attributes:
        data (DamagecreateJsonBodyData):
    """

    data: "DamagecreateJsonBodyData"
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
        from ..models.damagecreate_json_body_data import DamagecreateJsonBodyData

        d = dict(src_dict)
        data = DamagecreateJsonBodyData.from_dict(d.pop("data"))

        damagecreate_json_body = cls(
            data=data,
        )

        damagecreate_json_body.additional_properties = d
        return damagecreate_json_body

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
