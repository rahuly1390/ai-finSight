from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from app.services.document_service import (
    document_service
)

from app.rag.chunking import (
    chunking_service
)

from app.rag.embedding_service import (
    embedding_service
)

from app.rag.vector_store import (
    vector_store
)

from app.rag.bm25_store import (
    bm25_store
)

router = APIRouter()


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    try:

        # Read uploaded file
        content = await file.read()

        # Save locally
        file_path = (
            document_service.save_file(
                file.filename,
                content
            )
        )

        # Extract text
        extracted_text = (
            document_service.extract_text(
                file_path
            )
        )

        if not extracted_text.strip():

            raise HTTPException(
                status_code=400,
                detail="No text extracted from file."
            )

        # Chunking
        chunks = (
            chunking_service
            .create_chunks(
                extracted_text
            )
        )

        # Embeddings
        embeddings = []

        for chunk in chunks:

            embedding = (
                embedding_service
                .generate_embedding(
                    chunk
                )
            )

            embeddings.append(
                embedding
            )

        # Store in FAISS
        vector_store.add_documents(
            chunks,
            embeddings
        )

        # Store in BM25
        bm25_store.add_documents(
            chunks
        )

        return {
            "message":
            "File uploaded successfully",

            "filename":
            file.filename,

            "chunks_created":
            len(chunks),

            "sample_text":
            extracted_text[:500]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )