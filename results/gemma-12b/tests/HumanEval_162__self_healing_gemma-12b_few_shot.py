
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
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

class TestStringtoMD5:
    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_valid_string(self):
        assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_string_with_spaces(self):
        assert string_to_md5("  ") == '9c6a98d4695394a99999999999999999'

    def test_string_with_numbers(self):
        assert string_to_md5("12345") == '5994471abb01112afcc18159f0e07a83'

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^&*()") == '94699999999999999999999999999999'

    def test_string_with_unicode_characters(self):
        assert string_to_md5("你好世界") == 'a94a8fe5ccb19ba61c4c082e53e6d97b'

    def test_long_string(self):
        long_string = "This is a very long string to test the md5 hash function."
        expected_md5 = '99a99999999999999999999999999999'
        assert string_to_md5(long_string) == expected_md5

    def test_string_with_newlines(self):
        assert string_to_md5("Line1\nLine2") == '99a99999999999999999999999999999'

    def test_string_with_tabs(self):
        assert string_to_md5("Line1\tLine2") == '99a99999999999999999999999999999'