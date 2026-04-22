
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def test_string_to_md5_empty():
    """Test that an empty string returns None."""
    assert string_to_md5("") is None

def test_string_to_md5_example():
    """Test the specific example provided in the docstring."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

@pytest.mark.parametrize("input_text", [
    "a",
    "1234567890",
    " ",
    "    ",
    "!@#$%^&*()_+~`|}{[]:;?><,./",
    "Long string " * 50,
    "Unicode test: 🚀🔥你好",
])
def test_string_to_md5_various_inputs(input_text):
    """Test various string inputs against a known correct implementation using hashlib."""
    expected_hash = hashlib.md5(input_text.encode('utf-8')).hexdigest()
    assert string_to_md5(input_text) == expected_hash

def test_string_to_md5_case_sensitivity():
    """Test that the hash is case sensitive."""
    hash_lower = string_to_md5("hello")
    hash_upper = string_to_md5("HELLO")
    assert hash_lower != hash_upper
    assert hash_lower == hashlib.md5("hello".encode('utf-8')).hexdigest()
    assert hash_upper == hashlib.md5("HELLO".encode('utf-8')).hexdigest()

def test_string_to_md5_type_consistency():
    """Ensure the output is always a string (when not None)."""
    result = string_to_md5("test")
    assert isinstance(result, str)
    assert len(result) == 32  # MD5 hex strings are always 32 characters