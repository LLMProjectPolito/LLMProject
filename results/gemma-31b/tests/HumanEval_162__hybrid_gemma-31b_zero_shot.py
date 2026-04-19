
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from typing import Any

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()

class TestStringToMd5:
    """Comprehensive test suite for string_to_md5 function."""

    @pytest.mark.parametrize("input_text, expected_hash", [
        ('Hello world', '3e25960a79dbc69b674cd4ec67a72c62'),
        ('python', '11a83b40f2bf4832441e594a493ef742'),
        ('12345', '827ccb0eea8a706c4c34a16891f84e7b'),
        (' ', '7215ee9c7d97ef00d2bca9bf6a8701d3'),
        ('Special characters !@#$%^&*()', '56c498c8d24564605f06167318479852'),
    ])
    def test_standard_strings_hardcoded(self, input_text, expected_hash):
        """Test standard strings against known golden MD5 hashes."""
        assert string_to_md5(input_text) == expected_hash

    @pytest.mark.parametrize("unicode_text", [
        ("你好"),              # Chinese
        ("Привет"),            # Cyrillic
        ("🚀 Space Rocket"),    # Emoji
        ("Café"),              # Accented
        ("नमस्ते"),            # Hindi
        ("Unicode Test 🚀"),
    ])
    def test_unicode_strings(self, unicode_text):
        """Test that the function correctly handles various Unicode characters using dynamic verification."""
        expected = hashlib.md5(unicode_text.encode('utf-8')).hexdigest()
        assert string_to_md5(unicode_text) == expected

    def test_empty_string(self):
        """Test that an empty string returns None as per requirements."""
        assert string_to_md5("") is None

    @pytest.mark.parametrize("invalid_input", [
        None,
        123,
        45.67,
        True,
        ["list"],
        {"dict": "val"},
    ])
    def test_invalid_types(self, invalid_input: Any):
        """Test that non-string inputs raise an appropriate exception."""
        with pytest.raises((AttributeError, TypeError)):
            string_to_md5(invalid_input)

    def test_large_string(self):
        """Test stability and output format with a very large input string."""
        large_text = "a" * 10**6  # 1 million characters
        result = string_to_md5(large_text)
        assert isinstance(result, str)
        assert len(result) == 32
        assert result == hashlib.md5(large_text.encode('utf-8')).hexdigest()

    def test_determinism_and_idempotency(self):
        """Test that the same input always produces the same hash."""
        text = "Consistency check"
        assert string_to_md5(text) == string_to_md5(text)

    def test_case_sensitivity(self):
        """Test that MD5 hashing is case sensitive."""
        assert string_to_md5("HELLO") != string_to_md5("hello")

    def test_distinct_inputs(self):
        """Test that different inputs produce different hashes."""
        assert string_to_md5("Text A") != string_to_md5("Text B")