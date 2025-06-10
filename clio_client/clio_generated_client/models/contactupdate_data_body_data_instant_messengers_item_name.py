from enum import Enum


class ContactupdateDataBodyDataInstantMessengersItemName(str, Enum):
    OTHER = "Other"
    PERSONAL = "Personal"
    WORK = "Work"

    def __str__(self) -> str:
        return str(self.value)
