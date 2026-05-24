import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.dimension = 1536

        self.index = faiss.IndexFlatL2(
            self.dimension
        )

        self.documents = []

    def add_documents(
        self,
        chunks,
        embeddings
    ):

        vectors = np.array(
            embeddings,
            dtype="float32"
        )

        self.index.add(vectors)

        self.documents.extend(chunks)

    def search(
        self,
        embedding,
        top_k=5
    ):

        vector = np.array(
            [embedding],
            dtype="float32"
        )

        scores, indices = (
            self.index.search(
                vector,
                top_k
            )
        )

        results = []

        for idx in indices[0]:

            if idx < len(
                self.documents
            ):

                results.append(
                    self.documents[idx]
                )

        return results


vector_store = VectorStore()