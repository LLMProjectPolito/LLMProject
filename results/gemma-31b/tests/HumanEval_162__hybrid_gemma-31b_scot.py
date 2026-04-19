
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from typing import Any

def calculate_expected_md5(text: str) -> str:
    """Helper function to generate ground-truth MD5 hash for verification."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

class TestStringToMd5:
    """Superior test suite for the string_to_md5 function."""

    @pytest.mark.parametrize("input_text", [
        "Hello world",        # Docstring example
        "python",             # Standard lowercase
        "12345",              # Numeric string
        " ",                  # Single space
        "PyTest Suite 2024",  # Alphanumeric with spaces
    ])
    def test_standard_inputs(self, input_text):
        """Verify that standard strings return the correct MD5 hex digest."""
        assert string_to_md5(input_text) == calculate_expected_md5(input_text)

    def test_empty_string(self):
        """Verify that an empty string returns None per the requirements."""
        assert string_to_md5("") is None

    @pytest.mark.parametrize("unicode_text", [
        "🔥 Python 🐍",       # Emojis
        "Привет мир",         # Cyrillic
        "你好世界",            # Chinese
        "München",            # German Umlaut
        "Line 1\nLine 2\t!",  # Control characters (newline/tab)
        "@#$%^&*()_+",        # Symbols
    ])
    def test_unicode_and_special_chars(self, unicode_text):
        """Verify that multi-byte Unicode and special characters are handled correctly."""
        assert string_to_md5(unicode_text) == calculate_expected_md5(unicode_text)

    def test_long_string(self):
        """Verify the function handles very large strings without crashing or timing out."""
        large_text = "a" * 10**6  # 1 million characters
        assert string_to_md5(large_text) == calculate_expected_md5(large_text)

    def test_consistency(self):
        """Verify that the function is deterministic (same input always yields same output)."""
        text = "Consistency Test"
        result1 = string_to_md5(text)
        result2 = string_to_md5(text)
        assert result1 == result2
        assert result1 == calculate_expected_md5(text)

    def test_case_sensitivity(self):
        """Verify that MD5 hashing is case sensitive."""
        lower = string_to_md5("hello")
        upper = string_to_md5("HELLO")
        assert lower != upper
        assert lower == calculate_expected_md5("hello")
        assert upper == calculate_expected_md5("HELLO")

    @pytest.mark.parametrize("invalid_input", [
        None,
        12345,
        45.67,
        ["list"],
        {"key": "val"},
        (1, 2),
    ])
    def test_invalid_types(self, invalid_input: Any):
        """Verify that passing non-string types raises a TypeError or AttributeError."""
        with pytest.raises((TypeError, AttributeError)):
            string_to_md5(invalid_input)

    def test_hash_properties(self):
        """Verify that the resulting hash adheres to MD5 specifications (32 hex chars)."""
        text = "Property Check"
        result = string_to_md5(text)
        assert isinstance(result, str)
        assert len(result) == 32
        # Ensure all characters are valid hexadecimal digits
        assert all(c in '0123456789abcdef' for c in result)