from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.routes.chat import router as chat_router

load_dotenv()

app = FastAPI(title="Ollama + Langfuse PoC",
    version="1.0.0") 
app.include_router(chat_router, prefix="/api/chat", tags=["chat"])

