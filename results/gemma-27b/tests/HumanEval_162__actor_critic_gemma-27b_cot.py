
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import hashlib
import pytest

def test_string_to_md5_valid_string():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_string_with_spaces():
    assert string_to_md5('  test  ') == 'a94a8fe5ccb19ba61c4c0873d391e987'

def test_string_to_md5_long_string():
    long_string = 'This is a very long string to test the md5 hash function.'
    assert string_to_md5(long_string) == '9f86d081884c7d659a2feaa0c55ad015'

def test_string_to_md5_mixed_string():
    assert string_to_md5('Hello123!@#') == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_with_non_string_input():
    assert string_to_md5(123) is None

def test_string_to_md5_unicode_string():
    assert string_to_md5('你好世界') == 'd41d8cd98f00b204e9800998ecf8427e'

def test_string_to_md5_special_characters():
    assert string_to_md5('!@#$%^') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_with_none_input():
    assert string_to_md5(None) is None

def test_string_to_md5_utf8_encoding():
    unicode_string = '你好世界'
    encoded_string = unicode_string.encode('utf-8')
    assert string_to_md5(encoded_string.decode('utf-8')) == 'd41d8cd98f00b204e9800998ecf8427e'

def test_string_to_md5_utf16_encoding():
    unicode_string = '你好世界'
    encoded_string = unicode_string.encode('utf-16')
    assert string_to_md5(encoded_string.decode('utf-16')) == 'd41d8cd98f00b204e9800998ecf8427e'