from fastapi import FastAPI

from routers import plans, subscriptions, users

app = FastAPI(title="API de Assinaturas", version="1.0.0")

app.include_router(users.router)
app.include_router(plans.router)
app.include_router(subscriptions.router)