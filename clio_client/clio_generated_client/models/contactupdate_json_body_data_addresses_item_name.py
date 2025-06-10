from enum import Enum


class ContactupdateJsonBodyDataAddressesItemName(str, Enum):
    BILLING = "Billing"
    HOME = "Home"
    OTHER = "Other"
    WORK = "Work"

    def __str__(self) -> str:
        return str(self.value)
