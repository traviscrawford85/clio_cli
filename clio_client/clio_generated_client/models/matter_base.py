import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.matter_base_billing_method import MatterBaseBillingMethod
from ..models.matter_base_status import MatterBaseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matter_base_currency import MatterBaseCurrency


T = TypeVar("T", bound="MatterBase")


@_attrs_define
class MatterBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Matter*
        etag (Union[Unset, str]): ETag for the *Matter*
        number (Union[Unset, int]): The number given to the *Matter* within an account
        display_number (Union[Unset, str]): The reference and label of the *Matter*. Depending on the account's
            manual_matter_numbering setting, this is either read only (generated) or customizable.
        custom_number (Union[Unset, str]): User defined custom number of the *Matter*
        currency (Union[Unset, MatterBaseCurrency]): Currency of the matter
        description (Union[Unset, str]): The detailed description of the *Matter*
        status (Union[Unset, MatterBaseStatus]): The current status of the *Matter*
        location (Union[Unset, str]): The location of the *Matter*
        client_reference (Union[Unset, str]): Client Reference string for external uses
        client_id (Union[Unset, int]): Client ID
        billable (Union[Unset, bool]): Whether this matter is billable
        maildrop_address (Union[Unset, str]): A unique Maildrop email address for the matter
        billing_method (Union[Unset, MatterBaseBillingMethod]): Billing method of this matter
        open_date (Union[Unset, datetime.date]): The date the matter was set to open (as a ISO-8601 date)
        close_date (Union[Unset, datetime.date]): The date the matter was set to closed (as a ISO-8601 date)
        pending_date (Union[Unset, datetime.date]): The date the matter was set to pending (as a ISO-8601 date)
        created_at (Union[Unset, datetime.datetime]): The time the *Matter* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Matter* was last updated (as a ISO-8601 timestamp)
        shared (Union[Unset, bool]): Whether the matter is currently shared with Clio Connect
        has_tasks (Union[Unset, bool]): Whether or not the matter has any tasks.
        last_activity_date (Union[Unset, datetime.date]): The greatest date out of all of the activities on the matter
            (as a ISO-8601 date)
        matter_stage_updated_at (Union[Unset, datetime.datetime]): The date the matter stage was last updated (as a
            ISO-8601 date)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    display_number: Union[Unset, str] = UNSET
    custom_number: Union[Unset, str] = UNSET
    currency: Union[Unset, "MatterBaseCurrency"] = UNSET
    description: Union[Unset, str] = UNSET
    status: Union[Unset, MatterBaseStatus] = UNSET
    location: Union[Unset, str] = UNSET
    client_reference: Union[Unset, str] = UNSET
    client_id: Union[Unset, int] = UNSET
    billable: Union[Unset, bool] = UNSET
    maildrop_address: Union[Unset, str] = UNSET
    billing_method: Union[Unset, MatterBaseBillingMethod] = UNSET
    open_date: Union[Unset, datetime.date] = UNSET
    close_date: Union[Unset, datetime.date] = UNSET
    pending_date: Union[Unset, datetime.date] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    shared: Union[Unset, bool] = UNSET
    has_tasks: Union[Unset, bool] = UNSET
    last_activity_date: Union[Unset, datetime.date] = UNSET
    matter_stage_updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        number = self.number

        display_number = self.display_number

        custom_number = self.custom_number

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        description = self.description

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        location = self.location

        client_reference = self.client_reference

        client_id = self.client_id

        billable = self.billable

        maildrop_address = self.maildrop_address

        billing_method: Union[Unset, str] = UNSET
        if not isinstance(self.billing_method, Unset):
            billing_method = self.billing_method.value

        open_date: Union[Unset, str] = UNSET
        if not isinstance(self.open_date, Unset):
            open_date = self.open_date.isoformat()

        close_date: Union[Unset, str] = UNSET
        if not isinstance(self.close_date, Unset):
            close_date = self.close_date.isoformat()

        pending_date: Union[Unset, str] = UNSET
        if not isinstance(self.pending_date, Unset):
            pending_date = self.pending_date.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        shared = self.shared

        has_tasks = self.has_tasks

        last_activity_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_activity_date, Unset):
            last_activity_date = self.last_activity_date.isoformat()

        matter_stage_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.matter_stage_updated_at, Unset):
            matter_stage_updated_at = self.matter_stage_updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if number is not UNSET:
            field_dict["number"] = number
        if display_number is not UNSET:
            field_dict["display_number"] = display_number
        if custom_number is not UNSET:
            field_dict["custom_number"] = custom_number
        if currency is not UNSET:
            field_dict["currency"] = currency
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if location is not UNSET:
            field_dict["location"] = location
        if client_reference is not UNSET:
            field_dict["client_reference"] = client_reference
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if billable is not UNSET:
            field_dict["billable"] = billable
        if maildrop_address is not UNSET:
            field_dict["maildrop_address"] = maildrop_address
        if billing_method is not UNSET:
            field_dict["billing_method"] = billing_method
        if open_date is not UNSET:
            field_dict["open_date"] = open_date
        if close_date is not UNSET:
            field_dict["close_date"] = close_date
        if pending_date is not UNSET:
            field_dict["pending_date"] = pending_date
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if shared is not UNSET:
            field_dict["shared"] = shared
        if has_tasks is not UNSET:
            field_dict["has_tasks"] = has_tasks
        if last_activity_date is not UNSET:
            field_dict["last_activity_date"] = last_activity_date
        if matter_stage_updated_at is not UNSET:
            field_dict["matter_stage_updated_at"] = matter_stage_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matter_base_currency import MatterBaseCurrency

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        number = d.pop("number", UNSET)

        display_number = d.pop("display_number", UNSET)

        custom_number = d.pop("custom_number", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, MatterBaseCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = MatterBaseCurrency.from_dict(_currency)

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, MatterBaseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MatterBaseStatus(_status)

        location = d.pop("location", UNSET)

        client_reference = d.pop("client_reference", UNSET)

        client_id = d.pop("client_id", UNSET)

        billable = d.pop("billable", UNSET)

        maildrop_address = d.pop("maildrop_address", UNSET)

        _billing_method = d.pop("billing_method", UNSET)
        billing_method: Union[Unset, MatterBaseBillingMethod]
        if isinstance(_billing_method, Unset):
            billing_method = UNSET
        else:
            billing_method = MatterBaseBillingMethod(_billing_method)

        _open_date = d.pop("open_date", UNSET)
        open_date: Union[Unset, datetime.date]
        if isinstance(_open_date, Unset):
            open_date = UNSET
        else:
            open_date = isoparse(_open_date).date()

        _close_date = d.pop("close_date", UNSET)
        close_date: Union[Unset, datetime.date]
        if isinstance(_close_date, Unset):
            close_date = UNSET
        else:
            close_date = isoparse(_close_date).date()

        _pending_date = d.pop("pending_date", UNSET)
        pending_date: Union[Unset, datetime.date]
        if isinstance(_pending_date, Unset):
            pending_date = UNSET
        else:
            pending_date = isoparse(_pending_date).date()

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

        shared = d.pop("shared", UNSET)

        has_tasks = d.pop("has_tasks", UNSET)

        _last_activity_date = d.pop("last_activity_date", UNSET)
        last_activity_date: Union[Unset, datetime.date]
        if isinstance(_last_activity_date, Unset):
            last_activity_date = UNSET
        else:
            last_activity_date = isoparse(_last_activity_date).date()

        _matter_stage_updated_at = d.pop("matter_stage_updated_at", UNSET)
        matter_stage_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_matter_stage_updated_at, Unset):
            matter_stage_updated_at = UNSET
        else:
            matter_stage_updated_at = isoparse(_matter_stage_updated_at)

        matter_base = cls(
            id=id,
            etag=etag,
            number=number,
            display_number=display_number,
            custom_number=custom_number,
            currency=currency,
            description=description,
            status=status,
            location=location,
            client_reference=client_reference,
            client_id=client_id,
            billable=billable,
            maildrop_address=maildrop_address,
            billing_method=billing_method,
            open_date=open_date,
            close_date=close_date,
            pending_date=pending_date,
            created_at=created_at,
            updated_at=updated_at,
            shared=shared,
            has_tasks=has_tasks,
            last_activity_date=last_activity_date,
            matter_stage_updated_at=matter_stage_updated_at,
        )

        matter_base.additional_properties = d
        return matter_base

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
