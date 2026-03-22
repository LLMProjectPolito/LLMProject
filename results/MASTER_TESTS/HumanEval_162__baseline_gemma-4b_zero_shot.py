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

class TestStringToMD5:

    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_hello_world(self):
        assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_single_character(self):
        assert string_to_md5("a") == '2598cb87890b35d3'

    def test_long_string(self):
        long_string = "This is a very long string to test the function."
        expected_md5 = 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
        assert string_to_md5(long_string) == expected_md5

    def test_unicode_string(self):
        assert string_to_md5("你好世界") == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'

    def test_string_with_numbers(self):
        assert string_to_md5("12345") == '6e2862d8859d98999999999999999999'

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^") == 'b10a8db164e075416c839af3cb80a369'

    def test_mixed_string(self):
        assert string_to_md5("Hello123!@#") == 'b8a3b849999999999999999999999999'