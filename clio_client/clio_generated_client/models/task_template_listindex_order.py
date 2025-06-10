from enum import Enum


class TaskTemplateListindexOrder(str, Enum):
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"
    PRACTICE_AREA_NAMEASC = "practice_area.name(asc)"
    PRACTICE_AREA_NAMEDESC = "practice_area.name(desc)"

    def __str__(self) -> str:
        return str(self.value)
