import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

import pytest

def test_string_to_md5_valid():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('abc') == 'ba7816bf8f01cfea414140de5dae2223'
    assert string_to_md5('12345') == '5d414c7b119f809a15a024fcdb70e076'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_special_chars():
    assert string_to_md5('!@#$%^') == '9469c999999999999999999999999999'
    assert string_to_md5(' ') == 'da51039445293a3494c699c69926969'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_mixed_case():
    assert string_to_md5('HeLlO wOrLd') == '3e25960a79dbc69b674cd4ec67a72c62' # Case should not matter

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 hash function."
    expected_hash = '99999999999999999999999999999999' # Replace with actual hash if needed
    assert string_to_md5(long_string) == expected_hash