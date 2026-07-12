from pathlib import Path

from pypdf import PdfReader


class PDFService:
    def extract_text(self, file_path: Path) -> str:
        reader = PdfReader(file_path)

        text_parts = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text_parts.append(page_text)

        return "\n".join(text_parts)


pdf_service = PDFService()