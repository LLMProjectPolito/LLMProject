
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def test_string_to_md5_basic():
    """Test basic functionality with the provided example."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    """Test that an empty string returns None."""
    assert string_to_md5('') is None

@pytest.mark.parametrize("input_text", [
    "python",
    "12345",
    " ",
    "!@#$%^&*()",
    "CaseSensitive",
    "casesensitive",
    "pytest",
])
def test_string_to_md5_variations(input_text):
    """Test various strings including numbers, special characters, and case sensitivity using hashlib for verification."""
    expected_hash = hashlib.md5(input_text.encode('utf-8')).hexdigest()
    assert string_to_md5(input_text) == expected_hash

def test_string_to_md5_case_sensitivity():
    """Test that MD5 is case sensitive."""
    hash_upper = string_to_md5('HELLO')
    hash_lower = string_to_md5('hello')
    assert hash_upper != hash_lower

def test_string_to_md5_long_string():
    """Test with a very long string."""
    long_text = "a" * 10000
    expected = hashlib.md5(long_text.encode('utf-8')).hexdigest()
    assert string_to_md5(long_text) == expected

def test_string_to_md5_unicode():
    """Test with unicode/non-ASCII characters."""
    unicode_text = "你好世界" 
    expected = hashlib.md5(unicode_text.encode('utf-8')).hexdigest()
    assert string_to_md5(unicode_text) == expected

def test_string_to_md5_type_error():
    """Test that passing non-string types raises an appropriate error."""
    with pytest.raises((TypeError, AttributeError)):
        string_to_md5(None)
    with pytest.raises((TypeError, AttributeError)):
        string_to_md5(123)