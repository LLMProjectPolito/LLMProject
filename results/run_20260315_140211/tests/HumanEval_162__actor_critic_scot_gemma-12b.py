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
    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_simple_string(self):
        assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_string_with_spaces(self):
        assert string_to_md5("Hello world ") == '1713673a9a8399999999999999999999'

    def test_string_with_special_characters(self):
        test_string = "Hello!@#$%^&*()"
        md5_hash = hashlib.md5(test_string.encode('utf-8')).hexdigest()
        assert string_to_md5(test_string) == md5_hash

    def test_string_with_unicode(self):
        assert string_to_md5("你好世界") == 'b10a8db164e0754105b7a99be72e3fe5'

    def test_long_string(self):
        long_string = "This is a very long string to test the function with. It should handle it correctly."
        md5_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
        assert string_to_md5(long_string) == md5_hash

    def test_string_with_mixed_case(self):
        string1 = "HeLlO wOrLd"
        string2 = "hello world"
        assert string_to_md5(string1) != string_to_md5(string2)

    def test_case_sensitivity(self):
        assert string_to_md5("a") != string_to_md5("A")