from fastapi import APIRouter
from app.services.langfuse_traces import get_traces,simplify_trace,get_traces_id,simplify_traces

router = APIRouter()

@router.get("/traces")
def read_traces():
    traces= get_traces()
    return simplify_traces(traces)
@router.get("/traces/{trace_id}")
def read_trace(trace_id:str):
    trace= get_traces_id(trace_id)
    return simplify_trace(trace)