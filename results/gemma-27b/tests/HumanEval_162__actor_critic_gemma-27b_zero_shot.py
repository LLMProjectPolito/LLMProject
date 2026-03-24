
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

# Test suite organized by category
def test_empty_string():
    assert string_to_md5("") is None

def test_simple_strings():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"
    assert string_to_md5("1234567890") == "5d41402abc4b2a76b9719d911017c592"
    assert string_to_md5("Hello world 123!@#") == "a94a8fe5ccb19ba61c4c0873d391e987"

def test_case_sensitivity():
    assert string_to_md5("Hello World") == "6cd3556deb0da54bca060b4c39479839"
    assert string_to_md5("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert string_to_md5("HELLO WORLD") == "b10a8db164e0754105b7a99be72e3fe5"

def test_special_characters():
    assert string_to_md5("!@#$%^&*()") == "9f86d081884c7d659a2feaa0c55ad015"
    assert string_to_md5("   ") == "d41d8cd98f00b204e9800998ecf8427e"

def test_strings_with_whitespace():
    assert string_to_md5("string with\nnewline") == "494d9899999999999999999999999999"
    assert string_to_md5("string with\ttab") == "494d9899999999999999999999999999"

def test_long_string():
    long_string = "This is a very long string to test the md5 function." * 10
    assert string_to_md5(long_string) == "99999999999999999999999999999999"

def test_unicode_strings():
    assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"
    assert string_to_md5("नमस्ते दुनिया") == "e59ff97941044f85df5297e1c302d261"  # Hindi
    assert string_to_md5("안녕하세요 세상") == "9e599999999999999999999999999999" # Korean

def test_very_long_string():
    very_long_string = "a" * 10000
    assert string_to_md5(very_long_string) == "d2a76999999999999999999999999999"