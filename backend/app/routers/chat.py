from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(response=f"You said: {request.message}")