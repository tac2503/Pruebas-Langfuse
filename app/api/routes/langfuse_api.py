from fastapi import APIRouter
from app.services.langfuse_traces import get_traces,simplify_traces

router = APIRouter()

@router.get("/traces")
def read_traces():
    traces= get_traces()
    return simplify_traces(traces)