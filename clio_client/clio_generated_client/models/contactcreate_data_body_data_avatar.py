from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactcreateDataBodyDataAvatar")


@_attrs_define
class ContactcreateDataBodyDataAvatar:
    """
    Attributes:
        image (Union[Unset, str]): The avatar image for the *Contact*, base64-encoded. Must be a valid GIF, JPG, or PNG
            image of less than 2 megabytes in size.
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated Avatar is present, the Avatar is deleted from the Contact.
    """

    image: Union[Unset, str] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = d.pop("image", UNSET)

        field_destroy = d.pop("_destroy", UNSET)

        contactcreate_data_body_data_avatar = cls(
            image=image,
            field_destroy=field_destroy,
        )

        contactcreate_data_body_data_avatar.additional_properties = d
        return contactcreate_data_body_data_avatar

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
