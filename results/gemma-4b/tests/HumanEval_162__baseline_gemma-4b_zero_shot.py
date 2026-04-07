
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

def test_string_to_md5_hello_world():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_single_character():
    assert string_to_md5('a') == '9709d29698944493933296269793693a'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'b9a8a9c76357c631933939a89669696'

def test_string_to_md5_with_spaces():
    assert string_to_md5('  test  ') == 'b9a8a9c76357c631933939a89669696'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '6b9340a38081cf731a6764966969696'

def test_string_to_md5_mixed_characters():
    assert string_to_md5('Hello123!@#') == '69696969696969696969696969696969'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 function."
    expected_md5 = '8967999999999999999999999999999999999999999999999999999999999999'
    assert string_to_md5(long_string) == expected_md5