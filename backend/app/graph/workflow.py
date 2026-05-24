from langgraph.graph import (
    StateGraph,
    END
)

from app.graph.state import (
    GraphState
)

from app.graph.nodes import (
    rag_node,
    risk_node,
    wealth_node
)


class AgentWorkflow:

    def __init__(self):

        workflow = StateGraph(
            GraphState
        )

        workflow.add_node(
            "rag_agent",
            rag_node
        )

        workflow.add_node(
            "risk_agent",
            risk_node
        )

        workflow.add_node(
            "wealth_agent",
            wealth_node
        )

        workflow.set_entry_point(
            "rag_agent"
        )

        workflow.add_edge(
            "rag_agent",
            "risk_agent"
        )

        workflow.add_edge(
            "risk_agent",
            "wealth_agent"
        )

        workflow.add_edge(
            "wealth_agent",
            END
        )

        self.graph = (
            workflow.compile()
        )

    def run(
        self,
        query: str
    ):

        state = {

            "query": query,

            "retrieved_docs": [],

            "rag_response": "",

            "risk_analysis": "",

            "wealth_advice": "",

            "final_response": ""
        }

        return self.graph.invoke(
            state
        )


agent_workflow = (
    AgentWorkflow()
)