import pytest
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    Encoding used: UTF-8

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

def test_standard_string():
    text = 'Hello world'
    expected_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_hash

def test_empty_string():
    assert string_to_md5('') is None

def test_special_characters():
    assert string_to_md5('!@#$%^&*()') == '99d831a694432393569634496a53499a'

def test_long_string():
    long_string = "This is a very long string to test the md5 hash function. It should handle long strings without any issues."
    expected_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == expected_hash

def test_unicode_string():
    assert string_to_md5('你好世界') == 'a94a8fe5ccb19ba61c4c0873d391e987'

def test_numeric_string():
    assert string_to_md5('1234567890') == '6f874409999f99d9999999999999999'

def test_mixed_case_string():
    text = "Hello World"
    expected_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_hash

def test_string_with_whitespace():
    text = "  test  "
    expected_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_hash

def test_none_input():
    with pytest.raises(TypeError):
        string_to_md5(None)