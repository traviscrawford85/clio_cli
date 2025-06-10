import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_template_base_description_text_type import TaskTemplateBaseDescriptionTextType
from ..models.task_template_base_priority import TaskTemplateBasePriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cascading_task_template_base import CascadingTaskTemplateBase
    from ..models.reminder_template_base import ReminderTemplateBase
    from ..models.task_template_list_base import TaskTemplateListBase
    from ..models.task_type_base import TaskTypeBase
    from ..models.user_base import UserBase


T = TypeVar("T", bound="TaskTemplate")


@_attrs_define
class TaskTemplate:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *TaskTemplate*
        etag (Union[Unset, str]): ETag for the *TaskTemplate*
        name (Union[Unset, str]): The name of the *TaskTemplate*
        description (Union[Unset, str]): The text body of the *TaskTemplate*. This TaskTemplate supports rich text when
            setting the field `detail_text_type` to `rich_text`. With supported tags such as `<a>`, `<b>`, `<br>`, `<div>`,
            `<em>`, `<i>` `<li>`, `<ol>`, `<p>`, `<s>`, `<strong>`, `<u>` and `<ul>`. This TaskTemplate also supports
            attributes such as `href`, `rel`, `type`, and `target`.
        description_text_type (Union[Unset, TaskTemplateBaseDescriptionTextType]): The type of text in the description
            field.
        priority (Union[Unset, TaskTemplateBasePriority]): *TaskTemplate* priority
        private (Union[Unset, bool]): Whether the *TaskTemplate* is private.
        created_at (Union[Unset, datetime.datetime]): The time the *TaskTemplate* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *TaskTemplate* was last updated (as a ISO-8601
            timestamp)
        cascading_source (Union[Unset, CascadingTaskTemplateBase]):
        assignee (Union[Unset, UserBase]):
        task_template_list (Union[Unset, TaskTemplateListBase]):
        task_type (Union[Unset, TaskTypeBase]):
        template_creator (Union[Unset, UserBase]):
        reminder_templates (Union[Unset, list['ReminderTemplateBase']]): ReminderTemplate
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    description_text_type: Union[Unset, TaskTemplateBaseDescriptionTextType] = UNSET
    priority: Union[Unset, TaskTemplateBasePriority] = UNSET
    private: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    cascading_source: Union[Unset, "CascadingTaskTemplateBase"] = UNSET
    assignee: Union[Unset, "UserBase"] = UNSET
    task_template_list: Union[Unset, "TaskTemplateListBase"] = UNSET
    task_type: Union[Unset, "TaskTypeBase"] = UNSET
    template_creator: Union[Unset, "UserBase"] = UNSET
    reminder_templates: Union[Unset, list["ReminderTemplateBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        description = self.description

        description_text_type: Union[Unset, str] = UNSET
        if not isinstance(self.description_text_type, Unset):
            description_text_type = self.description_text_type.value

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        private = self.private

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        cascading_source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cascading_source, Unset):
            cascading_source = self.cascading_source.to_dict()

        assignee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        task_template_list: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.task_template_list, Unset):
            task_template_list = self.task_template_list.to_dict()

        task_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.to_dict()

        template_creator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.template_creator, Unset):
            template_creator = self.template_creator.to_dict()

        reminder_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reminder_templates, Unset):
            reminder_templates = []
            for reminder_templates_item_data in self.reminder_templates:
                reminder_templates_item = reminder_templates_item_data.to_dict()
                reminder_templates.append(reminder_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if description_text_type is not UNSET:
            field_dict["description_text_type"] = description_text_type
        if priority is not UNSET:
            field_dict["priority"] = priority
        if private is not UNSET:
            field_dict["private"] = private
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if cascading_source is not UNSET:
            field_dict["cascading_source"] = cascading_source
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if task_template_list is not UNSET:
            field_dict["task_template_list"] = task_template_list
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if template_creator is not UNSET:
            field_dict["template_creator"] = template_creator
        if reminder_templates is not UNSET:
            field_dict["reminder_templates"] = reminder_templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cascading_task_template_base import CascadingTaskTemplateBase
        from ..models.reminder_template_base import ReminderTemplateBase
        from ..models.task_template_list_base import TaskTemplateListBase
        from ..models.task_type_base import TaskTypeBase
        from ..models.user_base import UserBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _description_text_type = d.pop("description_text_type", UNSET)
        description_text_type: Union[Unset, TaskTemplateBaseDescriptionTextType]
        if isinstance(_description_text_type, Unset):
            description_text_type = UNSET
        else:
            description_text_type = TaskTemplateBaseDescriptionTextType(_description_text_type)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, TaskTemplateBasePriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = TaskTemplateBasePriority(_priority)

        private = d.pop("private", UNSET)

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

        _cascading_source = d.pop("cascading_source", UNSET)
        cascading_source: Union[Unset, CascadingTaskTemplateBase]
        if isinstance(_cascading_source, Unset):
            cascading_source = UNSET
        else:
            cascading_source = CascadingTaskTemplateBase.from_dict(_cascading_source)

        _assignee = d.pop("assignee", UNSET)
        assignee: Union[Unset, UserBase]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = UserBase.from_dict(_assignee)

        _task_template_list = d.pop("task_template_list", UNSET)
        task_template_list: Union[Unset, TaskTemplateListBase]
        if isinstance(_task_template_list, Unset):
            task_template_list = UNSET
        else:
            task_template_list = TaskTemplateListBase.from_dict(_task_template_list)

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, TaskTypeBase]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = TaskTypeBase.from_dict(_task_type)

        _template_creator = d.pop("template_creator", UNSET)
        template_creator: Union[Unset, UserBase]
        if isinstance(_template_creator, Unset):
            template_creator = UNSET
        else:
            template_creator = UserBase.from_dict(_template_creator)

        reminder_templates = []
        _reminder_templates = d.pop("reminder_templates", UNSET)
        for reminder_templates_item_data in _reminder_templates or []:
            reminder_templates_item = ReminderTemplateBase.from_dict(reminder_templates_item_data)

            reminder_templates.append(reminder_templates_item)

        task_template = cls(
            id=id,
            etag=etag,
            name=name,
            description=description,
            description_text_type=description_text_type,
            priority=priority,
            private=private,
            created_at=created_at,
            updated_at=updated_at,
            cascading_source=cascading_source,
            assignee=assignee,
            task_template_list=task_template_list,
            task_type=task_type,
            template_creator=template_creator,
            reminder_templates=reminder_templates,
        )

        task_template.additional_properties = d
        return task_template

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
