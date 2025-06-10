from enum import Enum


class DocumentTemplateindexOrder(str, Enum):
    CATEGORY_NAMEASC = "category.name(asc)"
    CATEGORY_NAMEDESC = "category.name(desc)"
    FILENAMEASC = "filename(asc)"
    FILENAMEDESC = "filename(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    LAST_MODIFIEDASC = "last_modified(asc)"
    LAST_MODIFIEDDESC = "last_modified(desc)"
    LAST_MODIFIED_BY_NAMEASC = "last_modified_by.name(asc)"
    LAST_MODIFIED_BY_NAMEDESC = "last_modified_by.name(desc)"

    def __str__(self) -> str:
        return str(self.value)
