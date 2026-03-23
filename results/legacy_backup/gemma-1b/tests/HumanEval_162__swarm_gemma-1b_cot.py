import pytest
import math

def string_to_md5(input_string):
    """
    Converts a string to its MD5 hash.
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
    assert string_to_md5('abc') == '7f9d47a1b9c8e9b1d0a5c6e7f8a9b0c1'
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') is None
    assert string_to_md5('a') == 'b'
    assert string_to_md5('abc') == 'fedcba48'
    assert string_to_md5('12345') == 'fedcba48'
    assert string_to_md5('abc') == 'fedcba48'

def test_string_to_md5_invalid():
    assert string_to_md5('Hello world') == None
    assert string_to_md5('') is None
    assert string_to_md5('a') == 'b'
    assert string_to_md5('abc') == 'fedcba48'
    assert string_to_md5('12345') == None
    assert string_to_md5('abc') == 'fedcba48'