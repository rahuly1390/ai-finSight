from app.rag.embedding_service import (
    embedding_service
)

from app.rag.vector_store import (
    vector_store
)

from app.rag.bm25_store import (
    bm25_store
)


class HybridRetriever:

    def retrieve(
        self,
        query: str
    ):

        query_embedding = (
            embedding_service
            .generate_embedding(query)
        )

        vector_results = (
            vector_store.search(
                query_embedding
            )
        )

        bm25_results = (
            bm25_store.search(
                query
            )
        )

        merged = list(
            set(
                vector_results +
                bm25_results
            )
        )

        return merged[:5]


hybrid_retriever = (
    HybridRetriever()
)