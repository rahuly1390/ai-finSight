from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)


class ChunkingService:

    def __init__(self):

        self.text_splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=800,
                chunk_overlap=150
            )
        )

    def create_chunks(
        self,
        text: str
    ):

        return self.text_splitter.split_text(
            text
        )


chunking_service = (
    ChunkingService()
)