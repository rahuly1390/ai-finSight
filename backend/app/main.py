from fastapi import FastAPI

from app.api.health import (
    router as health_router
)
from app.api.ask import (
    router as ask_router
)
from app.config.settings import settings


app = FastAPI(
    title=settings.PROJECT_NAME
)

app.include_router(
    health_router,
    prefix=settings.API_V1
)

app.include_router(
    ask_router,
    prefix=settings.API_V1
)


@app.get("/")
async def root():

    return {
        "message": "FinSight AI Running"
    }