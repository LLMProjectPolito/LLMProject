
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

class TestStringToMd5:

    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_valid_string(self):
        assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    def test_string_with_spaces(self):
        assert string_to_md5("This is a test string") == "d41d8cd98f00b204e9800998ecf8427e"

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^&*()") == "693a5f67f1959703e789b6e5d106a587"

    def test_string_with_unicode_characters(self):
        assert string_to_md5("你好世界") == "e587af510e34e587af510e34e587af510"

    def test_long_string(self):
        long_string = "This is a very long string to test the function." * 10
        assert string_to_md5(long_string) == "e8a6346879e5526e8d08949160966463"

    def test_string_with_numbers(self):
        assert string_to_md5("1234567890") == "d67841c3f037238a984413e531e20044"

    def test_string_with_mixed_characters(self):
        assert string_to_md5("a1b2c3d4e5f6") == "7805e129c97d8896f80916f62105439e"

    def test_string_with_newline(self):
        assert string_to_md5("Hello\nworld") == "f0c92e21a291e427b9273856403b8753"

    def test_string_with_whitespace(self):
        assert string_to_md5("   ") == "f3745e768877e17a4174967a6655a461"