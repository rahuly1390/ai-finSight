from app.services.openai_service import (
    openai_service
)

from app.prompts.wealth_prompt import (
    WEALTH_PROMPT
)


class WealthAdvisoryAgent:

    def run(
        self,
        state
    ):

        query = state["query"]

        risk_analysis = (
            state["risk_analysis"]
        )

        rag_context = (
            state["rag_response"]
        )

        prompt = f"""
        {WEALTH_PROMPT}

        User Question:
        {query}

        Retrieved Financial Context:
        {rag_context}

        Risk Analysis:
        {risk_analysis}
        """

        wealth_advice = (
            openai_service.ask(
                prompt
            )
        )

        state["wealth_advice"] = (
            wealth_advice
        )

        state["final_response"] = (
            wealth_advice
        )

        return state


wealth_agent = (
    WealthAdvisoryAgent()
)