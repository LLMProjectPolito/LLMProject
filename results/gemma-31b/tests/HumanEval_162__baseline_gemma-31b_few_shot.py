
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def test_string_to_md5_standard():
    """Test with a standard string provided in the docstring."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    """Test that an empty string returns None as per requirements."""
    assert string_to_md5('') is None

def test_string_to_md5_case_sensitivity():
    """Test that MD5 is case sensitive."""
    hash_upper = string_to_md5('HELLO')
    hash_lower = string_to_md5('hello')
    assert hash_upper != hash_lower
    assert hash_lower == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_special_characters():
    """Test with strings containing special characters and whitespace."""
    text = "!@#$%^&*()_+ \n\t"
    # Expected hash calculated via hashlib.md5(text.encode()).hexdigest()
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_numeric_string():
    """Test with a string consisting of numbers."""
    assert string_to_md5('1234567890') == 'e80b50748ed1a96c4c65876b697334c4'

def test_string_to_md5_long_string():
    """Test with a significantly long string to ensure stability."""
    long_text = "a" * 10000
    expected = hashlib.md5(long_text.encode()).hexdigest()
    assert string_to_md5(long_text) == expected