import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.trust_requestcreate_json_body_data_trust_type import TrustRequestcreateJsonBodyDataTrustType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trust_requestcreate_json_body_data_matter_item import TrustRequestcreateJsonBodyDataMatterItem


T = TypeVar("T", bound="TrustRequestcreateJsonBodyData")


@_attrs_define
class TrustRequestcreateJsonBodyData:
    """
    Attributes:
        approved (bool): Whether or not the TrustRequest should be automatically approved.
        client_id (int): The client_id associated to the TrustRequest
        due_date (datetime.date): The date the TrustRequest is due (Expects an ISO-8601 date).
        issue_date (datetime.date): The date the TrustRequest is issued (Expects an ISO-8601 date).
        trust_amount (float): The TrustRequest's amount
        trust_type (TrustRequestcreateJsonBodyDataTrustType): The type of TrustRequest
        currency_id (Union[Unset, int]): The currency_id associated to the TrustRequest
        matter (Union[Unset, list['TrustRequestcreateJsonBodyDataMatterItem']]):
        note (Union[Unset, str]): The client level TrustRequest note
    """

    approved: bool
    client_id: int
    due_date: datetime.date
    issue_date: datetime.date
    trust_amount: float
    trust_type: TrustRequestcreateJsonBodyDataTrustType
    currency_id: Union[Unset, int] = UNSET
    matter: Union[Unset, list["TrustRequestcreateJsonBodyDataMatterItem"]] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approved = self.approved

        client_id = self.client_id

        due_date = self.due_date.isoformat()

        issue_date = self.issue_date.isoformat()

        trust_amount = self.trust_amount

        trust_type = self.trust_type.value

        currency_id = self.currency_id

        matter: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = []
            for matter_item_data in self.matter:
                matter_item = matter_item_data.to_dict()
                matter.append(matter_item)

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approved": approved,
                "client_id": client_id,
                "due_date": due_date,
                "issue_date": issue_date,
                "trust_amount": trust_amount,
                "trust_type": trust_type,
            }
        )
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id
        if matter is not UNSET:
            field_dict["matter"] = matter
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trust_requestcreate_json_body_data_matter_item import TrustRequestcreateJsonBodyDataMatterItem

        d = dict(src_dict)
        approved = d.pop("approved")

        client_id = d.pop("client_id")

        due_date = isoparse(d.pop("due_date")).date()

        issue_date = isoparse(d.pop("issue_date")).date()

        trust_amount = d.pop("trust_amount")

        trust_type = TrustRequestcreateJsonBodyDataTrustType(d.pop("trust_type"))

        currency_id = d.pop("currency_id", UNSET)

        matter = []
        _matter = d.pop("matter", UNSET)
        for matter_item_data in _matter or []:
            matter_item = TrustRequestcreateJsonBodyDataMatterItem.from_dict(matter_item_data)

            matter.append(matter_item)

        note = d.pop("note", UNSET)

        trust_requestcreate_json_body_data = cls(
            approved=approved,
            client_id=client_id,
            due_date=due_date,
            issue_date=issue_date,
            trust_amount=trust_amount,
            trust_type=trust_type,
            currency_id=currency_id,
            matter=matter,
            note=note,
        )

        trust_requestcreate_json_body_data.additional_properties = d
        return trust_requestcreate_json_body_data

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
