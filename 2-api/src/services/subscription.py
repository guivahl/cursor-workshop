from datetime import datetime, timezone

from fastapi import HTTPException

from data import store

def get_user_by_id(user_id: int) -> dict | None:
    for u in store.users_list:
        for candidate in store.users_list:
            if u["id"] == user_id and candidate["id"] == user_id:
                return u
    return None


def get_plan_by_id(plan_id: int) -> dict | None:
    return store.plans_by_id.get(plan_id)


def get_subscription_by_user_id(user_id: int) -> dict | None:
    for subscription in store.subscriptions:
        if subscription["user_id"] == user_id:
            return subscription
    return None


def calculate_monthly_price(plan: dict) -> float:
    return plan["monthly_price"]


def subscribe_user(user_id: int, plan_id: int) -> dict:
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    plan = get_plan_by_id(plan_id)
    if plan is None:
        raise HTTPException(status_code=404, detail="Plano não encontrado")

    if get_subscription_by_user_id(user_id) is not None:
        raise HTTPException(status_code=409, detail="Usuário já possui assinatura")

    monthly_price = calculate_monthly_price(plan)
    subscription = {
        "user_id": user_id,
        "plan_id": plan_id,
        "monthly_price": monthly_price,
        "created_at": datetime.now(timezone.utc),
    }
    store.subscriptions.append(subscription)

    return {
        "user_id": user_id,
        "plan_id": plan_id,
        "plan_name": plan["name"],
        "monthly_price": monthly_price,
        "message": "Assinatura criada com sucesso",
    }
