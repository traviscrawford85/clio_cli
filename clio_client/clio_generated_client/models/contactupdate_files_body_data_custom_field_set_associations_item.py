from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contactupdate_files_body_data_custom_field_set_associations_item_custom_field_set import (
        ContactupdateFilesBodyDataCustomFieldSetAssociationsItemCustomFieldSet,
    )


T = TypeVar("T", bound="ContactupdateFilesBodyDataCustomFieldSetAssociationsItem")


@_attrs_define
class ContactupdateFilesBodyDataCustomFieldSetAssociationsItem:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier for a single CustomFieldSetAssociation associated with the
            Contact. The keyword `null` is not valid for this field.
        display_order (Union[Unset, int]): The order to display the CustomFieldSet in a Contact. If not specified, it is
            added as the last CustomFieldSet of the Contact.
        custom_field_set (Union[Unset, ContactupdateFilesBodyDataCustomFieldSetAssociationsItemCustomFieldSet]):
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated CustomFieldSetAssociation is present, the CustomFieldSetAssociation is deleted from the Contact.
    """

    id: Union[Unset, int] = UNSET
    display_order: Union[Unset, int] = UNSET
    custom_field_set: Union[Unset, "ContactupdateFilesBodyDataCustomFieldSetAssociationsItemCustomFieldSet"] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_order = self.display_order

        custom_field_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_field_set, Unset):
            custom_field_set = self.custom_field_set.to_dict()

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_order is not UNSET:
            field_dict["display_order"] = display_order
        if custom_field_set is not UNSET:
            field_dict["custom_field_set"] = custom_field_set
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contactupdate_files_body_data_custom_field_set_associations_item_custom_field_set import (
            ContactupdateFilesBodyDataCustomFieldSetAssociationsItemCustomFieldSet,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        display_order = d.pop("display_order", UNSET)

        _custom_field_set = d.pop("custom_field_set", UNSET)
        custom_field_set: Union[Unset, ContactupdateFilesBodyDataCustomFieldSetAssociationsItemCustomFieldSet]
        if isinstance(_custom_field_set, Unset):
            custom_field_set = UNSET
        else:
            custom_field_set = ContactupdateFilesBodyDataCustomFieldSetAssociationsItemCustomFieldSet.from_dict(
                _custom_field_set
            )

        field_destroy = d.pop("_destroy", UNSET)

        contactupdate_files_body_data_custom_field_set_associations_item = cls(
            id=id,
            display_order=display_order,
            custom_field_set=custom_field_set,
            field_destroy=field_destroy,
        )

        contactupdate_files_body_data_custom_field_set_associations_item.additional_properties = d
        return contactupdate_files_body_data_custom_field_set_associations_item

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
