
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def test_string_to_md5_standard():
    """Test the standard example provided in the docstring."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    """Test that an empty string returns None."""
    assert string_to_md5('') is None

def test_string_to_md5_case_sensitivity():
    """Test that the hash is case-sensitive."""
    assert string_to_md5('Hello') != string_to_md5('hello')

def test_string_to_md5_special_characters():
    """Test strings containing special characters and symbols."""
    text = "!@#$%^&*()_+ ~`|}{[]:;?/><,."
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_numeric_string():
    """Test strings containing only numbers."""
    text = "1234567890"
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_whitespace():
    """Test strings containing only whitespace (should not be treated as empty)."""
    text = "   "
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_long_string():
    """Test a very long string to ensure stability."""
    text = "a" * 10000
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_consistency():
    """Test that the same input always produces the same output."""
    text = "consistency_test"
    assert string_to_md5(text) == string_to_md5(text)

@pytest.mark.parametrize("input_text, expected_hash", [
    ("pytest", "63376767667836667836667836667836"), # This is a dummy, will use hashlib for real
])
def test_string_to_md5_parametrized(input_text):
    """Parametrized test to verify against hashlib implementation."""
    expected = hashlib.md5(input_text.encode()).hexdigest()
    assert string_to_md5(input_text) == expected