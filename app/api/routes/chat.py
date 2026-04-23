from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ollama_service import generate_response
from app.services.langfuse_service import LANGFUSE_ENABLED, langfuse


router = APIRouter()

@router.post("/", responses={502: {"description": "Error al llamar a Ollama"}})
def chat(req: ChatRequest) -> ChatResponse:
    trace = langfuse.start_observation(
        name="chat-request",
        as_type="span",
        input={"message": req.message},
    )
    generation = trace.start_observation(
        name="ollama-response",
        as_type="generation",
        input=req.message,
    )
    
    try: 
        response = generate_response(req.message)

        generation.update(output=response)
        generation.end()
        
        trace.update(output={"response": response})
        trace.end()
        langfuse.flush()
        
        return ChatResponse(response=response, trace_enabled=LANGFUSE_ENABLED)
    
    except Exception as e:
        generation.update(level="error", output=str(e))
        generation.end()
        trace.update(
            level="error",
            output=str(e)
        )
        trace.end()
        langfuse.flush()
        raise HTTPException(status_code=502, detail=str(e)) from e