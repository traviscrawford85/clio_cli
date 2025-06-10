from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_actioncreate_data_body_data_ui_reference import CustomActioncreateDataBodyDataUiReference

T = TypeVar("T", bound="CustomActioncreateDataBodyData")


@_attrs_define
class CustomActioncreateDataBodyData:
    """
    Attributes:
        label (str): Text label to be displayed on the custom link.
        target_url (str): Target URL which will be opened in a new tab when the user clicks the custom link.
        ui_reference (CustomActioncreateDataBodyDataUiReference): UI reference location within Clio where the link will
            be displayed.
    """

    label: str
    target_url: str
    ui_reference: CustomActioncreateDataBodyDataUiReference
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        target_url = self.target_url

        ui_reference = self.ui_reference.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "target_url": target_url,
                "ui_reference": ui_reference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        target_url = d.pop("target_url")

        ui_reference = CustomActioncreateDataBodyDataUiReference(d.pop("ui_reference"))

        custom_actioncreate_data_body_data = cls(
            label=label,
            target_url=target_url,
            ui_reference=ui_reference,
        )

        custom_actioncreate_data_body_data.additional_properties = d
        return custom_actioncreate_data_body_data

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
