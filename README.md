# Pruebas-Langfuse
Pruebas de la herramienta Langfuse

## Configuracion

Crear un archivo `.env` en la raiz del proyecto:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
OLLAMA_TIMEOUT_SECONDS=90

LANGFUSE_PUBLIC_KEY=tu_public_key
LANGFUSE_SECRET_KEY=tu_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

## Ejecutar

```bash
uvicorn app.main:app --reload
```

## Probar

```bash
curl -X POST "http://127.0.0.1:8000/api/chat/" \
	-H "Content-Type: application/json" \
	-d "{\"message\": \"Hola, resume FastAPI en 2 lineas\"}"
```

Respuesta esperada:

```json
{
	"response": "...",
	"trace_enabled": true
}
```

Si `trace_enabled` es `false`, la API sigue respondiendo, pero sin enviar trazas a Langfuse.
