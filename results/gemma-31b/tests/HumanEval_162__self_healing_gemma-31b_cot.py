
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import hashlib
import pytest

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_standard():
    """Test the function with the provided example."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    """Test that an empty string returns None."""
    assert string_to_md5('') is None

def test_string_to_md5_various_inputs():
    """Test various string inputs against hashlib implementation."""
    test_cases = [
        "pytest",
        "1234567890",
        "Special characters !@#$%^&*()",
        "A very long string " * 100,
        "   leading and trailing spaces   ",
        "\nNewlines\tTabs"
    ]
    for text in test_cases:
        expected = hashlib.md5(text.encode('utf-8')).hexdigest()
        assert string_to_md5(text) == expected

def test_string_to_md5_unicode():
    """Test strings with unicode characters."""
    text = "Python 🐍"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_case_sensitivity():
    """Test that the hash is case sensitive."""
    assert string_to_md5('hello') != string_to_md5('Hello')

@pytest.mark.parametrize("input_str, expected_hash", [
    ("abc", "900150983cd24fb0d6963f7d28e17f72"),
    ("test", "098f6bcd4621d373cade4e832627b4f6"),
])
def test_string_to_md5_parametrized(input_str, expected_hash):
    """Parametrized test for specific known MD5 hashes."""
    assert string_to_md5(input_str) == expected_hash