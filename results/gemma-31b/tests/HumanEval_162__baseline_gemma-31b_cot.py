
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from typing import Any

def get_expected_md5(text: str) -> str:
    """Helper to calculate expected MD5 hash for verification."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

class TestStringToMd5:
    def test_empty_string(self):
        """If 'text' is an empty string, return None."""
        assert string_to_md5("") is None

    def test_provided_example(self):
        """Verify the example provided in the docstring."""
        assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_standard_string(self):
        """Verify a standard alphanumeric string."""
        text = "pytest_testing_123"
        assert string_to_md5(text) == get_expected_md5(text)

    def test_case_sensitivity(self):
        """MD5 hashes should be case sensitive."""
        text_upper = "HELLO"
        text_lower = "hello"
        assert string_to_md5(text_upper) != string_to_md5(text_lower)
        assert string_to_md5(text_upper) == get_expected_md5(text_upper)
        assert string_to_md5(text_lower) == get_expected_md5(text_lower)

    def test_whitespace_and_special_chars(self):
        """Verify strings with spaces, tabs, and special characters."""
        texts = [
            "   ", 
            "\t\n", 
            "!@#$%^&*()_+", 
            "Hello, World!"
        ]
        for text in texts:
            assert string_to_md5(text) == get_expected_md5(text)

    def test_unicode_characters(self):
        """Verify that non-ASCII characters are handled correctly (UTF-8)."""
        texts = [
            "你好", 
            "🚀 Space", 
            "éàç"
        ]
        for text in texts:
            assert string_to_md5(text) == get_expected_md5(text)

    def test_long_string(self):
        """Verify the function handles very large strings."""
        text = "a" * 10**6  # 1 million characters
        assert string_to_md5(text) == get_expected_md5(text)

    def test_invalid_input_types(self):
        """
        Verify behavior with non-string inputs. 
        Depending on implementation, this should likely raise a TypeError.
        """
        invalid_inputs = [None, 123, 45.67, [], {}]
        for val in invalid_inputs:
            with pytest.raises(TypeError):
                string_to_md5(val) # type: ignore