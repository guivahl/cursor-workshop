from fastapi import APIRouter

from schemas.models import SubscribeRequest, SubscribeResponse
from services.subscription import subscribe_user

router = APIRouter(tags=["subscriptions"])

@router.post("/users/{user_id}/subscribe", response_model=SubscribeResponse)
def subscribe(user_id: int, body: SubscribeRequest) -> dict:
    return subscribe_user(user_id, body.plan_id)
