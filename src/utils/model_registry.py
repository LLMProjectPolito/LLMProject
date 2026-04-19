import os, threading, typing
from contextlib import nullcontext

AVAILABLE_MODELS = {
    "gemma-1b":      {"provider": "google", "id": "gemma-3-1b-it"},
    "gemma-4b":      {"provider": "google", "id": "gemma-3-4b-it"},
    "gemma-12b":     {"provider": "google", "id": "gemma-3-12b-it"},
    "gemma-27b":     {"provider": "google", "id": "gemma-3-27b-it"},
    "gemma-31b":     {"provider": "google", "id": "gemma-4-31b-it"},
    "llama-70b":     {"provider": "openrouter", "id": "meta-llama/llama-3.3-70b-instruct"},
    "chatgpt-oss":   {"provider": "openrouter", "id": "openai/gpt-oss-120b"},
    "gemma-4-31b":   {"provider": "google", "id": "gemma-4-31b-it"},
    "gemma-4-26b":   {"provider": "google", "id": "gemma-4-26b-a4b-it"},
    "gemma-4-4b":    {"provider": "google", "id": "gemma-3n-e4b-it"},
    "gemma-4-2b":    {"provider": "google", "id": "gemma-3n-e2b-it"},
}

from langchain_core.callbacks import BaseCallbackHandler

class TokenCounter(BaseCallbackHandler):
    def __init__(self): 
        super().__init__()
        self.prompt=0; self.completion=0; self.total=0; self._lock=threading.Lock()
    def reset(self):
        with self._lock: self.prompt=self.completion=self.total=0
    def add(self, p, c, t):
        with self._lock: self.prompt += p; self.completion += c; self.total += t
    def on_llm_end(self, response, **kwargs):
        with self._lock:
            for generations in response.generations:
                for gen in generations:
                    usage = gen.generation_info.get("token_usage", {})
                    self.prompt += usage.get("prompt_tokens", 0)
                    self.completion += usage.get("completion_tokens", 0)
                    self.total += usage.get("total_tokens", 0)

_global_counter = TokenCounter()

DEFAULT_MAX_OUTPUT_TOKENS = int(os.getenv("MODEL_MAX_OUTPUT_TOKENS", "2048"))
DEFAULT_PROVIDER_LIMITS = {
    "google": int(os.getenv("GOOGLE_MAX_CONCURRENT_PER_MODEL", "2")),
    "openrouter": int(os.getenv("OPENROUTER_MAX_CONCURRENT_PER_MODEL", "4")),
    "groq": int(os.getenv("GROQ_MAX_CONCURRENT_PER_MODEL", "4")),
}
_provider_model_limiters: dict[tuple[str, str], threading.Semaphore] = {}
_provider_model_lock = threading.Lock()

def get_token_usage():
    return {"prompt_tokens": _global_counter.prompt, "completion_tokens": _global_counter.completion, "total_tokens": _global_counter.total}

def reset_token_usage():
    _global_counter.reset()


def _get_model_limiter(provider: str, model_id: str):
    limit = DEFAULT_PROVIDER_LIMITS.get(provider, 0)
    if limit <= 0:
        return None
    key = (provider, model_id)
    with _provider_model_lock:
        limiter = _provider_model_limiters.get(key)
        if limiter is None:
            limiter = threading.Semaphore(limit)
            _provider_model_limiters[key] = limiter
        return limiter

class KeyRotator:
    def __init__(self, keys_str):
        self.keys = [k.strip() for k in keys_str.split(",") if k.strip()]
        if not self.keys:
            self.keys = [os.getenv("GOOGLE_API_KEY")]
        self.idx = 0
        self._lock = threading.Lock()
    def next_key(self):
        with self._lock:
            key = self.keys[self.idx]
            self.idx = (self.idx + 1) % len(self.keys)
            return key

# Rotazione specifica tra G1 e G2 del tuo account
_google_rotator = KeyRotator(",".join([os.getenv("G1", ""), os.getenv("G2", "")]).strip(","))

class SimpleGoogleGenAI:
    def __init__(self, model_id, temperature):
        self.model_id = model_id
        self.temp = temperature
        self.max_output_tokens = DEFAULT_MAX_OUTPUT_TOKENS
        self._limiter = _get_model_limiter("google", model_id)
    def invoke(self, prompt):
        from google import genai
        from google.genai import types
        with self._limiter or nullcontext():
            current_key = _google_rotator.next_key()
            client = genai.Client(api_key=current_key)

            if isinstance(prompt, list):
                content = prompt[0].content if hasattr(prompt[0], "content") else str(prompt[0])
            else:
                content = str(prompt)

            res = client.models.generate_content(
                model=self.model_id,
                contents=content,
                config=types.GenerateContentConfig(
                    temperature=self.temp,
                    maxOutputTokens=self.max_output_tokens,
                ),
            )
        usage = res.usage_metadata
        _global_counter.add(
            getattr(usage, "prompt_token_count", 0) or 0,
            getattr(usage, "candidates_token_count", 0) or 0,
            getattr(usage, "total_token_count", 0) or 0
        )
        class Response: pass
        r = Response(); r.content = res.text or ""; return r


class RateLimitedModel:
    def __init__(self, model, provider: str, model_id: str):
        self._model = model
        self._limiter = _get_model_limiter(provider, model_id)

    def invoke(self, *args, **kwargs):
        with self._limiter or nullcontext():
            return self._model.invoke(*args, **kwargs)

    def __getattr__(self, item):
        return getattr(self._model, item)

def _init_provider(provider: str, model_id: str, temperature: float) -> typing.Any:
    if provider == "google":
        return SimpleGoogleGenAI(model_id, temperature)
    elif provider == "groq":
        from langchain_groq import ChatGroq
        model = ChatGroq(model=model_id, temperature=temperature, max_retries=1, callbacks=[_global_counter])
        return RateLimitedModel(model, provider, model_id)
    elif provider == "openrouter":
        from langchain_openai import ChatOpenAI
        # Robust key retrieval: check multiple names and ensure it's not an empty string
        api_key = os.getenv("OR")
        if not api_key:
            api_key = None # Let it fail explicitly if missing
            
        model = ChatOpenAI(
            model=model_id, temperature=temperature, max_retries=1, 
            callbacks=[_global_counter],
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
            default_headers={"HTTP-Referer": "http://localhost", "X-Title": "AgenticEval"},
            max_completion_tokens=DEFAULT_MAX_OUTPUT_TOKENS,
        )
        return RateLimitedModel(model, provider, model_id)
    else:
        raise ValueError(f"Unknown provider: {provider}")

def get_model(name: str, temperature: float = 0.2):
    cfg = AVAILABLE_MODELS.get(name)
    if not cfg:
        raise ValueError(f"Unknown model '{name}'. Available: {list(AVAILABLE_MODELS.keys())}")
    return _init_provider(cfg["provider"], cfg["id"], temperature)
