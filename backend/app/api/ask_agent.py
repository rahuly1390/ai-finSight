from fastapi import APIRouter

from app.schemas.ask_schema import (
    AskRequest
)

from app.graph.workflow import (
    agent_workflow
)

router = APIRouter()


@router.post("/ask-agent")
async def ask_agent(
    request: AskRequest
):

    result = (
        agent_workflow.run(
            request.query
        )
    )

    return {

        "query":
        request.query,

        "retrieved_docs":
        result[
            "retrieved_docs"
        ],

        "risk_analysis":
        result[
            "risk_analysis"
        ],

        "wealth_advice":
        result[
            "wealth_advice"
        ]
    }