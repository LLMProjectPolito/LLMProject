import hashlib
import pytest

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_special_characters():
    assert string_to_md5("Hello, world!") == "b10a8db164e0754105b7a99be72e3fe5"

def test_long_string():
    long_string = "This is a very long string to test the MD5 hash function." * 10
    assert isinstance(string_to_md5(long_string), str)

def test_non_string_input():
    with pytest.raises(TypeError):
        string_to_md5(123)
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3])