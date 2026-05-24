from fastapi import APIRouter

from app.schemas.ask_schema import (
    AskRequest,
    AskResponse
)
from app.services.openai_service import (
    openai_service
)

router = APIRouter()


@router.post(
    "/ask",
    response_model=AskResponse
)
async def ask_question(
    request: AskRequest
):

    response = openai_service.ask(
        request.query
    )

    return AskResponse(
        response=response
    )