import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")

def get_traces():
    credentials= f"{LANGFUSE_PUBLIC_KEY}:{LANGFUSE_SECRET_KEY}"
    encoded_credentials: str = base64.b64encode(credentials.encode()).decode()
    
    headers={
        "Authorization": f"Basic {encoded_credentials}"
    }
    
    url ="https://cloud.langfuse.com/api/public/traces"
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_traces_id(trace_id:str):
    credentials= f"{LANGFUSE_PUBLIC_KEY}:{LANGFUSE_SECRET_KEY}"
    encoded_credentials: str = base64.b64encode(credentials.encode()).decode()
    
    headers={
        "Authorization": f"Basic {encoded_credentials}"
    }
    
    url =f"https://cloud.langfuse.com/api/public/traces/{trace_id}"
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def simplify_traces(traces:dict):
    traces=traces.get("data",[])
    simplified = []
    
    for t in traces:
        simplified.append({
            "id":t.get("id"),
            "name":t.get("name"),
            "input":t.get("input"),
            "output":t.get("output"),
            "metadata":t.get("metadata"),
            "totalCost":t.get("totalCost"),
            "latency":t.get("latency")
        })
    return simplified

def simplify_trace(trace:dict):
    simplified = {
        "id":trace.get("id"),
        "name":trace.get("name"),
        "input":trace.get("input"),
        "output":trace.get("output"),
        "metadata":trace.get("metadata"),
        "totalCost":trace.get("totalCost"),
        "latency":trace.get("latency")
    }
    return simplified
