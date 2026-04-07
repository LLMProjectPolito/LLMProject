
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
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

class TestStringtoMD5:
    def test_standard_string(self):
        assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_empty_string(self):
        assert string_to_md5('') is None

    def test_special_characters(self):
        input_string = '!@#$%^&*()'
        expected_hash = hashlib.md5(input_string.encode('utf-8')).hexdigest()
        assert string_to_md5(input_string) == expected_hash

    def test_long_string(self):
        long_string = "This is a very long string to test the function with a large input." * 10
        expected_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
        assert string_to_md5(long_string) == expected_hash

    def test_unicode_string(self):
        assert string_to_md5('你好世界') == 'a94a8fe5ccb19ba61c4c0873d391e987'

    def test_case_sensitivity(self):
        assert string_to_md5('Hello world') != string_to_md5('hello world')

    def test_numerical_string(self):
        assert string_to_md5('1234567890') == 'd1e2f3a4b5c6d7e8f9a0b1c2d3e4f5'

    def test_whitespace_string(self):
        assert string_to_md5('   ') == '90c9a3a29947499c9999999999999999'

    def test_none_input(self):
        assert string_to_md5(None) is None

    def test_leading_trailing_whitespace(self):
        assert string_to_md5('  test  ') == 'd2a9e999999999999999999999999999'

    def test_newline_characters(self):
        assert string_to_md5('test\nstring') == '99999999999999999999999999999999'