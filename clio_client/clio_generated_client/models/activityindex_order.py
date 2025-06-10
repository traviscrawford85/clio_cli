from enum import Enum


class ActivityindexOrder(str, Enum):
    DATEASC = "date(asc)"
    DATEDESC = "date(desc)"
    DISPLAY_NUMBERASC = "display_number(asc)"
    DISPLAY_NUMBERDESC = "display_number(desc)"
    EXPENSE_CATEGORY_NAMEASC = "expense_category.name(asc)"
    EXPENSE_CATEGORY_NAMEDESC = "expense_category.name(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NON_BILLABLEASC = "non_billable(asc)"
    NON_BILLABLEDESC = "non_billable(desc)"
    NON_BILLABLE_TOTALASC = "non_billable_total(asc)"
    NON_BILLABLE_TOTALDESC = "non_billable_total(desc)"
    NOTEASC = "note(asc)"
    NOTEDESC = "note(desc)"
    PRICEASC = "price(asc)"
    PRICEDESC = "price(desc)"
    TOTALASC = "total(asc)"
    TOTALDESC = "total(desc)"
    TYPEASC = "type(asc)"
    TYPEDESC = "type(desc)"
    UPDATED_ATASC = "updated_at(asc)"
    UPDATED_ATDESC = "updated_at(desc)"
    USER_NAMEASC = "user.name(asc)"
    USER_NAMEDESC = "user.name(desc)"
    VENDOR_NAMEASC = "vendor.name(asc)"
    VENDOR_NAMEDESC = "vendor.name(desc)"

    def __str__(self) -> str:
        return str(self.value)
