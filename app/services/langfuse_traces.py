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

# if __name__ == "__main__":
#     traces = get_traces()
#     print(json.dumps(traces, indent=2, ensure_ascii=False))