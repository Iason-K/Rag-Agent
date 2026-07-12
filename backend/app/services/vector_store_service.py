from app.services.database_service import database_service


class VectorStoreService:
    def save_document(self, filename: str, content_type: str):
        response = (
            database_service.client
            .table("documents")
            .insert({
                "filename": filename,
                "content_type": content_type,
            })
            .execute()
        )

        return response.data[0]

    def save_chunks(
        self,
        document_id: int,
        chunks: list[str],
        embeddings: list[list[float]],
    ):
        rows = [
            {
                "document_id": document_id,
                "content": chunk,
                "embedding": embedding,
            }
            for chunk, embedding in zip(chunks, embeddings)
        ]

        response = (
            database_service.client
            .table("chunks")
            .insert(rows)
            .execute()
        )

        return response.data


vector_store_service = VectorStoreService()