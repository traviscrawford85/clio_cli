from enum import Enum


class FolderlistOrder(str, Enum):
    CREATED_ATASC = "created_at(asc)"
    CREATED_ATDESC = "created_at(desc)"
    DOCUMENT_NUMBERASC = "document_number(asc)"
    DOCUMENT_NUMBERDESC = "document_number(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"
    RECEIVED_ATASC = "received_at(asc)"
    RECEIVED_ATDESC = "received_at(desc)"
    UPDATED_ATASC = "updated_at(asc)"
    UPDATED_ATDESC = "updated_at(desc)"

    def __str__(self) -> str:
        return str(self.value)
