from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.documentcreate_data_body_data import DocumentcreateDataBodyData


T = TypeVar("T", bound="DocumentcreateDataBody")


@_attrs_define
class DocumentcreateDataBody:
    """
    Attributes:
        data (DocumentcreateDataBodyData):
    """

    data: "DocumentcreateDataBodyData"
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
        from ..models.documentcreate_data_body_data import DocumentcreateDataBodyData

        d = dict(src_dict)
        data = DocumentcreateDataBodyData.from_dict(d.pop("data"))

        documentcreate_data_body = cls(
            data=data,
        )

        documentcreate_data_body.additional_properties = d
        return documentcreate_data_body

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
