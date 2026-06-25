from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


class Plan(BaseModel):
    id: int
    name: str
    monthly_price: float


class SubscribeRequest(BaseModel):
    plan_id: int


class SubscribeResponse(BaseModel):
    user_id: int
    plan_id: int
    plan_name: str
    monthly_price: float
    message: str


class Subscription(BaseModel):
    user_id: int
    plan_id: int
    monthly_price: float
    created_at: datetime
