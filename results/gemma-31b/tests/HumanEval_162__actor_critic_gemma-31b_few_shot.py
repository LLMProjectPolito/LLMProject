
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def test_string_to_md5_basic():
    """Test a standard string input based on the provided example."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    """Test that an empty string returns None as per requirements."""
    assert string_to_md5('') is None

def test_string_to_md5_case_sensitivity():
    """Test that MD5 is case-sensitive and verifies specific known hashes."""
    hash_upper = string_to_md5('HELLO')
    hash_lower = string_to_md5('hello')
    
    # Verify specific known MD5 values
    assert hash_upper == '8b1a9953c4611296a827abf8c47804d7'
    assert hash_lower == '5d41402abc4b2a76b9719d911017c592'
    assert hash_upper != hash_lower

@pytest.mark.parametrize("whitespace_str", [" ", "\t", "\n", "  \t  "])
def test_string_to_md5_whitespace(whitespace_str):
    """Test that strings containing only whitespace are hashed normally and not treated as empty."""
    result = string_to_md5(whitespace_str)
    assert result is not None
    assert result == hashlib.md5(whitespace_str.encode('utf-8')).hexdigest()

def test_string_to_md5_special_characters():
    """Test strings containing spaces, symbols, and numbers."""
    text = "123!@# "
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_long_string():
    """Test a very long string to ensure stability."""
    long_text = "a" * 10000
    expected = hashlib.md5(long_text.encode('utf-8')).hexdigest()
    assert string_to_md5(long_text) == expected

def test_string_to_md5_unicode():
    """Test multi-byte characters (Unicode) to ensure correct encoding (UTF-8)."""
    # Testing Chinese characters and emojis
    text = "你好 🌍"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

@pytest.mark.parametrize("invalid_input", [
    None, 
    123, 
    45.67, 
    ["string"], 
    {"text": "value"}
])
def test_string_to_md5_type_validation(invalid_input):
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        string_to_md5(invalid_input)