from enum import Enum


class BillindexOrder(str, Enum):
    BALANCEASC = "balance(asc)"
    BALANCEDESC = "balance(desc)"
    CLIENT_NAMEASC = "client_name(asc)"
    CLIENT_NAMEDESC = "client_name(desc)"
    DUE_ATASC = "due_at(asc)"
    DUE_ATDESC = "due_at(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    ISSUED_ATASC = "issued_at(asc)"
    ISSUED_ATDESC = "issued_at(desc)"
    LAST_SENT_ATASC = "last_sent_at(asc)"
    LAST_SENT_ATDESC = "last_sent_at(desc)"
    MATTER_DISPLAY_NUMBERASC = "matter_display_number(asc)"
    MATTER_DISPLAY_NUMBERDESC = "matter_display_number(desc)"
    NUMBERASC = "number(asc)"
    NUMBERDESC = "number(desc)"
    PAID_ATASC = "paid_at(asc)"
    PAID_ATDESC = "paid_at(desc)"

    def __str__(self) -> str:
        return str(self.value)
