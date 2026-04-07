
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

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
        assert string_to_md5("a") == "2aae6c711a8b77a766d9999999999999"

    def test_string_with_spaces(self):
        assert string_to_md5("  ") == "2f7d8913c69366c2d082499999999999"

    def test_string_with_numbers(self):
        assert string_to_md5("12345") == "6b934237964363a36463636363636363"

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^") == "88626999999999999999999999999999"

    def test_unicode_string(self):
        assert string_to_md5("你好世界") == "b9a896960e46b2b39ba636934949db3a"

    def test_long_string(self):
        long_string = "This is a very long string to test the function with a large input."
        expected_md5 = "8f79899999999999999999999999999999999999999999999999999999999999"
        assert string_to_md5(long_string) == expected_md5

    def test_string_with_mixed_characters(self):
        assert string_to_md5("Hello123!@#") == "b9a896960e46b2b39ba636934949db3a"