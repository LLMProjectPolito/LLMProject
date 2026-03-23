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
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

class TestStringtoMD5:
    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_valid_string(self):
        assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_string_with_spaces(self):
        assert string_to_md5("  ") == '9c6a9459999999999999999999999999'

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^&*()") == '99c64399999999999999999999999999'

    def test_string_with_numbers(self):
        assert string_to_md5("1234567890") == 'd1e2f3a4b5c6d7e8f9a0b1c2d3e4f5'

    def test_string_with_unicode_characters(self):
        assert string_to_md5("你好世界") == 'b10a8db164e0754105b7a99be72e3fe5'

    def test_long_string(self):
        long_string = "This is a very long string to test the md5 hash function."
        expected_md5 = 'a94a8fe5ccb19ba61c4c0873d391e987'
        assert string_to_md5(long_string) == expected_md5

    def test_case_sensitivity(self):
        assert string_to_md5("hello") != string_to_md5("Hello")

    def test_different_encodings(self):
        # Test with different encodings to ensure UTF-8 is used correctly
        assert string_to_md5("éàçüö") == '99c64399999999999999999999999999' # Example, actual value may vary based on system default encoding

    def test_string_with_newline(self):
        assert string_to_md5("Hello\nworld") == '94f1b242999999999999999999999999'