from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "RAG Agent Backend is running!"}