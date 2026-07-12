from pathlib import Path

from fastapi import APIRouter, File, UploadFile

from app.services.chunking_service import chunking_service
from app.services.embedding_service import embedding_service
from app.services.pdf_service import pdf_service
from app.services.vector_store_service import vector_store_service

router = APIRouter(prefix="/documents", tags=["documents"])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()

    file_path = UPLOAD_DIR / file.filename
    file_path.write_bytes(content)

    text = pdf_service.extract_text(file_path)
    chunks = chunking_service.chunk_text(text)
    embeddings = embedding_service.create_embeddings(chunks)

    document = vector_store_service.save_document(
        filename=file.filename,
        content_type=file.content_type,
    )

    saved_chunks = vector_store_service.save_chunks(
        document_id=document["id"],
        chunks=chunks,
        embeddings=embeddings,
    )

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(content),
        "saved_to": str(file_path),
        "text_preview": text[:500],
        "document_id": document["id"],
        "chunk_count": len(chunks),
        "saved_chunks": len(saved_chunks),
        "embedding_dimensions": len(embeddings[0]),
    }