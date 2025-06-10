from enum import Enum


class ContactupdateFilesBodyDataPhoneNumbersItemName(str, Enum):
    FAX = "Fax"
    HOME = "Home"
    MOBILE = "Mobile"
    OTHER = "Other"
    PAGER = "Pager"
    SKYPE = "Skype"
    WORK = "Work"

    def __str__(self) -> str:
        return str(self.value)
