from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactupdate_json_body_data_web_sites_item_name import ContactupdateJsonBodyDataWebSitesItemName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactupdateJsonBodyDataWebSitesItem")


@_attrs_define
class ContactupdateJsonBodyDataWebSitesItem:
    """
    Attributes:
        name (Union[Unset, ContactupdateJsonBodyDataWebSitesItemName]): Name of the WebSite. Default:
            ContactupdateJsonBodyDataWebSitesItemName.OTHER.
        address (Union[Unset, str]): URL of the WebSite.
        id (Union[Unset, int]): The unique identifier for a single WebSite associated with the Contact. The keyword
            `null` is not valid for this field.
        default_web_site (Union[Unset, bool]): Whether or not the Contact should be the default website for the Contact.
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated WebSite is present, the WebSite is deleted from the Contact.
    """

    name: Union[Unset, ContactupdateJsonBodyDataWebSitesItemName] = ContactupdateJsonBodyDataWebSitesItemName.OTHER
    address: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    default_web_site: Union[Unset, bool] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        address = self.address

        id = self.id

        default_web_site = self.default_web_site

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if id is not UNSET:
            field_dict["id"] = id
        if default_web_site is not UNSET:
            field_dict["default_web_site"] = default_web_site
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactupdateJsonBodyDataWebSitesItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactupdateJsonBodyDataWebSitesItemName(_name)

        address = d.pop("address", UNSET)

        id = d.pop("id", UNSET)

        default_web_site = d.pop("default_web_site", UNSET)

        field_destroy = d.pop("_destroy", UNSET)

        contactupdate_json_body_data_web_sites_item = cls(
            name=name,
            address=address,
            id=id,
            default_web_site=default_web_site,
            field_destroy=field_destroy,
        )

        contactupdate_json_body_data_web_sites_item.additional_properties = d
        return contactupdate_json_body_data_web_sites_item

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
