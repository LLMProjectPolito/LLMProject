
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from typing import Any

# The function string_to_md5 is assumed to be defined in the environment.

def get_expected_md5(text: str) -> str:
    """Helper to generate expected MD5 hash using hashlib."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_example():
    """Test the specific example provided in the docstring."""
    input_text = 'Hello world'
    expected = '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5(input_text) == expected

def test_string_to_md5_empty_string():
    """Test that an empty string returns None."""
    assert string_to_md5("") is None

def test_string_to_md5_whitespace():
    """Test strings consisting of various whitespace characters."""
    test_cases = [" ", "  ", "\t", "\n", "\r\n"]
    for case in test_cases:
        assert string_to_md5(case) == get_expected_md5(case)

def test_string_to_md5_unicode():
    """Test strings with Unicode characters to ensure encoding is handled."""
    test_cases = ["你好", "🚀 Space", "éàç", "Кот"]
    for case in test_cases:
        assert string_to_md5(case) == get_expected_md5(case)

def test_string_to_md5_case_sensitivity():
    """Test that MD5 hashes are case-sensitive."""
    text_lower = "hello"
    text_upper = "HELLO"
    assert string_to_md5(text_lower) != string_to_md5(text_upper)
    assert string_to_md5(text_lower) == get_expected_md5(text_lower)
    assert string_to_md5(text_upper) == get_expected_md5(text_upper)

def test_string_to_md5_long_string():
    """Test the function with a very large string."""
    long_text = "a" * 10**6  # 1 million characters
    assert string_to_md5(long_text) == get_expected_md5(long_text)

@pytest.mark.parametrize("input_val, expected", [
    ("pytest", get_expected_md5("pytest")),
    ("123456", get_expected_md5("123456")),
    ("!@#$%^&*()", get_expected_md5("!@#$%^&*()")),
])
def test_string_to_md5_parametrized(input_val, expected):
    """General purpose parametrization for various string inputs."""
    assert string_to_md5(input_val) == expected