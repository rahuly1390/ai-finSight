from typing import TypedDict


class GraphState(TypedDict):

    query: str

    retrieved_docs: list

    rag_response: str

    risk_analysis: str

    wealth_advice: str

    final_response: str