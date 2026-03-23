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

def test_valid_input():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_empty_string():
    assert string_to_md5('') is None

def test_string_with_spaces():
    assert string_to_md5('  leading and trailing spaces  ') == '9c999999999999999999999999999999'

def test_string_with_special_characters():
    assert string_to_md5('!@#$%^&*()_+=-`~[]\{}|;\':",./<>?') == '99999999999999999999999999999999'

def test_string_with_unicode_characters():
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_long_string():
    long_string = "a" * 1000
    assert len(string_to_md5(long_string)) == 32

def test_non_string_input():
    with pytest.raises(TypeError):
        string_to_md5(123)