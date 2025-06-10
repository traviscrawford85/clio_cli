from enum import Enum


class MatterindexOrder(str, Enum):
    CLIENT_NAMEASC = "client.name(asc)"
    CLIENT_NAMEDESC = "client.name(desc)"
    CLOSE_DATEASC = "close_date(asc)"
    CLOSE_DATEDESC = "close_date(desc)"
    CREATED_ATASC = "created_at(asc)"
    CREATED_ATDESC = "created_at(desc)"
    CUSTOM_NUMBERASC = "custom_number(asc)"
    CUSTOM_NUMBERDESC = "custom_number(desc)"
    DISPLAY_NUMBERASC = "display_number(asc)"
    DISPLAY_NUMBERDESC = "display_number(desc)"
    GRANTSASC = "grants(asc)"
    GRANTSDESC = "grants(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    MATTER_STAGE_NAMEASC = "matter_stage.name(asc)"
    MATTER_STAGE_NAMEDESC = "matter_stage.name(desc)"
    MATTER_STAGE_UPDATED_ATASC = "matter_stage_updated_at(asc)"
    MATTER_STAGE_UPDATED_ATDESC = "matter_stage_updated_at(desc)"
    OPEN_DATEASC = "open_date(asc)"
    OPEN_DATEDESC = "open_date(desc)"
    ORIGINATING_ATTORNEY_NAMEASC = "originating_attorney.name(asc)"
    ORIGINATING_ATTORNEY_NAMEDESC = "originating_attorney.name(desc)"
    PENDING_DATEASC = "pending_date(asc)"
    PENDING_DATEDESC = "pending_date(desc)"
    PRACTICE_AREA_NAMEASC = "practice_area.name(asc)"
    PRACTICE_AREA_NAMEDESC = "practice_area.name(desc)"
    RESPONSIBLE_ATTORNEY_NAMEASC = "responsible_attorney.name(asc)"
    RESPONSIBLE_ATTORNEY_NAMEDESC = "responsible_attorney.name(desc)"
    STATUTE_OF_LIMITATIONS_DUE_ATASC = "statute_of_limitations.due_at(asc)"
    STATUTE_OF_LIMITATIONS_DUE_ATDESC = "statute_of_limitations.due_at(desc)"
    UPDATED_ATASC = "updated_at(asc)"
    UPDATED_ATDESC = "updated_at(desc)"

    def __str__(self) -> str:
        return str(self.value)
