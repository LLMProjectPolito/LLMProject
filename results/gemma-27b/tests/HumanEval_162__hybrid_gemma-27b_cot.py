
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
    assert string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_string_with_spaces():
    assert string_to_md5('  test  ') == 'a94a8fe5ccb19ba61c4c0873d391e987'
    assert string_to_md5('  test  ') == '89f98999999999999999999999999999' #added from suite 2

def test_string_to_md5_string_with_numbers():
    assert string_to_md5('12345') == '5994471abb01112afcc18159f6cc74b4'

def test_string_to_md5_string_with_special_characters():
    assert string_to_md5('!@#$%^') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_long_string():
    long_string = 'This is a very long string to test the md5 hash function.'
    assert string_to_md5(long_string) == '9f86d081884c7d659a2feaa0c55ad015'
    long_string = "This is a very long string to test the md5 function." * 10
    expected_md5 = hashlib.md5(long_string.encode()).hexdigest()
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_unicode_string():
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'
    assert string_to_md5('你好世界') == '6f9d8969f99999999999999999999999' #added from suite 2

def test_string_to_md5_mixed_string():
    assert string_to_md5('Hello123!@#') == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_different_case():
    assert string_to_md5('hello world') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_string_with_newline():
    assert string_to_md5('Hello\nworld') == '6cd3556deb0da54bca060b4c39479839'

def test_string_to_md5_string_with_mixed_case():
    assert string_to_md5('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_string_with_newlines():
    assert string_to_md5('test\nline') == '99999999999999999999999999999999'