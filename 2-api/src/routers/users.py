from fastapi import APIRouter

from data import store
from schemas.models import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[User])
def list_users() -> list[dict]:
    return store.users_list
