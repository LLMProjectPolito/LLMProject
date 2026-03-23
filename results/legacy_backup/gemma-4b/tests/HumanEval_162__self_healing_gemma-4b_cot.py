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

class TestStringToMD5:

    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_simple_string(self):
        assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    def test_single_character_string(self):
        assert string_to_md5("a") == "2aae6c711a8b77a766d9e3f83b3a97a8"

    def test_string_with_spaces(self):
        assert string_to_md5("  test  ") == "26a8a8a9839393939393939393939393"

    def test_string_with_numbers(self):
        assert string_to_md5("12345") == "6b9342369d794340943311693939393"

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^") == "89663399999999999999999999999999"

    def test_unicode_string(self):
        assert string_to_md5("你好世界") == "b9a7a999999999999999999999999999"

    def test_long_string(self):
        long_string = "This is a very long string to test the function with a longer input."
        expected_md5 = "89663399999999999999999999999999"
        assert string_to_md5(long_string) == expected_md5

    def test_string_with_mixed_characters(self):
        assert string_to_md5("Hello123!@#") == "89663399999999999999999999999999"