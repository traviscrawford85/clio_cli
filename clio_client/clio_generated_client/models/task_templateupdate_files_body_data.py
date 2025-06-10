from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_templateupdate_files_body_data_cascading_offset_polarity import (
    TaskTemplateupdateFilesBodyDataCascadingOffsetPolarity,
)
from ..models.task_templateupdate_files_body_data_cascading_offset_type import (
    TaskTemplateupdateFilesBodyDataCascadingOffsetType,
)
from ..models.task_templateupdate_files_body_data_description_text_type import (
    TaskTemplateupdateFilesBodyDataDescriptionTextType,
)
from ..models.task_templateupdate_files_body_data_priority import TaskTemplateupdateFilesBodyDataPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_templateupdate_files_body_data_cascading_source import (
        TaskTemplateupdateFilesBodyDataCascadingSource,
    )
    from ..models.task_templateupdate_files_body_data_reminder_templates_item import (
        TaskTemplateupdateFilesBodyDataReminderTemplatesItem,
    )


T = TypeVar("T", bound="TaskTemplateupdateFilesBodyData")


@_attrs_define
class TaskTemplateupdateFilesBodyData:
    """
    Attributes:
        cascading (Union[Unset, bool]): Determines if the TaskTemplate has a due date that is derived from another
            TaskTemplate. (Note that if false, no other cascading information will be checked)
        cascading_offset (Union[Unset, int]): The amount of time that will differentiate the cascaded TaskTemplate from
            its parent.
        cascading_offset_polarity (Union[Unset, TaskTemplateupdateFilesBodyDataCascadingOffsetPolarity]): Determines
            whether or not the cascading_offset occurs before or after its parent.
        cascading_offset_type (Union[Unset, TaskTemplateupdateFilesBodyDataCascadingOffsetType]): Determines the
            quantity of the cascading offset (e.g. CalendarDays, CalendarWeeks etc.)
        cascading_source (Union[Unset, TaskTemplateupdateFilesBodyDataCascadingSource]):
        description (Union[Unset, str]): Longer description of the TaskTemplate. This TaskTemplate supports rich text
            when the `description_text_type` field is set to `rich_text`. With supported tags such as `<a>`, `<b>`, `<br>`,
            `<div>`, `<em>`, `<i>` `<li>`, `<ol>`, `<p>`, `<s>`, `<strong>`, `<u>` and `<ul>`. This TaskTemplate also
            supports attributes such as `href`, `rel`, `type`, and `target`.
        description_text_type (Union[Unset, TaskTemplateupdateFilesBodyDataDescriptionTextType]): The type of text in
            the description field. Default: TaskTemplateupdateFilesBodyDataDescriptionTextType.PLAIN_TEXT.
        name (Union[Unset, str]): Short name for the TaskTemplate.
        priority (Union[Unset, TaskTemplateupdateFilesBodyDataPriority]): Priority of the task. Default:
            TaskTemplateupdateFilesBodyDataPriority.NORMAL.
        private (Union[Unset, bool]): Whether or not this TaskTemplate should be private.
        reminder_templates (Union[Unset, list['TaskTemplateupdateFilesBodyDataReminderTemplatesItem']]):
    """

    cascading: Union[Unset, bool] = UNSET
    cascading_offset: Union[Unset, int] = UNSET
    cascading_offset_polarity: Union[Unset, TaskTemplateupdateFilesBodyDataCascadingOffsetPolarity] = UNSET
    cascading_offset_type: Union[Unset, TaskTemplateupdateFilesBodyDataCascadingOffsetType] = UNSET
    cascading_source: Union[Unset, "TaskTemplateupdateFilesBodyDataCascadingSource"] = UNSET
    description: Union[Unset, str] = UNSET
    description_text_type: Union[Unset, TaskTemplateupdateFilesBodyDataDescriptionTextType] = (
        TaskTemplateupdateFilesBodyDataDescriptionTextType.PLAIN_TEXT
    )
    name: Union[Unset, str] = UNSET
    priority: Union[Unset, TaskTemplateupdateFilesBodyDataPriority] = TaskTemplateupdateFilesBodyDataPriority.NORMAL
    private: Union[Unset, bool] = UNSET
    reminder_templates: Union[Unset, list["TaskTemplateupdateFilesBodyDataReminderTemplatesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cascading = self.cascading

        cascading_offset = self.cascading_offset

        cascading_offset_polarity: Union[Unset, str] = UNSET
        if not isinstance(self.cascading_offset_polarity, Unset):
            cascading_offset_polarity = self.cascading_offset_polarity.value

        cascading_offset_type: Union[Unset, str] = UNSET
        if not isinstance(self.cascading_offset_type, Unset):
            cascading_offset_type = self.cascading_offset_type.value

        cascading_source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cascading_source, Unset):
            cascading_source = self.cascading_source.to_dict()

        description = self.description

        description_text_type: Union[Unset, str] = UNSET
        if not isinstance(self.description_text_type, Unset):
            description_text_type = self.description_text_type.value

        name = self.name

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        private = self.private

        reminder_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reminder_templates, Unset):
            reminder_templates = []
            for reminder_templates_item_data in self.reminder_templates:
                reminder_templates_item = reminder_templates_item_data.to_dict()
                reminder_templates.append(reminder_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cascading is not UNSET:
            field_dict["cascading"] = cascading
        if cascading_offset is not UNSET:
            field_dict["cascading_offset"] = cascading_offset
        if cascading_offset_polarity is not UNSET:
            field_dict["cascading_offset_polarity"] = cascading_offset_polarity
        if cascading_offset_type is not UNSET:
            field_dict["cascading_offset_type"] = cascading_offset_type
        if cascading_source is not UNSET:
            field_dict["cascading_source"] = cascading_source
        if description is not UNSET:
            field_dict["description"] = description
        if description_text_type is not UNSET:
            field_dict["description_text_type"] = description_text_type
        if name is not UNSET:
            field_dict["name"] = name
        if priority is not UNSET:
            field_dict["priority"] = priority
        if private is not UNSET:
            field_dict["private"] = private
        if reminder_templates is not UNSET:
            field_dict["reminder_templates"] = reminder_templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_templateupdate_files_body_data_cascading_source import (
            TaskTemplateupdateFilesBodyDataCascadingSource,
        )
        from ..models.task_templateupdate_files_body_data_reminder_templates_item import (
            TaskTemplateupdateFilesBodyDataReminderTemplatesItem,
        )

        d = dict(src_dict)
        cascading = d.pop("cascading", UNSET)

        cascading_offset = d.pop("cascading_offset", UNSET)

        _cascading_offset_polarity = d.pop("cascading_offset_polarity", UNSET)
        cascading_offset_polarity: Union[Unset, TaskTemplateupdateFilesBodyDataCascadingOffsetPolarity]
        if isinstance(_cascading_offset_polarity, Unset):
            cascading_offset_polarity = UNSET
        else:
            cascading_offset_polarity = TaskTemplateupdateFilesBodyDataCascadingOffsetPolarity(
                _cascading_offset_polarity
            )

        _cascading_offset_type = d.pop("cascading_offset_type", UNSET)
        cascading_offset_type: Union[Unset, TaskTemplateupdateFilesBodyDataCascadingOffsetType]
        if isinstance(_cascading_offset_type, Unset):
            cascading_offset_type = UNSET
        else:
            cascading_offset_type = TaskTemplateupdateFilesBodyDataCascadingOffsetType(_cascading_offset_type)

        _cascading_source = d.pop("cascading_source", UNSET)
        cascading_source: Union[Unset, TaskTemplateupdateFilesBodyDataCascadingSource]
        if isinstance(_cascading_source, Unset):
            cascading_source = UNSET
        else:
            cascading_source = TaskTemplateupdateFilesBodyDataCascadingSource.from_dict(_cascading_source)

        description = d.pop("description", UNSET)

        _description_text_type = d.pop("description_text_type", UNSET)
        description_text_type: Union[Unset, TaskTemplateupdateFilesBodyDataDescriptionTextType]
        if isinstance(_description_text_type, Unset):
            description_text_type = UNSET
        else:
            description_text_type = TaskTemplateupdateFilesBodyDataDescriptionTextType(_description_text_type)

        name = d.pop("name", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, TaskTemplateupdateFilesBodyDataPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = TaskTemplateupdateFilesBodyDataPriority(_priority)

        private = d.pop("private", UNSET)

        reminder_templates = []
        _reminder_templates = d.pop("reminder_templates", UNSET)
        for reminder_templates_item_data in _reminder_templates or []:
            reminder_templates_item = TaskTemplateupdateFilesBodyDataReminderTemplatesItem.from_dict(
                reminder_templates_item_data
            )

            reminder_templates.append(reminder_templates_item)

        task_templateupdate_files_body_data = cls(
            cascading=cascading,
            cascading_offset=cascading_offset,
            cascading_offset_polarity=cascading_offset_polarity,
            cascading_offset_type=cascading_offset_type,
            cascading_source=cascading_source,
            description=description,
            description_text_type=description_text_type,
            name=name,
            priority=priority,
            private=private,
            reminder_templates=reminder_templates,
        )

        task_templateupdate_files_body_data.additional_properties = d
        return task_templateupdate_files_body_data

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
