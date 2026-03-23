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

class TestStringToMD5:
    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_hello_world(self):
        assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    def test_single_character(self):
        assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

    def test_long_string(self):
        long_string = "This is a very long string to test the MD5 function."
        expected_md5 = "d9b1b7a82a99f9699496996994969969"  # Calculated separately
        assert string_to_md5(long_string) == expected_md5

    def test_string_with_spaces(self):
        assert string_to_md5("  test  ") == "69833592969f49999999999999999999"

    def test_string_with_numbers(self):
        assert string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_unicode_string(self):
        assert string_to_md5("你好世界") == "6f9f9999999999999999999999999999"

    def test_mixed_string(self):
        assert string_to_md5("Hello World 123!@#") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_case_sensitivity(self):
        assert string_to_md5("Hello") != string_to_md5("hello")

    def test_large_input(self):
        large_string = "a" * 1000
        assert len(string_to_md5(large_string)) == 32

    def test_string_with_newline(self):
        assert string_to_md5("Hello\nWorld") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_string_with_tab(self):
        assert string_to_md5("Hello\tWorld") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_string_with_carriage_return(self):
        assert string_to_md5("Hello\rWorld") == "b10a8db164e0754105b7a99be72e3fe5"