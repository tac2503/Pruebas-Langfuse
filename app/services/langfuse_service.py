import os

from dotenv import load_dotenv
from langfuse import Langfuse

load_dotenv()


class _NoOpTrace:
	def start_observation(self, **kwargs):
		return _NoOpTrace()

	def update(self, **kwargs):
		return self

	def end(self, **kwargs):
		return None


class _NoOpLangfuse:
	def start_observation(self, **kwargs):
		return _NoOpTrace()

	def flush(self):
		return None


def _build_langfuse_client():
	public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
	secret_key = os.getenv("LANGFUSE_SECRET_KEY")
	base_url = os.getenv("LANGFUSE_BASE_URL") or os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

	if not public_key or not secret_key:
		return _NoOpLangfuse(), False

	try:
		client = Langfuse(
			public_key=public_key,
			secret_key=secret_key,
			base_url=base_url,
		)
		return client, True
	except Exception:
		return _NoOpLangfuse(), False


langfuse, LANGFUSE_ENABLED = _build_langfuse_client()
