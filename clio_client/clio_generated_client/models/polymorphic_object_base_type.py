from enum import Enum


class PolymorphicObjectBaseType(str, Enum):
    CALENDARENTRY = "CalendarEntry"
    CONTACT = "Contact"
    CONTACTNOTE = "ContactNote"
    CREDITMEMO = "CreditMemo"
    MATTER = "Matter"
    MATTERNOTE = "MatterNote"
    PAYMENT = "Payment"
    TASK = "Task"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
