from fastapi import APIRouter
from app.services.langfuse_traces import get_traces

router = APIRouter()

@router.get("/traces")
def read_traces():
    return get_traces()
    
    