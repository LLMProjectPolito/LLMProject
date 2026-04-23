
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

    def test_different_string(self):
        assert string_to_md5("This is a test") == "b10a8db164e0754105b7a5a0bc2e8e07"

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^&*()") == "a6735e134a612b8f9613923b76661a89"

    def test_string_with_unicode_characters(self):
        assert string_to_md5("你好世界") == "65317b2931373433393033353434303434"

    def test_string_with_numbers(self):
        assert string_to_md5("1234567890") == "a868358e978487254d17f2a198a6835f"

    def test_long_string(self):
        long_string = "This is a very long string to test the function." * 100
        assert string_to_md5(long_string) == "a6175447a172090457056719f26b5884"

    def test_string_with_whitespace(self):
        assert string_to_md5("   ") == "e289b945a528264604734493c54b291b"

    def test_string_with_mixed_case(self):
        assert string_to_md5("HeLlO wOrLd") == "256e1382d9922e4569c04390e1015816"

    def test_string_with_symbols(self):
        assert string_to_md5("!@#$%^&*()") == "a6735e134a612b8f9613923b76661a89"