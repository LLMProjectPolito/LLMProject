import os, threading, typing

AVAILABLE_MODELS = {
    "gemma-1b":      {"provider": "google", "id": "gemma-3-1b-it"},
    "gemma-4b":      {"provider": "google", "id": "gemma-3-4b-it"},
    "gemma-12b":     {"provider": "google", "id": "gemma-3-12b-it"},
    "gemma-27b":     {"provider": "openrouter", "id": "google/gemma-3-27b-it"},
    "llama-70b":     {"provider": "openrouter", "id": "meta-llama/llama-3.3-70b-instruct"},
    "chatgpt-oss":   {"provider": "openrouter", "id": "openai/gpt-oss-120b"},
}

def _get_base_callback():
    from langchain_core.callbacks import BaseCallbackHandler
    return BaseCallbackHandler

class TokenCounter:
    def __init__(self): 
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

def get_token_usage():
    return {"prompt_tokens": _global_counter.prompt, "completion_tokens": _global_counter.completion, "total_tokens": _global_counter.total}

def reset_token_usage():
    _global_counter.reset()

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

_google_rotator = KeyRotator(os.getenv("GOOGLE_API_KEYS", ""))

class SimpleGoogleGenAI:
    def __init__(self, model_id, temperature):
        self.model_id = model_id
        self.temp = temperature
        # No more fixed client here, we create one per-invoke for rotation
    def invoke(self, prompt):
        from google import genai
        from google.genai import types
        # ROTATION LOGIC: Pick next key for this specific call
        current_key = _google_rotator.next_key()
        client = genai.Client(api_key=current_key)
        
        if isinstance(prompt, list):
            content = prompt[0].content if hasattr(prompt[0], "content") else str(prompt[0])
        else:
            content = str(prompt)
            
        res = client.models.generate_content(model=self.model_id, contents=content)
        usage = res.usage_metadata
        _global_counter.add(
            getattr(usage, "prompt_token_count", 0) or 0,
            getattr(usage, "candidates_token_count", 0) or 0,
            getattr(usage, "total_token_count", 0) or 0
        )
        class Response: pass
        r = Response(); r.content = res.text or ""; return r

def _init_provider(provider: str, model_id: str, temperature: float) -> typing.Any:
    if provider == "google":
        return SimpleGoogleGenAI(model_id, temperature)
    elif provider == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(model=model_id, temperature=temperature, max_retries=1, callbacks=[_global_counter])
    elif provider == "openrouter":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model=model_id, temperature=temperature, max_retries=1, callbacks=[_global_counter],
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            default_headers={"HTTP-Referer": "http://localhost", "X-Title": "AgenticEval"}
        )
    else:
        raise ValueError(f"Unknown provider: {provider}")

def get_model(name: str, temperature: float = 0.2):
    cfg = AVAILABLE_MODELS.get(name)
    if not cfg:
        raise ValueError(f"Unknown model '{name}'. Available: {list(AVAILABLE_MODELS.keys())}")
    return _init_provider(cfg["provider"], cfg["id"], temperature)
