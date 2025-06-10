import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_base_description_text_type import TaskBaseDescriptionTextType
from ..models.task_base_priority import TaskBasePriority
from ..models.task_base_status import TaskBaseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_base import ActivityBase
    from ..models.matter_base import MatterBase
    from ..models.participant import Participant
    from ..models.reminder_base import ReminderBase
    from ..models.task_type_base import TaskTypeBase
    from ..models.user_base import UserBase


T = TypeVar("T", bound="Task")


@_attrs_define
class Task:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Task*
        etag (Union[Unset, str]): ETag for the *Task*
        name (Union[Unset, str]): The name of the *Task*
        status (Union[Unset, TaskBaseStatus]): Status of the *Task*. (Note that users without advanced tasks can only
            have either complete or pending)
        description (Union[Unset, str]): A detailed description of the *Task*. This Task supports rich text when setting
            the field `description_text_type` to `rich_text`. With supported tags such as `<a>`, `<b>`, `<br>`, `<div>`,
            `<em>`, `<i>` `<li>`, `<ol>`, `<p>`, `<s>`, `<strong>`, `<u>` and `<ul>`. This Task also supports attributes
            such as `href`, `rel`, `type`, and `target`.
        description_text_type (Union[Unset, TaskBaseDescriptionTextType]): The text type of the *Task*
        priority (Union[Unset, TaskBasePriority]): The priority of the *Task*
        due_at (Union[Unset, datetime.date]): The date the *Task* is due (as a ISO-8601 date)
        permission (Union[Unset, str]): The permission of the *Task*
        completed_at (Union[Unset, datetime.datetime]): The time the *Task* was completed (as a ISO-8601 timestamp)
        notify_completion (Union[Unset, bool]): Whether to notify the assigner of the task's completion
        statute_of_limitations (Union[Unset, bool]): Whether the task is a statute of limitations
        time_estimated (Union[Unset, int]): Time the *Task* should take to complete
        created_at (Union[Unset, datetime.datetime]): The time the *Task* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Task* was last updated (as a ISO-8601 timestamp)
        time_entries_count (Union[Unset, int]): The number of time entries associated with this task
        time_entries (Union[Unset, list['ActivityBase']]): Activity
        task_type (Union[Unset, TaskTypeBase]):
        assigner (Union[Unset, UserBase]):
        matter (Union[Unset, MatterBase]):
        assignee (Union[Unset, Participant]):
        reminders (Union[Unset, list['ReminderBase']]): Reminder
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, TaskBaseStatus] = UNSET
    description: Union[Unset, str] = UNSET
    description_text_type: Union[Unset, TaskBaseDescriptionTextType] = UNSET
    priority: Union[Unset, TaskBasePriority] = UNSET
    due_at: Union[Unset, datetime.date] = UNSET
    permission: Union[Unset, str] = UNSET
    completed_at: Union[Unset, datetime.datetime] = UNSET
    notify_completion: Union[Unset, bool] = UNSET
    statute_of_limitations: Union[Unset, bool] = UNSET
    time_estimated: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    time_entries_count: Union[Unset, int] = UNSET
    time_entries: Union[Unset, list["ActivityBase"]] = UNSET
    task_type: Union[Unset, "TaskTypeBase"] = UNSET
    assigner: Union[Unset, "UserBase"] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    assignee: Union[Unset, "Participant"] = UNSET
    reminders: Union[Unset, list["ReminderBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        description = self.description

        description_text_type: Union[Unset, str] = UNSET
        if not isinstance(self.description_text_type, Unset):
            description_text_type = self.description_text_type.value

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        due_at: Union[Unset, str] = UNSET
        if not isinstance(self.due_at, Unset):
            due_at = self.due_at.isoformat()

        permission = self.permission

        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        notify_completion = self.notify_completion

        statute_of_limitations = self.statute_of_limitations

        time_estimated = self.time_estimated

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        time_entries_count = self.time_entries_count

        time_entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.time_entries, Unset):
            time_entries = []
            for time_entries_item_data in self.time_entries:
                time_entries_item = time_entries_item_data.to_dict()
                time_entries.append(time_entries_item)

        task_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.to_dict()

        assigner: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assigner, Unset):
            assigner = self.assigner.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        assignee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        reminders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reminders, Unset):
            reminders = []
            for reminders_item_data in self.reminders:
                reminders_item = reminders_item_data.to_dict()
                reminders.append(reminders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if description_text_type is not UNSET:
            field_dict["description_text_type"] = description_text_type
        if priority is not UNSET:
            field_dict["priority"] = priority
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if permission is not UNSET:
            field_dict["permission"] = permission
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if notify_completion is not UNSET:
            field_dict["notify_completion"] = notify_completion
        if statute_of_limitations is not UNSET:
            field_dict["statute_of_limitations"] = statute_of_limitations
        if time_estimated is not UNSET:
            field_dict["time_estimated"] = time_estimated
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if time_entries_count is not UNSET:
            field_dict["time_entries_count"] = time_entries_count
        if time_entries is not UNSET:
            field_dict["time_entries"] = time_entries
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if assigner is not UNSET:
            field_dict["assigner"] = assigner
        if matter is not UNSET:
            field_dict["matter"] = matter
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if reminders is not UNSET:
            field_dict["reminders"] = reminders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_base import ActivityBase
        from ..models.matter_base import MatterBase
        from ..models.participant import Participant
        from ..models.reminder_base import ReminderBase
        from ..models.task_type_base import TaskTypeBase
        from ..models.user_base import UserBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, TaskBaseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskBaseStatus(_status)

        description = d.pop("description", UNSET)

        _description_text_type = d.pop("description_text_type", UNSET)
        description_text_type: Union[Unset, TaskBaseDescriptionTextType]
        if isinstance(_description_text_type, Unset):
            description_text_type = UNSET
        else:
            description_text_type = TaskBaseDescriptionTextType(_description_text_type)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, TaskBasePriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = TaskBasePriority(_priority)

        _due_at = d.pop("due_at", UNSET)
        due_at: Union[Unset, datetime.date]
        if isinstance(_due_at, Unset):
            due_at = UNSET
        else:
            due_at = isoparse(_due_at).date()

        permission = d.pop("permission", UNSET)

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        notify_completion = d.pop("notify_completion", UNSET)

        statute_of_limitations = d.pop("statute_of_limitations", UNSET)

        time_estimated = d.pop("time_estimated", UNSET)

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

        time_entries_count = d.pop("time_entries_count", UNSET)

        time_entries = []
        _time_entries = d.pop("time_entries", UNSET)
        for time_entries_item_data in _time_entries or []:
            time_entries_item = ActivityBase.from_dict(time_entries_item_data)

            time_entries.append(time_entries_item)

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, TaskTypeBase]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = TaskTypeBase.from_dict(_task_type)

        _assigner = d.pop("assigner", UNSET)
        assigner: Union[Unset, UserBase]
        if isinstance(_assigner, Unset):
            assigner = UNSET
        else:
            assigner = UserBase.from_dict(_assigner)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        _assignee = d.pop("assignee", UNSET)
        assignee: Union[Unset, Participant]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = Participant.from_dict(_assignee)

        reminders = []
        _reminders = d.pop("reminders", UNSET)
        for reminders_item_data in _reminders or []:
            reminders_item = ReminderBase.from_dict(reminders_item_data)

            reminders.append(reminders_item)

        task = cls(
            id=id,
            etag=etag,
            name=name,
            status=status,
            description=description,
            description_text_type=description_text_type,
            priority=priority,
            due_at=due_at,
            permission=permission,
            completed_at=completed_at,
            notify_completion=notify_completion,
            statute_of_limitations=statute_of_limitations,
            time_estimated=time_estimated,
            created_at=created_at,
            updated_at=updated_at,
            time_entries_count=time_entries_count,
            time_entries=time_entries,
            task_type=task_type,
            assigner=assigner,
            matter=matter,
            assignee=assignee,
            reminders=reminders,
        )

        task.additional_properties = d
        return task

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
