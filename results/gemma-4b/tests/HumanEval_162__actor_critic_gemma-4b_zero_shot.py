
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

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
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_normal():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_single_char():
    assert string_to_md5('a') == '9709a533666666666666666666666666'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'b9a8f9c8877612345678901234567890'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '6b934d08857a988a6d8a988a6d8a988a'

def test_string_to_md5_special_chars():
    assert string_to_md5('!@#$%^') == '8e98b399999999999999999999999999'

def test_string_to_md5_mixed():
    assert string_to_md5('Hello123!@#') == 'b8a39999999999999999999999999999'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the function with a large input."
    expected_md5 = 'a94a8fe5ccb19ba61c4c0873d391e987'
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_whitespace():
    assert string_to_md5('   ') == 'e3b0c44298fc1c149afbf4c8996fb924'

def test_string_to_md5_newline():
    assert string_to_md5('hello\nworld') == '8862692d999999999999999999999999'

def test_string_to_md5_tab():
    assert string_to_md5('hello\tworld') == '69666666666666666666666666666666'