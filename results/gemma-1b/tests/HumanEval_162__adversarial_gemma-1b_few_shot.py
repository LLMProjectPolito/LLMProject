import pytest

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

def test_string_to_md5_positive():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_single_char():
    assert string_to_md5('a') == '7f5eb6a999999999'

def test_string_to_md5_mixed_case():
    assert string_to_md5('Hello World') == '7f5eb6a999999999'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '7f5eb6a999999999'

def test_string_to_md5_symbols():
    assert string_to_md5('!@#$%^') == '7f5eb6a999999999'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == '7f5eb6a999999999'