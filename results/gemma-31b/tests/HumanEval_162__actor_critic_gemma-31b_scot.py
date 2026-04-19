
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from typing import Any

# The function is assumed to be imported or defined in the environment.
# Since I cannot redefine it, I am writing the tests to target the 
# function signature provided in the problem description.

def get_expected_md5(text: str) -> str:
    """Helper to calculate ground truth MD5 hash."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

class TestStringToMd5:
    
    def test_string_to_md5_basic(self):
        """Test the provided example case."""
        input_text = 'Hello world'
        expected = '3e25960a79dbc69b674cd4ec67a72c62'
        assert string_to_md5(input_text) == expected

    def test_string_to_md5_empty(self):
        """Test that an empty string returns None."""
        assert string_to_md5("") is None

    @pytest.mark.parametrize("text", [
        " ", 
        "  ", 
        "\n", 
        "\t", 
        " Hello "
    ])
    def test_string_to_md5_whitespace(self, text):
        """Test that whitespace strings are hashed and not treated as empty."""
        result = string_to_md5(text)
        assert result is not None
        assert result == get_expected_md5(text)

    def test_string_to_md5_unicode(self):
        """Test strings with Unicode characters (UTF-8)."""
        text = "Python 🐍 is awesome! 🚀"
        assert string_to_md5(text) == get_expected_md5(text)

    def test_string_to_md5_case_sensitivity(self):
        """Test that MD5 is case sensitive."""
        text_lower = "hello"
        text_upper = "HELLO"
        assert string_to_md5(text_lower) != string_to_md5(text_upper)
        assert string_to_md5(text_lower) == get_expected_md5(text_lower)
        assert string_to_md5(text_upper) == get_expected_md5(text_upper)

    def test_string_to_md5_long_string(self):
        """Test with a very large string to ensure stability."""
        text = "a" * 10**6  # 1 million characters
        assert string_to_md5(text) == get_expected_md5(text)

    @pytest.mark.parametrize("invalid_input", [
        None,
        123,
        45.67,
        ["list"],
        {"key": "val"}
    ])
    def test_string_to_md5_invalid_types(self, invalid_input: Any):
        """Test that non-string inputs raise a TypeError."""
        with pytest.raises(TypeError):
            string_to_md5(invalid_input)