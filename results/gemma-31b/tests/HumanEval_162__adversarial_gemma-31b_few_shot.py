
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def test_md5_basic():
    """Test the provided example case."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_md5_empty_string():
    """Test that an empty string returns None as per requirements."""
    assert string_to_md5('') is None

@pytest.mark.parametrize("text", [
    "python",
    "123456",
    "Special characters !@#$%^&*()_+",
    "   ", # String with only spaces (should NOT be None)
    "A very long string " * 100,
])
def test_md5_consistency(text):
    """
    Verify that the function output matches the standard hashlib implementation.
    This ensures the implementation is mathematically correct.
    """
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_md5_case_sensitivity():
    """MD5 is case-sensitive; 'Hello' and 'hello' must produce different hashes."""
    assert string_to_md5('Hello') != string_to_md5('hello')

def test_md5_unicode():
    """Test handling of non-ASCII characters (UTF-8 encoding)."""
    text = "🚀 Palindrome 🌈"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_md5_invalid_input_types():
    """
    Robustness check: How does the function handle non-string inputs?
    Depending on implementation, it should either raise a TypeError 
    or handle it gracefully.
    """
    with pytest.raises(TypeError):
        string_to_md5(None)
    
    with pytest.raises(TypeError):
        string_to_md5(12345)