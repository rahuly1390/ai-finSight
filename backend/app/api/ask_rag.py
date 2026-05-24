from fastapi import APIRouter

from app.schemas.ask_schema import (
    AskRequest
)

from app.services.openai_service import (
    openai_service
)

from app.rag.retriever import (
    hybrid_retriever
)

router = APIRouter()


@router.post("/ask-rag")
async def ask_rag(
    request: AskRequest
):

    retrieved_docs = (
        hybrid_retriever.retrieve(
            request.query
        )
    )

    context = "\n\n".join(
        retrieved_docs
    )

    prompt = f"""
    Context:
    {context}

    Question:
    {request.query}
    """

    response = (
        openai_service.ask(
            prompt
        )
    )

    return {
        "retrieved_docs":
        retrieved_docs,

        "response":
        response
    }