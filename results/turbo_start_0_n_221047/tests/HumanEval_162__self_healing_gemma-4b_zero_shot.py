import pytest
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def test_string_to_md5_hello_world():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_single_character():
    assert string_to_md5('a') == '96a3cd49a87965432b65dfa5feac51c1'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '6b9340a3607d18604149969496969696'

def test_string_to_md5_special_characters():
    assert string_to_md5('!@#$%^') == '8862699999999999999999999999999999999999'

def test_string_to_md5_mixed_characters():
    assert string_to_md5('Hello123!@#') == 'b94d27b9934d3e08a52e52d97d3b3cb0'

def test_string_to_md5_unicode_characters():
    assert string_to_md5('你好世界') == 'b9a3699999999999999999999999999999999999'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the function with a large input."
    expected_md5 = '8967896789678967896789678967896789678967'
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_whitespace():
    assert string_to_md5('   ') == '39a8a693b39a8a69'