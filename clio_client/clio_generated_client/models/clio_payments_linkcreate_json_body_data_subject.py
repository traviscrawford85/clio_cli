from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clio_payments_linkcreate_json_body_data_subject_type import ClioPaymentsLinkcreateJsonBodyDataSubjectType

T = TypeVar("T", bound="ClioPaymentsLinkcreateJsonBodyDataSubject")


@_attrs_define
class ClioPaymentsLinkcreateJsonBodyDataSubject:
    """
    Attributes:
        id (int): The ID of the record associated with the payment link.
        type_ (ClioPaymentsLinkcreateJsonBodyDataSubjectType): The type of the record associated with the payment link.
            The type of record determines the behavior of the payment link.

            Type of subject object:
            * 'BankAccount' results in a payment link for a direct payment.
            * 'Bill' results in a payment link for paying an existing invoice or trust request.
            * 'Contact' results in a payment link for paying the outstanding invoices of a contact.
    """

    id: int
    type_: ClioPaymentsLinkcreateJsonBodyDataSubjectType
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

        type_ = ClioPaymentsLinkcreateJsonBodyDataSubjectType(d.pop("type"))

        clio_payments_linkcreate_json_body_data_subject = cls(
            id=id,
            type_=type_,
        )

        clio_payments_linkcreate_json_body_data_subject.additional_properties = d
        return clio_payments_linkcreate_json_body_data_subject

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
