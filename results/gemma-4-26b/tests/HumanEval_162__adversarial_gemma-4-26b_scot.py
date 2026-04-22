
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def test_docstring_example():
    """Verify the specific example provided in the docstring."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_empty_string_returns_none():
    """Verify that an empty string returns None as per requirements."""
    assert string_to_md5("") is None

def test_whitespace_string():
    """Verify that whitespace-only strings are hashed, not treated as empty."""
    whitespace_input = "   "
    expected_hash = hashlib.md5(whitespace_input.encode('utf-8')).hexdigest()
    assert string_to_md5(whitespace_input) == expected_hash

@pytest.mark.parametrize("input_str", [
    "abc",
    "1234567890",
    "Complex!@#$%^&*()_+",
    "A very long sentence to test the stability of the md5 hashing function.",
])
def test_parameterized_standard_inputs(input_str):
    """Verify various standard strings against the hashlib ground truth."""
    expected_hash = hashlib.md5(input_str.encode('utf-8')).hexdigest()
    assert string_to_md5(input_str) == expected_hash

def test_unicode_and_emojis():
    """Verify that the function handles Unicode/UTF-8 characters correctly."""
    unicode_str = "Python 🐍 is awesome! 🚀"
    expected_hash = hashlib.md5(unicode_str.encode('utf-8')).hexdigest()
    assert string_to_md5(unicode_str) == expected_hash

def test_large_string():
    """Verify the function handles large inputs (1MB string)."""
    large_str = "a" * 1_000_000
    expected_hash = hashlib.md5(large_str.encode('utf-8')).hexdigest()
    assert string_to_md5(large_str) == expected_hash

@pytest.mark.parametrize("invalid_input", [
    123,
    None,
    ["list", "of", "strings"],
    {"key": "value"},
    1.5
])
def test_invalid_input_types(invalid_input):
    """Verify that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        string_to_md5(invalid_input)