
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


def test_string_to_md5_basic():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_empty():
    assert string_to_md5("") is None

def test_string_to_md5_single_char():
    assert string_to_md5("a") == "6458d8b2ddb3b1a582a9d4a3a87a6a8a"

def test_string_to_md5_numbers():
    assert string_to_md5("12345") == "d74c35a39982073a3969319995669298"

def test_string_to_md5_special_chars():
    assert string_to_md5("!@#$%^") == "6d325839935542933514a08382564948"

def test_string_to_md5_mixed_case():
    assert string_to_md5("HeLlO wOrLd") == "83a38a84a26252596384599365983466"

def test_string_to_md5_unicode():
    assert string_to_md5("你好世界") == "94f9795275729811331927593682396f"