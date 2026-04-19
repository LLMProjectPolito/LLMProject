
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from your_module import string_to_md5  # Replace 'your_module' with the actual module name

@pytest.mark.parametrize("input_text, expected_output", [
    ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
    ("python", "47130117364447519694462452124444"), # This is a placeholder, will use hashlib for dynamic check
    ("12345", "827ccb0eea8a706c4c34a16891f84e7b"),
    ("!@#$%^&*()", "67696646686766686766686766686766"), # Placeholder
])
def test_string_to_md5_valid_strings(input_text, expected_output):
    # Using hashlib to ensure the expected output is always correct for the test
    actual_hash = hashlib.md5(input_text.encode()).hexdigest()
    assert string_to_md5(input_text) == actual_hash

def test_string_to_md5_empty_string():
    """Ensure that an empty string returns None as per requirements."""
    assert string_to_md5("") is None

def test_string_to_md5_long_string():
    """Test with a significantly long string to ensure stability."""
    long_text = "a" * 10000
    expected_hash = hashlib.md5(long_text.encode()).hexdigest()
    assert string_to_md5(long_text) == expected_hash

def test_string_to_md5_whitespace():
    """Test strings consisting only of whitespace."""
    text = "   "
    expected_hash = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected_hash