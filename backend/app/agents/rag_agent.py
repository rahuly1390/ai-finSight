from app.rag.retriever import (
    hybrid_retriever
)

from app.services.openai_service import (
    openai_service
)

from app.prompts.rag_prompt import (
    RAG_PROMPT
)


class RAGAgent:

    def run(
        self,
        state
    ):

        query = state["query"]

        retrieved_docs = (
            hybrid_retriever.retrieve(
                query
            )
        )

        context = "\n\n".join(
            retrieved_docs
        )

        prompt = f"""
        {RAG_PROMPT}

        Context:
        {context}

        Question:
        {query}
        """

        rag_response = (
            openai_service.ask(
                prompt
            )
        )

        state["retrieved_docs"] = (
            retrieved_docs
        )

        state["rag_response"] = (
            rag_response
        )

        return state


rag_agent = RAGAgent()