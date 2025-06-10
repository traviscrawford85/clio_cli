import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.damage_base_damage_type import DamageBaseDamageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matter_base import MatterBase


T = TypeVar("T", bound="Damage")


@_attrs_define
class Damage:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Damage*
        amount (Union[Unset, float]): Amount for Damage
        damage_type (Union[Unset, DamageBaseDamageType]): Damage type of the record
        description (Union[Unset, str]): Description for Damage
        etag (Union[Unset, str]): ETag for the *Damage*
        created_at (Union[Unset, datetime.datetime]): The time the *Damage* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Damage* was last updated (as a ISO-8601 timestamp)
        matter (Union[Unset, MatterBase]):
    """

    id: Union[Unset, int] = UNSET
    amount: Union[Unset, float] = UNSET
    damage_type: Union[Unset, DamageBaseDamageType] = UNSET
    description: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount = self.amount

        damage_type: Union[Unset, str] = UNSET
        if not isinstance(self.damage_type, Unset):
            damage_type = self.damage_type.value

        description = self.description

        etag = self.etag

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if damage_type is not UNSET:
            field_dict["damage_type"] = damage_type
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if matter is not UNSET:
            field_dict["matter"] = matter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matter_base import MatterBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        amount = d.pop("amount", UNSET)

        _damage_type = d.pop("damage_type", UNSET)
        damage_type: Union[Unset, DamageBaseDamageType]
        if isinstance(_damage_type, Unset):
            damage_type = UNSET
        else:
            damage_type = DamageBaseDamageType(_damage_type)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        damage = cls(
            id=id,
            amount=amount,
            damage_type=damage_type,
            description=description,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            matter=matter,
        )

        damage.additional_properties = d
        return damage

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
