
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def test_string_to_md5_standard():
    """Test the function with the provided example case."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    """Test that an empty string returns None."""
    assert string_to_md5('') is None

def test_string_to_md5_whitespace():
    """Test that strings containing only whitespace are hashed and not treated as empty."""
    text = ' '
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_unicode():
    """Test that the function handles unicode characters correctly."""
    text = 'Python 🐍'
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_case_sensitivity():
    """Test that the hash is case-sensitive."""
    assert string_to_md5('Hello') != string_to_md5('hello')

def test_string_to_md5_long_string():
    """Test the function with a very long string."""
    text = 'a' * 10000
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

@pytest.mark.parametrize("input_text", [
    "test1",
    "123456",
    "!@#$%^&*()",
    "A very long sentence to ensure the hashing algorithm is consistent across different lengths."
])
def test_string_to_md5_consistency(input_text):
    """Parametrized test to ensure consistency with hashlib.md5."""
    expected = hashlib.md5(input_text.encode()).hexdigest()
    assert string_to_md5(input_text) == expected