from enum import Enum


class ReminderindexOrder(str, Enum):
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NEXT_DELIVERY_ATASC = "next_delivery_at(asc)"
    NEXT_DELIVERY_ATDESC = "next_delivery_at(desc)"

    def __str__(self) -> str:
        return str(self.value)
