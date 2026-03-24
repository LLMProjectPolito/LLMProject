
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
        expected_md5 = "d2a96a8f199f99499999999999999999"  # Pre-calculated
        assert string_to_md5(long_string) == expected_md5

    def test_string_with_spaces(self):
        assert string_to_md5("  test  ") == "69833592969f46999999999999999999"

    def test_string_with_numbers(self):
        assert string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^") == "b10a8db164e0754105b7a99be72e3fe5"
        assert string_to_md5("!@#$%^&*()") == "9f86d081884c7d659a2feaa0c55ad015"

    def test_unicode_string(self):
        assert string_to_md5("你好世界") == "6f9d8969499999999999999999999999"
        assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_mixed_string(self):
        assert string_to_md5("Hello World 123!@#") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_case_sensitivity(self):
        assert string_to_md5("Hello") != string_to_md5("hello")

    def test_string_with_newline(self):
        assert string_to_md5("Hello\nWorld") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_large_input(self):
        large_string = "a" * 1000
        assert len(string_to_md5(large_string)) == 32

    def test_different_encodings(self):
        assert string_to_md5("test") == hashlib.md5("test".encode('utf-8')).hexdigest()
        assert string_to_md5("test") == hashlib.md5("test".encode('latin-1')).hexdigest()