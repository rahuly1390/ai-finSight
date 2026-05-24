from app.services.openai_service import (
    openai_service
)

from app.prompts.risk_prompt import (
    RISK_PROMPT
)


class RiskAgent:

    def run(
        self,
        state
    ):

        rag_context = (
            state["rag_response"]
        )

        query = state["query"]

        prompt = f"""
        {RISK_PROMPT}

        User Query:
        {query}

        Financial Context:
        {rag_context}
        """

        risk_analysis = (
            openai_service.ask(
                prompt
            )
        )

        state["risk_analysis"] = (
            risk_analysis
        )

        state["final_response"] = (
            risk_analysis
        )

        return state


risk_agent = RiskAgent()