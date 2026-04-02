from __future__ import annotations

import re


def classify_generation_error(exc: Exception) -> dict[str, object]:
    message = str(exc).strip()
    normalized = message.lower()

    error_type = "unknown_error"
    retryable = False

    if _contains_any(normalized, ["429", "rate limit", "resource_exhausted", "quota exceeded", "retry in"]):
        error_type = "rate_limit"
        retryable = True
    elif _contains_any(normalized, ["maximum context length", "context length", "too many tokens", "token limit", "max tokens"]):
        error_type = "token_limit"
    elif _contains_any(normalized, ["timeout", "timed out", "deadline exceeded"]):
        error_type = "timeout"
        retryable = True
    elif _contains_any(normalized, ["validation error", "validation errors", "pydantic"]):
        error_type = "validation_error"
    elif _contains_any(normalized, ["unexpected keyword argument", "missing required positional argument", "unknown model"]):
        error_type = "config_error"
    elif _contains_any(normalized, ["api key", "unauthorized", "permission denied", "forbidden", "authentication"]):
        error_type = "auth_error"
    elif _contains_any(normalized, ["503", "502", "500", "service unavailable", "temporarily unavailable", "connection reset", "connection aborted"]):
        error_type = "provider_error"
        retryable = True

    return {
        "type": error_type,
        "retryable": retryable,
        "message": _sanitize_error_message(message),
    }


def compute_retry_delay(attempt: int, base_seconds: float = 5.0, max_seconds: float = 90.0) -> float:
    delay = min(base_seconds * (2 ** max(0, attempt - 1)), max_seconds)
    jitter = min(1.5 * attempt, 5.0)
    return round(delay + jitter, 2)


def _sanitize_error_message(message: str, max_chars: int = 500) -> str:
    single_line = re.sub(r"\s+", " ", message).strip()
    return single_line[:max_chars]


def _contains_any(text: str, patterns: list[str]) -> bool:
    return any(pattern in text for pattern in patterns)
