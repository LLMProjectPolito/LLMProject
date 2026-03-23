import hashlib
import pytest

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_different_strings():
    assert string_to_md5("test") == "098f6bcd4621d373cade4e832627b4f6"
    assert string_to_md5("another test") == "5d41402abc4b2a76b9719d911017c592"
    assert string_to_md5("12345") == "5994471abb01112afcc18159f6cc74b4"

def test_unicode_string():
    assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

def test_long_string():
    long_string = "a" * 1000
    assert len(string_to_md5(long_string)) == 32

def test_input_type():
    with pytest.raises(TypeError):
        string_to_md5(123)
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3])