import pytest
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    >>> string_to_md5('') is None
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_with_leading_and_trailing_whitespace():
    text = "  test  "
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == md5_hash

def test_string_with_punctuation():
    text = "!@#$%^&*()"
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == md5_hash

def test_string_with_unicode_characters():
    text = "你好世界"
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == md5_hash

def test_string_with_numbers_only():
    text = "1234567890"
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == md5_hash

def test_string_with_mixed_case_characters():
    text = "Hello123World!"
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == md5_hash

def test_long_string():
    long_string = "This is a very long string to test the md5 hash function."
    md5_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == md5_hash

def test_string_with_newline():
    text = "Hello\nWorld"
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == md5_hash

def test_string_with_repeated_characters():
    text = "aaaaaa"
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == md5_hash

def test_very_large_string():
    large_string = "A" * 1000000
    md5_hash = hashlib.md5(large_string.encode('utf-8')).hexdigest()
    assert string_to_md5(large_string) == md5_hash

def test_invalid_input_type():
    with pytest.raises(TypeError):
        string_to_md5(123)