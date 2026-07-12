from openai import OpenAI

from app.config import (
    EMBEDDING_DIMENSIONS,
    EMBEDDING_MODEL,
    OPENROUTER_API_KEY,
)


class EmbeddingService:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY,
        )

    def create_embeddings(
        self,
        texts: list[str],
        batch_size: int = 50,
    ) -> list[list[float]]:
        embeddings = []

        for start in range(0, len(texts), batch_size):
            batch = texts[start:start + batch_size]

            response = self.client.embeddings.create(
                model=EMBEDDING_MODEL,
                input=batch,
                dimensions=EMBEDDING_DIMENSIONS,
            )

            embeddings.extend(
                item.embedding for item in response.data
            )

        return embeddings


embedding_service = EmbeddingService()