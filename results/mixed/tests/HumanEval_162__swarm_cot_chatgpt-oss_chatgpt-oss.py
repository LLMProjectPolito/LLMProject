import pytest
import hashlib
import math  # Imported as per requirement, though not used directly in these tests.

def test_string_to_md5_empty_string_returns_none():
    """Empty input should return None."""
    assert string_to_md5("") is None

def test_string_to_md5_space_only():
    """A single space should produce its known MD5 hash."""
    assert string_to_md5(" ") == "7215ee9c7d9dc229d2921a40e899ec5f"

def test_string_to_md5_very_long_input():
    """Very long input (1,000,000 'a's) should match hashlib's result."""
    long_text = "a" * 1_000_000
    expected = hashlib.md5(long_text.encode()).hexdigest()
    assert string_to_md5(long_text) == expected