from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm_service import LLMService

router = APIRouter(prefix="/chat", tags=["chat"])

llm_service = LLMService()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = llm_service.generate_response(request.message)
    return ChatResponse(response=response)