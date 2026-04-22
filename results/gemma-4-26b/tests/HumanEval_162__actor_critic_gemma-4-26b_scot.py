
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def test_string_to_md5_standard_case():
    """Test with the example provided in the docstring."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    """Test that an empty string returns None as per requirements."""
    assert string_to_md5("") is None

@pytest.mark.parametrize("whitespace_str", [" ", "\n", "  ", " \t "])
def test_string_to_md5_whitespace_preservation(whitespace_str):
    """Test that whitespace is preserved and not stripped or normalized."""
    expected = hashlib.md5(whitespace_str.encode('utf-8')).hexdigest()
    assert string_to_md5(whitespace_str) == expected

def test_string_to_md5_unicode():
    """Test that Unicode characters are handled correctly."""
    text = "Python 🐍"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_case_sensitivity():
    """Test that the hash is case sensitive."""
    # We only need to verify the hash matches the expected MD5 for the specific case.
    # The mathematical difference between 'ABC' and 'abc' is implied.
    assert string_to_md5("ABC") == hashlib.md5("ABC".encode('utf-8')).hexdigest()
    assert string_to_md5("abc") == hashlib.md5("abc".encode('utf-8')).hexdigest()

def test_string_to_md5_null_bytes():
    """Test that strings containing null bytes are handled correctly."""
    text = "a\x00b"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_large_input():
    """Test with a 1MB input to ensure efficient handling of large buffers."""
    text = "a" * (1024 * 1024)  # 1MB
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

@pytest.mark.parametrize("invalid_input", [None, 123, 45.6, [], {}])
def test_string_to_md5_non_string_inputs(invalid_input):
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        string_to_md5(invalid_input)