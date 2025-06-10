from enum import Enum


class TaskTemplateindexOrder(str, Enum):
    ASSIGNEE_NAMEASC = "assignee.name(asc)"
    ASSIGNEE_NAMEDESC = "assignee.name(desc)"
    DAYS_FROM_ASSIGNMENTASC = "days_from_assignment(asc)"
    DAYS_FROM_ASSIGNMENTDESC = "days_from_assignment(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"
    PERMISSIONASC = "permission(asc)"
    PERMISSIONDESC = "permission(desc)"
    PRIORITYASC = "priority(asc)"
    PRIORITYDESC = "priority(desc)"

    def __str__(self) -> str:
        return str(self.value)
