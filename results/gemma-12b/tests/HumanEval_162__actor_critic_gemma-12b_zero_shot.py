
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
    Encoding used: UTF-8

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

class TestStringtoMD5:
    def test_valid_string(self):
        assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_empty_string(self):
        assert string_to_md5('') is None

    def test_string_with_spaces(self):
        assert string_to_md5('  ') == '9c648693994333e9899969699969996'

    def test_string_with_special_characters(self):
        assert string_to_md5('!@#$%^&*()') == '9c648693994333e9899969699969996'

    def test_string_with_unicode_characters(self):
        assert string_to_md5('你好世界') == '3e25960a79dbc69b674cd4ec67a72c62'  # Test with Unicode characters

    def test_string_with_numbers(self):
        assert string_to_md5('1234567890') == 'd162b37f990175a959f799999999999'

    def test_string_with_mixed_characters(self):
        assert string_to_md5('Hello123World!') == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_long_string(self):
        long_string = "This is a very long string to test the md5 hash function." * 100  # Increased length
        md5_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
        assert string_to_md5(long_string) == md5_hash

    def test_case_sensitivity(self):
        assert string_to_md5('hello world') != string_to_md5('Hello world')  # Check case sensitivity

    def test_string_with_only_whitespace(self):
        assert string_to_md5("   \t\n") == '9c648693994333e9899969699969996'

    def test_string_with_newline_characters(self):
        assert string_to_md5("Hello\nWorld") == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_string_with_tab_characters(self):
        assert string_to_md5("Hello\tWorld") == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_none_input(self):
        with pytest.raises(TypeError):
            string_to_md5(None)

    def test_non_string_input(self):
        with pytest.raises(TypeError):
            string_to_md5(123)