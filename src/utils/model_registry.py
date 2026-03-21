import os
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel

AVAILABLE_MODELS = {
    "llama3-8b": {
        "primary":   {"provider": "cerebras",   "id": "llama3.1-8b"},
        "fallbacks": [
            {"provider": "gemini",     "id": "gemini-1.5-flash"},
            {"provider": "groq",       "id": "llama-3.1-8b-instant"}
        ]
    },
    "llama3-70b": {
        "primary":   {"provider": "groq",       "id": "llama-3.3-70b-versatile"},
        "fallbacks": [
            {"provider": "gemini",     "id": "gemini-1.5-pro"},
            {"provider": "openrouter", "id": "meta-llama/llama-3.3-70b-instruct:free"}
        ]
    },
    "qwen": {
        "primary":   {"provider": "cerebras",   "id": "qwen-3-235b-a22b-instruct-2507"},
        "fallbacks": [
            {"provider": "gemini",     "id": "gemini-2.0-flash"},
            {"provider": "openrouter", "id": "qwen/qwen3-coder:free"}
        ]
    },
    
    "llama3-3b": {"provider": "openrouter", "id": "meta-llama/llama-3.2-3b-instruct:free"},
    "gemma-2b":  {"provider": "gemini",     "id": "gemma-3-4b-it"},
    "gemma-4b":  {"provider": "gemini",     "id": "gemma-3-4b-it"},
    "gemma-1b":  {"provider": "gemini",     "id": "gemma-3-1b-it"},
    "qwen-1.5b": {"provider": "openrouter", "id": "qwen/qwen-2.5-1.5b-instruct:free"},
    "liquid-1.2b":{"provider": "openrouter", "id": "liquid/lfm-2.5-1.2b-instruct:free"},

    "scout":         {"provider": "groq",   "id": "meta-llama/llama-4-scout-17b-16e-instruct"},
    "kimi":          {"provider": "groq",   "id": "moonshotai/kimi-k2-instruct"},
    "gemini-flash":  {"provider": "gemini", "id": "models/gemini-1.5-flash"},
    "gemini-lite":   {"provider": "gemini", "id": "models/gemini-1.5-flash-8b"},
    "gemma-12b":     {"provider": "gemini", "id": "gemma-3-12b-it"},
    "gemma-27b":     {"provider": "gemini", "id": "gemma-3-27b-it"},
    "chatgpt-oss":   {"provider": "openrouter", "id": "openai/gpt-oss-120b"},
}

def _init_provider(provider: str, model_id: str, temperature: float) -> BaseChatModel:
    if provider == "groq":
        return ChatGroq(model=model_id, temperature=temperature, max_retries=1) # Limit groq retries so it hits fallback quickly
    elif provider == "gemini":
        return ChatGoogleGenerativeAI(model=model_id, temperature=temperature)
    elif provider == "openrouter":
        return ChatOpenAI(
            model=model_id, temperature=temperature, max_retries=1,
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            default_headers={"HTTP-Referer": "http://localhost", "X-Title": "AgenticEval"}
        )
    elif provider == "cerebras":
        return ChatOpenAI(
            model=model_id, temperature=temperature, max_retries=1,
            api_key=os.getenv("CEREBRAS_API_KEY"),
            base_url="https://api.cerebras.ai/v1",
        )
    else:
        raise ValueError(f"Unknown provider: {provider}")

def get_model(name: str, temperature: float = 0.2):
    cfg = AVAILABLE_MODELS.get(name)
    if not cfg:
        raise ValueError(f"Unknown model '{name}'. Available: {list(AVAILABLE_MODELS.keys())}")

    # Fallback Schema Check
    if "primary" in cfg:
        primary = _init_provider(cfg["primary"]["provider"], cfg["primary"]["id"], temperature)
        fallbacks = []
        for f in cfg.get("fallbacks", []):
            try:
                fallbacks.append(_init_provider(f["provider"], f["id"], temperature))
            except Exception:
                pass
        
        if fallbacks:
            return primary.with_fallbacks(fallbacks)
        return primary
    
    # Old direct Schema Check
    return _init_provider(cfg["provider"], cfg["id"], temperature)
