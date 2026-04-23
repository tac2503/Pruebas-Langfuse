from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Mensaje del usuario")
    
class ChatResponse(BaseModel):
    response: str
    trace_enabled: bool
    