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

def test_string_to_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_long_string():
    long_string = 'a' * 1000
    assert string_to_md5(long_string) == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'

def test_string_to_md5_special_characters():
    assert string_to_md5('Hello\nworld\t!') == '6cd3556deb0da54bca060b4c39479839'

def test_string_to_md5_with_numbers():
    assert string_to_md5('Hello123world') == '5994471abb01112afcc18159f6cc74b4'

def test_string_to_md5_whitespace():
    assert string_to_md5('   ') == 'd41d8cd98f00b204e9800998ecf8427e'

def test_string_to_md5_long_repeating():
    long_repeating_string = 'a' * 5000
    assert string_to_md5(long_repeating_string) == '964f9989999999999999999999999999'