# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import List, Optional

from clio_clients.models.communicationbase import CommunicationBase
from pydantic import Field
from clio_clients.models.communicationemlfilebase import CommunicationEmlFileBase
from clio_clients.models.documentbase import DocumentBase
from clio_clients.models.externalpropertybase import ExternalPropertyBase
from clio_clients.models.matterbase import MatterBase
from clio_clients.models.notificationeventsubscriberbase import NotificationEventSubscriberBase
from clio_clients.models.participant import Participant
from clio_clients.models.participant import Participant
from clio_clients.models.activitybase import ActivityBase
from clio_clients.models.userbase import UserBase


class Communication(CommunicationBase):
    communication_eml_file: Optional[CommunicationEmlFileBase] = None
    documents: Optional[List[DocumentBase]] = Field(None, description="Document")
    external_properties: Optional[List[ExternalPropertyBase]] = Field(
        None, description="ExternalProperty"
    )
    matter: Optional[MatterBase] = None
    notification_event_subscribers: Optional[List[NotificationEventSubscriberBase]] = (
        Field(None, description="NotificationEventSubscriber")
    )
    receivers: Optional[List[Participant]] = Field(None, description="Participant")
    senders: Optional[List[Participant]] = Field(None, description="Participant")
    time_entries: Optional[List[ActivityBase]] = Field(None, description="Activity")
    user: Optional[UserBase] = None
