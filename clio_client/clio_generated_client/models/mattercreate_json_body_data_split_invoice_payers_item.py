from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MattercreateJsonBodyDataSplitInvoicePayersItem")


@_attrs_define
class MattercreateJsonBodyDataSplitInvoicePayersItem:
    """
    Attributes:
        contact_id (int): Contact id for the matter payer.
        split_portion (float): The split portion for the payer.
        send_to_bill_recipients (Union[Unset, bool]): Boolean indication to send a split invoice to all bill recipients.
    """

    contact_id: int
    split_portion: float
    send_to_bill_recipients: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_id = self.contact_id

        split_portion = self.split_portion

        send_to_bill_recipients = self.send_to_bill_recipients

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact_id": contact_id,
                "split_portion": split_portion,
            }
        )
        if send_to_bill_recipients is not UNSET:
            field_dict["send_to_bill_recipients"] = send_to_bill_recipients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact_id = d.pop("contact_id")

        split_portion = d.pop("split_portion")

        send_to_bill_recipients = d.pop("send_to_bill_recipients", UNSET)

        mattercreate_json_body_data_split_invoice_payers_item = cls(
            contact_id=contact_id,
            split_portion=split_portion,
            send_to_bill_recipients=send_to_bill_recipients,
        )

        mattercreate_json_body_data_split_invoice_payers_item.additional_properties = d
        return mattercreate_json_body_data_split_invoice_payers_item

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
