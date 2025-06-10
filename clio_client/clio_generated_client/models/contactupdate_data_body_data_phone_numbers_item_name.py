from enum import Enum


class ContactupdateDataBodyDataPhoneNumbersItemName(str, Enum):
    FAX = "Fax"
    HOME = "Home"
    MOBILE = "Mobile"
    OTHER = "Other"
    PAGER = "Pager"
    SKYPE = "Skype"
    WORK = "Work"

    def __str__(self) -> str:
        return str(self.value)
