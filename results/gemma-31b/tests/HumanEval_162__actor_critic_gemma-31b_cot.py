
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def calculate_md5(text: str) -> str:
    """Helper to calculate expected MD5 hash for test verification."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

class TestStringToMd5:
    def test_empty_string(self):
        """Test that an empty string returns None as per requirements."""
        assert string_to_md5('') is None

    @pytest.mark.parametrize("input_text", [
        "Hello world",                # Basic example case
        " ",                          # Single space
        "   ",                        # Multiple spaces
        "1234567890",                 # Numeric string
        "!@#$%^&*()_+~`",             # Special characters
        "Hello World!",               # Mixed case and punctuation
        "a" * 1000,                   # Long string
        "你好世界",                    # Unicode/Chinese characters
        "🚀🌟🔥",                      # Emojis
        "\n\t\r",                     # Whitespace characters
        "null\0byte",                 # String containing null bytes
    ])
    def test_various_strings(self, input_text):
        """Test a variety of string inputs against hashlib's implementation."""
        expected = calculate_md5(input_text)
        assert string_to_md5(input_text) == expected

    def test_case_sensitivity(self):
        """Test that MD5 is case sensitive."""
        assert string_to_md5('hello') != string_to_md5('Hello')

    @pytest.mark.parametrize("invalid_input", [
        None,
        123,
        45.67,
        [],
        {},
    ])
    def test_non_string_input(self, invalid_input):
        """
        Test how the function handles non-string inputs.
        Should raise AttributeError (if .encode() is called) or TypeError.
        """
        with pytest.raises((AttributeError, TypeError)):
            string_to_md5(invalid_input) # type: ignore