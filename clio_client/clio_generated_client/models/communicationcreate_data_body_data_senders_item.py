from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.communicationcreate_data_body_data_senders_item_type import CommunicationcreateDataBodyDataSendersItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommunicationcreateDataBodyDataSendersItem")


@_attrs_define
class CommunicationcreateDataBodyDataSendersItem:
    """
    Attributes:
        field_deleted (Union[Unset, bool]): Whether or not the senders should be deleted.
        id (Union[Unset, int]): Unique ids for the senders of this Communication.
        type_ (Union[Unset, CommunicationcreateDataBodyDataSendersItemType]): Types of the senders of this
            Communication.
    """

    field_deleted: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    type_: Union[Unset, CommunicationcreateDataBodyDataSendersItemType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_deleted = self.field_deleted

        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_deleted is not UNSET:
            field_dict["_deleted"] = field_deleted
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_deleted = d.pop("_deleted", UNSET)

        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CommunicationcreateDataBodyDataSendersItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CommunicationcreateDataBodyDataSendersItemType(_type_)

        communicationcreate_data_body_data_senders_item = cls(
            field_deleted=field_deleted,
            id=id,
            type_=type_,
        )

        communicationcreate_data_body_data_senders_item.additional_properties = d
        return communicationcreate_data_body_data_senders_item

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
