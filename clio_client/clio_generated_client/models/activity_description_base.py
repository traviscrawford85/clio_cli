import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_description_base_currency import ActivityDescriptionBaseCurrency


T = TypeVar("T", bound="ActivityDescriptionBase")


@_attrs_define
class ActivityDescriptionBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *ActivityDescription*
        etag (Union[Unset, str]): ETag for the *ActivityDescription*
        name (Union[Unset, str]): The name of the *ActivityDescription*
        visible_to_co_counsel (Union[Unset, bool]): A toggle that determines if a co-counsel user of the firm can have
            access to this activity description
        created_at (Union[Unset, datetime.datetime]): The time the *ActivityDescription* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *ActivityDescription* was last updated (as a ISO-8601
            timestamp)
        default (Union[Unset, bool]): Whether it is the user's default activity description
        type_ (Union[Unset, str]): The type of the *ActivityDescription*
        utbms_activity_id (Union[Unset, int]): The UTBMS activity id if the *ActivityDescription* is a UTBMS activity
            description
        utbms_task_name (Union[Unset, str]): The UTBMS activity task name if attached to a UTBMS activity description
        utbms_task_id (Union[Unset, int]): The UTBMS activity task id if attached to a UTBMS activity description
        xero_service_code (Union[Unset, str]): Custom Xero service code for this activity description
        accessible_to_user (Union[Unset, bool]): Determines if activity description is accessible to user
        category_type (Union[Unset, str]): Activity category rate type. Either hourly or flat fee
        currency (Union[Unset, ActivityDescriptionBaseCurrency]): The currency of the activity description
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    visible_to_co_counsel: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    default: Union[Unset, bool] = UNSET
    type_: Union[Unset, str] = UNSET
    utbms_activity_id: Union[Unset, int] = UNSET
    utbms_task_name: Union[Unset, str] = UNSET
    utbms_task_id: Union[Unset, int] = UNSET
    xero_service_code: Union[Unset, str] = UNSET
    accessible_to_user: Union[Unset, bool] = UNSET
    category_type: Union[Unset, str] = UNSET
    currency: Union[Unset, "ActivityDescriptionBaseCurrency"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        visible_to_co_counsel = self.visible_to_co_counsel

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        default = self.default

        type_ = self.type_

        utbms_activity_id = self.utbms_activity_id

        utbms_task_name = self.utbms_task_name

        utbms_task_id = self.utbms_task_id

        xero_service_code = self.xero_service_code

        accessible_to_user = self.accessible_to_user

        category_type = self.category_type

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if visible_to_co_counsel is not UNSET:
            field_dict["visible_to_co_counsel"] = visible_to_co_counsel
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if default is not UNSET:
            field_dict["default"] = default
        if type_ is not UNSET:
            field_dict["type"] = type_
        if utbms_activity_id is not UNSET:
            field_dict["utbms_activity_id"] = utbms_activity_id
        if utbms_task_name is not UNSET:
            field_dict["utbms_task_name"] = utbms_task_name
        if utbms_task_id is not UNSET:
            field_dict["utbms_task_id"] = utbms_task_id
        if xero_service_code is not UNSET:
            field_dict["xero_service_code"] = xero_service_code
        if accessible_to_user is not UNSET:
            field_dict["accessible_to_user"] = accessible_to_user
        if category_type is not UNSET:
            field_dict["category_type"] = category_type
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_description_base_currency import ActivityDescriptionBaseCurrency

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        visible_to_co_counsel = d.pop("visible_to_co_counsel", UNSET)

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

        default = d.pop("default", UNSET)

        type_ = d.pop("type", UNSET)

        utbms_activity_id = d.pop("utbms_activity_id", UNSET)

        utbms_task_name = d.pop("utbms_task_name", UNSET)

        utbms_task_id = d.pop("utbms_task_id", UNSET)

        xero_service_code = d.pop("xero_service_code", UNSET)

        accessible_to_user = d.pop("accessible_to_user", UNSET)

        category_type = d.pop("category_type", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, ActivityDescriptionBaseCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = ActivityDescriptionBaseCurrency.from_dict(_currency)

        activity_description_base = cls(
            id=id,
            etag=etag,
            name=name,
            visible_to_co_counsel=visible_to_co_counsel,
            created_at=created_at,
            updated_at=updated_at,
            default=default,
            type_=type_,
            utbms_activity_id=utbms_activity_id,
            utbms_task_name=utbms_task_name,
            utbms_task_id=utbms_task_id,
            xero_service_code=xero_service_code,
            accessible_to_user=accessible_to_user,
            category_type=category_type,
            currency=currency,
        )

        activity_description_base.additional_properties = d
        return activity_description_base

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
