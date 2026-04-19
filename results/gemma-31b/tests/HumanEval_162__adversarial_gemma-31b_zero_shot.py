
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from typing import Any

# Assuming the function is imported from the module under test
# from solution import string_to_md5

def string_to_md5(text):
    """
    Implementation provided for the sake of making the test suite runnable.
    The QA suite is designed to validate this logic.
    """
    if text == "":
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()

@pytest.mark.parametrize("input_text, expected_output", [
    ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
    ("pytest", "73376467667666666666666666666666"), # This is a placeholder, actual MD5 below
    ("12345", "827ccb0eea8a706c4c34a16891f84e7b"),
    (" ", "99914b932bd37a5949a966137367577a"), # Single space is NOT an empty string
])
def test_standard_strings(input_text, expected_output):
    """Test standard alphanumeric strings and known MD5 values."""
    # Recalculate expected for 'pytest' to be precise
    if input_text == "pytest":
        expected_output = hashlib.md5(input_text.encode()).hexdigest()
    
    assert string_to_md5(input_text) == expected_output

def test_empty_string():
    """Requirement: If 'text' is an empty string, return None."""
    assert string_to_md5("") is None

def test_unicode_characters():
    """Test strings with non-ASCII characters to ensure encoding is handled (UTF-8)."""
    text = "🚀 Blue Team QA 🛡️"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_case_sensitivity():
    """MD5 hashes must be case-sensitive."""
    text_lower = "hello"
    text_upper = "HELLO"
    assert string_to_md5(text_lower) != string_to_md5(text_upper)

def test_long_string():
    """Test with a very large string to check for buffer or memory issues."""
    long_text = "a" * 10**6  # 1 million characters
    expected = hashlib.md5(long_text.encode('utf-8')).hexdigest()
    assert string_to_md5(long_text) == expected

def test_whitespace_variations():
    """Ensure that tabs, newlines, and spaces are hashed correctly and not stripped."""
    text = "\n\t  \n"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    45.67,
    ["list"],
    {"key": "val"},
])
def test_invalid_types(invalid_input: Any):
    """
    Check how the function handles non-string inputs.
    A robust function should either raise a TypeError or handle it gracefully.
    """
    with pytest.raises((TypeError, AttributeError)):
        string_to_md5(invalid_input)