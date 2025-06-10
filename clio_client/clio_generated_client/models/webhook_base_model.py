from enum import Enum


class WebhookBaseModel(str, Enum):
    ACTIVITY = "activity"
    BILL = "bill"
    CALENDAR_ENTRY = "calendar_entry"
    CLIO_PAYMENTS_PAYMENT = "clio_payments_payment"
    COMMUNICATION = "communication"
    CONTACT = "contact"
    DOCUMENT = "document"
    FOLDER = "folder"
    MATTER = "matter"
    TASK = "task"

    def __str__(self) -> str:
        return str(self.value)
