from datetime import timedelta
from typing import Optional

from models import MatterUpdateRequestDataStatuteOfLimitations  # generated model


class StatuteOfLimitationsService:
    """
    Service to handle computation and update of Statute of Limitations.
    """

    def compute_statute_due_date(self, date_of_incident: Optional[str]) -> Optional[str]:
        """
        Compute the statute of limitations date as 3 years from the date of incident.
        """
        if not date_of_incident:
            return None
        
        incident_date = date.fromisoformat(date_of_incident)
        statute_due_date = incident_date + timedelta(days=3 * 365)
        return statute_due_date.isoformat()

    def prepare_update_payload(self, status: str, due_at: str) -> MatterUpdateRequestDataStatuteOfLimitations:
        """
        Prepare the update payload.
        """
        return MatterUpdateRequestDataStatuteOfLimitations(
            status=status,
            due_at=due_at,
            reminders=[]
        )
