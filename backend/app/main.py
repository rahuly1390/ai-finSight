from fastapi import FastAPI

from app.api.health import (
    router as health_router
)

from app.api.ask import (
    router as ask_router
)

from app.api.upload import (
    router as upload_router
)

from app.api.ask_rag import (
    router as ask_rag_router
)

from app.api.ask_agent import (
    router as ask_agent_router
)

from app.config.settings import (
    settings
)

app = FastAPI(
    title=settings.PROJECT_NAME
)

# Health API
app.include_router(
    health_router,
    prefix=settings.API_V1,
    tags=["Health"]
)

# OpenAI Ask API
app.include_router(
    ask_router,
    prefix=settings.API_V1,
    tags=["OpenAI"]
)

# Document Upload API
app.include_router(
    upload_router,
    prefix=settings.API_V1,
    tags=["Upload"]
)

# Hybrid RAG API
app.include_router(
    ask_rag_router,
    prefix=settings.API_V1,
    tags=["RAG"]
)

app.include_router(
    ask_agent_router,
    prefix=settings.API_V1,
    tags=["Agentic AI"]
)

@app.get("/")
async def root():

    return {
        "message": "FinSight AI Running",
        "version": "v0.2.0"
    }