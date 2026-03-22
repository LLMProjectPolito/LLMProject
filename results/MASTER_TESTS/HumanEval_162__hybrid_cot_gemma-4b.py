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


def test_string_to_md5():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_whitespace():
    assert string_to_md5('   ') == '29c9cb4b989999999999999999999999'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '26a8368b739999999999999999999999'

def test_string_to_md5_special_chars():
    assert string_to_md5('!@#$%^') == 'b9a8f99999999999999999999999999'

def test_string_to_md5_mixed_case():
    assert string_to_md5('HeLlO') == '6a799999999999999999999999999999'

def test_string_to_md5_long_string():
    long_string = 'a' * 1000
    assert string_to_md5(long_string) == 'a94a8fe5ccb19ba61c4c0873d391e987'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'b9a8f99999999999999999999999999'

def test_string_to_md5_none():
    assert string_to_md5(None) is None

def test_empty_string():
    assert string_to_md5("") is None

def test_simple_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_spaces():
    assert string_to_md5("  Hello world  ") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_special_characters():
    assert string_to_md5("Hello!@#$%^") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_long_string():
    long_string = "a" * 1000
    assert string_to_md5(long_string) == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_numbers():
    assert string_to_md5("12345") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_unicode_characters():
    assert string_to_md5("你好世界") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_mixed_characters():
    assert string_to_md5("Hello, 世界!") == "3e25960a79dbc69b674cd4ec67a72c62"