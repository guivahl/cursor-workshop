from fastapi import APIRouter

from data import store
from schemas.models import Plan

router = APIRouter(prefix="/plans", tags=["plans"])


@router.get("", response_model=list[Plan])
def list_plans() -> list[dict]:
    return store.plans_list
