users_list: list[dict] = [
    {"id": 1, "name": "Ana Silva", "email": "ana@email.com"},
    {"id": 2, "name": "Bruno Costa", "email": "bruno@email.com"},
    {"id": 3, "name": "Carla Mendes", "email": "carla@email.com"},
    {"id": 4, "name": "Diego Lima", "email": "diego@email.com"},
]

plans_list: list[dict] = [
    {"id": 1, "name": "Basic", "monthly_price": 29.0},
    {"id": 2, "name": "Pro", "monthly_price": 79.0},
    {"id": 3, "name": "Enterprise", "monthly_price": 199.0},
]

plans_by_id: dict[int, dict] = {plan["id"]: plan for plan in plans_list}

subscriptions: list[dict] = []
