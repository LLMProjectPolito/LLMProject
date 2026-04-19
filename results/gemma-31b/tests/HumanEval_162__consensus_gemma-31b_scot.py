
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from your_module import string_to_md5

def get_expected_md5(text):
    """Helper to calculate expected MD5 hash for verification."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

@pytest.mark.parametrize("input_text", [
    'Hello world',
    'hello world',
    '12345',
    ' ',
    '!@#$%^&*()',
    'Python Pytest',
    'python',
    'a',
])
def test_string_to_md5_valid_inputs(input_text):
    """Test that valid strings return the correct MD5 hash."""
    assert string_to_md5(input_text) == get_expected_md5(input_text)

def test_string_to_md5_empty_string():
    """Test that an empty string returns None."""
    assert string_to_md5('') is None

def test_string_to_md5_case_sensitivity():
    """Test that the hash is case-sensitive."""
    assert string_to_md5('Test') != string_to_md5('test')

def test_string_to_md5_unicode():
    """Test that unicode characters are handled correctly."""
    text = '你好世界 🚀 Unicode Test 🌈'
    assert string_to_md5(text) == get_expected_md5(text)

def test_string_to_md5_long_string():
    """Test with a very long string to ensure stability."""
    long_text = "a" * 10000
    assert string_to_md5(long_text) == get_expected_md5(long_text)

def test_string_to_md5_invalid_types():
    """Test that non-string inputs raise an appropriate error."""
    with pytest.raises(AttributeError):
        string_to_md5(None)
    with pytest.raises(AttributeError):
        string_to_md5(123)