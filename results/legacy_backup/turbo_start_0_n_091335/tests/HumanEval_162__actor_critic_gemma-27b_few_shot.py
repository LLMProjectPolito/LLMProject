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

import pytest

def test_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_md5_empty():
    assert string_to_md5('') == None

def test_md5_single_char():
    assert string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'

def test_md5_numbers():
    assert string_to_md5('12345') == '5994471abb01112afcc18159f6cc74b4'

def test_md5_mixed_chars():
    assert string_to_md5('Hello123!') == '5d41402abc4b2a76b9719d911017c592'

def test_md5_long_string():
    long_string = "This is a very long string to test the MD5 function." * 20  # Create a string > 1000 chars
    expected_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == expected_hash

def test_md5_unicode():
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_md5_whitespace():
    assert string_to_md5('   ') == '7a59b69a89141a996999196969991969'

def test_md5_docstring_example():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'