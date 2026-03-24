
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
    def test_standard_string(self):
        assert string_to_md5('Hello world') == hashlib.md5('Hello world'.encode('utf-8')).hexdigest()

    def test_numeric_string(self):
        assert string_to_md5('1234567890') == hashlib.md5('1234567890'.encode('utf-8')).hexdigest()

    def test_whitespace_string(self):
        assert string_to_md5('   ') == hashlib.md5('   '.encode('utf-8')).hexdigest()

    def test_case_sensitivity(self):
        assert string_to_md5('Hello') != string_to_md5('hello')

    def test_long_string(self):
        long_string = "This is a very long string to test the function with. " * 100
        expected_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
        assert string_to_md5(long_string) == expected_hash

    def test_unicode_string(self):
        assert string_to_md5('你好世界') == hashlib.md5('你好世界'.encode('utf-8')).hexdigest()

    def test_special_characters(self):
        assert string_to_md5('!@#$%^&*()_+=-`~[]\{}|;\':",./<>?') == hashlib.md5('!@#$%^&*()_+=-`~[]\{}|;\':",./<>?'.encode('utf-8')).hexdigest()

    def test_empty_string(self):
        assert string_to_md5('') is None