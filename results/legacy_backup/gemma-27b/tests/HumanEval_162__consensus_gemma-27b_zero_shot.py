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
    return hashlib.md5(text.encode()).hexdigest()

def test_string_to_md5_valid_string():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert string_to_md5('This is a test string.') == '5994471abb01112afcc18159f6cc74b4'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_string_with_spaces():
    assert string_to_md5('   ') == 'd41d8cd98f00b204e9800998ecf8427e'

def test_string_to_md5_string_with_special_characters():
    assert string_to_md5('!@#$%^&*()') == '827ccb0eea8a706c4c34a16891f84e7b'

def test_string_to_md5_long_string():
    long_string = 'a' * 100
    assert len(string_to_md5(long_string)) == 32

def test_string_to_md5_unicode_string():
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_single_character():
    assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

def test_string_to_md5_with_spaces():
    assert string_to_md5("  test  ") == "e5e9fa1ba31ecd1ae84f75caaa474f3a"

def test_string_to_md5_with_numbers():
    assert string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"

def test_string_to_md5_with_special_characters():
    assert string_to_md5("!@#$%^") == "b10a8db164e0754105b7a99be72e3fe5"

def test_string_to_md5_long_string_2():
    long_string = "This is a very long string to test the md5 function."
    assert string_to_md5(long_string) == "9f86d081884c7d659a2feaa0c55ad015"