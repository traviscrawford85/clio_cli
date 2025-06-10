from enum import Enum


class MedicalRecordsRequestupdateFilesBodyDataBillsStatus(str, Enum):
    CERTIFIED = "certified"
    INCOMPLETE = "incomplete"
    NOT_YET_REQUESTED = "not_yet_requested"
    RECEIVED = "received"
    REQUESTED = "requested"

    def __str__(self) -> str:
        return str(self.value)
