from enum import Enum


class ContactupdateFilesBodyDataEmailAddressesItemName(str, Enum):
    HOME = "Home"
    OTHER = "Other"
    WORK = "Work"

    def __str__(self) -> str:
        return str(self.value)
