from enum import Enum


class TaskindexOrder(str, Enum):
    COMPLETED_ATASC = "completed_at(asc)"
    COMPLETED_ATDESC = "completed_at(desc)"
    DUE_ATASC = "due_at(asc)"
    DUE_ATDESC = "due_at(desc)"
    DUE_AT_STRICTASC = "due_at_strict(asc)"
    DUE_AT_STRICTDESC = "due_at_strict(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    MATTER_DISPLAY_NUMBERASC = "matter.display_number(asc)"
    MATTER_DISPLAY_NUMBERDESC = "matter.display_number(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"
    PRIORITYASC = "priority(asc)"
    PRIORITYDESC = "priority(desc)"
    TASK_TYPE_NAMEASC = "task_type.name(asc)"
    TASK_TYPE_NAMEDESC = "task_type.name(desc)"

    def __str__(self) -> str:
        return str(self.value)
