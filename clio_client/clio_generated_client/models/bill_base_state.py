from enum import Enum


class BillBaseState(str, Enum):
    AWAITING_APPROVAL = "awaiting_approval"
    AWAITING_PAYMENT = "awaiting_payment"
    DELETED = "deleted"
    DRAFT = "draft"
    PAID = "paid"
    VOID = "void"

    def __str__(self) -> str:
        return str(self.value)
