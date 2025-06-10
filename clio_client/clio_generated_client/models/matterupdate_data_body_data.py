import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.matterupdate_data_body_data_status import MatterupdateDataBodyDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matterupdate_data_body_data_client import MatterupdateDataBodyDataClient
    from ..models.matterupdate_data_body_data_currency import MatterupdateDataBodyDataCurrency
    from ..models.matterupdate_data_body_data_custom_field_set_associations_item import (
        MatterupdateDataBodyDataCustomFieldSetAssociationsItem,
    )
    from ..models.matterupdate_data_body_data_custom_field_values_item import (
        MatterupdateDataBodyDataCustomFieldValuesItem,
    )
    from ..models.matterupdate_data_body_data_custom_rate import MatterupdateDataBodyDataCustomRate
    from ..models.matterupdate_data_body_data_evergreen_retainer import MatterupdateDataBodyDataEvergreenRetainer
    from ..models.matterupdate_data_body_data_group import MatterupdateDataBodyDataGroup
    from ..models.matterupdate_data_body_data_matter_budget import MatterupdateDataBodyDataMatterBudget
    from ..models.matterupdate_data_body_data_matter_stage import MatterupdateDataBodyDataMatterStage
    from ..models.matterupdate_data_body_data_originating_attorney import MatterupdateDataBodyDataOriginatingAttorney
    from ..models.matterupdate_data_body_data_practice_area import MatterupdateDataBodyDataPracticeArea
    from ..models.matterupdate_data_body_data_relationships_item import MatterupdateDataBodyDataRelationshipsItem
    from ..models.matterupdate_data_body_data_responsible_attorney import MatterupdateDataBodyDataResponsibleAttorney
    from ..models.matterupdate_data_body_data_responsible_staff import MatterupdateDataBodyDataResponsibleStaff
    from ..models.matterupdate_data_body_data_split_invoice_payers_item import (
        MatterupdateDataBodyDataSplitInvoicePayersItem,
    )
    from ..models.matterupdate_data_body_data_statute_of_limitations import MatterupdateDataBodyDataStatuteOfLimitations
    from ..models.matterupdate_data_body_data_task_template_list_instances_item import (
        MatterupdateDataBodyDataTaskTemplateListInstancesItem,
    )


T = TypeVar("T", bound="MatterupdateDataBodyData")


@_attrs_define
class MatterupdateDataBodyData:
    """
    Attributes:
        billable (Union[Unset, bool]): Whether or not the matter is billable. Default: True.
        client (Union[Unset, MatterupdateDataBodyDataClient]):
        client_reference (Union[Unset, str]): Client Reference string for external uses.
        close_date (Union[Unset, datetime.date]): Date the Matter was set to closed. (Expects an ISO-8601 date).
        currency (Union[Unset, MatterupdateDataBodyDataCurrency]): Currency of the matter
        custom_field_set_associations (Union[Unset, list['MatterupdateDataBodyDataCustomFieldSetAssociationsItem']]):
        custom_field_values (Union[Unset, list['MatterupdateDataBodyDataCustomFieldValuesItem']]):
        custom_rate (Union[Unset, MatterupdateDataBodyDataCustomRate]):
        description (Union[Unset, str]): Detailed description of the Matter.
        display_number (Union[Unset, str]): Matter reference and label. Depending on the account's
            manual_matter_numbering setting, this is either read only (generated), or customizable.
        evergreen_retainer (Union[Unset, MatterupdateDataBodyDataEvergreenRetainer]):
        group (Union[Unset, MatterupdateDataBodyDataGroup]):
        location (Union[Unset, str]): Location of the Matter.
        matter_budget (Union[Unset, MatterupdateDataBodyDataMatterBudget]):
        matter_stage (Union[Unset, MatterupdateDataBodyDataMatterStage]):
        open_date (Union[Unset, datetime.date]): Date the Matter was set to open. (Expects an ISO-8601 date).
        originating_attorney (Union[Unset, MatterupdateDataBodyDataOriginatingAttorney]):
        pending_date (Union[Unset, datetime.date]): Date the Matter was set to pending. (Expects an ISO-8601 date).
        practice_area (Union[Unset, MatterupdateDataBodyDataPracticeArea]):
        relationships (Union[Unset, list['MatterupdateDataBodyDataRelationshipsItem']]):
        reset_matter_number (Union[Unset, bool]): Defaults to false. Resets the matter's number based on the account's
            matter numbering scheme. Default: False.
        responsible_attorney (Union[Unset, MatterupdateDataBodyDataResponsibleAttorney]):
        responsible_staff (Union[Unset, MatterupdateDataBodyDataResponsibleStaff]):
        split_invoice_payers (Union[Unset, list['MatterupdateDataBodyDataSplitInvoicePayersItem']]):
        status (Union[Unset, MatterupdateDataBodyDataStatus]): Matter status.
        statute_of_limitations (Union[Unset, MatterupdateDataBodyDataStatuteOfLimitations]):
        task_template_list_instances (Union[Unset, list['MatterupdateDataBodyDataTaskTemplateListInstancesItem']]):
    """

    billable: Union[Unset, bool] = True
    client: Union[Unset, "MatterupdateDataBodyDataClient"] = UNSET
    client_reference: Union[Unset, str] = UNSET
    close_date: Union[Unset, datetime.date] = UNSET
    currency: Union[Unset, "MatterupdateDataBodyDataCurrency"] = UNSET
    custom_field_set_associations: Union[Unset, list["MatterupdateDataBodyDataCustomFieldSetAssociationsItem"]] = UNSET
    custom_field_values: Union[Unset, list["MatterupdateDataBodyDataCustomFieldValuesItem"]] = UNSET
    custom_rate: Union[Unset, "MatterupdateDataBodyDataCustomRate"] = UNSET
    description: Union[Unset, str] = UNSET
    display_number: Union[Unset, str] = UNSET
    evergreen_retainer: Union[Unset, "MatterupdateDataBodyDataEvergreenRetainer"] = UNSET
    group: Union[Unset, "MatterupdateDataBodyDataGroup"] = UNSET
    location: Union[Unset, str] = UNSET
    matter_budget: Union[Unset, "MatterupdateDataBodyDataMatterBudget"] = UNSET
    matter_stage: Union[Unset, "MatterupdateDataBodyDataMatterStage"] = UNSET
    open_date: Union[Unset, datetime.date] = UNSET
    originating_attorney: Union[Unset, "MatterupdateDataBodyDataOriginatingAttorney"] = UNSET
    pending_date: Union[Unset, datetime.date] = UNSET
    practice_area: Union[Unset, "MatterupdateDataBodyDataPracticeArea"] = UNSET
    relationships: Union[Unset, list["MatterupdateDataBodyDataRelationshipsItem"]] = UNSET
    reset_matter_number: Union[Unset, bool] = False
    responsible_attorney: Union[Unset, "MatterupdateDataBodyDataResponsibleAttorney"] = UNSET
    responsible_staff: Union[Unset, "MatterupdateDataBodyDataResponsibleStaff"] = UNSET
    split_invoice_payers: Union[Unset, list["MatterupdateDataBodyDataSplitInvoicePayersItem"]] = UNSET
    status: Union[Unset, MatterupdateDataBodyDataStatus] = UNSET
    statute_of_limitations: Union[Unset, "MatterupdateDataBodyDataStatuteOfLimitations"] = UNSET
    task_template_list_instances: Union[Unset, list["MatterupdateDataBodyDataTaskTemplateListInstancesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billable = self.billable

        client: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        client_reference = self.client_reference

        close_date: Union[Unset, str] = UNSET
        if not isinstance(self.close_date, Unset):
            close_date = self.close_date.isoformat()

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        custom_field_set_associations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_field_set_associations, Unset):
            custom_field_set_associations = []
            for custom_field_set_associations_item_data in self.custom_field_set_associations:
                custom_field_set_associations_item = custom_field_set_associations_item_data.to_dict()
                custom_field_set_associations.append(custom_field_set_associations_item)

        custom_field_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_field_values, Unset):
            custom_field_values = []
            for custom_field_values_item_data in self.custom_field_values:
                custom_field_values_item = custom_field_values_item_data.to_dict()
                custom_field_values.append(custom_field_values_item)

        custom_rate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_rate, Unset):
            custom_rate = self.custom_rate.to_dict()

        description = self.description

        display_number = self.display_number

        evergreen_retainer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.evergreen_retainer, Unset):
            evergreen_retainer = self.evergreen_retainer.to_dict()

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        location = self.location

        matter_budget: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter_budget, Unset):
            matter_budget = self.matter_budget.to_dict()

        matter_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter_stage, Unset):
            matter_stage = self.matter_stage.to_dict()

        open_date: Union[Unset, str] = UNSET
        if not isinstance(self.open_date, Unset):
            open_date = self.open_date.isoformat()

        originating_attorney: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.originating_attorney, Unset):
            originating_attorney = self.originating_attorney.to_dict()

        pending_date: Union[Unset, str] = UNSET
        if not isinstance(self.pending_date, Unset):
            pending_date = self.pending_date.isoformat()

        practice_area: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.practice_area, Unset):
            practice_area = self.practice_area.to_dict()

        relationships: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for relationships_item_data in self.relationships:
                relationships_item = relationships_item_data.to_dict()
                relationships.append(relationships_item)

        reset_matter_number = self.reset_matter_number

        responsible_attorney: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.responsible_attorney, Unset):
            responsible_attorney = self.responsible_attorney.to_dict()

        responsible_staff: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.responsible_staff, Unset):
            responsible_staff = self.responsible_staff.to_dict()

        split_invoice_payers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.split_invoice_payers, Unset):
            split_invoice_payers = []
            for split_invoice_payers_item_data in self.split_invoice_payers:
                split_invoice_payers_item = split_invoice_payers_item_data.to_dict()
                split_invoice_payers.append(split_invoice_payers_item)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        statute_of_limitations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statute_of_limitations, Unset):
            statute_of_limitations = self.statute_of_limitations.to_dict()

        task_template_list_instances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.task_template_list_instances, Unset):
            task_template_list_instances = []
            for task_template_list_instances_item_data in self.task_template_list_instances:
                task_template_list_instances_item = task_template_list_instances_item_data.to_dict()
                task_template_list_instances.append(task_template_list_instances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billable is not UNSET:
            field_dict["billable"] = billable
        if client is not UNSET:
            field_dict["client"] = client
        if client_reference is not UNSET:
            field_dict["client_reference"] = client_reference
        if close_date is not UNSET:
            field_dict["close_date"] = close_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if custom_field_set_associations is not UNSET:
            field_dict["custom_field_set_associations"] = custom_field_set_associations
        if custom_field_values is not UNSET:
            field_dict["custom_field_values"] = custom_field_values
        if custom_rate is not UNSET:
            field_dict["custom_rate"] = custom_rate
        if description is not UNSET:
            field_dict["description"] = description
        if display_number is not UNSET:
            field_dict["display_number"] = display_number
        if evergreen_retainer is not UNSET:
            field_dict["evergreen_retainer"] = evergreen_retainer
        if group is not UNSET:
            field_dict["group"] = group
        if location is not UNSET:
            field_dict["location"] = location
        if matter_budget is not UNSET:
            field_dict["matter_budget"] = matter_budget
        if matter_stage is not UNSET:
            field_dict["matter_stage"] = matter_stage
        if open_date is not UNSET:
            field_dict["open_date"] = open_date
        if originating_attorney is not UNSET:
            field_dict["originating_attorney"] = originating_attorney
        if pending_date is not UNSET:
            field_dict["pending_date"] = pending_date
        if practice_area is not UNSET:
            field_dict["practice_area"] = practice_area
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if reset_matter_number is not UNSET:
            field_dict["reset_matter_number"] = reset_matter_number
        if responsible_attorney is not UNSET:
            field_dict["responsible_attorney"] = responsible_attorney
        if responsible_staff is not UNSET:
            field_dict["responsible_staff"] = responsible_staff
        if split_invoice_payers is not UNSET:
            field_dict["split_invoice_payers"] = split_invoice_payers
        if status is not UNSET:
            field_dict["status"] = status
        if statute_of_limitations is not UNSET:
            field_dict["statute_of_limitations"] = statute_of_limitations
        if task_template_list_instances is not UNSET:
            field_dict["task_template_list_instances"] = task_template_list_instances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matterupdate_data_body_data_client import MatterupdateDataBodyDataClient
        from ..models.matterupdate_data_body_data_currency import MatterupdateDataBodyDataCurrency
        from ..models.matterupdate_data_body_data_custom_field_set_associations_item import (
            MatterupdateDataBodyDataCustomFieldSetAssociationsItem,
        )
        from ..models.matterupdate_data_body_data_custom_field_values_item import (
            MatterupdateDataBodyDataCustomFieldValuesItem,
        )
        from ..models.matterupdate_data_body_data_custom_rate import MatterupdateDataBodyDataCustomRate
        from ..models.matterupdate_data_body_data_evergreen_retainer import MatterupdateDataBodyDataEvergreenRetainer
        from ..models.matterupdate_data_body_data_group import MatterupdateDataBodyDataGroup
        from ..models.matterupdate_data_body_data_matter_budget import MatterupdateDataBodyDataMatterBudget
        from ..models.matterupdate_data_body_data_matter_stage import MatterupdateDataBodyDataMatterStage
        from ..models.matterupdate_data_body_data_originating_attorney import (
            MatterupdateDataBodyDataOriginatingAttorney,
        )
        from ..models.matterupdate_data_body_data_practice_area import MatterupdateDataBodyDataPracticeArea
        from ..models.matterupdate_data_body_data_relationships_item import MatterupdateDataBodyDataRelationshipsItem
        from ..models.matterupdate_data_body_data_responsible_attorney import (
            MatterupdateDataBodyDataResponsibleAttorney,
        )
        from ..models.matterupdate_data_body_data_responsible_staff import MatterupdateDataBodyDataResponsibleStaff
        from ..models.matterupdate_data_body_data_split_invoice_payers_item import (
            MatterupdateDataBodyDataSplitInvoicePayersItem,
        )
        from ..models.matterupdate_data_body_data_statute_of_limitations import (
            MatterupdateDataBodyDataStatuteOfLimitations,
        )
        from ..models.matterupdate_data_body_data_task_template_list_instances_item import (
            MatterupdateDataBodyDataTaskTemplateListInstancesItem,
        )

        d = dict(src_dict)
        billable = d.pop("billable", UNSET)

        _client = d.pop("client", UNSET)
        client: Union[Unset, MatterupdateDataBodyDataClient]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = MatterupdateDataBodyDataClient.from_dict(_client)

        client_reference = d.pop("client_reference", UNSET)

        _close_date = d.pop("close_date", UNSET)
        close_date: Union[Unset, datetime.date]
        if isinstance(_close_date, Unset):
            close_date = UNSET
        else:
            close_date = isoparse(_close_date).date()

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, MatterupdateDataBodyDataCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = MatterupdateDataBodyDataCurrency.from_dict(_currency)

        custom_field_set_associations = []
        _custom_field_set_associations = d.pop("custom_field_set_associations", UNSET)
        for custom_field_set_associations_item_data in _custom_field_set_associations or []:
            custom_field_set_associations_item = MatterupdateDataBodyDataCustomFieldSetAssociationsItem.from_dict(
                custom_field_set_associations_item_data
            )

            custom_field_set_associations.append(custom_field_set_associations_item)

        custom_field_values = []
        _custom_field_values = d.pop("custom_field_values", UNSET)
        for custom_field_values_item_data in _custom_field_values or []:
            custom_field_values_item = MatterupdateDataBodyDataCustomFieldValuesItem.from_dict(
                custom_field_values_item_data
            )

            custom_field_values.append(custom_field_values_item)

        _custom_rate = d.pop("custom_rate", UNSET)
        custom_rate: Union[Unset, MatterupdateDataBodyDataCustomRate]
        if isinstance(_custom_rate, Unset):
            custom_rate = UNSET
        else:
            custom_rate = MatterupdateDataBodyDataCustomRate.from_dict(_custom_rate)

        description = d.pop("description", UNSET)

        display_number = d.pop("display_number", UNSET)

        _evergreen_retainer = d.pop("evergreen_retainer", UNSET)
        evergreen_retainer: Union[Unset, MatterupdateDataBodyDataEvergreenRetainer]
        if isinstance(_evergreen_retainer, Unset):
            evergreen_retainer = UNSET
        else:
            evergreen_retainer = MatterupdateDataBodyDataEvergreenRetainer.from_dict(_evergreen_retainer)

        _group = d.pop("group", UNSET)
        group: Union[Unset, MatterupdateDataBodyDataGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = MatterupdateDataBodyDataGroup.from_dict(_group)

        location = d.pop("location", UNSET)

        _matter_budget = d.pop("matter_budget", UNSET)
        matter_budget: Union[Unset, MatterupdateDataBodyDataMatterBudget]
        if isinstance(_matter_budget, Unset):
            matter_budget = UNSET
        else:
            matter_budget = MatterupdateDataBodyDataMatterBudget.from_dict(_matter_budget)

        _matter_stage = d.pop("matter_stage", UNSET)
        matter_stage: Union[Unset, MatterupdateDataBodyDataMatterStage]
        if isinstance(_matter_stage, Unset):
            matter_stage = UNSET
        else:
            matter_stage = MatterupdateDataBodyDataMatterStage.from_dict(_matter_stage)

        _open_date = d.pop("open_date", UNSET)
        open_date: Union[Unset, datetime.date]
        if isinstance(_open_date, Unset):
            open_date = UNSET
        else:
            open_date = isoparse(_open_date).date()

        _originating_attorney = d.pop("originating_attorney", UNSET)
        originating_attorney: Union[Unset, MatterupdateDataBodyDataOriginatingAttorney]
        if isinstance(_originating_attorney, Unset):
            originating_attorney = UNSET
        else:
            originating_attorney = MatterupdateDataBodyDataOriginatingAttorney.from_dict(_originating_attorney)

        _pending_date = d.pop("pending_date", UNSET)
        pending_date: Union[Unset, datetime.date]
        if isinstance(_pending_date, Unset):
            pending_date = UNSET
        else:
            pending_date = isoparse(_pending_date).date()

        _practice_area = d.pop("practice_area", UNSET)
        practice_area: Union[Unset, MatterupdateDataBodyDataPracticeArea]
        if isinstance(_practice_area, Unset):
            practice_area = UNSET
        else:
            practice_area = MatterupdateDataBodyDataPracticeArea.from_dict(_practice_area)

        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for relationships_item_data in _relationships or []:
            relationships_item = MatterupdateDataBodyDataRelationshipsItem.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        reset_matter_number = d.pop("reset_matter_number", UNSET)

        _responsible_attorney = d.pop("responsible_attorney", UNSET)
        responsible_attorney: Union[Unset, MatterupdateDataBodyDataResponsibleAttorney]
        if isinstance(_responsible_attorney, Unset):
            responsible_attorney = UNSET
        else:
            responsible_attorney = MatterupdateDataBodyDataResponsibleAttorney.from_dict(_responsible_attorney)

        _responsible_staff = d.pop("responsible_staff", UNSET)
        responsible_staff: Union[Unset, MatterupdateDataBodyDataResponsibleStaff]
        if isinstance(_responsible_staff, Unset):
            responsible_staff = UNSET
        else:
            responsible_staff = MatterupdateDataBodyDataResponsibleStaff.from_dict(_responsible_staff)

        split_invoice_payers = []
        _split_invoice_payers = d.pop("split_invoice_payers", UNSET)
        for split_invoice_payers_item_data in _split_invoice_payers or []:
            split_invoice_payers_item = MatterupdateDataBodyDataSplitInvoicePayersItem.from_dict(
                split_invoice_payers_item_data
            )

            split_invoice_payers.append(split_invoice_payers_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, MatterupdateDataBodyDataStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MatterupdateDataBodyDataStatus(_status)

        _statute_of_limitations = d.pop("statute_of_limitations", UNSET)
        statute_of_limitations: Union[Unset, MatterupdateDataBodyDataStatuteOfLimitations]
        if isinstance(_statute_of_limitations, Unset):
            statute_of_limitations = UNSET
        else:
            statute_of_limitations = MatterupdateDataBodyDataStatuteOfLimitations.from_dict(_statute_of_limitations)

        task_template_list_instances = []
        _task_template_list_instances = d.pop("task_template_list_instances", UNSET)
        for task_template_list_instances_item_data in _task_template_list_instances or []:
            task_template_list_instances_item = MatterupdateDataBodyDataTaskTemplateListInstancesItem.from_dict(
                task_template_list_instances_item_data
            )

            task_template_list_instances.append(task_template_list_instances_item)

        matterupdate_data_body_data = cls(
            billable=billable,
            client=client,
            client_reference=client_reference,
            close_date=close_date,
            currency=currency,
            custom_field_set_associations=custom_field_set_associations,
            custom_field_values=custom_field_values,
            custom_rate=custom_rate,
            description=description,
            display_number=display_number,
            evergreen_retainer=evergreen_retainer,
            group=group,
            location=location,
            matter_budget=matter_budget,
            matter_stage=matter_stage,
            open_date=open_date,
            originating_attorney=originating_attorney,
            pending_date=pending_date,
            practice_area=practice_area,
            relationships=relationships,
            reset_matter_number=reset_matter_number,
            responsible_attorney=responsible_attorney,
            responsible_staff=responsible_staff,
            split_invoice_payers=split_invoice_payers,
            status=status,
            statute_of_limitations=statute_of_limitations,
            task_template_list_instances=task_template_list_instances,
        )

        matterupdate_data_body_data.additional_properties = d
        return matterupdate_data_body_data

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
