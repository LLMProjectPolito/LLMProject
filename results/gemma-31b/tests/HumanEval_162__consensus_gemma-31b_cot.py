
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

@pytest.mark.parametrize("input_text", [
    "Hello world",
    "abc",
    "12345",
    " ",
    "Python Programming",
    "Pytest",
    "!@#$%^&*()_+",
    "Python",
])
def test_string_to_md5_valid_strings(input_text):
    """Test standard strings against dynamically calculated MD5 hashes to avoid hallucinations."""
    expected = hashlib.md5(input_text.encode('utf-8')).hexdigest()
    assert string_to_md5(input_text) == expected

def test_string_to_md5_empty_string():
    """Test that an empty string returns None as per requirements."""
    assert string_to_md5('') is None

def test_string_to_md5_unicode():
    """Test that unicode and special characters are handled correctly."""
    text = "Héllö Wörld 🚀 Pytest Testing!"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_case_sensitivity():
    """Test that MD5 is case sensitive."""
    lower = string_to_md5("hello")
    upper = string_to_md5("HELLO")
    assert lower != upper

def test_string_to_md5_long_string():
    """Test a very long string to ensure stability."""
    text = "a" * 10**6  # 1 million characters
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_invalid_type():
    """Test how the function handles non-string inputs (should raise TypeError)."""
    with pytest.raises(TypeError):
        string_to_md5(None)
    with pytest.raises(TypeError):
        string_to_md5(123)
    with pytest.raises(TypeError):
        string_to_md5(["list", "of", "strings"])