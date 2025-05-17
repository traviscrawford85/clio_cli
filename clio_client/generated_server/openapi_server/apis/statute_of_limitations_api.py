from fastapi import APIRouter, HTTPException, Path
from services.statute_of_limitations_service import StatuteOfLimitationsService
from generated_server.openapi_server.models import MatterUpdateRequestDataStatuteOfLimitations

router = APIRouter()
service = StatuteOfLimitationsService()

@router.post("/matters/{id}/compute_statute.json", response_model=MatterUpdateRequestDataStatuteOfLimitations)
async def compute_statute_of_limitations(
    id: int = Path(..., description="The unique identifier of the Matter")
):
    """
    Compute and update the statute of limitations for a Matter.
    """

    # 🚀 Example placeholder for fetching the matter date_of_incident:
    date_of_incident = "2022-01-01"  # In real use: fetch from DB or external API

    statute_due_date = service.compute_statute_due_date(date_of_incident)
    if not statute_due_date:
        raise HTTPException(status_code=400, detail="Missing date_of_incident; cannot compute statute date.")

    payload = service.prepare_update_payload(status="pending", due_at=statute_due_date)
    return payload
