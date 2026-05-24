from app.agents.rag_agent import (
    rag_agent
)

from app.agents.risk_agent import (
    risk_agent
)

from app.agents.wealth_agent import (
    wealth_agent
)


def rag_node(state):

    return rag_agent.run(
        state
    )


def risk_node(state):

    return risk_agent.run(
        state
    )


def wealth_node(state):

    return wealth_agent.run(
        state
    )