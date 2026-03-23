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
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

class TestStringToMd5(pytest.KeywordTest):
    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_simple_string(self):
        assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    def test_string_with_special_characters(self):
        assert string_to_md5("Hello, world!") == "f3a6b7c8d9e0a1b2c3d4e5f6"

    def test_string_with_spaces(self):
        assert string_to_md5("Hello world") == "4d6a8b7c9e0a1b2c3d4e5f6"

    def test_string_that_is_an_md5_hash(self):
        assert string_to_md5("Hello") == "a6b7c8d9e0a1b2c3d4e5f6"

    def test_long_string(self):
        assert string_to_md5("This is a very long string") == "f3a6b7c8d9e0a1b2c3d4e5f6"