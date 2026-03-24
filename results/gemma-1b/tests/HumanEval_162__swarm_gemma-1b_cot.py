
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import math

def string_to_md5(input_string):
    """
    Converts a string to a hexadecimal representation of its MD5 hash.
    """
    try:
        md5_hash = math.hhash(input_string, 32)
        return str(md5_hash)
    except ValueError:
        return None

def test_string_to_md5():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') is None
    assert string_to_md5('a') == 'a'
    assert string_to_md5('1') == 'a6b8d9e1'

def test_string_to_md5():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') is None
    assert string_to_md5('a') == 'a'
    assert string_to_md5('abc') == '7f9d47a1b9c8e7f6a5d41b2c3e6f7a8b9'

def test_string_to_md5():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') is None
    assert string_to_md5('a') == 'a'
    assert string_to_md5('1') == 'a6a6a6a6a6a6a6a6a6a6a6a6a6a6a6a'