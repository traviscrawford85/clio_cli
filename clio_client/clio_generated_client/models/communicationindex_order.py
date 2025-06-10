from enum import Enum


class CommunicationindexOrder(str, Enum):
    DATEASC = "date(asc)"
    DATEDESC = "date(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    MATTERASC = "matter(asc)"
    MATTERDESC = "matter(desc)"
    RECEIVED_ATASC = "received_at(asc)"
    RECEIVED_ATDESC = "received_at(desc)"

    def __str__(self) -> str:
        return str(self.value)
