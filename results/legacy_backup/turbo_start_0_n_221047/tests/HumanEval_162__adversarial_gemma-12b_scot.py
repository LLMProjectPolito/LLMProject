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

class TestStringMD5:
    def test_valid_string(self):
        assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_string_with_spaces(self):
        assert string_to_md5("  Hello world  ") == "a94a8fe5ccb19ba61c4c0873d391e987"

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^&*()") == "941d9999999999999999999999999999"

    def test_string_with_unicode_characters(self):
        assert string_to_md5("你好世界") == "a94a8fe5ccb19ba61c4c0873d391e987"

    def test_long_string(self):
        long_string = "This is a very long string to test the MD5 hash function. It should handle long strings without any issues."
        assert string_to_md5(long_string) == hashlib.md5(long_string.encode('utf-8')).hexdigest()

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            string_to_md5(123)
        with pytest.raises(TypeError):
            string_to_md5([1, 2, 3])