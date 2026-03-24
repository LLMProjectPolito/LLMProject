
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
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

@pytest.mark.parametrize(
    "input_string, expected_md5",
    [
        ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
        ("test", "098f6bcd4621d373cade4e832627b4f6"),
        ("a", "0cc175b9c0f1b6a831c399e269772661"),
        ("12345", "827ccb0eea8a706c4c34a16891f84e7b"),
        ("!@#$%^", "b10a8db164e0754105b7a99be72e3fe5"),
        ("Hello123!", "5d41402abc4b2a76b9719d911017c592"),
    ],
)
def test_md5_parametrized(input_string, expected_md5):
    assert string_to_md5(input_string) == expected_md5

def test_md5_unicode():
    assert string_to_md5('你好世界') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert string_to_md5('你好世界！') == '6f9f8999999999999999999999999999'
    assert string_to_md5('नमस्ते दुनिया') == '99999999999999999999999999999999'

def test_md5_long_string():
    long_string = "This is a very long string to test the MD5 function. " * 100
    expected_md5 = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == expected_md5

def test_md5_docstring():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_md5_different_encoding():
    assert string_to_md5('你好世界'.encode('gbk').decode('utf-8')) == 'd41d8cd98f00b204e9800998ecf8427e'