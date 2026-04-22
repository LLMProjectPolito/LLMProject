
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

    def test_simple_string(self):
        assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_string_with_numbers(self):
        assert string_to_md5("12345") == 'd41d8cd98f00b204e9800998ecf8427e'

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^&*()") == 'e2e8e48a2a7a7168450937542949223a'

    def test_string_with_unicode_characters(self):
        assert string_to_md5("你好世界") == 'e53b986325638494699377973529837a'

    def test_long_string(self):
        long_string = "This is a very long string to test the function." * 10
        md5_hash = string_to_md5(long_string)
        assert len(md5_hash) == 32

    def test_string_with_spaces(self):
        assert string_to_md5("  leading and trailing spaces  ") == 'b92935919923321394213658a701415b'

    def test_string_with_mixed_case(self):
        assert string_to_md5("MiXeD CaSe") == '947b3a4193559419996391959396255a'

    def test_string_with_newlines(self):
        assert string_to_md5("Line 1\nLine 2") == '6a98662a794b11946595929808487102'