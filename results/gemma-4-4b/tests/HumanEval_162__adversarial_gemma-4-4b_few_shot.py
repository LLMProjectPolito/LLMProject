
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

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


def test_string_to_md5_empty():
    assert string_to_md5("") is None

def test_string_to_md5_simple():
    assert string_to_md5("hello") == "b10a8db164e0755b78b35a1b8db32dbd"

def test_string_to_md5_with_spaces():
    assert string_to_md5("hello world") == "b10a8db164e0755b78b35a1b8db32dbd"

def test_string_to_md5_with_special_characters():
    assert string_to_md5("!@#$%^&*()") == "e29863d14232050f3254f8b91642830d"

def test_string_to_md5_unicode():
    assert string_to_md5("你好世界") == "e539f2996a69283481e939195593494a"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 hash function." * 10
    md5_hash = string_to_md5(long_string)
    assert len(md5_hash) == 32 # md5 hash is always 32 characters long