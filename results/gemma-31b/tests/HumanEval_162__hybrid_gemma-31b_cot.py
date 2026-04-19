
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def calculate_expected_md5(text):
    """Helper to calculate MD5 for verification using standard library."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

class TestStringToMd5:
    """Superior test suite for the string_to_md5 function."""

    def test_empty_string(self):
        """Verify that an empty string returns None as specified."""
        assert string_to_md5('') is None

    def test_provided_example(self):
        """Verify the specific example case provided in requirements."""
        assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    @pytest.mark.parametrize("text", [
        "python",
        "1234567890",
        " ",
        "\n",
        "\t",
        "!@#$%^&*()_+",
        "Case Sensitivity Test",
        "A" * 1000,
    ])
    def test_valid_strings(self, text):
        """Test various valid string inputs and verify against hashlib."""
        result = string_to_md5(text)
        expected = calculate_expected_md5(text)
        assert result == expected
        assert len(result) == 32  # MD5 hex strings must always be 32 characters

    def test_unicode_and_emojis(self):
        """Verify that non-ASCII characters and emojis are handled correctly via UTF-8."""
        unicode_text = "你好🚀 こんにちは世界 🌍"
        assert string_to_md5(unicode_text) == calculate_expected_md5(unicode_text)

    def test_case_sensitivity(self):
        """Verify that the MD5 hash is case sensitive."""
        text_lower = "hello"
        text_upper = "HELLO"
        text_mixed = "Hello"
        assert string_to_md5(text_lower) != string_to_md5(text_upper)
        assert string_to_md5(text_lower) != string_to_md5(text_mixed)

    def test_determinism(self):
        """Verify that the same input always yields the same output."""
        text = "consistency_test_123"
        assert string_to_md5(text) == string_to_md5(text)

    def test_null_character(self):
        """Test strings containing null bytes to ensure binary transparency."""
        text_with_null = "null\0byte"
        assert string_to_md5(text_with_null) == calculate_expected_md5(text_with_null)

    def test_whitespace_variants(self):
        """Ensure that different types of whitespace are treated as distinct strings."""
        s1 = " "
        s2 = "  "
        s3 = "\r\n"
        assert string_to_md5(s1) != string_to_md5(s2)
        assert string_to_md5(s1) != string_to_md5(s3)
        assert string_to_md5(s1) is not None

    def test_long_string_stability(self):
        """Test with a very large input string to ensure stability and performance."""
        text = "a" * 10**6  # 1 million characters
        assert string_to_md5(text) == calculate_expected_md5(text)

    @pytest.mark.parametrize("invalid_input", [
        None,
        123,
        45.67,
        ["list"],
        {"key": "value"},
        (1, 2),
    ])
    def test_invalid_types(self, invalid_input):
        """
        Verify that passing non-string types raises an appropriate error.
        Usually AttributeError (from .encode()) or TypeError.
        """
        with pytest.raises((AttributeError, TypeError)):
            string_to_md5(invalid_input)