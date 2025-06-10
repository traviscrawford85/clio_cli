from enum import Enum


class ContactupdateFilesBodyDataAddressesItemName(str, Enum):
    BILLING = "Billing"
    HOME = "Home"
    OTHER = "Other"
    WORK = "Work"

    def __str__(self) -> str:
        return str(self.value)
