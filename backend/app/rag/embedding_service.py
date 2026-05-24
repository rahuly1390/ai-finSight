from openai import OpenAI

from app.config.settings import (
    settings
)


class EmbeddingService:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def generate_embedding(
        self,
        text: str
    ):

        response = (
            self.client.embeddings.create(
                model="text-embedding-3-small",
                input=text
            )
        )

        return response.data[0].embedding


embedding_service = (
    EmbeddingService()
)