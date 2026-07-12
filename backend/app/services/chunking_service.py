class ChunkingService:
    def chunk_text(
        self,
        text: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ) -> list[str]:
        text = text.replace("\x00", " ")

        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end].strip()

            if chunk:
                chunks.append(chunk)

            start += chunk_size - chunk_overlap

        return chunks


chunking_service = ChunkingService()