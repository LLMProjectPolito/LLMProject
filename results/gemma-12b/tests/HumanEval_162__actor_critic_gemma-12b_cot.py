
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    The input string is encoded using UTF-8 before calculating the MD5 hash.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_with_spaces():
    md5_hash = hashlib.md5("  ".encode('utf-8')).hexdigest()
    assert string_to_md5("  ") == md5_hash

def test_string_with_special_characters():
    md5_hash = hashlib.md5("!@#$%^&*()".encode('utf-8')).hexdigest()
    assert string_to_md5("!@#$%^&*()") == md5_hash

def test_string_with_unicode_characters():
    md5_hash = hashlib.md5("你好世界".encode('utf-8')).hexdigest()
    assert string_to_md5("你好世界") == md5_hash

def test_string_with_numbers():
    md5_hash = hashlib.md5("1234567890".encode('utf-8')).hexdigest()
    assert string_to_md5("1234567890") == md5_hash

def test_string_with_mixed_characters():
    md5_hash = hashlib.md5("Hello123!@#".encode('utf-8')).hexdigest()
    assert string_to_md5("Hello123!@#") == md5_hash

def test_long_string():
    long_string = "This is a very long string to test the md5 hash function."
    md5_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == md5_hash

def test_string_with_newline():
    md5_hash = hashlib.md5("Hello\nworld".encode('utf-8')).hexdigest()
    assert string_to_md5("Hello\nworld") == md5_hash

def test_case_sensitivity():
    md5_hash_hello = hashlib.md5("Hello".encode('utf-8')).hexdigest()
    md5_hash_hello_lower = hashlib.md5("hello".encode('utf-8')).hexdigest()
    assert string_to_md5("Hello") != string_to_md5("hello")

def test_whitespace_only_string():
    md5_hash = hashlib.md5("   ".encode('utf-8')).hexdigest()
    assert string_to_md5("   ") == md5_hash

def test_invalid_input_type():
    with pytest.raises(TypeError):
        string_to_md5(123)
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3])

def test_docstring_example():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'