
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def test_string_to_md5_empty_string():
    """Test that an empty string returns None."""
    assert string_to_md5('') is None

def test_string_to_md5_docstring_example():
    """Test the specific example provided in the docstring."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

@pytest.mark.parametrize("input_text", [
    " ",                                # Single space
    "1234567890",                       # Numeric string
    "!@#$%^&*()_+-=[]{}|;':\",./<>?",   # Special characters
    "Line 1\nLine 2",                   # Newlines
    "Tab\tCharacter",                   # Tabs
    "Unicode testing: 🚀🌟",            # Emojis
    "日本語",                            # Multi-byte characters (Japanese)
    "A" * 10000,                        # Long string
    "\x00\x01\x02",                     # Non-printable ASCII
])
def test_string_to_md5_various_contents(input_text):
    """Test various string contents against a direct hashlib implementation."""
    expected_hash = hashlib.md5(input_text.encode('utf-8')).hexdigest()
    assert string_to_md5(input_text) == expected_hash

def test_string_to_md5_consistency():
    """Test that the function is deterministic (same input produces same output)."""
    text = "consistency_test"
    assert string_to_md5(text) == string_to_md5(text)