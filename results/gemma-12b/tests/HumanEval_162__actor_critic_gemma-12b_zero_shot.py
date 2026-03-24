
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
        assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_empty_string(self):
        assert string_to_md5('') is None

    def test_string_with_leading_and_trailing_spaces(self):
        assert string_to_md5('  ') == 'da510399999999999999999999999999'

    def test_string_with_punctuation(self):
        assert string_to_md5('!@#$%^&*()') == '99499999999999999999999999999999'

    def test_string_with_unicode_characters(self):
        assert string_to_md5('你好世界') == 'a94a8fe5ccb19ba61c4c0873d391e987'

    def test_string_with_numbers(self):
        assert string_to_md5('1234567890') == 'd162b3f8d453906a9999999999999999'

    def test_string_with_newline(self):
        assert string_to_md5("Hello\nWorld") == '9e299999999999999999999999999999'

    def test_string_with_tab(self):
        assert string_to_md5("Hello\tWorld") == '9e299999999999999999999999999999'

    def test_long_string(self):
        long_string = "This is a very long string to test the md5 hash function."
        assert string_to_md5(long_string) == '9e299999999999999999999999999999'

    def test_very_long_string(self):
        very_long_string = "A" * 2000
        assert string_to_md5(very_long_string) == 'd162b3f8d453906a9999999999999999'

    def test_string_with_non_bmp_characters(self):
        assert string_to_md5('你好😊') == '9e299999999999999999999999999999'

    def test_string_with_control_characters(self):
        assert string_to_md5("Hello\x00World") == '9e299999999999999999999999999999'

    def test_invalid_input_type(self):
        with pytest.raises(TypeError):
            string_to_md5(123)

    def test_invalid_input_type_list(self):
        with pytest.raises(TypeError):
            string_to_md5(['a', 'b'])