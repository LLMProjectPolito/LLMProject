
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
    def test_valid_string(self):
        assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_string_with_spaces(self):
        assert string_to_md5("  ") == "d14a028c2a3a2bc9476102bb288234c4"

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^&*()") == "94a9999f999999999999999999999999"

    def test_string_with_unicode_characters(self):
        assert string_to_md5("你好世界") == "a94a8fe5ccb19ba61c4c0873d391e987"

    def test_string_with_numbers(self):
        assert string_to_md5("1234567890") == "d162b3f7d4913e5a9b94a819c1999999"

    def test_string_with_mixed_characters(self):
        assert string_to_md5("Hello123World!") == "92999999999999999999999999999999"

    def test_long_string(self):
        long_string = "This is a very long string to test the md5 hash function."
        expected_md5 = hashlib.md5(long_string.encode('utf-8')).hexdigest()
        assert string_to_md5(long_string) == expected_md5

    def test_string_with_newlines(self):
        assert string_to_md5("Line1\nLine2") == "99999999999999999999999999999999"

    def test_string_with_tabs(self):
        assert string_to_md5("Line1\tLine2") == "99999999999999999999999999999999"

    def test_string_with_carriage_return(self):
        assert string_to_md5("Line1\rLine2") == "99999999999999999999999999999999"

    def test_string_with_newline_characters(self):
        assert string_to_md5("Hello\nWorld") == "941d1344936669999999999999999999"

    def test_string_with_tab_characters(self):
        assert string_to_md5("Hello\tWorld") == "941d1344936669999999999999999999"

    def test_string_with_carriage_return_characters(self):
        assert string_to_md5("Hello\rWorld") == "941d1344936669999999999999999999"

    def test_string_with_utf8_encoded_characters(self):
        assert string_to_md5("éàçüö") == "941d1344936669999999999999999999"