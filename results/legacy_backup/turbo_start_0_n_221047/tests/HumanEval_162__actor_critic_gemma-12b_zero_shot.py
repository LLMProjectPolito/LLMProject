import pytest
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text is None:
        return None
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

    def test_string_with_punctuation(self):
        assert string_to_md5("!@#$%^&*()") == "9469c999999999999999999999999999"

    def test_string_with_unicode_characters(self):
        assert string_to_md5("你好世界") == "a94a8fe5ccb19ba61c4c0873d391e987"

    def test_string_with_numbers(self):
        assert string_to_md5("1234567890") == "2741816d3373697a729953113a21696a"

    def test_string_with_mixed_characters(self):
        assert string_to_md5("Hello123World!") == "92999999999999999999999999999999"

    def test_long_string(self):
        long_string = "This is a very long string to test the md5 hash function." * 100
        assert string_to_md5(long_string) == "d2a99a99999999999999999999999999"

    def test_string_with_newlines(self):
        assert string_to_md5("Hello\nWorld") == "941b3f72999999999999999999999999"

    def test_string_with_tabs(self):
        assert string_to_md5("Hello\tWorld") == "941b3f72999999999999999999999999"

    def test_invalid_input_integer(self):
        with pytest.raises(TypeError):
            string_to_md5(123)

    def test_invalid_input_list(self):
        with pytest.raises(TypeError):
            string_to_md5(["a", "b"])

    def test_none_input(self):
        assert string_to_md5(None) is None

    def test_case_sensitivity(self):
        assert string_to_md5("Hello") != string_to_md5("hello")