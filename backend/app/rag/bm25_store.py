from rank_bm25 import BM25Okapi


class BM25Store:

    def __init__(self):

        self.documents = []
        self.bm25 = None

    def add_documents(
        self,
        chunks
    ):

        self.documents.extend(
            chunks
        )

        tokenized_docs = [
            doc.split()
            for doc in self.documents
        ]

        self.bm25 = BM25Okapi(
            tokenized_docs
        )

    def search(
        self,
        query,
        top_k=5
    ):

        if not self.bm25:
            return []

        tokenized_query = (
            query.split()
        )

        docs = self.bm25.get_top_n(
            tokenized_query,
            self.documents,
            n=top_k
        )

        return docs


bm25_store = BM25Store()