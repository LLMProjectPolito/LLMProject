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
    return hashlib.md5(text.encode()).hexdigest()

def test_string_to_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5('') == None

def test_string_to_md5_single_char():
    assert string_to_md5('a') == '9fa0b64a299994999999999999999999'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '6b934d099c377644969d137999999999'

def test_string_to_md5_special_chars():
    assert string_to_md5('!@#$%^') == '89669399999999999999999999999999'

def test_string_to_md5_mixed():
    assert string_to_md5('Hello123!') == '69666669666666666666666666666666'