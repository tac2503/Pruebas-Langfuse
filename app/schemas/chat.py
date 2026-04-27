from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Mensaje del usuario")
    user_id: str = Field(..., min_length=1, description="ID del usuario que hace la consulta")
class ChatResponse(BaseModel):
    response: str
    trace_enabled: bool
