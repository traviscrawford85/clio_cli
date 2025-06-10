from enum import Enum


class ReportPresetindexOrder(str, Enum):
    CREATED_ATASC = "created_at(asc)"
    CREATED_ATDESC = "created_at(desc)"
    LAST_GENERATED_ATASC = "last_generated_at(asc)"
    LAST_GENERATED_ATDESC = "last_generated_at(desc)"
    LAST_MODIFIED_ATASC = "last_modified_at(asc)"
    LAST_MODIFIED_ATDESC = "last_modified_at(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"
    NEXT_SCHEDULED_DATEASC = "next_scheduled_date(asc)"
    NEXT_SCHEDULED_DATEDESC = "next_scheduled_date(desc)"

    def __str__(self) -> str:
        return str(self.value)
