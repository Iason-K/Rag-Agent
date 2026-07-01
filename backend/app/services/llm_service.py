from openai import OpenAI

from app.config import OPENROUTER_API_KEY, LLM_MODEL


class LLMService:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY,
        )

    def generate_response(self, message: str) -> str:
        completion = self.client.chat.completions.create(
    model=LLM_MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful RAG assistant. Keep answers short."},
        {"role": "user", "content": message},
    ],
    max_tokens=500,
)

        return completion.choices[0].message.content