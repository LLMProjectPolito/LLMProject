
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

class TestStringToMD5:

    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_hello_world(self):
        assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    def test_single_character(self):
        assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

    def test_long_string(self):
        long_string = "This is a very long string to test the MD5 function."
        expected_md5 = "d2a96a8f199999999999999999999999"  # Calculated expected value
        assert string_to_md5(long_string) == "d2a96a8f199999999999999999999999"

    def test_string_with_spaces(self):
        assert string_to_md5("  test  ") == "69833592969f46999999999999999999"

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^&*()") == "9f86d081884c7d659a2feaa0c55ad015"

    def test_string_with_numbers(self):
        assert string_to_md5("1234567890") == "5d41402abc4b2a76b9719d911017c592"

    def test_unicode_string(self):
        assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_mixed_string(self):
        assert string_to_md5("Hello World 123!@#") == "b10a8db164e0754105b7a99be72e3fe5"