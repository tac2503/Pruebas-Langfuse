import requests
import os 
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")


def generate_response(message: str) -> str:
    endpoint = f"{OLLAMA_BASE_URL.rstrip('/')}/api/generate"
    data = {
        "model": "deepseek-v3.1:671b-cloud", 
        "prompt": message,
        "stream": False,
    }

    try:
        response = requests.post(endpoint, json=data)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Error al llamar a Ollama: {exc}") from exc

    body = response.json()
    output = body.get("response")
    if not output:
        raise RuntimeError("Ollama devolvio una respuesta vacia")

    return output

